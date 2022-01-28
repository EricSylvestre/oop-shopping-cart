
class Donut:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def __repr__(self):
        return f"Donut({self.name}, ${self.price})"
       

food1 = Donut("Glazed", 3)
#---------
food2 = Donut("Chocolate", 3)
#---------
food3 = Donut("Powdered", 3)
#---------
food4= Donut("Frosted", 3)
#---------
food5= Donut("Special", 100)

menu = {
    1:food1, 2:food2, 3:food3, 4:food4, 5:food5
}

class Cart:
    def __init__(self):
        self.items = []
        self.total_cost = 0

    def add_donut(self, donut):
        self.items.append(donut)
        self.total_cost += donut.price

    def __repr__(self):
        return f"Cart({self.items} \nThis is your total cost: ${self.total_cost}"
    
        
cart = Cart()



print(f"Welcome to Eric's Donut Shop!")


while True:
    user_enter = input(f"Press 'V' to view inventory or 'E' to leave. ")
    if user_enter == "V":
        print(menu)
    elif user_enter == "E":
        print("Okay Bye")
        break


  
    choice= int(input(f"Which donut would you like? " ))
    donut_choice = menu[choice]
    cart.add_donut(donut_choice)
    print("This is your cart: ")
    print(" - " *17)
    print(cart)
    print(" - " *17)









        
    


