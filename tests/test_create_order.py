import allure
import data

from api import OrderApi


@allure.suite('Создание заказа')
class TestCreateOrder:
    @allure.title('С авторизацией и ингредиентами')
    @allure.description('Отправляем запрос на создание заказа с авторизацией и корректными ингредиентами')
    def test_create_correct_order_after_auth(self, logged, valid_ingredient_list_id):
        payload = {
            'ingredients': valid_ingredient_list_id
        }
        token = logged['accessToken']
        response = OrderApi.create_order(payload, token)
        assert response.status_code == 200
        assert response.json()['success'] is True


    @allure.title('Без авторизации')
    @allure.description('Отправляем запрос на создание заказа без авторизации и с корректными ингредиентами')
    def test_create_order_without_auth(self, valid_ingredient_list_id):
        payload = {
            'ingredients': valid_ingredient_list_id
        }
        token = None
        response = OrderApi.create_order(payload, token)
        assert response.status_code == 200
        assert response.json()['success'] is True


    @allure.title('Без ингредиентов')
    @allure.description('Отправляем запрос на создание заказа с авторизацией и без ингредиентов')
    def test_create_order_without_ingredients(self, logged):
        payload = {
            'ingredients': []
        }
        token = logged['accessToken']
        response = OrderApi.create_order(payload, token)
        assert response.status_code == 400
        assert response.json()['message'] == data.MESSAGE_MISSED_INGREDIENTS


    @allure.title('С неверным хешем ингредиентов')
    @allure.description('Отправляем запрос на создание заказа с авторизацией и с неверным хешем ингредиентов')
    def test_create_order_with_invalid_ingredients(self, logged):
        payload = {
            'ingredients': data.INVALID_LIST_HASHES
        }
        token = logged['accessToken']
        response = OrderApi.create_order(payload, token)
        assert response.status_code == 500
