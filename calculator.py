print("Simple Calculator")
# to make the calculator run
while True:
    print("\n Enter tow number")
    num1=float(input("Enter your first number: "))
    num2=float(input("Enter your second number: "))
    
    # allow the user to select an operator
    print("\n Select an operator")
    print("1. Addition(+)")
    print("2. Subtraction(-)")
    print("3. Multiplication(*)")
    print("4. Division(/)")
    
    choice=input("Enter an operator of your choice(+,-,*,/)")
    # checker 
    if choice== "+":
        result=num1+num2
    elif choice=="-":
        result=num1-num2
    elif choice=="*":
        result=num1*num2
    elif choice=="/":
        result=num1/num2
    else:
        print("invalid input")
        continue
    
    print(f"\n Result: {result}")
    
    
    again= input("\n Do you want to calculate again(yes/no)").lower()
    # if the user puts Yes instead of yes, .lower()will change it to yes
    if again !="yes":
        print("calculator stop")
        break