# products name
products = ["Hot chocolate", "Mocha", "Americano"]

# orders_list
orders_list = ["something"]


# print main menu option
# function main menu option(may be redundant. revise)
def main_menu_options():
    print(
        "Main menu options\n"
        "0 - Exit the app.\n"
        "1 - Product menu options. \n"
        "2 - "
    )


main_menu_options()


# function to get a product list with their index
def product_index_list():
    return list(enumerate(products))


# get user input for main menu option
user_input_menu = int(input())

# main menu options
if user_input_menu == 0:
    quit("Exitting the app. Don't be a stranger!")
elif user_input_menu == 1:
    print(
        "Product menu options\n"
        "0 - Return to main menu\n"
        "1 - View products.\n"
        "2 - Create a new product.\n"
        "3 - Update an existing product.\n"
        "4 - Delete a product.\n"
    )
elif user_input_menu == 2:
    print(
        "Orders menu\n"
        "0 - Return to main menu.\n"
        "1 - Orders list.\n"
        "2 - Enter customer information and get order status\n"
        "3 - Update order status\n"
        "4 - Update existing order\n"
        "5 - Delete order"
    )

# get user input for product options
user_input_options = int(input())

# list of product options
# used function from above to print products with index
# get user input index and product name to update and delete
if user_input_options == 0:
    print(main_menu_options())
elif user_input_options == 1:
    print(products)
elif user_input_options == 2:
    print(products.append(input("What product would you like to add? ")))
elif user_input_options == 3:
    print(product_index_list())
    user_input_index = int(
        input("Type in the number of the product you would like to update:")
    )
    user_input_product_name = input("What product would you like to add?\n")
    products[user_input_index] = user_input_product_name.title()
elif user_input_options == 4:
    print(product_index_list())
    user_input_index_pop = int(
        input("Please input the number of the product you want to delete: ")
    )
    products.pop(user_input_index_pop)
else:
    print(
        "Invalid input. Product lists will remain unchanged. Restart the app to reconfigure."
    )

# orders menu
