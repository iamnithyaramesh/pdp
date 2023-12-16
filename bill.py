from vegetable import Vegetable


class Bill:
    def __init__(self, items=None, tax=None):
        self.items = items or {}
        self.tax = tax

    def calc_price(self):
        return sum(item.price * qty for item, qty in self.items.items())
    
    def create_receipt(self):
        receipt = []
        total_amount = 0
        
        for item, quantity in self.items.items():
            item_price = item.price * quantity
            total_amount += item_price
            item_info = {
                'name': item._name,
                'quantity': quantity,
                'price_per_unit': item.price,
                'total_price': item_price
            }
            receipt.append(item_info)
        
        # Adding the total amount to the receipt
        receipt.append({'total_amount': total_amount})
        
        return receipt

if __name__ == "__main__":
    # Creating instances of Vegetable
    carrot = Vegetable(name="Carrot", price=1.50, stock=5)
    tomato = Vegetable(name="Tomato", price=2.00, stock=8)
    broccoli = Vegetable(name="Broccoli", price=3.00, stock=6)
    spinach = Vegetable(name="Spinach", price=1.75, stock=9)
    onion = Vegetable(name="Onion", price=1.25, stock=7)

    # Creating a Bill instance
    bill = Bill()

    # Adding vegetables to the bill with quantities less than 10
    bill.items = {carrot: 3, tomato: 5, broccoli: 2, spinach: 4, onion: 3}

    # Calculating the total bill amount
    total_amount = bill.calc_price()

    # Creating and printing the receipt
    receipt = bill.create_receipt()
    print(receipt)