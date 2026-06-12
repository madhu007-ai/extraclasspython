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


username = "admin"
password = "secure123"
code = "456"
a = input("Enter your username")
b= input("Enter your password")
c = (input("Enter your code"))
if a == username and b==password and c==code:
    print("Login Sucesssfully!")
elif  username!=a:
    print("Invalid Username")
elif  password!=b:
    print("Invalid Password")
elif  code!=c:
    print("Invalid Code")
else:
    print("Invalid! please try again")