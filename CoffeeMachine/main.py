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


def print_report(resources, money):
    return (
        f"Water: {resources['water']}ml \n"
        f"Milk: {resources['milk']}ml \n"
        f"Coffee: {resources['coffee']}g \n"
        f"Money: ${round(money, 2)}"
    )


def check_resources(coffee_choice, resources):
    has_enough_resources = True

    for resource in MENU[coffee_choice]["ingredients"]:
        if resources[resource] < MENU[coffee_choice]["ingredients"][resource]:
            has_enough_resources = False
            print(f"Sorry there is not enough {resource}")
            break

    return has_enough_resources


def process_coins():
    print ("Please insert coins.")
    quarters = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickles = int(input("how many nickles?: "))
    pennies = int(input("how many pennies?: "))
    return quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01


def execute_transaction(user_money, coffee_choice):
    coffee_price = MENU[coffee_choice]["cost"]

    if user_money < coffee_price:
        print(f"Sorry {coffee_choice} costs ${coffee_price}. ${user_money} is not enough money. Money refunded.")
        return False
    else:
        refund = round(user_money - coffee_price, 2)
        print(f"Here is your change ${refund}")
        return True


def make_coffee(coffee_choice, resources):
    for resource in MENU[coffee_choice]["ingredients"]:
        resources[resource] -= MENU[coffee_choice]["ingredients"][resource]
    print(f"Here is your {coffee_choice} ☕. Enjoy!")
    return resources

def coffee_machine():
    resources = {
        "water": 300,
        "milk": 200,
        "coffee": 100
    }
    money = 0

    can_continue = True

    while can_continue:
        machine_options = "/".join(MENU.keys())
        command = input(f"What would you like? ({machine_options}): ").lower()

        if command == "off":
            # TODO: Turn off the machine
            can_continue = False
        elif command == "report":
            # TODO: Print report
            print(print_report(resources, money))
        elif command in MENU.keys():
            # TODO: Check resources sufficient?
            has_enough_resources = check_resources(command, resources)
            if has_enough_resources:
                # TODO: Process coins
                user_money = process_coins()

                # TODO: Check transaction successful
                is_transaction_successful = execute_transaction(user_money, command)

                if has_enough_resources and is_transaction_successful:
                    money += MENU[command]["cost"]
                    # TODO: Make coffee
                    resources = make_coffee(command, resources)


coffee_machine()
