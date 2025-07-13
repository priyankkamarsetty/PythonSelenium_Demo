from behave import given, when, then, step
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time, os, csv, logging
from datetime import datetime

# Setup logging
log_dir = "logs"
screenshot_dir = "screenshots"
os.makedirs(log_dir, exist_ok=True)
os.makedirs(screenshot_dir, exist_ok=True)
logging.basicConfig(
    filename=f"{log_dir}/test_log_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log",
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def capture_screenshot(context, name="screenshot"):
    filepath = os.path.join(screenshot_dir, f"{name}_{int(time.time())}.png")
    context.driver.save_screenshot(filepath)
    logging.info(f"Screenshot saved: {filepath}")

# -------------------- ReactJS --------------------
@given("I open ReactJS homepage")
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://reactjs.org")
    context.wait = WebDriverWait(context.driver, 10)

@when("I click the Learn React link")
def step_impl(context):
    context.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Learn React"))).click()

@then("The Quick Start section should be visible")
def step_impl(context):
    try:
        context.wait.until(EC.visibility_of_element_located((By.ID, "quick-start")))
        assert "Quick Start" in context.driver.page_source
        logging.info("Quick Start section is visible.")
    except Exception as e:
        capture_screenshot(context, "react_quickstart_fail")
        raise e
    finally:
        context.driver.quit()

# -------------------- IMDb --------------------
@given("I open IMDb homepage")
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://www.imdb.com")
    context.wait = WebDriverWait(context.driver, 10)

@then("The IMDb title should match expected")
def step_impl(context):
    assert "IMDb" in context.driver.title
    logging.info("IMDb title verified.")

@then("IMDb search box should be visible")
def step_impl(context):
    context.wait.until(EC.presence_of_element_located((By.ID, "suggestion-search")))

@when("I search for the movie Inception on IMDb")
def step_impl(context):
    try:
        box = context.driver.find_element(By.ID, "suggestion-search")
        box.send_keys("Inception")
        box.send_keys(Keys.RETURN)
        time.sleep(2)
        logging.info("Inception searched.")
    except Exception as e:
        capture_screenshot(context, "imdb_search_fail")
        raise e
    finally:
        context.driver.quit()

# -------------------- Wikipedia --------------------
@given("I open Wikipedia homepage")
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://www.wikipedia.org")
    context.wait = WebDriverWait(context.driver, 10)

@then("Wikipedia logo and search box should be visible")
def step_impl(context):
    context.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "central-featured-logo")))
    context.wait.until(EC.presence_of_element_located((By.NAME, "search")))

@when('I search for "JavaScript" on Wikipedia')
def step_impl(context):
    box = context.driver.find_element(By.NAME, "search")
    box.send_keys("JavaScript")
    box.send_keys(Keys.RETURN)
    time.sleep(2)
    context.driver.quit()

# -------------------- CSV Login --------------------
@given("I perform login tests using CSV data")
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://www.saucedemo.com")
    with open('features/testdata/data.csv') as file:
        reader = csv.DictReader(file)
        for row in reader:
            user = row['username']
            pwd = row['password']
            context.driver.find_element(By.ID, "user-name").clear()
            context.driver.find_element(By.ID, "password").clear()
            context.driver.find_element(By.ID, "user-name").send_keys(user)
            context.driver.find_element(By.ID, "password").send_keys(pwd)
            context.driver.find_element(By.ID, "login-button").click()
            time.sleep(1)
            context.driver.get("https://www.saucedemo.com")
    context.driver.quit()

# -------------------- SauceDemo Scenarios --------------------
@given("I open SauceDemo login page")
@given("I open SauceDemo Task6 login page")
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://www.saucedemo.com")
    context.wait = WebDriverWait(context.driver, 10)

@when('I login with username "standard_user" and password "secret_sauce"')
@when('I enter Task6 username "standard_user" and password "secret_sauce"')
def step_impl(context):
    context.driver.find_element(By.ID, "user-name").send_keys("standard_user")
    context.driver.find_element(By.ID, "password").send_keys("secret_sauce")
    context.driver.find_element(By.ID, "login-button").click()

@then("I should see an error page")
def step_impl(context):
    assert "inventory" in context.driver.current_url
    context.driver.quit()

@when('I login with username "locked_out_user" and password "wrong_password"')
def step_impl(context):
    context.driver.find_element(By.ID, "user-name").send_keys("locked_out_user")
    context.driver.find_element(By.ID, "password").send_keys("wrong_password")
    context.driver.find_element(By.ID, "login-button").click()

@then('I should see error "This message will intentionally fail."')
def step_impl(context):
    capture_screenshot(context, "intentional_failure")
    assert False, "This message will intentionally fail."

@when('I login with username "standard_user" and password "wrong_password"')
@when('I enter Task6 username "standard_user" and password "wrong_password"')
def step_impl(context):
    context.driver.find_element(By.ID, "user-name").send_keys("standard_user")
    context.driver.find_element(By.ID, "password").send_keys("wrong_password")
    context.driver.find_element(By.ID, "login-button").click()

@then('I should see error "Epic sadface: Username and password do not match any user in this service"')
@then('I should see Task6 error message "Epic sadface: Username and password do not match any user in this service"')
def step_impl(context):
    msg = context.driver.find_element(By.XPATH, "//h3[@data-test='error']").text
    assert "Username and password do not match" in msg
    context.driver.quit()

@then("I should successfully login for Task6")
def step_impl(context):
    assert "inventory.html" in context.driver.current_url
    context.driver.quit()
