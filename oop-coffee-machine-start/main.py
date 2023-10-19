from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

print ("Welcome to the coffee machine!\nWhat would you like to order?")
items = Menu()
print (items.get_items())
get_drink = input()
