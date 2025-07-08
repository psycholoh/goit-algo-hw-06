from collections import UserDict

class AddressBook(UserDict):





    def find(self, name):
        return self.data.get(name)


    def add_record(self, record):
        self.data[record.name.value] = record

    def delete(self, name):
        if name in self.data:
            del self.data[name]
        else:
            raise KeyError(f"No contact with name '{name}' found.")

    def __str__(self):
        if not self.data:
            return "AddressBook is empty."
        return '\n'.join(str(record) for record in self.data.values())





def parse_input(user_input):
    return user_input.strip().split()



class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):

        return str(self.value)

class Name(Field):
		pass

class Phone(Field):
    def __init__(self, value):
        if not value.isdigit() or len(value) != 10:
            raise ValueError("Phone number must be exactly 10 digits.")
        super().__init__(value)

    def add_phone(self, phone_number):
        phone = Phone(phone_number)
        self.phones.append(phone)

    def remove_phone(self, phone_number):
        for phone in self.phones:
            if phone.value == phone_number:
                self.phones.remove(phone)
                return
        raise ValueError("Phone number not found.")

    def edit_phone(self,old_number, new_number):
        for phone in self.phones:
            if phone.value == old_number:
                phone.value = Phone(new_number)
                return
        raise ValueError("Old phone number not found.")  


    def find_phone(self, phone_number):
        for phone in self.phones:
            if phone.value == phone_number:
                return phone
        return None
    


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []


    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
		pass


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Contact not found."
        except ValueError:
            return "Give me name and phone please."
        except IndexError:
            return "Enter user name."
    return inner

@input_error
def add_contact(command_parts, contacts):
    name, phone = command_parts[1], command_parts[2]
    contacts[name] = phone
    return "Contact added."

@input_error
def change_contact(command_parts, contacts):
    name, phone = command_parts[1], command_parts[2]
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    else:
        raise KeyError

@input_error
def show_phone(command_parts, contacts):
    name = command_parts[1]
    return contacts[name]


def show_all(contacts):
    if not contacts:
        return "No contacts found."
    return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])

def main():
    contacts = {}
    print("Welcome to the assistant bot!")

    while True:
        user_input = input(">>> ")
        command_parts = parse_input(user_input)

        if not command_parts:
            print("Invalid command.")
            continue

        command = command_parts[0].lower()
        result = ""

        if command == "add":
            result = add_contact(command_parts, contacts)
        elif command == "change":
            result = change_contact(command_parts, contacts)
        elif command == "phone":
            result = show_phone(command_parts, contacts)
        elif command == "all":
            result = show_all(contacts)
        elif command in ["exit", "close"]:
            print("Good bye!")
            break
        else:
            result = "Unknown command."

        if result:
            print(result)








if __name__ == "__main__":
    main()







