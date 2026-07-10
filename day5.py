# class student:
#     name ="vinay"
#     def study(self):
#         print("studying")
# student1 = student()  #student1 is object of student class
# print(student1.name)
# student1.study()   #study is method

# class student:
#     def details(self):
#         print("had breakfast")
# s1=student()
# s1.details()

# student.details(s1)  #another way to call method

# class student:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
# s1=student("vinay",20)
# s2=student("vinayak",21)
# print(s1.name)
# print(s1.age)
# print(s2.name)
# print(s2.age)

# class bank:
#     def __init__(self,balance):
#         self.balance=balance

#     def check_balance(self):
#         print(self.balance)

# account=bank(50000)
# account.check_balance()

# class user:
#     def __init__(self,name):
#         self.name=name
#     def login(self):
#         print(self.name,"logged in")

# u1=user("vinay")
# u2=user("vinayak")

# u1.login()
# u2.login()

# Parent class (Base class)
# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def eat(self):
#         print(self.name,"is eating.")

# class Dog(Animal):
#     def bark(self):
#         print(self.name,"says bow")
# my_dog = Dog("Buddy")
# my_dog.eat()
# my_dog.bark()

# Grandparent class (Base class)
# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def eat(self):
#         print(self.name, "is eating.")

# class Dog(Animal):
#     def bark(self):
#         print(self.name, "says Woof!")

# class Puppy(Dog):
#     def weep(self):
#         print(self.name, "is whining.")

# class chintu(Puppy):
#     def play(self):
#         print(self.name, "playing!")   
# my_puppy = chintu("Biscuit")
# my_puppy.eat()   
# my_puppy.bark() 
# my_puppy.weep()  
# my_puppy.play()


# class thatta:
#     def land(self):
#         print("thatta has land")

# class appa(thatta):
#     def car(self):
#         print("appa has car")

# class maga(appa):
#     def bike(self):
#         print("maga has bike")
# obj=maga()
# obj.land()
# obj.car()
# obj.bike()

# ####hirarchial
# ####__init__ is constructor
# class animal:
#     def __init__(self, name):
#         self.name = name

# class lion(animal):
#     def walk(self):
#         print(self.name, "lion is walking")

# class tiger(animal):
#     def walk(self):
#         print(self.name, "tiger is walking")

# class jaguar(animal):
#     def walk(self):
#         print(self.name, "jaguar is walking")     


# obj1 = lion("Simba")
# obj2 = tiger("Sher Khan")
# obj3 = jaguar("Shadow")
# obj1.walk()
# obj2.walk()
# obj3.walk()

class student:
    def __init__(self,name):
        self.name=name
    def __str__(self):
        return self.name
    
s=student("king")
print(s)        