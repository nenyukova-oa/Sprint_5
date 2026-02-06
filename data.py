from faker import Faker

faker = Faker()

email_fix = 'ol_n38@dfsdf.ru'
password_fix = 'f12345678'

# Функция для генерации с валидными данными
def generate_registration_valid():
    name = faker.name()
    email = faker.email()
    password = faker.password(length=10)
    return name, email, password

# Функция для генерации данных с невалидным паролем
def generate_registration_with_invalid_password():
    name = faker.name()
    email = faker.email()
    password = faker.password(length=5)
    return name, email, password