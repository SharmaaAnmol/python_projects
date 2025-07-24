from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


user_menu =  Menu()
user_report = CoffeeMaker()
user_money= MoneyMachine()

def start ():
    is_machine_on = True

    while is_machine_on:

       choice = input(f"What would you like ? {user_menu.get_items()}").lower()

       if choice == "off":
           is_machine_on = False
           print("the machine is off")
       elif choice == "report":
           user_report.report()
           user_money.report()
       else :
           drink =user_menu.find_drink(choice)
           if user_report.is_resource_sufficient(drink):
               if user_money.make_payment(drink.cost):
                    user_report.make_coffee(drink)




start()