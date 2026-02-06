from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from data import *
from locators import Locators
from curl import *


class TestRegistrationPOSITIVE:
    #1 успешная регистрация пользователя с новыми данными
    def test_success_registration(self, driver): 
        name, email, password = generate_registration_valid()    
        driver.find_element(*Locators.ENTRY_BUTTON).click()
        driver.find_element(*Locators.REG_BUTTON).click()
        driver.find_element(*Locators.NAME).send_keys(name)
        driver.find_element(*Locators.EMAIL).send_keys(email)
        driver.find_element(*Locators.PASSWORD).send_keys(password)
        driver.find_element(*Locators.REGISTER_BUTTON).click() 
        
        WebDriverWait(driver, 10, poll_frequency=0.5).until(EC.url_to_be(entry_site))                                
        assert driver.current_url == entry_site 
    

class TestRegistrationNEGATIVE:
    #2 ошибка при регистрации с некорректным паролем
    def test_failed_registration(self, driver):
        name, email, password = generate_registration_with_invalid_password()    
          
        driver.find_element(*Locators.ENTRY_BUTTON).click()
        driver.find_element(*Locators.REG_BUTTON).click()
        driver.find_element(*Locators.NAME).send_keys(name)
        driver.find_element(*Locators.EMAIL).send_keys(email)
        driver.find_element(*Locators.PASSWORD).send_keys(password)
        driver.find_element(*Locators.REGISTER_BUTTON).click()

        reg_text = WebDriverWait(driver, 10, poll_frequency=0.5).until(EC.visibility_of_element_located(Locators.REG_POPUP)).text
        assert reg_text == 'Некорректный пароль'
    