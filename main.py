#Robot Barista
import time

print("Welcome to Maxi™ Coffee Cabin!\n" + "I am Barista_01\n")

name = input("What is your name?\n")

print("\nHello " + name + ",\n\n" + "Our Menu today is:\n")

menu = """Americano
Latte
Cappuccino
Espresso
Hot Chocolate"""

print(menu)

drink = input("\nWhat can I get for you?\n\n")


print("\nOkay " + name + ", we will have that " + drink + " ready in just a moment!")

price_latte = "£1.05"
price_americano = "£1.00"
price_cappuccino = "£1.10"

print("For your " + drink + " that will be " + price_latte)


