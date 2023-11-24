class Customer:

    def __init__(self,name,ph_no):

        self.name=name
        self.ph_no=ph_no
    
    def show_shop(self,shop_name):

        print("Welcome to",shop_name)
        
    def update(self,product_list):

        print(f"Hey {self.name} These are the available vegetables:",product_list)
    

class Vendor:

    def __init__(self,reg_no,shop_name):

        self.reg_no=reg_no
        self.shop_name=shop_name
        self.customer_list=[]
        self.product_list=['Tomato','Onion','Potato']
    
    def add_customer(self,other):

        self.customer_list.append(other)
    
    def display_products(self):

        for i in self.customer_list:
            i.update(self.product_list)
    
    def display_shop(self):
        for i in self.customer_list:
            i.show_shop(self.shop_name)