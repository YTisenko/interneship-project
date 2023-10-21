from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep



@given("Open the main page")
def step_open_main_page(context):
    context.driver.get("https://soft.reelly.io/sign-in")

@when("User logs in")
def step_user_logs_in(context):
    email = "first@email.com"
    password = "careerist"
    email_field = context.driver.find_element(By.ID, "email-2")
    password_field = context.driver.find_element(By.ID, "field")
    continue_button = context.driver.find_element(By.XPATH, "//a[@wized='loginButton' and contains(text(), 'Continue')]")
    email_field.send_keys(email)
    password_field.send_keys(password)
    continue_button.click()
    sleep(2)

@when("User clicks on the Secondary option in the left side menu")
def step_user_clicks_secondary_option(context):
    secondary_menu_option = context.driver.find_element(By.XPATH,"//div[contains(text(),'Secondary')]")
    secondary_menu_option.click()
    sleep(2)

@then("Correct page is open")
def step_verify_correct_page(context):
    expected_url= "https://soft.reelly.io/secondary-listings"
    actual_url = context.driver.current_url
    assert expected_url == actual_url, f"Expected URL: {expected_url}, Actual URL: {actual_url}"

@when("User filters the products by 'want to buy'")
def step_filter_products_by_want_to_buy(context):
    filter_element = context.driver.find_element(By.CSS_SELECTOR, ".filter-button")
    filter_element.click()
    sleep(2)
    want_to_buy_element= context.driver.find_element(By.XPATH, "//div[@class='switcher-button']//div[contains(text(), 'Want to buy')]")
    want_to_buy_element.click()
    sleep(2)
    apply_filter_element=context.driver.find_element (By.XPATH, "//a[contains(text(), 'Apply filter') and contains(@class, 'button-filter')]")
    apply_filter_element.click()
    sleep(2)
    expected_url="https://soft.reelly.io/secondary-listings"
    actual_url=context.driver.current_url
    assert expected_url == actual_url, f"Expected URL: {expected_url}, Actual URL: {actual_url}"

@then("Verify all cards have a 'want to buy' tag")
def step_verify_cards_have_want_to_buy(context):
    # expected_tag = context.driver.find_element(By.XPATH, "//div[@wized='saleTagMLS' and text()='Want to buy']")
    # expected_tag='Want to buy'
    all_cards = context.driver.find_element(By.XPATH,"//div[@wized='listingCardMLS']")
    all_cards_have_tag = True
    for card in all_cards:
        card_text=card.text
        expected_tag = 'Want to buy'
        if expected_tag not in card_text:
            all_cards_have_tag=False
            break
    if all_cards_have_tag:
        print("All cards have the 'want to buy' tag")
    else:
        print("Not all cards have the 'want to buy' tag")









