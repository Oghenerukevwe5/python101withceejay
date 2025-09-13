# if condition
x=10
if x>5:
    print("x is greater than 5")
    
x=300
if x<=400:
    print("cash out")
else:
    print("cash in")
    
score=85
if score>=90:
    print("A")  
elif score>=80:
    print("B")
elif score>=70:
    print("C")
elif score>=60:
    print("D")
elif score>=50:
    print("E")
else:
    print("F")
    

# number 1
# Function called login
def login():    
    valid_user=["Joshua","admin","ceejay"]
# ask for the user's username
    username=input("Enter your username: ")
    if username in valid_user :
        print("Login Successful")
    else:
        print("Username not found")
login()

# number 2
# function called check number type
def check_number_type():
    return{
        "number":number
    }
# request for a number
number=float(input("Enter a number: "))
if number%2==0:
    print("The number is even")
else:
    print("The number is odd")
    check_number_type()
    
# number 3
def number_guess_name():
    secret_number=6
# ask the user to guess the number
    guess_number1=int(input("Guess a number"))
    if guess_number1==secret_number:
        print("one jombo")
    elif guess_number1< secret_number:
        print("too low")
    else:
        print("Too high")
    guess_number2=int(input("Guess a number"))
    if guess_number2==secret_number:
        print("one jombo")
    elif guess_number2 < secret_number:
        print("too low")
    else:
        print("Too high")
    guess_number3=int(input("Guess a number"))
    if guess_number3==secret_number:
        print("one jombo")
    else:
        print("Game over")
    number_guess_name()
    