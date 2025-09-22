import json
with open("file.json","r", encoding="utf-8")as f:
    data=json.load(f)
    print(data)
    print(type(data))
    
data={
    "name":"Ruky",
    "age":26,
    "occupation":"Student",
    "is_student" :True
}
with open("user.json","w",encoding="utf-8")as f:
    json.dump(data,f,indent=2)