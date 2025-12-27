# Number Guessing Game
# import random
# random_num=random.randint(1,10)
# name=input("Enter your name: ")
# print(f"Hello {name.capitalize()}\nWelcome to the NUMBER GUESSING GAME")
# for i in range(3):
#     num=int(input("Guess the number between 1 to 10: "))
#     if num==random_num:
#         print("congratulations")
#         break
#     elif num>random_num:
#         print("too high")
#     elif num<random_num:
#         print("too low")
#     else:
#         print("sorry, you guess wrong number")

# Simple Calculator
# def add(x,y):
#     return x+y
# def subtract(x,y):
#     return x-y
# def multiply(x,y):
#     return x*y
# def divide(x,y):
#     return x/y
# print("Select operation")
# print("1.Addition")
# print("2.Subtraction")
# print("3.Mulitiplication")
# print("4.Division")
# choice=input("Enter choice(1/2/3/4): ")
# num1=int(input("Enter first number:"))
# num2=int(input("Enter second number:"))
# if choice=='1':
#     print(f"{num1}+{num2}={add(num1,num2)}")
# elif choice=='2':
#     print(f"{num1}-{num2}={subtract(num1,num2)}")
# elif choice==3:
#     print(f"{num1}*{num2}={multiply(num1,num2)}")
# elif choice==4:
#     print(f"{num1}/{num2}={divide(num1,num2)}")
# else:
#     print("Invalid input")
# print("Thank you for using the calculator")

# Possword Generator
# import random
# letters="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
# numbers="0123456789"
# symbols="!@#$%^&*()_+"
# print("Welcome to the password generator!")
# password=""
# password_length=int(input("Enter the length of the password: "))
# for i in range(password_length):
#     group=random.choice([letters,numbers,symbols])
#     password+=random.choice(group)
# print(f"Generated password is: {password}")

# Rock Paper Scissors Game
import random
print("Welcome to Rock, Paper, Scissors Game!")
choices=["rock","paper","scissors"]
user_score=0
computer_score=0
for i in range(5):
    print(f"\nRound {i+1}")
    user=input("Enter rock, paper or scissors: ").lower()
    computer=random.choice(choices)
    print(f"Compputer choice: {computer}")