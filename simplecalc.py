users=["vinay","vinayak","monitha"]
for users in users:
    print("message sent to",users)


name ="virat kholi"

for ch in name:
    print(ch)


count =1
while count>=15:
    print(count)
    count+=1

for i in range(10):
    if i==5:
        continue
    print(i)    
   
   
password=""
while password != "1234":
    password = input("enter passwpord:")
    print("login success")    
    
student = [
    "ram",
    "sam",
    "rana"
] 
student.append("alex") 
student.remove("sam")
print(student)
