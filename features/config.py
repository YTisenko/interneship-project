from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

def get_chrome_driver():
    chromedriver_path = './chromedriver'
    chrome_options = ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    return webdriver.Chrome(executable_path=chromedriver_path, options=chrome_options)

def get_firefox_driver():
    geckodriver_path ='/Users/Yulia/Downloads/interneship-project/geckodriver'
    firefox_options = FirefoxOptions()
    firefox_options.headless = True
    return webdriver.Firefox(executable_path=geckodriver_path, options=firefox_options)
