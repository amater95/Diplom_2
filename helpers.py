import string
import random
import api

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


def create_user(user_data):
    response = api.create_user(user_data)
    response_payload = response.json()
    user_data['accessToken'] = response_payload['accessToken']


def login_user(user_data):
    data_for_login = {
        'email': user_data['email'],
        'password': user_data['password']
    }
    response = api.login_user(data_for_login)
    response_payload = response.json()
    user_data['accessToken'] = response_payload['accessToken']


def delete_user(user_data):
    api.delete_user(user_data['accessToken'])


def generate_new_user_data(field):
    faker = Faker()
    if field == 'email':
        return faker.email()
    elif field == 'password':
        return faker.password()
    elif field == 'name':
        return faker.name()


def get_ingredient_list_id():
    response = api.get_ingredients()
    ingredients = response.json()['data']
    list_id = []
    for ingredient in ingredients:
        list_id.append(ingredient['_id'])
        if len(list_id) >= random.randint(1, 5):
            break
    return list_id
