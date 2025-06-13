#products name


products = ["Hot chocolate", "Mocha", "Americano"]

#print main menu options
#get user input for main menu option
#function main menu option(may be redundant. revise)
def main_menu_options():
    print("Main menu options\n0 - Exit the app.\n1 - Product menu options.")

main_menu_options()

#function to get a product list with their index 
def product_index_list():
    print (list(enumerate(products)))

#get user input for main menu option
user_input_menu = int(input())

#main menu options
if user_input_menu == 1 :
    print("Product menu options\n0 - Return to main menu\n1 - View products.\n2 - Create a new product.\n3 - Update an existing product.\n4 - Delete a product.\n")
elif user_input_menu > 1:
    print("Invalid input.")
elif user_input_menu == 0:
    quit()

#get user input for product options
user_input_options = int(input())

#product options
#used function from above to print products with index
#get user input index and product name to update and delete
if user_input_options == 0:
    print(main_menu_options())
elif user_input_options == 1:
    print(products)
elif user_input_options == 2:
    print(products.append(input("What product would you like to add? ")))
elif user_input_options == 3:
    print(product_index_list())
    user_input_index = int(input("Type in the number of the product you would like to update:"))
    user_input_product_name = input("What product would you like to add?\n")
    products[user_input_index] = user_input_product_name
elif user_input_options == 4:
    print(product_index_list())
    user_input_index_pop = int(input("Please input the number of the product you want to delete: "))
    products.pop(user_input_index_pop)

#check results
print(products)