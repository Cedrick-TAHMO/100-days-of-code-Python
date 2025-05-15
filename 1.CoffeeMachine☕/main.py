#!/usr/bin/env python3
"""
Coffee Machine Simulator

This module simulates a coffee vending machine that can:
- Serve multiple types of coffee drinks
- Handle money transactions
- Track resources
- Generate reports

Author: Your Name
Version: 1.0.0
Python Version: 3.13.2
"""

# Constants for drink recipes and their costs
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

# Constants for coin values in dollars
QUARTER_VALUE = 0.25
DIME_VALUE = 0.10
NICKEL_VALUE = 0.05
PENNY_VALUE = 0.01


def is_resources_sufficient(order_ingredients: dict) -> bool:
    """
    Check if there are enough resources to make the requested drink.

    Args:
        order_ingredients (dict): Dictionary containing required ingredients and their amounts.

    Returns:
        bool: True if all resources are sufficient, False otherwise.
    """
    for item, amount in order_ingredients.items():
        if amount > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def process_coins() -> float:
    """
    Process inserted coins and calculate total value.

    Prompts user to input the count of each coin denomination
    and calculates the total amount.

    Returns:
        float: Total monetary value of inserted coins.
    """
    print("Please insert coins.")
    total = int(input("How many quarters? ")) * QUARTER_VALUE
    total += int(input("How many dimes? ")) * DIME_VALUE
    total += int(input("How many nickels? ")) * NICKEL_VALUE
    total += int(input("How many pennies? ")) * PENNY_VALUE
    return total


def is_transaction_successful(money_received: float, drink_cost: float) -> bool:
    """
    Verify if the payment is sufficient and handle the transaction.

    Args:
        money_received (float): Amount of money received from the customer.
        drink_cost (float): Cost of the selected drink.

    Returns:
        bool: True if payment is sufficient, False otherwise.
    """
    if money_received < drink_cost:
        print("Sorry that's not enough money. Money refunded.")
        return False
    
    change = round(money_received - drink_cost, 2)
    if change > 0:
        print(f"Here is ${change:.2f} in change.")
    
    global profit
    profit += drink_cost
    return True


def make_coffee(drink_name: str, order_ingredients: dict) -> None:
    """
    Prepare the coffee by deducting resources and serving the drink.

    Args:
        drink_name (str): Name of the drink being prepared.
        order_ingredients (dict): Dictionary of ingredients to be used.
    """
    # Deduct used resources
    for item, amount in order_ingredients.items():
        resources[item] -= amount

    print(f"Here is your {drink_name} ☕️. Enjoy!")


def print_report() -> None:
    """Display current resource levels and profit."""
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${profit:.2f}")


def print_menu() -> None:
    """Display available drinks menu."""
    print("\nAvailable Drinks:")
    for drink in MENU:
        print(f"- {drink.title()} (${MENU[drink]['cost']:.2f})")


# Initialize machine state
profit = 0
resources = {
    "water": 300,  # Water in ml
    "milk": 200,   # Milk in ml
    "coffee": 100, # Coffee in grams
}

def main():
    """Main program loop for the coffee machine."""
    is_on = True

    while is_on:
        choice = input("\nWhat would you like? (espresso/latte/cappuccino): ").lower()

        # Handle commands
        if choice == "off":
            print("Shutting down the coffee machine...")
            is_on = False
        elif choice == "report":
            print_report()
        elif choice == "menu":
            print_menu()
        # Process drink orders
        elif choice in MENU:
            drink = MENU[choice]
            if is_resources_sufficient(drink["ingredients"]):
                payment = process_coins()
                if is_transaction_successful(payment, drink["cost"]):
                    make_coffee(choice, drink["ingredients"])
        else:
            print("Invalid selection. Please try again.")


if __name__ == "__main__":
    main()