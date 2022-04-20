import keyсloakfunc
import pprint
import os
import sys


def menu():
    """
    Текстовый интерфейс для управления утилитой
    """


route = input('Что требуется сделать?\n'
              '1 - Узнать айди всех пользователей и их параметры\n'
              '2 - Узнать айди всех групп\n'
              '3 - Узнать айди конкретного пользователя\n'
              '4 - Узнать айди определенной группы\n'
              '5 - Создать пользователя\n'
              '6 - Добавить пользователя в группу(нужен айди пользователя и группы)\n'
              '7 - Узнать в каких группах состоит пользователь(нужен айди)\n'
              '8 - Удалить пользователя\n'
              '9 - Удалить пользователя из группы(id группы и пользователя)\n'
              'q - закрыть утилиту\n')
if route == '1':
    pprint.pprint(keyсloakfunc.all_users_id())
elif route == '2':
    pprint.pprint(keyсloakfunc.groups_list())
elif route == '3':
    pprint.pprint(keyсloakfunc.users_id())
elif route == '4':
    pprint.pprint(keyсloakfunc.group_list())
elif route == '5':
    pprint.pprint(keyсloakfunc.create_client())
elif route == '6':
    pprint.pprint(keyсloakfunc.add_group_to_user())
elif route == '7':
    pprint.pprint(keyсloakfunc.user_groups())
elif route == '8':
    pprint.pprint(keyсloakfunc.del_user())
elif route == '9':
    pprint.pprint(keyсloakfunc.del_user_from_group())
elif route == 'q':
    exit(0)

os.execl(sys.executable, sys.executable, *sys.argv)
