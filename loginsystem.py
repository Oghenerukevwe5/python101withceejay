# Registeration step
print("Register")
# request for user's input
new_username=input("Enter a new username: ")
new_password=input("Enter a new password: ")
print("Registeration successful!! ")
print("Please Login")
# Login step
max_attempts=3
attempts=0
Logged_in= False
while not Logged_in and attempts<max_attempts:
    # Request user's inputs
    username=input("Enter your username: ")
    password=input("Enter your password: ")
    
    if username==new_username and password==new_password:
        print(f"Login Successful {username}!")
        logged_in=True 
        break
    else:
        attempts+=1
        print(f"Incorrect Username or Password. You have {max_attempts-attempts} left \n ")
    if not Logged_in:
        print("Too many failed attempts. Access Denied.")       