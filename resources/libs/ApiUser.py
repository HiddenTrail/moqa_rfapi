from requests import Session
from urllib.parse import urljoin
import logging


class ApiUser(Session):
    def __init__(self, url, username, password, auth_url=None):
        super().__init__()
        self.url = url
        self.username = username
        self.password = password
        if auth_url:
            self.fetch_token(auth_url)
            self.login_user(auth_url)

    def request(self, method, url, *args, **kwargs):
        if url.startswith('http'):
            joined_url = url
        else:
            joined_url = urljoin(self.url, url)
        logging.info(f'{method} Request to {joined_url}')
        logging.debug(f'Request headers: {self.headers}')
        response = super().request(method, joined_url, *args, **kwargs)
        logging.debug(f'Response: {response.text}')
        logging.debug(f'Response headers: {response.headers}')
        return response

    def fetch_token(self, auth_url):
        response = self.get(f'{auth_url}/samuli-paasimaa-ht/fake_auth/token')
        response.raise_for_status()
        json_response = response.json()
        try:
            self.access_token = json_response['access_token']
        except KeyError:
            raise AssertionError('access_token not present in the response')
        try:
            self.token_type = json_response['token_type']
        except KeyError:
            raise AssertionError('token_type not present in the response')
        self.headers['Authorization'] = f'{self.token_type} {self.access_token}'

    def login_user(self, auth_url):
        payload = {
            "username": self.username,
            "password": self.password
        }
        logging.info(f'Payload {payload}')
        response = self.post(f'{auth_url}/samuli-paasimaa-ht/fake_auth/login', json=payload)
        response.raise_for_status()
        json_response = response.json()
        assert 'username' and 'password' in json_response, \
            'username and/or password not present in the response'
        return json_response

    def get_users(self):
        response = self.get('/users')
        response.raise_for_status()
        json_response = response.json()
        user_id = 1
        for user in json_response:
            try:
                assert user['id'] == user_id, \
                    f'User id not as expected. Should be {user_id} but was {user["id"]}'
            except KeyError:
                raise AssertionError('id not present in the response')
            user_id += 1
        return json_response
