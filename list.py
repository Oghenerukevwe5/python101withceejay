fruits=["apple","banana","cherry"]
print(fruits[0])
print(fruits[-1])

fruits[1]="orange"
print(fruits)

fruits.append('banana')
# this means to add to the back
print(fruits)

fruits.insert(1,'grape')
# inserts grape after apple
print(fruits)

fruits.remove('banana')
print(fruits)

fruits.pop(4)
print(fruits)

# to clear the whole list
fruits.clear