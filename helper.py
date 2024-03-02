def is_resources_sufficient(ingredients,resources):
    for i in ingredients:
        if ingredients[i] > resources[i]:
            print(f"Sorry !  There is not enough {i}")
            return False
    return True

def check_transaction(amount,ingredients,resources,money,option):
    remain = amount - ingredients["cost"]
    if remain >= 0:
        print("Transaction Successful")
        money += ingredients["cost"]
        for i in ingredients["ingredients"]:
            resources[i] -= (ingredients["ingredients"])[i]
        if remain > 0:
            print()
            print("------------------------------------")
            print(f"Here is ${remain} dollars in change.")

        print()
        print(f"Here is your {option}. Enjoy!")
        print("          >^_^<          ")
        
    else:
        print("Sorry ! That's not enough money. Money refunded")

def make_report(resources,money):
        print()
        print(" Final Report ")
        print("--------------------")
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${money}")

def make_report(resources):
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")