#  function to manage a simple order receipt 
# function to calulate the total cost of a product
def calculate_total(price,quantity):
    return (price*quantity)
# function to create order that returns a dictionary
def create_order(product_name,price,quantity):
    return{
        "product":{product_name},
        "price":{price},
        "quantity":{quantity},
        "total":calculate_total(price,quantity)
    }
# Request user's input
name=input("Enter the product name:")
price=float(input("Enter the price of the product:"))
quantity=int(input("Enter the number of items:"))
order=create_order(name,price,quantity)
# display final order
print("\n Order Receipt:")
print (f"{order}")



# Assignment 1
# Function to validate user login credentials
# Function to create user
def create_user(username, password):
    return{
        "username":{username},
        "password":{password}
    }
    # function to create login
def login(user,input_username,input_password):
    if "username"and "password" == login:
     return{
        "status":"success","Message":"Login Successful"
    } 
    else:
        return{
            "status":"error","Message":"Invalid Credentials"
        }
# Request user's input to create an account
username=input("Enter your username:")
password=input("Enter your password:")
create_account=create_user(username,password)
# Ask user to login
username=input("Login with your username:")
password=input("Login with your password:")
log_in=login(user=username ,input_username=username,input_password=password)
print (f"{log_in}")