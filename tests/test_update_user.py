import pytest
import allure
import data
import helpers

from api import UserApi

@allure.suite('Изменение данных пользователя')
class TestUpdateUser:
    @allure.title('С авторизацией')
    @allure.description('Отправляем запрос на смену данных после авторизации')
    @pytest.mark.parametrize(
        'field_to_update', 
        [
            'email', 
            'password', 
            'name'
        ]
    )
    def test_update_user_after_auth(self, logged, field_to_update):
        token = logged['accessToken']
        new_value = helpers.generate_new_user_data(field_to_update)
        payload = {field_to_update: new_value}
        response = UserApi.update_user(payload, token)
        assert response.status_code == 200
        assert response.json()["success"] is True


    @allure.title('Без авторизации')
    @allure.description('Отправляем запрос на смену данных без авторизации')
    @pytest.mark.parametrize(
        'field_to_update', 
        [
            'email', 
            'password', 
            'name'
        ]
    )
    def test_update_user_without_auth(self, created_user_data, field_to_update):
        token = None
        new_value = helpers.generate_new_user_data(field_to_update)
        payload = {field_to_update: new_value}
        response = UserApi.update_user(payload, token)
        assert response.status_code == 401
        assert response.json()["success"] is False
        assert response.json()["message"] == data.MESSAGE_WITHOUT_AUTHORIZED
