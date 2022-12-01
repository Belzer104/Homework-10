from collections import UserDict

class AddressBook(UserDict):

    def add_record(self, name):
        self.data[name] = Record(name)


class Record:

    def __init__(self, name, phone=None):
        self.name = Name(name)
        self.phones = [Phone(phone)] if phone else []

    def delete_phone(self, number):
        for values in self.phones:
            if values.value == number:
                self.phones.remove(values)
                return f"Phone number {number} delete for contact {self.name.value}."
        else:
            return f"Don't find {number} in contact {self.name.value}"

    def edit_phone(self, old_number, new_number):
        for values in self.phones:
            if values.value == old_number:
                values.value = new_number
                return f"Phone number {old_number} has change {new_number} in contact {self.name.value}."
        else:
            return f"Don't find {old_number} in contact {self.name.value}"

    def add_phone(self, number):
        self.phones.append(Phone(number))
        return f"Phone number {number} add in contact {self.name.value}."


class Field:
    def __init__(self, name):
        self.value = name


class Name(Field):
    pass


class Phone(Field):
    pass