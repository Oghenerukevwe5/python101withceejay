my_turple=()
colors=("red","green","blue")

single=("apple")

temp=list(colors)
temp[1]='yellow'
colors=tuple(temp)
print(colors)