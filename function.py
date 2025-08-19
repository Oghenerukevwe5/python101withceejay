def function_name(parameter):
    print()

def greet():
    print("Hello, World!")
    
    
greet()
# calling the function to execute its code

# function with pararmeter
def greet_student(name):
    print(f"Hello,{name}")
    
greet_student("Ruky")

# function with return
def add(a,b):
    return a+b
result= add(7,5)
print("The sum of 7 and 5 is:",result)

# function with default parameter
def greet_student(name="Ceejay"):
    print(f"Hello, {name}")
    
    greet_student()
    greet_student("Ruky")
    
    
def full_name(first_name,last_name):
        return f"{first_name} {last_name}"
        
print(full_name("Agbaire","Oghenerukevwe"))
        
        
def greet_user(username):
    print(f"Welcome {username}  you are now logged in")
greet_user("Chris")

def is_valid_password(password):
    return len(password)>=8
print(is_valid_password("jok"))
print(is_valid_password("jok12345"))

#  function of simple interest to calculate a product
def simple_interest(p, r ,t):
    return (p*r*t) /100
print(simple_interest(2000,5,2))

# function to create username for a user
def create_username(first_name,last_name):
    return (first_name[:3]+last_name[:3]).lower()
# function to create email
def create_email(first_name, last_name, domain="fliptotech.com"):
    return f"{first_name.lower()}.{last_name.lower()}@{domain}"
# function to create profile
def create_user_profile(first_name,last_name):
 return{
    "username":create_username(first_name, last_name),
    "email":create_email(first_name, last_name)
}
 
first=input("Enter yor first name:")
last=input("Enter your last name:")

profile=create_user_profile(first,last)
print("\n User profile created")
print(f"{profile}") 
 
#  function to manage a simple order receipt 
# function to calulate the total cost of a product
def calculate_total(price,quantity):
    return add(price,quantity)
# function to create order taht returns a dictionary
def create_order(product_name,price,quantity):
    return{
        "product":{product_name},
        "price":{price},
        "quantity":{quantity},
        "total":{calculate_total}
    }
# Request user's input
name=input("Enter the product name:")
price=int(input("Enter the price of the product:"))
quantity=int(input("Enter the number of items:"))
order=create_order(name,price,quantity)
# display final order
print("\n Order Receipt:")
print (f"{order}")
