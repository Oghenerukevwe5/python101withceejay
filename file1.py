# open file 
# read file
f=open("mytext.txt","r")
print(f.read())
f.close()
# OR
with open("note.txt","r")as f:
    print(f.read())
    
# write file
with open("python.py","w")as f:
    f.write("Hello World \n")

# append files
with open("python.py","a") as f:
    f.write("another line \n")
    
