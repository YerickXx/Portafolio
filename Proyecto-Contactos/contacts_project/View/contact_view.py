from Controller.CRUD import *

class ContactView:

    def main_menu():
       while True:
        print("Menu")
        print("1.Add contact")
        print("2.delete contact")
        print("3.show contact")
        print("4.update contact")
        print("5.exit")

        return input("Enter the option you want to execute: ")
    
    def get_contact_info(self):
        name = input("Enter name: ")
        phone = input("Enter phone: ")
        return name, phone
    
    def get_contact_id(self):
        return input("Enter the ID to delete: ")
    
    def show_contacts(self, contacts):
     for contact in contacts:
        print(contact)

    def show_message(self, msg):
        print(msg)
