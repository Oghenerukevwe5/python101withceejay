# class
class Cocacola:
    secret_formula="Sugar + Caramel+ Carbonated Water"
    print(secret_formula)
    def __init__(self, drink_name,size,price):
           self.drink_name=drink_name
           self.size=size
           self.price=price
           self.sold=0  
    def drinks(self):
        print(f"{self.drink_name}, of size {self.size} with price {self.price}") 
              
    def sell(self,sold):
           self.sold=sold
           sold=0
           print(f"Serving {self.drink_name} {self.size}.Total sold: {self.sold}")
drink1=Cocacola("Coke Zero","500ml",200)
drink2=Cocacola("Diet Coke","330ml",150)

drink1.drinks()
drink1.sell(6)
drink2.drinks()
drink2.sell(3)