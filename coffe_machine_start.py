MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money = 0


def is_resource_sufficient(order):
    order_ingredients = order['ingredients']
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def process_coins():
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    if money_received < drink_cost:
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global money
        money += drink_cost
        return True


def make_coffee(drink_name):
    order_ingredients = MENU[drink_name]['ingredients']
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")


def run_machine(drink_name):
    drink_item = MENU[drink_name]
    if is_resource_sufficient(drink_item):
        total = process_coins()
        if is_transaction_successful(total, drink_item["cost"]):
            make_coffee(drink_name)
            return True
            
if __name__ == "__main__":
    flag = True
    while flag:
        choice = input("What would you like?(espresso/latte/cappuccino):")
        if choice == "off":
            flag = False
        elif choice == "report":
            print(f"Water: {resources['water']}ml")
            print(f"Milk: {resources['milk']}ml")
            print(f"Coffe: {resources['coffee']}g")
            print(f"Money: ${money}")
        else:
            if not run_machine(choice):
                flag = False

