""" Libraies need to run script."""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time, datetime, random,sys
import credentials

class Product:
    """ Product class with helper functions. """
    
    def __init__(self,**kwargs):
        """ Constructor function of Product class. 
        Delay is set to random to avoid detection by amazon which
        could result in temporarily block. """

        self.uname = credentials.User().UNAME
        self.passwd = credentials.User().PASSWD
        self.product = kwargs['p_url']
    
    def launch_bot(self):
        """ Initializes bot and emulates selenium browser. 
        It goes to login page first. """

        self.browser_emulator = webdriver.Firefox()
        self.browser_emulator.get('''https://www.amazon.in/ap/signin?openid.assoc_handle=inflex&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.mode=checkid_setup&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0''')
        
    def user_login_session(self):
        """ Enter user credentials and goto product page. """

        self.browser_emulator.find_element_by_xpath('''//*[@id="ap_email"]''').send_keys(self.uname,Keys.RETURN)
        time.sleep(random.randint(3,8))
        self.browser_emulator.find_element_by_xpath('''//*[@id="ap_password"]''').send_keys(self.passwd,Keys.RETURN)
        time.sleep(random.randint(3,8))
        
        """ Change this URL to add another product to cart. """
        self.browser_emulator.get(self.product)
        #self.browser_emulator.get('''https://www.amazon.in/OnePlus-Bullets-Wireless-Earphones-Black/dp/B07D3FN6QM/''')
        
    def check_availability(self):
        """ This function checks product availability
        and adds it to cart when possible. """
        
        try:
        	available = self.browser_emulator.find_element_by_xpath('''//*[@id="priceblock_saleprice"]''')
        except:
        	self.browser_emulator.refresh()
        	time.sleep(random.randint(3,8))
        	print('It is not is Stock yet.')
        else:
            self.browser_emulator.find_element_by_xpath('//*[@id="add-to-cart-button"]').click()
            print('Product has been added to your Cart.')
            self.browser_emulator.quit()

if __name__ == '__main__':
    """ This script is executed, when you run .py file. """

    product = sys.argv[1]
    bot = Product(p_url=product)
    bot.launch_bot()
    bot.user_login_session()
    while 1:
        bot.check_availability()
