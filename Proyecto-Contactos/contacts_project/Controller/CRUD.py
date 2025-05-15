from View.contact_view import ContactView
from Model.contact_db import ContactDB
from Model.contacto import contacto
import sqlite3 as db
import random
contact = ()

class Controller_contact:
     
    def __init__(self):
        self.db = ContactDB()
        self.view = ContactView()


    def run(self):
      while True:
            option = self.view.main_menu()

            if option == '1':
                name, phone = self.view.get_contact_info()
                contact_id = random.randint(1, 100)
                c = contacto(contact_id, name, phone)
                self.db.add_contact(c)
                self.view.show_message("Contact added.")

            elif option == '2':
                contact_id = self.view.get_contact_id()
                if self.db.delete_contact(contact_id):
                    self.view.show_message("Contact deleted.")
                else:
                    self.view.show_message("Contact not found.")

            elif option == '3':
                contacts = self.db.get_all_contacts()
                self.view.show_contacts(contacts)

            elif option == '4':
                self.view.show_message("Goodbye!")
                break

            else:
                self.view.show_message("Invalid option.")


