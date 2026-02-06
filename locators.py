from selenium.webdriver.common.by import By


class Locators:
    # Локаторы для регистрации
    ENTRY_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']") #кнопка "Войти в аккаунт" на главной странице
    REG_BUTTON = (By.XPATH, "//a[text()='Зарегистрироваться']") #кнопка "Зарегистрироваться" под формой входа
    NAME = (By.XPATH, "//*[@id='root']/div/main/div/form/fieldset[1]/div/div/input")  #поле "Имя" в форме регистрации
    EMAIL = (By.XPATH, "//*[@id='root']/div/main/div/form/fieldset[2]/div/div/input")  #поле "Email" в форме регистрации
    PASSWORD = (By.XPATH, "//*[@id='root']/div/main/div/form/fieldset[3]/div/div/input") #поле "Пароль" в форме регистрации
    REGISTER_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']") #кнопка "Зарегистрироваться" под формой регистрации
    REG_POPUP = (By.XPATH, "//p[text()='Некорректный пароль']") #сообщение об ошибке при вводе невалидного пароля 

    #локаторы для входа в аккаунт
    EMAIL_ENTRY = (By.XPATH, "//h2/following-sibling::form//fieldset/div/div/input") #поле "Email" в форме входа
    PASSWORD_ENTRY =(By.XPATH, "//h2/following-sibling::form//input[@name='Пароль']") #поле "Пароль" в форме входа
    ENTRY_BUTTON_PAGE_ENTRY = (By.XPATH, "//button[text()='Войти']") #кнопка "Войти" на странице входа
    ACCOUNT_BUTTON = (By.XPATH, "//*[@id='root']/div/header/nav/a") #кнопка "Личный кабинет" для зарегистрированных пользователей
    PROFILE = (By.XPATH, "//a[text()='Профиль']") #строка "Профиль" с данными пользователя в личном кабинете
    ENTRY_BUTTON_PAGE_REG = (By.XPATH, "//p[text()='Уже зарегистрированы?']/a[text()='Войти']") #кнопка "Войти" на странице регистрации
    BUTTON_RECOVER_PAS = (By.XPATH, "//a[text()='Восстановить пароль']") #кнопка "Восстановить пароль" на странице входа
    ENTRY_BUTTON_RECOVER_PAS = (By.XPATH, "//p[text()='Вспомнили пароль?']/a[text()='Войти']") #кнопка "Войти" на странице восстановления пароля

    #локаторы для выхода из аккаунта
    EXIT_BUTTON_PROFILE = (By.XPATH, "//button [text()='Выход']") #кнопка "Выход" на странице профиля

    #локаторы для переходов
    ACCOUNT_KONS = (By.XPATH, "//*[@id='root']/div/header/nav/ul/li[1]/a") #кнопка "Конструктор" на странице профиля
    ACCOUNT_LOG = (By.XPATH, "//*[@id='root']/div/header/nav/div/a") #логотип на странице профиля
    FILLINGS_SECTION = (By.XPATH, "//span[text()='Начинки']")  #раздел "Начинки" на главной странице
    TEXT_FILLINGS = (By.XPATH, "//h2[text()='Начинки']") #заголовок раздела "Начинки" на главной странице
    SAUCES_SECTION = (By.XPATH, "//span[text()='Соусы']")  #раздел "Соусы" на главной странице
    TEXT_SAUCES = (By.XPATH, "//h2[text()='Соусы']") #заголовок раздела "Соусы" на главной странице
    BUNS_SECTION = (By.XPATH, "//span[text()='Булки']")  #раздел "Булки" на главной странице
    TEXT_BUNS = (By.XPATH, "//h2[text()='Булки']") #заголовок раздела "Булки" на главной странице