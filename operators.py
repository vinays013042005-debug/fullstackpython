product_price = 5000
delivery_charges = 100

total =product_price+delivery_charges
print(total)



#####
a=10
b=3

print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a%b)
print(a**b)

student=10
groups=2

print(student // groups)

####assigned
followers = 100
followers += 1
print(followers)

#####relational

saved_password ="12345@adc"
entered_password="12345@adc"
num1 = 200
num2 = 159
print(saved_password == entered_password)
print(num1 != num2)

#####logical

balance=1500
pin_correct=True
if balance >= 1000 and pin_correct:
    print("withdraw allowed")
else:
    print("failed")    
    

#####
age = 20
if age >= 18:
    print("you are eligible to vote.")
marks= int(input("enter your  marks: "))    
if marks>=90:
    print("Grade:A")
elif marks >=80:
    print("Grade:B")   
elif marks >=70:
    print("Grade:C") 
elif marks >=60:
    print("Grade:D")  
else:
    print("failed")   


###########
def withdraw_money():
    
      pin = 1234
      password = int(input("Enter PIN: "))

      if password == pin:
          balance = 1500
          print("Your current balance is:",balance) 
    
    
          withdraw_amt = int(input("Enter amount to withdraw: "))
    
    
          if balance >= withdraw_amt:
             balance=balance-withdraw_amt
             print("Withdrawal allowed")
             print("remaining amount:",balance)
        
          else:
              print("Failed: Insufficient funds") 
      else:
         print("PIN invalid")
withdraw_money()         


#######
users=["vinay","vinayak","monitha"]
for users in users:
    print("message sent to",users)

           