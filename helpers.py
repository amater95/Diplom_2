import string
import random
import api as api

from faker import Faker


def generate_user_data(empty_field=None):
    faker=Faker()

    user_data = {
        "email": generate_random_string(10)+"@yandex.ru",
        "password": faker.password(),
        "name": faker.name()
    }
    #Хотел email тоже через faker делать, но с ним периодически не проходят тесты связанные с созданием пользователя
    if empty_field is not None:
        user_data[empty_field] = ""
    return user_data


def generate_random_string(length):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for _ in range(length))
    return random_string


def generate_new_user_data(field):
    faker = Faker()
    if field == 'email':
        return faker.email()
    elif field == 'password':
        return faker.password()
    elif field == 'name':
        return faker.name()
