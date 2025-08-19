# Assignment 1
# Function to validate user login credentials
# Function to create user
def create_user(username, password):
    return{
        "username":username,
        "password":password
    }
    # function to create login
def login(user,input_username,input_password):
    if user["username"]==input_username and user["password"] == input_password:
     return{
        "status":"success","message":"Login Successful"
    } 
    else:
        return{
            "status":"error","message":"Invalid Credentials"
        }
# Request user's input to create an account
username=input("Enter a new username:")
password=input("Enter a new password:")
create_account=create_user(username,password)
# Ask user to login
login_username=input("Login with your username:")
login_password=input("Login with your password:")
log_in=login(create_account,login_username,login_password)
print (f"{log_in}")

# Assignment 2
# Function to generate students report card
# function to calculate average scores
def calculate_average(scores):
    if scores:
        return sum(scores)/len(scores)
    else:
        return 0
def create_report(student_name,scores):
    return{
        "student": student_name,
        "scores": scores,
        "average": calculate_average(scores)
    }
# Request student's name
student_name=input("Enter your name: ")
score_1=float(input("Enter score 1: "))
score_2=float(input("Enter score 2: "))
score_3=float(input("Enter score 3: "))
scores= [score_1, score_2, score_3]
report=create_report(student_name,scores)
print(f"{report}")

# Assignment 3
# Function to build a simple banking backend system
# function to create account
def create_account(name, balance):
    return{
        "name": name,
        "balance":balance
    }
# function to deposit
def function_deposit(account, amount):
    account['balance']+=amount
    return account
# Request for user's name and initial balance
name=input("Enter your name: ")
balance=float(input("Enter your initial balance: "))
# create the account
account_details=create_account(name,balance)
# Request a deposit amount
deposit_amount=float(input("Enter a deposit amount: "))
account_details=function_deposit(account_details,deposit_amount)
print(f"{account_details}")