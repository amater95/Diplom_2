import allure
import data

from api import OrderApi


@allure.suite('Получение заказов конкретного пользователя')
class TestGetOrder:
    @allure.title('Авторизованный пользователь')
    @allure.description('Отправляем запрос на получение заказов после авторизации')
    def test_get_orders_after_auth(self, logged, valid_ingredient_list_id):
        token = logged['accessToken']
        order_payload = {
            'ingredients': valid_ingredient_list_id
        }
        response = OrderApi.create_order(order_payload, token)
        assert response.status_code == 200
        response = OrderApi.get_orders(token)
        response_payload = response.json()
        assert response.status_code == 200
        assert response_payload['success'] is True
        assert len(response_payload['orders']) == 1
        assert response_payload['orders'][0]['ingredients'][0] in order_payload['ingredients']


    @allure.title('Неавторизованный пользователь')
    @allure.description('Отправляем запрос на получение заказов без авторизации')
    def test_get_orders_without_auth(self):
        token = None
        response = OrderApi.get_orders(token)
        assert response.status_code == 401
        assert response.json()['message'] == data.MESSAGE_WITHOUT_AUTHORIZED
