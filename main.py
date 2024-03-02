import helper as h
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

money = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


is_on = True

while is_on:
    print()
    print(" Ingredients Remain ")
    print("--------------------")
    h.make_report(resources)

    print()
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    
    if choice == "off":
        is_on = False
    elif choice == "admin":
        count = 5
        while count !=0:
            password = input("Enter Admin Password : \n")
            if password == "Uiewwb605":
                print("  Menu  ")
                print("--------")
                print("--> Press 1 for Generate Report")
                print("--> Press 2 for Refill Ingredients \n")

                ans = input("Press --> ")
                if ans == "1":
                    h.make_report(resources)
                    print(f"Money: ${money}")
                    break
                elif ans =="2":
                    h.refill_ingredients(resources)
                    h.make_report(resources)
                    break
            else:
                count -=1
                print(f"Oops! Wrong Password. Try remain {count} times")
        
    else:
        select_choice = MENU[choice]
        if h.is_resources_sufficient(select_choice['ingredients'], resources):
            quarters =int(input("Number of quarters ($0.25) insert : "))
            dimes    =int(input("Number of dimes  ($0.10) insert   : "))
            nickles  =int(input("Number of nickles ($0.05) insert  : "))
            pennies  =int(input("Number of pennies ($0.01) insert  : "))
            print()
            total_amount = pennies * 0.01 + nickles * 0.05 + dimes *0.10 + quarters *0.25
            h.check_transaction(total_amount,select_choice,resources,money,choice.title())