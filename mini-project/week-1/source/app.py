# created products names

'''
homemade_lunch = [""]
refreshements = [""]
hot_drinks = [""]
cold_drink = [""]
add_ons = [""]
'''
main_menu = """0, 1, 2"""
product_menu = ["0. Return to main menu", "1. mocha", "2. "]
user_input= print(input(f"What would you like to order? Here is the main menu: {main_menu}"))


if user_input == 0:
    print("Exit the app.")
elif user_input == 1:
    print(f"Here is the product menu opetion: {product_menu}")
elif user_input == 2:
    print(f"Main menu:{main_menu}")
if user_input == product_menu[1]:
    print(f"products list: {product_menu}")
if  user_input == product_menu[2]:
    product_menu.append(input("What product would you like to create?"))


