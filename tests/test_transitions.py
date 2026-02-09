import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import Locators
from data import *
from curl import *


class TestTransitions:

    #1 переход по клику на «Личный кабинет»
    def test_success_transition_account(self, login_account_main): 
        profile_text = login_account_main.find_element(*Locators.PROFILE).text
        assert profile_text == TestData.PROFILE_TEXT 
    
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
    
    #4 тест на переход к разделам "Начинки", "Соусы"
    @pytest.mark.parametrize("section_locator, text_locator, expected_text", [
        (Locators.FILLINGS_SECTION, Locators.TEXT_FILLINGS, f"{TestData.FILLINGS_T}"),
        (Locators.SAUCES_SECTION, Locators.TEXT_SAUCES, f"{TestData.SAUCES_T}"),
    ])
    def test_success_transition_to_sections(self, driver, section_locator, text_locator, expected_text):
        driver.find_element(*section_locator).click()       
        actual_text = WebDriverWait(driver, 10, poll_frequency=0.5).until(
            EC.visibility_of_element_located(text_locator)
        ).text
                
        assert actual_text == expected_text
    
    #5 переход к разделу "Булки" (не включен в параметризацию, т.к. раздел находится сверху главной страницы и 
    # клик на него не позволит выполнить проверку, нужен предварительный переход к другому разделу)
    def test_success_transition_buns(self, driver): 
        driver.find_element(*Locators.SAUCES_SECTION).click()
        WebDriverWait(driver, 10, poll_frequency=0.5).until(EC.visibility_of_element_located(Locators.TEXT_SAUCES)).text
        driver.find_element(*Locators.BUNS_SECTION).click()
        
        buns_text = WebDriverWait(driver, 10, poll_frequency=0.5).until(EC.visibility_of_element_located(Locators.TEXT_BUNS)).text
        assert buns_text == TestData.BUNS_T

