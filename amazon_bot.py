""" Libraies need to run script."""
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
import time, datetime, random,sys
from credentials import Email, User
import smtplib

class Product:
    """ Product class with helper functions. """
    
    def __init__(self,**kwargs):
        """ Constructor function of Product class. 
        Delay is set to random to avoid detection by amazon which
        could result in temporarily block. """

        self.amazon_credential = User()
        self.email_credential = Email()
        self.product = kwargs['p_url']
    
    def launch_bot(self):
        """ Initializes bot and emulates selenium browser. 
        It goes to login page first. """

        options = Options()
        options.set_headless(headless=True)
        self.browser_emulator = webdriver.Firefox(firefox_options=options)
        self.browser_emulator.get\
        ('''https://www.amazon.in/ap/signin?openid.assoc_handle=inflex&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.mode=checkid_setup&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0''')
        
    def user_login_session(self):
        """ Enter user credentials and goto product page. """

        self.browser_emulator.find_element_by_xpath\
        ('''//*[@id="ap_email"]''').send_keys(self.amazon_credential.UNAME,Keys.RETURN)
        time.sleep(10)
        self.browser_emulator.find_element_by_xpath\
        ('''//*[@id="ap_password"]''').send_keys(self.amazon_credential.PASSWD,Keys.RETURN)
        time.sleep(10)
        
        """ Change this URL to add another product to cart. """
        self.browser_emulator.get(self.product)
        #self.browser_emulator.get\('''https://www.amazon.in/OnePlus-Bullets-Wireless-Earphones-Black/dp/B07D3FN6QM/''')
        
    def check_availability(self):
        """ This function checks product availability
        and adds it to cart when possible. """
        
        try:
        	self.browser_emulator.find_element_by_xpath\
            ('''//*[@id="priceblock_ourprice"]''')
        except:
        	self.browser_emulator.refresh()
        	time.sleep(random.randint(10,45))
        	print('It is not is Stock yet.')
        else:
            self.browser_emulator.find_element_by_xpath('//*[@id="add-to-cart-button"]').click()
            self.email_notification()
            self.browser_emulator.quit()

    def email_notification(self):
        """ Sends email to user to alert that product have been added to cart.
        Server in this function is setup for Outlook.com, it'll be different for other
        email services. """

        email = '''FROM: {user}\nTO: {to}\nSUBJECT: {subject}\n\n{body}'''\
        .format(user = self.email_credential.EMAIL,to=self.email_credential.RECEIVER,\
            subject=self.email_credential.SUBJECT,body=self.email_credential.BODY)
        server = smtplib.SMTP('smtp-mail.outlook.com',25)
        server.starttls()
        server.login(self.email_credential.EMAIL,self.email_credential.EMAILPASSWD)
        server.sendmail(self.email_credential.EMAIL,self.email_credential.RECEIVER, email)
        server.quit()

if __name__ == '__main__':
    """ This script is executed, when you run .py file. """

    product = sys.argv[1]
    bot = Product(p_url=product)
    bot.launch_bot()
    bot.user_login_session()
    while 1:
        bot.check_availability()