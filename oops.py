# def login(func):
#     def wrapper():
#         print("checking login")
#         func()
#     return wrapper
# @login
# def dashboard():
#     print("dashboard page")
# dashboard()        

# def message(func):
#     def wrapper():
#         print("function started")
#         func()
#         print("function ended")
#     return wrapper
# @message
# def hello():
#     print("hello python")
# hello()    

# def world():
#     print("epstein island")    
# world()    


# import json
# student ={
#     "name":"vinayak",
#     "age":22
# }
# data=json.dumps(student)
# print(data)

# import json

# data = '{"name":"vinayaka","age":21}'

# result = json.loads(data)

# print(result)
# print(type(result))

import requests
response = requests.get (
    "https://api.github.com/users/python"
)
data =response.json()
print(data)