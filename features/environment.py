from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
# from App.application import Application
# from support.logger import logger
import allure


# behave -f allure_behave.formatter:AllureFormatter -o test_results/ features/tests/bestsellers.feature

def browser_init(context):
    """
    :param context: Behave context
    """
    #
    # service = Service(executable_path='/Users/balamurugann/Downloads/Internshp-Project/chromedriver')
    # context.driver = webdriver.Chrome(service=service)
    # context.driver.maximize_window()
    #
    driver_path = executable_path = './chromedriver'
    service = Service(driver_path)
    context.driver = webdriver.Chrome(service=service)

    # # ### FIREFOX ###
    # service = Service(executable_path='./geckodriver')
    # context.driver = webdriver.Firefox(service=service)

    ## OTHER BROWSER####
    # context.driver = webdriver.Safari()

    # context.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

    # HEADLESS MODE ####
    # options = webdriver.FirefoxOptions()
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')

    service = Service(executable_path='./chromedriver')
    context.driver = webdriver.Chrome(options=options, service=service)
    context.driver.set_window_size(1920, 1080)

    ## BROWSERSTACK ###
    # # Register for BrowserStack, then grab it from https://www.browserstack.com/accounts/settingspip3 install -r requirements.txt
    bs_user = 'yulia_YNeRTd'
    bs_key = 'ZSaxRKmqUF8usu7ZWCXB'
    url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'

    options = Options()
    bstack_options = {
        "os": "OS X",
        "osVersion": "Monterey",
        "browserName": "Chrome",
        "browserVersion": "latest",
        "buildName": "browserstack-build-1",
        "projectName": "BrowserStack Sample",
        "sessionName": "Secondary Deals Filtering"
    }
    # options.set_capability('bstack:options', bstack_options)
    # context.driver = webdriver.Remote(command_executor=url, options=options)

    ## for mobile web testing
    # mobile_emulation = {"deviceName": "Nexus 5"}
    # chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
    # context.driver = webdriver.Chrome(options=chrome_options)

    # context.driver.maximize_window()
    context.driver.implicitly_wait(10)
    context.driver.wait = WebDriverWait(context.driver, 15)

    # context.app = Application(context.driver)


# allure testing:
# command for the terminal:  behave -f allure_behave.formatter:AllureFormatter -o test_results/ features/


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    # logger.info(f'\nStarted scenario: {scenario.name}')
    browser_init(context)
    # browser_init(context, scenario.name)


def before_step(context, step):
    print('\nStarted step: ', step)
    # logger.info(f'Started step: {step}')


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)
        # logger.error(f'Step failed: {step}')


def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()
