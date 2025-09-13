# ARITHMETIC OPERATORS
# number 1
# two numbers
a,b=10,5
# sum
print (a+b)
print(a-b)
print(a/b)
print(a%b)
print(a**b)
# number 2
# area of a circle
import math
r=7
area= 3.14 *r**2
print(area)

# number 3
buy=50 
sell=75
profit= sell-buy 
print (profit)
profit_percentage=((sell-buy)/buy) *100
print(profit_percentage)
# RELATIONAL OPERATORS
# number 4
x=15
y=25
print(x >y)
print(x==y)
print(y<=x)
# number 5
marks=72 
if marks >=40:
    print("Pass")
if marks>=70:
    print("Distinction")
# LOGICAL OPERATORS
# number 6
# person entering a club
age =20
has_id=True
if age>=18 and has_id is True:
    print("Allowed")
else:
    print("Not Allowed")
# number 7
number= 25
print(number>=10 and number<=50)
print(number>=10 or number<=50)
print(not(number==25))
# number 8
# weather condition
is_raining=False
has_umbrella=False
if is_raining and has_umbrella:
    print("stay inside")
else:
    print("Go outside")
