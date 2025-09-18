my_dict={}

student={
    "name": "John",
    "age": 21,
    "courses": ["Math","CompSci"]
}
print(student["name"])
print(student.get("age"))
print(student.get("courses"))
# use get when you want to get items in the dictionary that are not strings
print(student)
student["phone"]="555-5555"
print(student)

student.pop("courses")
print(student)

student.popitem()
