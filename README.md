# Amazon.in Bot

## How to use this Bot?
### Follow these steps, _this is only for Linux_:
1. Clone this Repository
2. Setup an virtual environment
  * sudo apt-get install virtualenv
  * virtualenv -p python3.6 name_of_environment 
  * Activate environment by **source ./name_of_environment/bin/activate**
3. Install Dependencies, such are as
  * pip install -r requirements.txt
4. Setup geckodriver
  * Download [Latest Geckodrivers.](https://github.com/mozilla/geckodriver/releases)
  * Extract and copy in _/usr/local/bin_
4. Enter your Amazon.in credentials in credentials.py
5. Run script by executing amazon_bot.py file, **python amazon_bot.py product-url-here**
