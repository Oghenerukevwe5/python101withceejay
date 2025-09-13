# function to check login
def check_login(username,password):
    users={"joshua":"1234","dayo":"abcd"}
    if username in users and users[username]==password:
        return {"status":"success","message":f"Welcome {username}!"}
    else:
        return{"status":"Unsuccessful","message":f"Invalid username or password"}
print(check_login("dayo","abcd"))


# condition
user=int(input("Enter your age: "))
if user>=18:
    if user<= 18:
        print("This user is a young adult")
    else:
       print("This user is an old adult")
else:
    print("This user is a minor")
    
# 1: Student Grading system
def get_grade(score):
    if score >=90:
        return "A"
    elif score >=75:
        return "B"
    elif score >=60:
        return "C"
    else:
        return "F"
users_score=int(input("Enter your score: "))
users_grade=get_grade(users_score)
print(f"{users_grade}")

# 2: Even or odd checker function
def check_number(n):
    if n%2==0:
        print("Even")
    else:
        print("Odd")
num=int(input("Enter an integer: "))
users_num=check_number(num)
print(f"{users_num}")

# 3:simple calculator
def calculator(a,b,operator):
    if operator == "+":
        return a+b
    elif operator == "-":
        return a-b
    elif operator == "*":
        return a*b
    elif operator == "/":
        return a/b
    else:
        return "Invalid Operator"
# request users input
a=float(input("Enter num1: "))
b=float(input("Enter num2: "))
operator=input("Enter an operator: ")
users_result=calculator(a,b,operator)
print(f"{users_result}")

# 4:voting eligibility
def can_vote(age):
    if age<18:
        return "Not Eligible"
    elif 18<=age >=21:
        return "Young voter"
    else:
        return "Eligible voter"
# request users input
age=int(input("Enter your age: "))
vote=can_vote(age)
print(f"{vote}")

# 5: number classifier
def classify_number(n):
    if n >0 and n%2==0:
        return "Positive Even"
    elif n>0 and n%2!=0:
        return "Positive Odd"
    elif n<0:
        return "Negative"
    elif n==0:
        return "Zero"
# request users input 
number=float(input("Enter a number: "))
number_class=classify_number(number)
print(f"{number_class}")
    
        