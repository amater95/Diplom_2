from api import UserApi


def create_user(user_data):
    response = UserApi.create_user(user_data)
    response_payload = response.json()
    user_data['accessToken'] = response_payload['accessToken']


def login_user(user_data):
    data_for_login = {
        'email': user_data['email'],
        'password': user_data['password']
    }
    response = UserApi.login_user(data_for_login)
    response_payload = response.json()
    user_data['accessToken'] = response_payload['accessToken']


def delete_user(user_data):
    UserApi.delete_user(user_data['accessToken'])


def try_delete_user(user_data):
    response = UserApi.login_user(user_data)
    if response.status_code == 200 and 'accessToken' in response.json():
        UserApi.delete_user(response.json()['accessToken'])
