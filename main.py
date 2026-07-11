# age =19
# height = 1.52
# number = 7
# price = "4000000"

# print(age)
# print(height)
# print(number)
# print(price)



# name = "Madhu"
# hobby = "Playing Basketball"
# is_student = "true"
# is_programming = "True"

# print(name)
# print(hobby)
# print(is_student)
# print(is_programming)

# name = input("Enter your name")
# age = int(input("Enter your age"))
# height = float(input("Enter your height"))

# print(name)
# print(age)
# print(height)


# price = 300
# print(price)
# price +=200
# print(price)
# price -=100
# print(price)
# price *=3
# print(price)

# age = int(input("Enter your age"))
# citizenship = "Valid"

# if age >=18:
#     print(citizenship)
# else:
#     print("Not valid")



# a = int(input("Enter your first number"))
# b = int(input("Enter your second number"))

# print("Press 1 for addition")
# print("Press 2 for subtraction")
# print("Press 3 for multiplication")
# print("Press 4 for division")

# response = int(input("Enter your response"))

# a = int(input("Enter your first number"))
# b = int(input("Enter your second number"))

# print("Press 1 for addition")
# print("Press 2 for subtraction")
# print("Press 3 for multiplication")
# print("Press 4 for division")

# response = int(input("Enter your response"))

# if response ==1:
#     print(a+b)
# elif response ==2:
#     print(a-b)
# elif response ==3:
#     print(a*b)
# elif response ==4:
#     print(a/b)
# else:
#     print("Please enter valid number")


# print("Madhu\Shrestha")
# print("Name\tAge\nMadhu\t19")
# print("I said \"Hello\"")

# name ="Madhu Shrestha"
# city= "Kathmandu"
# print(f"My name is {name} and I live in {city}")


# username = input("Enter username:")
# domain = "sthamadhu009@gmail.com"
# email = username + "@" + domain
# print(email)

# word = "Sophiya"
# print (word[1])
# print(word[3])
# print(word[5])



# word = "Hello" 
# last = word[-1]
# print(last)

# word= 'Python'
# result=word[-3:]
# s = word[-5:-2]
# print(word )
# a = word[-5:-1]
# print(a)
# s= word[: : -1]
# print(s)
# p =word[0:6:3]
# print(p)

# text = "hello world"
# a = text.capitalize()
# b= text.lower()
# result = text.upper()
# c = text.title()
# print(result)
# print(a)
# print(b)
# print(c)
# position =text.find("world")
# count= text.count("o")
# print(position)
# print(count)


# age = 20
# if age >= 18:
#     print("You can vote")
# else:
#     print("You cannot vote")
# if condition:
#     #runs when True
# else:
#     #runs when False

# nested if
# age = 20
# marks = 80
# if age >=18:
#     if marks >=80:
#         print("Eligible")


# elif condition 
# marks =35

# if marks >=85:
#     print("A")
# elif marks >=60:
#     print("B")
# elif marks >=40:
#     print("C")
# else:
#     print("Failed")

# game Health system
# health = int(input("Enter the health value"))
# if health > 70:
#     print("Healthy")
# elif health >30:
#     print("Injured")
# elif health < 30:
#     print("Critical")
# else:
#     print("Game Over")


# stress and sleep mood system
# sleep = int(input ("Enter your sleep hours"))
# stress = int(input("Enter your stress level"))
# if sleep <= 24 and stress <=10:
#     if sleep < 5 and stress > 7:
#         print("Exhausted")
#     elif sleep < 5:
#         print("Tired")
#     elif stress > 7:
#         print("Stressed")
#     else:
#         print("Normal")
# else:
#     print("Inavalid! Enter the number between 1 to 10")

# print("Based Price is $10")
# age = int(input("Enter your age"))
# showtime = int(input("Enter your showtime"))

# if age <12 :
#     print("$5")
# elif age >=65:
#     print("$7.5")
# elif showtime > 5:
#     print("$8")
# else:
#     print("No Discount")

