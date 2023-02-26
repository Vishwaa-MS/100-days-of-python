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

profit = 0
resource = {
    "water": 1000,
    "milk": 800,
    "coffee": 600,
}


def is_resource_sufficient(ingredient):
    for items in ingredient:
        if ingredient[items] >= resource[items]:
            print(f"sorry the {items} is insufficient")
            return False
    return True


def process_coin():
    """Returns total amount of coin inserted"""
    print('Please insert coins !')
    total = 0
    total = int(input('How many quarters!?: ')) * 0.25
    total += int(input('How many dimes!?: ')) * 0.1
    total += int(input('How many nickels!?: ')) * 0.05
    total += int(input('How many pennies!?: ')) * 0.01
    return total


def is_payment_successful(money_received, drink_cost):
    """Returns True is amount is sufficient or False if insufficient"""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"\nHere is your ${change} in change")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money, Money refunded !")
        return False


def make_coffee(drink_name, order_ingredient):
    for items in order_ingredient:
        resource[items] -= order_ingredient[items]
    print(f'Here is your {drink_name} ☕, Enjoy !')


is_on = True
while is_on:
    choice = input('What would you like? (espresso/latte/cappuccino):')
    if choice == 'off':
        is_on = False
    elif choice == 'report':
        print(f"Water: {resource['water']} ml")
        print(f"Milk: {resource['milk']} ml")
        print(f"Coffee: {resource['coffee']} g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink['ingredients']):
            payments = process_coin()
            if is_payment_successful(payments, drink['cost']):
                make_coffee(choice, drink['ingredients'])
