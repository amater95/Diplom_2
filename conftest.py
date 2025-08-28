import pytest
import helpers


@pytest.fixture
def create_user_data():
    user_data = helpers.generate_user_data()
    return user_data


@pytest.fixture
def created_user_data():
    user_data = helpers.generate_user_data()
    helpers.create_user(user_data)
    yield user_data
    helpers.delete_user(user_data)


@pytest.fixture
def logged():
    user_data = helpers.generate_user_data()
    helpers.create_user(user_data)
    helpers.login_user(user_data)
    yield user_data
    helpers.delete_user(user_data)


@pytest.fixture
def valid_ingredient_list_id():
    return helpers.get_ingredient_list_id()