# weight = float(input("Enter your weight in kg"))
# height = float(input("Enter your height in metre"))
# bmi = weight/(height**2)
# if bmi<18.5:
#     print("Underweight")
# elif bmi >18.5 and bmi < 24.9:
#     print("Normal Weight")
# elif bmi > 25 and bmi < 29.9:
#     print("Overweight")
# elif bmi>=30:
#     print("Obese")
# else:
#     print("Invalid Data")


# username = "admin"
# password = "secure123"
# code = "456"
# a = input("Enter your username")
# b= input("Enter your password")
# c = (input("Enter your code"))
# if a == username and b==password and c==code:
#     print("Login Sucesssfully!")
# elif  username!=a:
#     print("Invalid Username")
# elif  password!=b:
#     print("Invalid Password")
# elif  code!=c:
#     print("Invalid Code")
# else:
#     print("Invalid! please try again")


# x= 1
# while x <=5:
#     print(x)
#     x+=1



# a = input("Enter your name")
# age = int(input("Enter your age"))

# for i in range (age):
#     print(a)

# for i in range(10):
#     if i==5:
#         break
#     print(i)

# for i in range (10):
# if i ==5:
# continue:
# print(i)


# for i in range (1,6):
#     print("*" *i)


# for i in range (1, 6):
#     for j in range(1, i+1):
#         print(j, end ="")
#     print ()



# for i in range(6, 0, -1):

#     print('*' * (i - 1))

# for i in range (1,0,2):
#     print("*" *(i+1))

# def greet(name):
#     print("Hello", name)
#     print("Welcome")

# greet("Madhu")
# greet("Sophiya")
# greet("Rupa")

# def introduce(name="Madhu",city="Kathmandu"):
#     print(f"I am {name} and I live in {city}")

# introduce()
# import random
# def fortune():
#     fortune =["go school", "eat momo", "get surprise"]
# random.choice(fortune)
# returned_fortune = random.choice(fortune)
# print(f"You will {random.choice(fortune)} ")


#Function for 

# def add_numbers(*numbers):
#     total = sum(numbers)
#     return total

# print(add_numbers(1,2))
# print(add_numbers(1,2,3,4))

# def student_info(**kwargs):
#     print(kwargs)

# student_info(name="Madhu", age =19, city="Kathmandu" )

# def student_info(**kwargs):
#     print("Name:", kwargs["name"])
#     print("Age:", kwargs ["age"])

# student_info(name="Madhu", age = 19)    

# square = lambda x: x*x

# print(square(5))
# print(square(10))


# cube = lambda x: x*x*x

# print(cube(5))
# print(cube(10))


# Recursion

# this will cause an recusrdion error
# def greet():
#     print("Greet")
#     greet()

# greet()

# def factorial(n):
#     if n==1:
#         return 1
#     return n * factorial (n-1)
# print(factorial(5))

# def fibonacci(n):
#     if n<=1:
#         return n
    
#     return fibonacci(n-1) + fibonacci(n-2)

# print(fibonacci(5))


# def greet():
#     message ="Hello"
#     print(message)

# greet()

# name= "Madhu"
# def show():
#     print(name)
# show()


# x= 10
# def change():
#     x =20
#     print("Inside Function", x)

# change()
# print("Outside Function", x)


# data structure
# list

# data =["Ram", 20, True, 3.14]
# print(data[0])

# fruits = ["Apple", "Banana", "Mango"]
# print(fruits[0])
# print(fruits[1])
# print(fruits[-2])

# list slicing

# numbers = [10,20,30,40,50]
# numbers[1:4]
# numbers [:3]
# numbers[2:]
# numbers [:]
# print(numbers)


# Modifying List

# fruits =["Apple", "Banana","Mango"]
# fruits[1]= "Orange"
# print(fruits)

# list methods
# append()= Add items at end
# student = ["Ram", "Shyam"]
# student.append("Hari")
# print(student)

