# Bill Generation Class

# Strategy Pattern

# To define Sales on particular days and discount for 
#particular prices

class Sales:

    def cost(self,price):

        pass

class SundaySales(Sales):

    def cost(self,price=100):

        return price*0.9
    
class Above1000(Sales):

    def cost(self,price=1100):

        return price*0.8
    
class Bill:

    def __init__(self,bill_amount):

        self.bill_amount=bill_amount

    def discount(self):

        return self.bill_amount.cost()


#Driver Code

S=SundaySales()
Sale=Bill(S)
print(Sale.discount())

T=Above1000()
Sale2=Bill(T)
print(Sale2.discount())
