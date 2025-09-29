"""
class Car:
    
    def drive(self):
        print("The car is driving")
    def jumping(self):
        print("The car is jumping")

car1= Car()
car1.drive()
car2=Car()
car2.jumping()
"""
class Car:
    wheel=4
    
    def __init__(self,make,model,year):
        self.make= make
        self.model=model
        self.year=year
        self.brand="Toyota"
    
    def drive(self):
        self.brand="Lexus"
        print(f"{self.make} of {self.model} of year {self.year} that has {self.wheel} tires, is driving personal brand made by {self.brand} ")
car1=Car("Toyota","Camry",2005)
car1.drive()
        
    