# insert()=insert at specific position
# students=["Ram", "Hari"]
# students.insert(1, "shyam")

# remove()=removes by value
# student.remove("Shyam")

# pop() = Removes item by index
# student.pop()


# sort() = sort data
# numbers = [1,5,4,3]
# numbers.sort()
# print (numbers)

# fruits = ["Mango", "Apple", "Banana"]
# fruits.sort()
# print(fruits)

# Tuple
# t = (10,20,30)
# name , age , city = "Madhu", 19 , "Kathmandu"
# print(t[0])
# print (name)

# country = ("Nepal", "India", "China")
# print (country[1])

# Concatenation and repetition
# a = (1,2)
# b = (3,4)
# print(a + b)
# print(a * 2)

# Methods and Membership
# t = (1,2,2,3)
# print(2 in t)
# print(t.count(2))
# print(t.index(3))

# t = (1,2,3,3,4,)
# print(t[1:4])
# print(t.count(3))

# Set
# s = {1,2,3,3,4}
# print(s)

# s.add(5)
# s.update([6,7])
# s.remove(2)
# s.discard(99)
# print(s)

# s= {5,5,7,8,7,9}
# s.add(6)
# s.remove(5)
# print(s)


# A = {1,2,3,4}
# B = {3,4,5,6}
# print(A|B)
# print(A & B)
# print(A-B)
# print(A^B)

# A ={"Mango", "Apple", "Watermelon"}
# B = {"Watermelon", "Litchi"}
# print(A&B)

# dictionary

# student = {
#     "name": "Madhu",
#     "age" : 19,
#     "grade" : 12
# }
# print(student["name"])
# student["age"]
# student["city"] = "Kathmandu"

# keys()/values()/items()
# d = {
#     "a":1,
#     "b":2
# }
# print(d.keys())
# print(d.values())
# print(d.items())

# get() - Safe Access
# print(d.get("a"))
# print(d.get("z", 0))

# update()/pop()/clear()
# d.update({"c": 3})
# d.pop("b")
# d.popitem()
# d.clear()



# loop through keys
# for key in student:
#     print(key)

# for val in student.values():
#     print(val)

# for k, v in student.items():
#     print(k,v)

# opening files with open()
# file = open("student.txt")

# Three Ways Read a File
# read()-Everything at once
# print(file.read())


# Using write()
# file = open("notes.txt","w")
# file.write("Hello Students")
# file.write("\nPython is fun!")
# file.close()


# print("Enter student details:")
# student_data = {
#     "Name": input("Enter name: "),
#     "Age": input("Enter age: "),
#     "Major": input("Enter major: ")
# }

# with open("student_records.txt", "w") as file:

#     file.write("--- Student Record ---\n")
    
#     for key, value in student_data.items():

#         line = f"{key}: {value}\n"
#         file.write(line)
        
#     print("\nData successfully saved to 'student_records.txt'!")

# import csv
# with open ("student.csv", "r") as file:
#     reader = csv.reader(file)
#     for row in reader:
#         print(row)


# import csv 
# with open ("student.csv", "a", newline="")as file:
#     writer =csv.writer(file)
#     writer .writerow(["Name", "Age","Grade"])
#     writer.writerow(["Madhu", 19 , "B"])


# import csv 
# student = {
#     "name":"Madhu",
#     "age": 19,
#     "grade": "A"
# }
# with open("student.csv", "w", newline="")as file:
#     writer =csv.DictWriter(
#         file,
#         fieldnames=["name", "age", "grade"]
#     )
#     writer.writeheader()
#     writer.writerow(student)

# import csv

# print("Enter student details:")


# student_data = {
#     "name": input("Enter name: "),
#     "age": input("Enter age: "),
#     "major": input("Enter major: ")
# }

# with open("student_records.csv", "w", newline="") as file:
#     writer = csv.DictWriter(file, fieldnames=["name", "age", "major"])
    
#     writer.writeheader()
#     writer.writerow(student_data)

# print("\nData successfully saved to student_records.csv!")
