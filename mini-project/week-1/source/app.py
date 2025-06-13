#products name


#homemade_lunch = ["Chicken Burger", "Mushroom Risotto", "Classic Beef Bacon Sandwich"]
#drinks = ["Hot chocolate", "Mocha", "Americano"]
#add_ons = ["Syrup", "Cream", "Chocolate"]

products = ["Hot chocolate", "Mocha", "Americano"]


#print("Products")
#for product_list in products:
#    print(f"- {product_list}")
#def product_list():
#    print(products)
#
#    product_list()
#print main menu options
#get user input for main menu option
def main_menu_options():
    print("Main menu options\n0 - Exit the app.\n1 - Product menu options.")

main_menu_options()

user_input_menu = int(input())

if user_input_menu > 0 :
    print("Product menu options\n0 - Return to main menu\n1 - View products.\n2 - Create a new product.\n3 - Update an existing product.\n4 - Delete a product.\n")
else:
    quit()

#get user input for product options

user_input_options = int(input())

if user_input_options < 1:
    print(main_menu_options())
elif user_input_options == 1:
    print(products)
else:
    print("Wait for an update.")


#def product_list():
#    print(f"Products {homemade_lunch}")

    

#def my_function():
#    print(homemade_lunch, 
#        drinks,
#        add_ons)
#my_function()
#
#for products in (my_function):
#    print(my_function)
#goals to remember
#user ability to create, update, delete a product