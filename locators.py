from selenium.webdriver.common.by import By
from data import TestData


class Locators:
    # Локаторы для регистрации
    ENTRY_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']") #кнопка "Войти в аккаунт" на главной странице
    REG_BUTTON = (By.XPATH, "//a[text()='Зарегистрироваться']") #кнопка "Зарегистрироваться" под формой входа
    NAME = (By.XPATH, "//h2[text()='Регистрация']/following-sibling::form//label[text()='Имя']/following-sibling::input")  #поле "Имя" в форме регистрации
    EMAIL = (By.XPATH, "//h2[text()='Регистрация']/following-sibling::form//label[text()='Email']/following-sibling::input")  #поле "Email" в форме регистрации
    PASSWORD = (By.XPATH, "//h2[text()='Регистрация']/following-sibling::form//input[@type='password']") #поле "Пароль" в форме регистрации
    REGISTER_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']") #кнопка "Зарегистрироваться" под формой регистрации
    REG_POPUP = (By.XPATH, f"//p[text()='{TestData.ERROR_INVALID_PASSWORD}']") #сообщение об ошибке при вводе невалидного пароля

    #локаторы для входа в аккаунт
    EMAIL_ENTRY = (By.XPATH, "//h2[text()='Вход']/following-sibling::form//label[text()='Email']/following-sibling::input") #поле "Email" в форме входа
    PASSWORD_ENTRY =(By.XPATH, "//h2[text()='Вход']/following-sibling::form//input[@name='Пароль']") #поле "Пароль" в форме входа
    ENTRY_BUTTON_PAGE_ENTRY = (By.XPATH, "//button[text()='Войти']") #кнопка "Войти" на странице входа
    ACCOUNT_BUTTON = (By.XPATH, "//p[text()='Личный Кабинет']") #кнопка "Личный кабинет" для зарегистрированных пользователей
    ENTRY_BUTTON_PAGE_REG = (By.XPATH, "//p[text()='Уже зарегистрированы?']/a[text()='Войти']") #кнопка "Войти" на странице регистрации
    BUTTON_RECOVER_PAS = (By.XPATH, "//a[text()='Восстановить пароль']") #кнопка "Восстановить пароль" на странице входа
    ENTRY_BUTTON_RECOVER_PAS = (By.XPATH, "//p[text()='Вспомнили пароль?']/a[text()='Войти']") #кнопка "Войти" на странице восстановления пароля
    PROFILE = (By.XPATH, f"//a[text()='{TestData.PROFILE_TEXT}']") #строка "Профиль" с данными пользователя в личном кабинете

    #локаторы для выхода из аккаунта
    EXIT_BUTTON_PROFILE = (By.XPATH, "//button [text()='Выход']") #кнопка "Выход" на странице профиля

    #локаторы для переходов
    ACCOUNT_KONS = (By.XPATH, "//p[text()='Конструктор']") #кнопка "Конструктор" на странице профиля
    ACCOUNT_LOG = (By.XPATH, "//*[local-name()='svg' and @viewBox='0 0 290 50']") #логотип на странице профиля
    FILLINGS_SECTION = (By.XPATH, "//span[text()='Начинки']")  #раздел "Начинки" на главной странице
    TEXT_FILLINGS = (By.XPATH, f"//h2[text()='{TestData.FILLINGS_T}']") #заголовок раздела "Начинки" на главной странице
    SAUCES_SECTION = (By.XPATH, "//span[text()='Соусы']")  #раздел "Соусы" на главной странице
    TEXT_SAUCES = (By.XPATH, f"//h2[text()='{TestData.SAUCES_T}']") #заголовок раздела "Соусы" на главной странице
    BUNS_SECTION = (By.XPATH, "//span[text()='Булки']")  #раздел "Булки" на главной странице
    TEXT_BUNS = (By.XPATH, f"//h2[text()='{TestData.BUNS_T}']") #заголовок раздела "Булки" на главной странице