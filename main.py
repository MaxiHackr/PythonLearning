#Robot Barista
import time

print("Welcome to Maxi™ Coffee Cabin!\n" + "I am Barista_01\n")

name = input("What is your name?\n")

if name == "Ben" or name == "Patricia" or name == "Loki" or name == "Jonny":
    evil_status = input("Are you evil?\n\n")
    good_deeds = int(input("How many good deeds have you done today?\n\n"))
    if evil_status == "Yes" and good_deeds < 4:
        print("You're not welcome here " + name + ". Get out!!")
        exit()
    else:
        print("Oh you're one of the good " + name +
              "'s! You are welcome to stay")
else:
    print("\nHello " + name + ",\n\n" + "Our Menu today is:\n")

price = 0
menu = """
£2.00 Americano
£2.20 Latte
£2.20 Cappuccino
£1.80 Espresso
£2.30 Hot Chocolate
£2.50 Iced Latte

Syrups: 50p /(per pump)"""

print(menu)

order = input("\nWhat can I get for you?\n\n")

yes = ("Yes" or "yes")
quantity2 = 0

if order == "Americano":
    price = 2.00
elif order == "Latte":
    price = 2.20
elif order == "Cappuccino":
    price = 2.20
elif order == "Espresso":
    price = 1.80
elif order == "Hot Chocolate":
    price = 2.30
elif order == "Iced Latte":
    price = 2.50
else:
    print("We dont have that on our menu.")
    price = 0
    exit()

quantity = input("\nHow many would you like?\n")
##Syrups##
syrup = input("\nWould you like any syrup added in? Answer (Yes/No)\n\n")
syrup_price = 0.50
syrup_menu = """\n-=Syrup Menu=-
Hazelnut
Chocolate
Vanilla
Caramel
Salted Caramel
White Chocolate
"""

if syrup == "Yes" or syrup == "yes" or syrup == "Y" or syrup == "y":
    print(syrup_menu)
    syrup = input("Which one would you like\n\n")
elif syrup == "No" or syrup == "no" or syrup == "N" or syrup == "n":
    syrup_price = 0

##2nd Order/Do you want anything else?
order2 = input("\nWould you like anything else? Answer with (Yes or No)\n\n")

if order2 == yes:
    print(menu)
    order2 = input("\nWhat can I get for you?\n")
    quantity2 = input("\nHow many would you like\n")
    print("\nWe will now proceed to payment.\n")
else:
    print("\nI will now direct you to payment\n")
    order2 = ""

quantity = int(quantity) + int(quantity2)
total = price * int(quantity) + int(syrup_price)

print("Your total is: £" + str(total))

print("\nThank you " + name + ", we will have your " + order + "(s) and " +
      order2 + "(s) ready in just a moment!\n\n")

print("Please collect your drink(s) at the counter")

print(str(quantity) + " " + order + "(s)")
print(str(quantity2) + " " + order2 + "(s)")
print("£" + str(total))
