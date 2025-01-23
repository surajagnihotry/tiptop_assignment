from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time


driver = webdriver.Chrome()

driver.get('https://d3pv22lioo8876.cloudfront.net/tiptop/')

# 1. Verify that the text input element is disabled in the form
def test_disabled_input():
    disabled_input = driver.find_element(By.XPATH, "//input[@placeholder='Disabled input']")
    assert not disabled_input.is_enabled(), "The input should be disabled"
    print("Test 1 passed: Disabled input field is correctly disabled.")


# 2. Verify that the text input with value 'Readonly input' is in readonly state
def test_readonly_input():
    readonly_input_1 = driver.find_element(By.XPATH, "//input[@name='my-readonly']")
    readonly_input_2 = driver.find_element(By.XPATH, "//input[@value='Readonly input']")
    assert readonly_input_1.get_attribute('readonly') == 'true', "The input should be readonly"
    assert readonly_input_2.get_attribute('readonly') == 'true', "The input should be readonly"
    print("Test 2 passed: Readonly input is correctly in readonly state.")

# 3. Verify that the dropdown field to select color is having 8 elements
def test_dropdown_elements_count():
    dropdown_1 = driver.find_element(By.XPATH, "//select[@class='form-select']")
    dropdown_2 = driver.find_element(By.XPATH, "//select[@name='my-select']")
    options_1 = dropdown_1.find_elements(By.TAG_NAME, 'option')
    options_2 = dropdown_2.find_elements(By.TAG_NAME, 'option')
    assert len(options_1) == 8, "Dropdown should have 8 options."
    assert len(options_2) == 8, "Dropdown should have 8 options."
    print("Test 3 passed: Dropdown has 8 elements.")

# 4. Verify that the submit button is disabled when no data is entered in Name field
def test_submit_button_disabled_no_data():
    name_input = driver.find_element(By.XPATH, "//input[@id='my-name-id']")
    password_input = driver.find_element(By.XPATH, "//input[@id='my-password-id']")
    submit_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    
    name_input.clear()
    password_input.clear()
    
    assert not submit_button.is_enabled(), "Submit button should be disabled when fields are empty."
    print("Test 4 passed: Submit button is disabled when no data is entered.")

# 5. Verify that the submit button is enabled when both Name and Password field are entered
def test_submit_button_enabled():
    name_input = driver.find_element(By.XPATH, "//input[@id='my-name-id']")
    password_input = driver.find_element(By.XPATH, "//input[@id='my-password-id']")
    submit_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    
    name_input.clear()
    password_input.clear()
    
    name_input.send_keys("Test Name")
    password_input.send_keys("Test Password")
    
    assert submit_button.is_enabled(), "Submit button should be enabled when both fields are filled."
    print("Test 5 passed: Submit button is enabled when both Name and Password are entered.")

# 6. Verify that on submit of 'Submit' button the page shows 'Received' text
def test_received_text_on_submit():
    name_input = driver.find_element(By.XPATH, "//input[@id='my-name-id']")
    password_input = driver.find_element(By.XPATH, "//input[@id='my-password-id']")
    submit_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    
    name_input.clear()
    password_input.clear()
    
    name_input.send_keys("Test Name")
    password_input.send_keys("Test Password")
    submit_button.click()

    time.sleep(2)  # wait for page to update after submission
    received_text = driver.page_source
    assert 'Received' in received_text, "The page should show 'Received' after submitting."
    print("Test 6 passed: 'Received' text is displayed after submitting the form.")

# 7. Verify that on submit of form all the data passed to the URL
def test_data_in_url():
    name_input = driver.find_element(By.XPATH, "//input[@id='my-name-id']")
    password_input = driver.find_element(By.XPATH, "//input[@id='my-password-id']")
    submit_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    
    name_input.clear()
    password_input.clear()
    
    name_input.send_keys("Test Name")
    password_input.send_keys("Test Password")
    submit_button.click()

    time.sleep(2)  # wait for URL to update after submission
    current_url = driver.current_url
    assert 'name=Test%20Name' in current_url, "Name data should be passed in the URL."
    assert 'password=Test%20Password' in current_url, "Password data should be passed in the URL."
    print("Test 7 passed: Data is passed in the URL.")

# Run test cases
try:
    test_disabled_input()
    test_readonly_input()
    test_dropdown_elements_count()
    test_submit_button_disabled_no_data()
    test_submit_button_enabled()
    test_received_text_on_submit()
    test_data_in_url()
except AssertionError as e:
    print(f"Test failed: {e}")

finally:
    driver.quit()
