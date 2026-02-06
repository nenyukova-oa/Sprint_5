from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from data import email_fix, password_fix
from locators import Locators
from curl import *


class TestLoginLogout:

    #1 вход по кнопке «Войти в аккаунт» на главной 
    def test_success_entry_main(self, login_account_main): 
        profile_text = login_account_main.find_element(*Locators.PROFILE).text
        assert profile_text == 'Профиль' #проверяем, что находимся именно в личном кабинете

    
    #2 вход через кнопку «Личный кабинет» на главной
    def test_success_entry_account(self, driver): 
        driver.find_element(*Locators.ACCOUNT_BUTTON).click()       
        driver.find_element(*Locators.EMAIL_ENTRY).send_keys(email_fix)
        driver.find_element(*Locators.PASSWORD_ENTRY).send_keys(password_fix)
        driver.find_element(*Locators.ENTRY_BUTTON_PAGE_ENTRY).click()
        driver.find_element(*Locators.ACCOUNT_BUTTON).click() 

        profile_text = WebDriverWait(driver, 10, poll_frequency=0.5).until(EC.visibility_of_element_located(Locators.PROFILE)).text
        assert profile_text == 'Профиль'
    
    #3 вход через кнопку в форме регистрации
    def test_success_entry_reg(self, driver): 
        driver.find_element(*Locators.ENTRY_BUTTON).click()
        driver.find_element(*Locators.REG_BUTTON).click()
        driver.find_element(*Locators.ENTRY_BUTTON_PAGE_REG).click()     
        driver.find_element(*Locators.EMAIL_ENTRY).send_keys(email_fix)
        driver.find_element(*Locators.PASSWORD_ENTRY).send_keys(password_fix)
        driver.find_element(*Locators.ENTRY_BUTTON_PAGE_ENTRY).click()
        driver.find_element(*Locators.ACCOUNT_BUTTON).click() 

        profile_text = WebDriverWait(driver, 10, poll_frequency=0.5).until(EC.visibility_of_element_located(Locators.PROFILE)).text
        assert profile_text == 'Профиль'
   
    #4 вход через кнопку в форме восстановления пароля
    def test_success_entry_pas_recover(self, driver): 
        driver.find_element(*Locators.ENTRY_BUTTON).click()
        driver.find_element(*Locators.BUTTON_RECOVER_PAS).click()
        driver.find_element(*Locators.ENTRY_BUTTON_RECOVER_PAS).click()     
        driver.find_element(*Locators.EMAIL_ENTRY).send_keys(email_fix)
        driver.find_element(*Locators.PASSWORD_ENTRY).send_keys(password_fix)
        driver.find_element(*Locators.ENTRY_BUTTON_PAGE_ENTRY).click()
        driver.find_element(*Locators.ACCOUNT_BUTTON).click() 

        profile_text = WebDriverWait(driver, 10, poll_frequency=0.5).until(EC.visibility_of_element_located(Locators.PROFILE)).text
        assert profile_text == 'Профиль'

    #5 выход из аккаунта
    def test_success_exit(self, login_account_main): 
        driver = login_account_main
        driver.find_element(*Locators.EXIT_BUTTON_PROFILE).click()
        WebDriverWait(driver, 10, poll_frequency=0.5).until(EC.url_to_be(entry_site))
        assert driver.current_url == entry_site
    


