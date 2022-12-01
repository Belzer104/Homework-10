from collections import UserDict

'''
Создан класс AddressBook наследуемый от UserDict
в котором хранится словарь с контактами
'''
class AddressBook(UserDict):
    
    '''
    Создан метод класа который записывает 
    все данные которые вводит пользователь 
    '''
    def add_record(self, name):
        self.data[name] = Record(name)

'''
Создан класс Record, который отвечает за логику 
добавления/удаления/редактирования 
необязательных полей и хранения обязательного поля Name.
'''
class Record:

    def __init__(self, name, phone=None):
        self.name = Name(name)
        self.phones = [Phone(phone)] if phone else []

    '''
    Метод отвечающий за удаоение необязательных значений
    '''
    def delete_phone(self, number):
        for values in self.phones:
            if values.value == number:
                self.phones.remove(values)
                return f"Phone number {number} delete for contact {self.name.value}."
        else:
            return f"Don't find {number} in contact {self.name.value}"
    '''
    Метод отвечающий за изменение необязательных значений
    '''
    def edit_phone(self, old_number, new_number):
        for values in self.phones:
            if values.value == old_number:
                values.value = new_number
                return f"Phone number {old_number} has change {new_number} in contact {self.name.value}."
        else:
            return f"Don't find {old_number} in contact {self.name.value}"
    
    '''
    Метод отвечающий за добавление необязательных значений
    '''
    def add_phone(self, number):
        self.phones.append(Phone(number))
        return f"Phone number {number} add in contact {self.name.value}."

'''
Класс Field, на будущее
'''
class Field:
    def __init__(self, name):
        self.value = name

'''
Класс Name наследуется из класа Field, на будущее
'''
class Name(Field):
    pass

'''
Класс Phone наследуется из класа Field, на будущее
'''
class Phone(Field):
    pass