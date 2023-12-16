import pickle
import datetime

from inventory import Inventory

class Customer:

    def __init__(self, name, contact, address):
        self.name = name
        self.contact = contact
        self.address = address
        self.order_history = {}

        details = [self.name, self.contact, self.address, self.order_history]
        self.dump_to_file(details)

    def load_customer_details(self, det):
        with open('customer_details.txt', 'wb') as f:
            pickle.dump(det, f)

    def place_order(self, order_no):
        self.order_history[order_no] = datetime.datetime.now().strftime("%d/%m/%y")

    def view_order_history(self):
        for i in self.order_history:
            print(f"Order Number:", i, "Placed On", self.order_history[i])

    def view_available_items(self):
        inventory_instance = Inventory()
        print(inventory_instance.view_all_items())

    def add_details(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def change_details(self):
        user_menu = int(input("Enter 1 to Change name\nEnter 2 to change Contact Number\nEnter 3 to change Address"))
        if user_menu == 1:
            new_n = input("Enter new name: ")
            self.name = new_n
        elif user_menu == 2:
            new_contact = input("Enter new contact: ")
            self.contact = new_contact
        elif user_menu == 3:
            new_address = input("Enter new address: ")

    def remove_details(self):
        user_menu = int(input("Enter 1 to remove name\nEnter 2 to remove Contact Number\nEnter 3 to remove Address"))
        if user_menu == 1:
            self.name = None
        elif user_menu == 2:
            self.contact = None
        elif user_menu == 3:
            self.address = None

    def view_customer_details(self):
        with open ('customer_details.txt','rb') as f:
            data=pickle.load(f)
        
        for row in data:
            print(row)


C=Customer('A','1','5,Park road')

C.view_customer_details()
