import requests
import allure
import urls


class UserApi:
    @allure.step('Создание пользователя')
    def create_user(payload):
        return requests.post(urls.CREATE_USER, json=payload)
    

    @allure.step('Авторизация пользователя')
    def login_user(payload):
        return requests.post(urls.LOGIN_USER, json=payload)
    

    @allure.step('Обновление информации о пользователе')
    def update_user(payload, token):
        if token:
            return requests.patch(urls.UPDATE_USER, headers={"Authorization": token}, json=payload)
        else:
            return requests.patch(urls.UPDATE_USER, json=payload)
    

    @allure.step('Удаление пользователя')
    def delete_user(token):
        return requests.delete(urls.DELETE_USER, headers={"Authorization": token})


class IngredientApi:
    @allure.step('Получение данных об ингредиентах')
    def get_ingredients():
        return requests.get(urls.GET_INGREDIENTS)


class OrderApi:
    @allure.step('Создание заказа')
    def create_order(payload, token):
        if token:
            return requests.post(urls.CREATE_ORDER, headers={"Authorization": token}, json=payload)
        else:
            return requests.post(urls.CREATE_ORDER, json=payload)


    @allure.step('Получение заказов пользователя')
    def get_orders(token):
        if token:
            return requests.get(urls.GET_ORDERS_BY_USER, headers={"Authorization": token})
        else:
            return requests.get(urls.GET_ORDERS_BY_USER)
