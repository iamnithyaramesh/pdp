from vegetable import Vegetable

class Inventory:

    def __init__(self,items):

        self.items=items
    
    def view_items(self):

        for i in self.items:

            return i , self.items[i]
    
    def remove_item(self,p_id):

        for i in self.items:

            if i==p_id:

                self.items.pop(i)
        
    def add_item(self,p_id,item):

        self.items[p_id]=item
    
    def search_item(self,p_id):

        for i in self.items:

            if i==p_id:

                print('true')
            
            else:

                print('false')