from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import Locators
from curl import *


class TestTransitions:

    #1 переход по клику на «Личный кабинет»
    def test_success_transition_account(self, login_account_main): 
        profile_text = login_account_main.find_element(*Locators.PROFILE).text
        assert profile_text == 'Профиль' 
    
    #2 переход из личного кабинета на главную страницу по клику на Конструктор
    def test_success_transition_kons(self, login_account_main): 
        driver = login_account_main
        driver.find_element(*Locators.ACCOUNT_KONS).click()
        WebDriverWait(driver, 10, poll_frequency=0.5).until(EC.url_to_be(main_site))
        assert driver.current_url == main_site

    #3 переход из личного кабинета на главную страницу по клику на логотип Stellar Burgers
    def test_success_transition_log(self, login_account_main): 
        driver = login_account_main
        driver.find_element(*Locators.ACCOUNT_LOG).click()
        WebDriverWait(driver, 10, poll_frequency=0.5).until(EC.url_to_be(main_site))
        assert driver.current_url == main_site
    
    #4 переход к разделу "Начинки"
    def test_success_transition_fillings(self, driver): 
        driver.find_element(*Locators.FILLINGS_SECTION).click()
        
        fillings_text = WebDriverWait(driver, 10, poll_frequency=0.5).until(EC.visibility_of_element_located(Locators.TEXT_FILLINGS)).text
        assert fillings_text == 'Начинки'
   
    #5 переход к разделу "Соусы"
    def test_success_transition_sauces(self, driver): 
        driver.find_element(*Locators.SAUCES_SECTION).click()
        
        success_text = WebDriverWait(driver, 10, poll_frequency=0.5).until(EC.visibility_of_element_located(Locators.TEXT_SAUCES)).text
        assert success_text == 'Соусы'
    
    #6 переход к разделу "Булки"
    def test_success_transition_buns(self, driver): 
        driver.find_element(*Locators.SAUCES_SECTION).click()
        WebDriverWait(driver, 10, poll_frequency=0.5).until(EC.visibility_of_element_located(Locators.TEXT_SAUCES)).text
        driver.find_element(*Locators.BUNS_SECTION).click()
        
        buns_text = WebDriverWait(driver, 10, poll_frequency=0.5).until(EC.visibility_of_element_located(Locators.TEXT_BUNS)).text
        assert buns_text == 'Булки'

