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
coffee_machine_off = False
water = 300
milk = 200
coffee = 100
money = float()
while not  coffee_machine_off :
   

    def report(drink):
        
        global water 
        global milk 
        global coffee
        global money 
        if drink == "latte":
            water -= MENU['latte']['ingredients']['water']
            milk -= MENU['latte']['ingredients']['milk']
            coffee -= MENU['latte']['ingredients']['coffee']
            money += MENU['latte']['cost']
        elif drink == "espresso":
            water -= MENU['esresso']['ingredients']['water']
            milk -= MENU['esresso']['ingredients']['milk']
            coffee -= MENU['esresso']['ingredients']['coffee']
            money += MENU['esresso']['cost']
        elif drink == "cappuccino":
            water -= MENU['cappuccino']['ingredients']['water']
            milk -= MENU['cappuccino']['ingredients']['milk']
            coffee -= MENU['cappuccino']['ingredients']['coffee']
            money += MENU['cappuccino']['cost']

    def coin(quarters,dimers,nickles,pennies):
        
        totals =((quarters * 0.25)+(dimers *0.1 )+(nickles *  0.05)+(pennies * 0.01) )
        
        return totals

    def coffee_selection(coffee):
        prize = 0
        if coffee == "espresso":
            prize = MENU['espresso']['cost']
        elif coffee == "latte":
            prize = MENU['latte']['cost']
        elif coffee == "cappuccino":
            prize = MENU['cappuccino']['cost']
        return prize




    coffee_selected = input("What would you like? (espresso/latte/cappuccino): ")
    if coffee_selected == "report":
        print(f"water: {water}ml")
        print(f"Milk: {milk}ml")
        print(f"Coffee: {coffee}gm")
        print(f"Money: ${money}")
        coffee_selected = input("What would you like? (espresso/latte/cappuccino): ")
    elif coffee_selected == "off":
        coffee_machine_off = True 
    print("Please insert coins.")

    quarters1 =int( input("how many quarters?:"))
    dimers1  = int( input("how many dimers?:"))
    nickles1 = int( input("how many nickles?:"))
    pennies1 = int( input("how many pennies?:"))
    price = int
    price = coffee_selection(coffee_selected)
    money += price
    change = int
    change = coin(quarters1,dimers1,nickles1,pennies1) - price
    print(f"Here is ${round(change,2)} in change")
    print(f"Here is your {coffee_selected}. Enjoy!")
    report(coffee_selected)








