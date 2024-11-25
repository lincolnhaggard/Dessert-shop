from abc import ABC, abstractmethod
from packaging import Packaging

class DessertItem(Packaging,ABC):
    def __init__(self,name):
        self.name=name
        self.tax_percent=7.25
        if isinstance(self,Candy):
            self.packaging="Bag"
        if isinstance(self,Cookie):
            self.packaging="Box"
        if isinstance(self,IceCream):
            self.packaging="Bowl"
        if isinstance(self,Sundae):
            self.packaging="Boat"

    def __str__(self):
        return self.name
    
    def calculate_tax(self):
        return round(self.calculate_cost()*self.tax_percent/100,2)

    @abstractmethod
    def calculate_cost(self):
        pass

class Candy(DessertItem):
    def __init__(self,name,candy_weight,price_per_pound):
        super().__init__(name)#Pass up to DessertItem
        self.candy_weight=candy_weight
        self.price_per_pound=price_per_pound

    def calculate_cost(self):
        return self.price_per_pound*self.candy_weight
    
    def __str__(self):
        return f"{self.name} ({self.packaging})\n   {self.candy_weight} lbs. @ {self.price_per_pound}/lb{" "*(54-len(f"   {self.candy_weight} lbs. @ {self.price_per_pound}/lb"))}${self.calculate_cost()}{" "*(16-len(f"${self.calculate_cost()}"))}${self.calculate_tax()}"

class Cookie(DessertItem):
    def __init__(self,name,cookie_quantity,price_per_dozen):
        super().__init__(name)#Pass up to DessertItem
        self.cookie_quantity=cookie_quantity
        self.price_per_dozen=price_per_dozen

    def calculate_cost(self):
        return self.cookie_quantity/12*self.price_per_dozen
    
    def __str__(self):
        return f"{self.name} ({self.packaging})\n   {self.cookie_quantity} cookies @ {self.price_per_dozen}/dozen{" "*(54-len(f"   {self.cookie_quantity} cookies @ {self.price_per_dozen}/dozen"))}${self.calculate_cost()}{" "*(16-len(f"${self.calculate_cost()}"))}${self.calculate_tax()}"

class IceCream(DessertItem):
    def __init__(self,name,scoop_count,price_per_scoop):
        super().__init__(name)#Pass up to DessertItem
        self.scoop_count=scoop_count
        self.price_per_scoop=price_per_scoop

    def calculate_cost(self):
        return self.scoop_count*self.price_per_scoop

    def __str__(self):
        return f"{self.name} ({self.packaging})\n   {self.scoop_count} scoops @ {self.price_per_scoop}/scoop{" "*(54-len(f"   {self.scoop_count} scoops @ {self.price_per_scoop}/scoop"))}${self.calculate_cost()}{" "*(16-len(f"${self.calculate_cost()}"))}${self.calculate_tax()}"

class Sundae(IceCream):
    def __init__(self,name,scoop_count,price_per_scoop,topping_name,topping_price):
        super().__init__(name,scoop_count,price_per_scoop)#Pass up to IceCream class
        self.topping_name=topping_name
        self.topping_price=topping_price
    
    def calculate_cost(self):
        return super().calculate_cost()+(self.topping_price)
    def __str__(self):
        return f"{self.name} ({self.packaging})\n   {self.scoop_count} scoops @ {self.price_per_scoop}/scoop\n   {self.topping_name} @ ${self.topping_price}{" "*(54-len(f"   {self.topping_name} @ ${self.topping_price}"))}${self.calculate_cost()}{" "*(16-len(f"${self.calculate_cost()}"))}${self.calculate_tax()}"


class Order:
    def __init__(self):
        self.order=[]

    def add(self,item):
        if isinstance(item,DessertItem):
            self.order.append(item)
    
    def __len__(self):
        return len(self.order)

    def order_cost(self):
        total=0
        for item in self.order:
            total+=item.calculate_cost()
        return total
    
    def order_tax(self):
        total_tax=0
        for item in self.order:
            total_tax+=item.calculate_tax()
        return total_tax
    
    def __str__(self):
        toret="----------------------------------------------Receipt---------------------------\n"
        for i in self.order:
            toret+=f"{i}\n"
        toret+="---------------------------------------------------------------------------------\n"
        toret+=f"Total number of items in order: {len(self.order)}\n"
        toret+=f"Order Subtotals:                                      ${self.order_cost()}{" "*(16-len(f"${self.order_cost()}"))}[Tax: ${self.order_tax()}]\n"
        toret+=f"Order Total:                                                                ${self.order_cost()+self.order_tax()}\n"
        toret+="---------------------------------------------------------------------------------"
        return toret
    



