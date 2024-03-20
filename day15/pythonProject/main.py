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

resource = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def is_resource_sufficient(order_igredients):
    for item in order_igredients:
        if order_igredients[item] >= resource[item]:
            print("not enough resource")
            return False
    return True


def is_transaction_suceess(money_received, drink_cost):
    """return true when the pyament is acceppted"""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"here is change {change}")
        global profit
        profit += drink_cost
        return True
    else:
        print('Not enough money garrib: ')
        return False


def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resource[item] -= order_ingredients[item]
    print(f"here is your {drink_name}")


def process_coins():
    """returns the total coins"""
    print("Please Enter the coins")
    total = int(input("how many quaters: ")) * 0.25
    total += int(input("how many dimes: ")) * 0.1
    total += int(input("how many nickels: ")) * 0.05
    total += int(input("how many pennies: ")) * 0.01
    return total


profit = 0
is_on = True
while is_on:
    choice = input("What whould you like to have (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"water: {resource["water"]}")
        print(f"milk: {resource["milk"]}")
        print(f"coffee: {resource["coffee"]}")
        print(f"profit: {profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_suceess(payment, drink["cost"]):
                make_coffee(drink, drink["ingredients"])
