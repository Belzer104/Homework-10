from classes import AddressBook, Record

'''
Создаем деккоратор который отлавливает ошибки
(Неверная команда, не достаточно аргументов, не найдены контакты)
'''
def input_error(func):
    def inner(*args, **kwargs):

        try:           
            return func(*args, **kwargs)
                        
        except KeyError:
            return 'This contact doesnt exist, please try again.'

        except ValueError as exception:
            return exception.args[0]

        except IndexError:
            return 'This contac cannot be added'
        except AttributeError:
            return 'No have information'
        except TypeError:
            return 'Unknown command or parametrs, please try again.'
                       
    return inner

'''
Создаем функцию "hello" которая будет возвращать ответ 
после того как пользователь запустит бот
'''
def hello():
    print("How can I help you?")


'''
Создаем функцию add_contact, которая создает новый контакт,
или сообщение о том что контакт уже создан
'''
@input_error
def add_contact(user_info, *_):

    name = user_info[0]
    if name not in contacts:
        contacts.add_record(name)
        return f"Coantact_add {name}."
    else:
        return f"Contact {name} is used."


'''
Создаем функцию add_number которая добавляет номер телевона к указаному контакту
'''
@input_error
def add_number(record: Record, user_info):
        return record.add_phone(user_info[1])


'''    
Создаем функцию "change" которая изменяет старый номер телефона 
на новый
'''    
@input_error
def change (record, user_info):
    return record.edit_phone(user_info[1], user_info[2])


'''
Создаем функцию delete_phone, которая удаляет телефон
у указаного пользователя 
'''
@input_error
def delete_phone(record, user_info):
    return record.delete_phone(user_info[1])
        

'''
Создаем функцию "phone" которая ищет данные по ключу и выводит: 
ключ и текущее значение, которое есть в словаре "contacts" 
'''
@input_error
def phones(record, *_):
    return f"{record.name.value} contact phone numbers are: {[v.value for v in record.phones]}"

'''
Создаем функцию "show_all" которая выводит:
всю книгу контактов хранящуюся в словаре "contacts"
'''
@input_error
def show_all(*_):

    full_list = []
    for contact_name, numbers in contacts.items():
        full_list.append(f"{contact_name} have phones {[v.value for v in numbers.phones]}")
    return full_list

'''
Создаем функцию "close" которая завершает работу
бота (прирывает цикл в функции "main")
'''
def close(*_):

    print("Good bye!")
    quit()

'''
Создаем функция для извлечения комынды
'''
def split_user_input(user_command):

    command_split = user_command.split()

    if command_split[0] in ("show", "good", "delete"):
        return [" ".join(command_split[:2]), command_split[2:]]
    
    else:
        return [command_split[0], command_split[1:]]


'''
Создаем функцию реализации функционала
'''
@input_error
def functional(command: str):

    signature = commands[command]

    return signature

'''
Создадим функцию help_me которая отобразит пользователю команды и как с ними работать
'''
def help_me(*_):
    return  "Contact - обозначение контакта, Phone - обозначение телефона, OldPhone, - старый номер телефона\n"\
            "Команда (create) создает Сontact, пример (create Contact)\n"\
            "Команда (add) добавляет Phone к уже созданому Contact, пример (add Contact phone)\n"\
            "Команда (change) заменяет OldPhone на новый Phone, пример (change Contact OldPhone Phone)\n"\
            "Команда (phone) отображает все доступные телефоны у Contact, пример (phone Contact)\n"\
            "Команда (delete phone) удаляет номер Phone у Contact, пример (delete phone Contact Phone)\n"\
            "Команда (show all) отображает все доступные Contact в словаре, пример (show all)\n"\
            "Команды (good bye, close, exit) заканчивают работу с ботом, пример (close)\n"\



'''
Создаем словарь с коммандами
'''
commands = {
            "help": help_me,
            "create": add_contact,
            "add": add_number,
            "change": change,
            "phone": phones,
            "delete phone": delete_phone,
            "show all": show_all,
            "good bye": close,
            "close": close,
            "exit": close
            }

'''
Создаем фукцию "main" в которой прописана вся логика
взаимодействия пользователя
'''
def main():

    '''
    Ожидается запуск бота
    '''
    bot_start = input("Start bot enter('Hello, Hi, Start'): ").casefold()

    if bot_start in ("hello","hi","start"): 
        '''
        Условия для запуски бота при определенных значениях
        '''  
        hello()

        '''
        Бесконечный цикл в котором обрабатываются команды
        '''
        while True:
            '''
            Ожидается действие от пользователя
            '''
            user_command = input("Please enter (help): ").casefold()
            command, user_data = split_user_input(user_command)

            if command not in commands:
                print(f"I don't know comand '{command}'")
                continue
            
            if command == "create":
                result = functional(command)(user_data)
                print(result)
                continue

            try:
                record = contacts[user_data[0]] if user_data else None
            except KeyError:
                print(f"Contact {user_data[0]} don't found")
                continue

            result = functional(command)(record, user_data)

            if result:
                if type(result) is list:
                    print(*result, sep="\n")
                else:
                    print(result)

    elif bot_start in ("exit", "close","good bye"):
        '''
        Условие для закрытия бота если пользователь передумал
        ''' 
        close()

    else:
        '''
        Условие если пользователь не запустил бот
        '''
        print("Bot don't start") 

        
if __name__ == "__main__":

    contacts = AddressBook()
    main()