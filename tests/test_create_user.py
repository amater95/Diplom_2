import pytest
import allure
import data
import helpers

from api import UserApi


@allure.suite('Создание пользователя')
class TestCreateUser:
    @allure.title('Создание уникального пользователя')
    @allure.description('Отправляем запрос на создание пользователя с вновь сгенерированными данными')
    def test_create_user(self, create_user_data):
        response = UserApi.create_user(create_user_data)
        assert response.status_code == 200
        response_payload = response.json()
        assert response_payload['success'] is True
        assert len(response_payload['accessToken']) > 0


    @allure.title('Создание пользователя, который уже зарегистрирован')
    @allure.description('Отправляем запрос на создание уже зарегистрированного пользователя')
    def test_create_user_twice(self, created_user_data):
        response = UserApi.create_user(created_user_data)
        assert response.status_code == 403
        assert response.json()["message"] == data.MESSAGE_USER_ALREADY_EXISTS


    @allure.title('Создать пользователя и не заполнить одно из обязательных полей')
    @allure.description('Отправляем запрос на создание пользователя с вновь сгенерированными данными, но без одного из обязательных полей')
    @pytest.mark.parametrize(
        'user_data',
        [
            helpers.generate_user_data(empty_field='email'),
            helpers.generate_user_data(empty_field='password'),
            helpers.generate_user_data(empty_field='name')
        ]
    )
    def test_create_user_withouth_one_field(self, user_data):
        response = UserApi.create_user(user_data)
        assert response.status_code == 403
        assert response.json()["message"] == data.MESSAGE_USER_MISSED_FIELD
