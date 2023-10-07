# работа с data
from view import *

# запись информации о новом контакте
def add_info(info):
    with open('data.txt', 'a', encoding = 'utf-8') as file:
        file.write(info)

# поиск контакта
def search_info(info):
    with open('data.txt', 'r', encoding = 'utf-8') as file:
        lst = file.readlines()
        for id in range(len(lst)):
            if info in lst[id]:
                print(f'id пользователя: {id}, Данные пользователя: {lst[id]}')
                
# просмотр всего справочника 
def all_user_info():
    print('\nСписок контактов:')
    with open('data.txt', 'r', encoding = 'utf-8') as file:
        lst = [info.strip() for info in file.readlines()]
        for id in range(len(lst)):
            print(f'id: {id}, Информация: {lst[id]}')
    print()

# изменение контакта
def change_user_info():
    lst = []
    user_id = int(input('Введите id: '))
    with open('data.txt', 'r', encoding = 'utf-8') as file:
        lst = file.readlines()
    print(lst[user_id]+ '\n' + 'Введите новые данные:')
    lst[user_id] = get_info()
    
    with open('data.txt', 'w', encoding = 'utf-8') as file:
        for user in lst:
            file.write(user)

# удаление контакта
def remove_user_info():
    user_id = int(input('Введите id: '))
    with open('data.txt', 'r', encoding = 'utf-8') as file:
        lst = file.readlines()
    print(lst[user_id])
    confirm_deleted = int(input('Подтвердите удаление(1 - да, 2 - нет): ')) 
    match confirm_deleted:
        case 1:
            lst.pop(user_id)
            with open('data.txt', 'w', encoding = 'utf-8') as file:
                for user in lst:
                    file.write(user)
        case 2:
            print('Отмена операции.')
            