# withdrawal for an ATM
balance= 50000
withdraw=float(input("Enter the amount you will like to withdraw: \n"))
if withdraw <= balance :
    print("Sucessful")
else:
    print("You do not have enough Money.")