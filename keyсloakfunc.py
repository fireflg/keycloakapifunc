import requests
import ast
import pprint
from requests import Response
import json


def get_token():
    url = 'https://YOUR_URL/auth/realms/master/protocol/openid-connect/token'

    params = dict(client_id='admin-cli', grant_type='password', username='', password='')
    x = requests.post(url, params, verify=False).content.decode('utf-8')
    return ast.literal_eval(x)['access_token']


def create_client():
    url = 'https://YOUR_URL/auth/admin/realms/botkin/users'

    headers = {
        'content-type': 'application/json',
        'Authorization': 'Bearer ' + str(get_token())
    }

    params = {"firstName": f'{input("Имя:")}', "lastName": f'{input("Фамилия:")}', "email": f'{input("Почта:")}',
              "enabled": "true",
              "username": f'{input("Имя пользователя:")}'
              }
    x = requests.post(url, headers=headers, json=params)


# pprint.pprint(create_client())


def groups_list():
    url = 'https://YOUR_URL/auth/admin/realms/botkin/groups/'
    headers = {
        'content-type': 'application/json',
        'Authorization': 'Bearer ' + str(get_token())
    }
    x = requests.get(url, headers=headers)
    print(x)
    return x.json()


def group_list():
    url = 'https://YOUR_URLi/auth/admin/realms/botkin/groups/'
    group_name = input("Введите имя группы:")
    headers = {
        'content-type': 'application/json',
        'Authorization': 'Bearer ' + str(get_token())
    }
    x = requests.get(url, headers=headers)
    x = x.json()
    for smth in x:
        if smth['name'] == f'{group_name}':
            x = smth
            break
    return x


def users_id():
    url = f'https://YOUR_URL/auth/admin/realms/botkin/users'
    username = input("Введите имя пользователя:")
    headers = {
        'content-type': 'application/json',
        'Authorization': 'Bearer ' + str(get_token())
    }
    params = {
        "username": f'{username}', "id": '',
        "enabled": "true"
    }
    x = requests.get(url, headers=headers, params=params)
    print(x)
    return x.json()


def all_users_id():
    url = f'https://YOUR_URL/auth/admin/realms/botkin/users'
    headers = {
        'content-type': 'application/json',
        'Authorization': 'Bearer ' + str(get_token())
    }

    x = requests.get(url, headers=headers)
    print(x)
    return x.json()


def add_group_to_user():
    errors = []
    userId = input("Id пользователя:")
    groupId = input("Id группы:")
    url = f'https://YOUR_URL/auth/admin/realms/botkin/users/{userId}/groups/{groupId}'
    headers = {
        'content-type': 'application/json',
        'Authorization': 'Bearer ' + str(get_token())
    }
    x = requests.put(url, headers=headers)
    if x.status_code != 200:
        errors.append(f'step {id}: {x.status_code} ({x.text})')
    if len(errors) > 0:
        for error in errors:
            print(error)
    else:
        print('Пользователь добавлен в группу!')


def user_groups():
    userId = input("Id пользователя:")
    url = f'https://YOUR_URL/auth/admin/realms/botkin/users/{userId}/groups/'
    headers = {
        'content-type': 'application/json',
        'Authorization': 'Bearer ' + str(get_token())
    }
    x = requests.get(url, headers=headers)
    return x.json()


def del_user():
    userId = input("Id пользователя:")
    url = f'https://YOUR_URL/auth/admin/realms/botkin/users/{userId}'
    headers = {
        'content-type': 'application/json',
        'Authorization': 'Bearer ' + str(get_token())
    }
    x = requests.delete(url, headers=headers)


def del_user_from_group():
    groupId = input("Id группы:")
    userId = input("Id пользователя:")
    url = f'https:/YOUR_URL/auth/admin/realms/botkin/users/{userId}/groups/{groupId}'
    headers = {
        'content-type': 'application/json',
        'Authorization': 'Bearer ' + str(get_token())
    }
    x = requests.delete(url, headers=headers)
