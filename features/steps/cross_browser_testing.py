# from selenium.webdriver.common.by import By
# from behave import given, when, then
# from time import sleep
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options as ChromeOptions
# from selenium.webdriver.firefox.options import Options as FirefoxOptions
# from selenium.webdriver.chrome.options import Options as ChromeOptions
# from selenium.webdriver.firefox.options import Options as FirefoxOptions
# from secondary_option import *
# @given('User has a "<browser>" browser')
# def step_given_browser(context, browser):
#     if browser == "Chrome":
#         context.driver = webdriver.Chrome()
#     elif browser == "Firefox":
#         context.driver = webdriver.Firefox()
#
# @then('Execute all steps from secondary_option')
# def step_execute_secondary_option(context):
#     step_open_main_page(context)
#     step_user_logs_in(context)
#     step_user_clicks_secondary_option(context)
#     step_verify_correct_page(context)
#     step_filter_products_by_want_to_buy(context)
#     step_verify_cards_have_want_to_buy(context)
#
# @then('Close the browser')
# def step_then_close_browser(context):
#     context.driver.quit()