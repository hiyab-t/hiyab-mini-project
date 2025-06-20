#product list
products = ["Hot chocolate", "Mocha", "Americano"]

#orders 
order = {
    'customer_name':'',
    'customer_address': '',
    'customer_phone': '',
    'status':''
}

#orders_list
orders_list = [{}]


#print main menu option
#function main menu option(may be redundant. revise)
def main_menu_options():
    print("Main menu options\n" \
    "0 - Exit the app.\n" \
    "1 - Product menu options.\n" \
    "2 - Orders menu.")

main_menu_options()

#function to get a product list with their index 
def product_index_list():
    print (list(enumerate(products)))

#function to get user inputs
#def user_input_product_options():
#    return int(input())

#while loop


#get user input for main menu option
user_input_menu = int(input())

#main menu options
while user_input_menu > 2:
    print('Invalid input. Please enter the appropriate number again.')
    user_input_menu = int(input())
    if user_input_menu == 0:
            quit("Exitting the app. Don't be a stranger!")
    elif user_input_menu == 1:
            print("Product menu options\n"
                "0 - Return to main menu\n" \
                "1 - View products.\n" \
                "2 - Create a new product.\n" \
                "3 - Update an existing product.\n" \
                "4 - Delete a product.")
            user_input_product_options = int(input())
    elif user_input_menu == 2:
            print("Orders menu\n" \
                "0 - Return to main menu.\n" \
                "1 - Orders list.\n" \
                "2 - Enter customer information and get order status\n" \
                "3 - Update order status\n" \
                "4 - Update existing order\n" \
                "5 - Delete order")
            user_input_orders_menu = int(input())
#user_input_orders_menu = int(input())
        
#else: break
    #print('Oop! Invalid input. Please enter the appropriate number according to the given choices.')
    

#get user input for product options


#list of product options
#used function from above to print products with index
#get user input index and product name to update and delete

while user_input_product_options > 4:
    print('Invalid input. Please enter the appropriate number again.')
    user_input_product_options = int(input())
    if user_input_product_options == 0:
        print(main_menu_options())
    elif user_input_product_options == 1:
        print(products) 
    elif user_input_product_options == 2:
        print(products.append(input("What product would you like to add? ")))
    elif user_input_product_options == 3:
        print(product_index_list())
        user_input_index = (input("Type in the number of the product you would like to update:"))
        user_input_product_name = input("What product would you like to add?\n")
        products[user_input_index] = user_input_product_name.title()
    elif user_input_product_options == 4:
        print(product_index_list())
        user_input_index_pop = (input("Please input the number of the product you want to delete: "))
        products.pop(user_input_index_pop)


#order menu
#if user_input_order_menu  
while user_input_orders_menu > 3:
    print("Invalid input. Please enter the appropriate number again.")
    user_input_orders_menu = int(input())
if user_input_orders_menu == 0: #REVISE CODE. free play for now
    print(orders_list)
elif user_input_orders_menu == 1:
    print(orders_list)
elif user_input_orders_menu == 2:
    user_input_name = input("Enter customer full name: ")
    user_input_address = input("Enter customer address: ")
    user_input_number = int(input("Enter customer phone number: "))
    order_status = 'PREPARING'
    order = {
        'customer name': user_input_name,
        'customer address': user_input_address,
        'Customer phone number': user_input_number,
        'Status': order_status
    }
    orders_list.append(order)
    print(order)
elif user_input_orders_menu == 3:
    print(list(enumerate(order)))
    user_input_customer_order_num = int(input("Which customer's order would you like to update? "))
    print(list(enumerate()))



