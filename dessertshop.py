from receipt import make_receipt
from desserts import (Candy,Cookie,IceCream,Sundae,Order)

class DessertShop:
    def user_prompt_candy(self):
        while True:
            try:
                name=input("Enter the name of your candy: ")
                break
            except ValueError:
                print("I don't know what you did")
                continue
        while True:
            try:
                candy_weight=float(input("Enter the weight purchased of your candy: "))
                break
            except ValueError:
                print("Not a float, try again")
                continue
        while True:
            try:
                price_per_pound=float(input("Enter the price per pound of your candy: "))
                break
            except ValueError:
                print("Not a number, try again")
                continue
        candy=Candy(name,candy_weight,price_per_pound)
        return candy
    
    def user_prompt_cookie(self):
        while True:
            try:
                name=input("Enter the name of your cookie: ")
                break
            except ValueError:
                print("I don't know what you did")
                continue
        while True:
            try:
                cookie_quantity=int(input("Enter the quantity purchased of your cookies: "))
                break
            except ValueError:
                print("Not a a whole number, try again")
                continue
        while True:
            try:
                price_per_dozen=float(input("Enter the price per dozen of your cookie: "))
                break
            except ValueError:
                print("Not a number, try again")
                continue
        cookie=Cookie(name,cookie_quantity,price_per_dozen)
        return cookie
    
    def user_prompt_icecream(self):
        while True:
            try:
                name=input("Enter the name of your icecream: ")
                break
            except ValueError:
                print("I don't know what you did")
                continue
        while True:
            try:
                scoop_count=int(input("Enter the scoop count purchased of your icecream: "))
                break
            except ValueError:
                print("Not a a whole number, try again")
                continue
        while True:
            try:
                price_per_scoop=float(input("Enter the price per scoop of your icecream: "))
                break
            except ValueError:
                print("Not a number, try again")
                continue
        icecream=IceCream(name,scoop_count,price_per_scoop)
        return icecream
    
    def user_prompt_sundae(self):
        while True:
            try:
                name=input("Enter the name of your sundae: ")
                break
            except ValueError:
                print("I don't know what you did")
                continue
        while True:
            try:
                scoop_count=int(input("Enter the scoop count purchased of your sundae: "))
                break
            except ValueError:
                print("Not a a whole number, try again")
                continue
        while True:
            try:
                price_per_scoop=float(input("Enter the price per scoop of your sundae: "))
                break
            except ValueError:
                print("Not a number, try again")
                continue
        while True:
            try:
                topping_name=input("Enter the name of your sundae toppings: ")
                break
            except ValueError:
                print("I don't know what you did")
                continue
        while True:
            try:
                topping_price=float(input("Enter the price of your sundae toppings: "))
                break
            except ValueError:
                print("Not a number, try again")
                continue
        sundae=Sundae(name,scoop_count,price_per_scoop,topping_name,topping_price)
        return sundae

def main():
    shop = DessertShop()
    order = Order()
    '''
    order.add(Candy('Candy Corn', 1.5, 0.25))
    order.add(Candy('Gummy Bears', 0.25, 0.35))
    order.add(Cookie('Chocolate Chip', 6, 3.99))
    order.add(IceCream('Pistachio', 2, 0.79))
    order.add(Sundae('Vanilla', 3, 0.69, 'Hot Fudge', 1.29))
    order.add(Cookie('Oatmeal Raisin', 2, 3.45))
    '''
    # boolean done = false
    done: bool = False
    # build the prompt string once
    prompt = '\n'.join([ '\n',
    '1: Candy',
    '2: Cookie',
    '3: Ice Cream',
    '4: Sunday',
    '\nWhat would you like to add to the order? (1-4, Enter for done): '
    ])
    while not done:
        choice = input(prompt)
        match choice:
            case '':
                done = True
            case '1':
                item = shop.user_prompt_candy()
                order.add(item)
                print(f'{item.name} has been added to your order.')
            case '2':
                item = shop.user_prompt_cookie()
                order.add(item)
                print(f'{item.name} has been added to your order.')
            case '3':
                item = shop.user_prompt_icecream()
                order.add(item)
                print(f'{item.name} has been added to your order.')
            case '4':
                item = shop.user_prompt_sundae()
                order.add(item)
                print(f'{item.name} has been added to your order.')
            case _:
                print('Invalid response: Please enter a choice from the menu (1-4) or Enter')
        print()
    data=[]
    total_tax=0
    subtotal=0
    for item in order.order:
        data.append([item.name,item.calculate_cost(),item.calculate_tax()])
        total_tax+=item.calculate_tax()
        subtotal+=item.calculate_cost()
    data.append(["--------------------------------------------------------",None,None])
    data.append(["Order Subtotals",subtotal,total_tax])
    data.append(["Order Total",None,subtotal+total_tax])
    data.append(["Total items in the order",None,str(len(order))])
    make_receipt(data,"receipt.pdf")
main()