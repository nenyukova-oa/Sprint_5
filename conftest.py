import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from data import *
from locators import Locators
from curl import *

# session, module, class, function
@pytest.fixture(scope="function")
def driver():

    options = Options()
    options.add_experimental_option("prefs", {
            "profile.password_manager_leak_detection": False
        })
    #options.add_argument("--headless")
    browser = webdriver.Chrome(options=options)
    browser.get(main_site)
    yield browser
    browser.quit()

# успешный вход зарегистрированного пользователя вход по кнопке «Войти в аккаунт» на главной
@pytest.fixture
def login_account_main(driver):
       
    driver.find_element(*Locators.ENTRY_BUTTON).click()       
    driver.find_element(*Locators.EMAIL_ENTRY).send_keys(email_fix)
    driver.find_element(*Locators.PASSWORD_ENTRY).send_keys(password_fix)
    driver.find_element(*Locators.ENTRY_BUTTON_PAGE_ENTRY).click()
    driver.find_element(*Locators.ACCOUNT_BUTTON).click() 

    WebDriverWait(driver, 10, poll_frequency=0.5).until(EC.visibility_of_element_located(Locators.PROFILE))
    yield driver  
    
