# работа с пользователем

# действия со справочником
def action_user():
    action = int(input('Выбор действий: \n Добавить контакт - 1 \n Найти контакт - 2 \n Изменить контакт - 3'
                       '\n Удалить контакт - 4 \n Показать все контакты - 5 \n Выйти - 6 \n Введите нужную цифру: ')) 
    return action

# получение данных пользователя
def get_info():
    name = input('Введите имя: ')
    surname = input('Введите фамилию: ')
    phone_number = int(input('Введите номер телефона: '))
    
    return name + ' ' + surname + ' ' + str(phone_number) + '\n'
    
# данные для поиска
def data_from_search():
    return input('Введите фамилии и (или) имя: ')
    