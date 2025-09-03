import pytest
import allure
import data
import helpers

from api import UserApi


@allure.suite('Логин пользователя')
class TestLoginUser:
    @allure.title('Логин под существующим пользователем')
    @allure.description('Отправляем запрос на авторизацию существующего пользователя')
    def test_login_user_with_correct_user_data(self, created_user_data):
        response = UserApi.login_user(created_user_data)
        assert response.status_code == 200
        assert response.json()["success"] is True


    @allure.title('Логин с неверным логином и паролем')
    @allure.description('Создаём пользователя и авторизуем его с некорректным логином и паролем')
    @pytest.mark.parametrize(
        'incorrect_field',
        [
            'email',
            'password'
        ]
    )
    def test_login_user_with_incorrect_user_data(self, created_user_data, incorrect_field):
        created_user_data[incorrect_field] = helpers.generate_new_user_data(incorrect_field)
        response = UserApi.login_user(created_user_data)
        payload = response.json()
        assert response.status_code == 401
        assert payload["success"] is False
        assert payload["message"] == data.MESSAGE_INCORRECT_LOGIN_OR_PASWORD
