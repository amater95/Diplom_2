import pytest
import helpers

from methods_api import user_api, ingredient_api


@pytest.fixture
def create_user_data():
    user_data = helpers.generate_user_data()
    yield user_data
    user_api.try_delete_user(user_data)


@pytest.fixture
def created_user_data(create_user_data):
    user_api.create_user(create_user_data)
    yield create_user_data
    user_api.delete_user(create_user_data)


@pytest.fixture
def logged(created_user_data):
    user_api.login_user(created_user_data)
    yield created_user_data
    user_api.delete_user(created_user_data)


@pytest.fixture
def valid_ingredient_list_id():
    return ingredient_api.get_ingredient_list_id()
