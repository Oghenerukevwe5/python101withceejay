# basic operators
a= 15
b=10 
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(a**b)


# comparison operators
x=10
y=20
print(x==y)
print(x!=y)
print(x<y)
print(x>y)
print(x>=y)
print(x<=y)

# logical operators
x=7
print(x>5 and x<15)
print(x<5 or x<15)
print(not(x==7))

# identity operators
a=[1,2,3,4,5]
a=b  
c= [1,2,3,4,5]
print(a is b)
# gives true because they both refer to the same object
print(a is not c)
# true because a and c are differrent objects
print(a is c )
# false because a and c are different objects 

# membership operators
my_list=[1,2,3,4,5]
print(2 in my_list)
# true
print(6 not in my_list)
# true
print (20 in my_list)
# false


# Classwork
# 1
a=2 
print(a%2==0)
# 2
a= 5
b= 7
print(a>b)
# 3
word="banana"
print("a" in word)
# 5
role='guest'
print(not role=='admin'and "Access Denied")
# 6
a=["egg","banana","milk"]
b=["beans","milk","bread"]
print(a is not b)
# Question 8: count how many numbers in a list are greater than 10
numbers=[5,8,9,10,11,15,20,25,30,50]
print(len([n for n in numbers if n >10]))
# Question 9:Check if all numbers in a list are even using a loop and logical AND
numbers=[1,2,3,4,5,6,7,8,9,10]
all_even=True
for n in numbers:all_even= all_even and n %2==0
print(all_even)
# Question 10: Check if a keyword is in a sentence and the sentence starts with 
# the keywod using the membership and logical operators
sentence="Backend is quite confusing"
keyword="Backend"
print((keyword in sentence) and sentence.startswith(keyword))