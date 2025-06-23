#product list

products = ['Mocha', 'Hot chocolate']

#order list

orders_list = [{
    "customer_name": "John Jones",
    "customer_address": "Main Street, LONDON",
    "customer_phone": "07987654321",
    "status": "preparing"
}]

#print main menu options and get user input
def main_menu_opt():
    print("Main menu options\n" \
    "0 - Exit the app.\n" \
    "1 - Product menu options.\n" \
    "2 - Orders menu.\n")

#func to get products list with index
def product_index_list():
    return enumerate(products)

#main menu opt
while True:
        main_menu_opt()
        main_menu_input = input()

        if main_menu_input == '0':
            quit("Exitting the app. Don't be a stanger!")

        elif main_menu_input == '1':
            user_input_product_opt = input(
                "Product menu options\n"
                "0 - Return to main menu\n" \
                "1 - View products.\n" \
                "2 - Create a new product.\n" \
                "3 - Update an existing product.\n" \
                "4 - Delete a product.\n")
            
            if user_input_product_opt == '0':
                continue

            elif user_input_product_opt == '1':
                print(products)

            elif user_input_product_opt == '2':
                print(products.append(input("What would you like to add? ")))

            elif user_input_product_opt == 3:
                print(product_index_list())
                user_input_index = int(input("Type in the number of the product you would like to update:"))
                user_input_product_name = input("What product would you like to add?\n")
                products[user_input_index] = user_input_product_name.title()

            elif user_input_product_opt == '4':
                print(product_index_list())
                user_input_index_pop = int(input("Please input the number of the product you want to delete: "))
                products.pop(user_input_index_pop)
                user_input_product_opt = (input())
                
        elif main_menu_input == '2':
            input_orders_menu = input(
                "Orders menu\n" \
                "0 - Return to main menu.\n" \
                "1 - Orders list.\n" \
                "2 - Enter customer information and get order status\n" \
                "3 - Update order status\n" \
                "4 - Update existing order\n" \
                "5 - Delete order\n")
            
            if input_orders_menu == '0':
                continue

            elif input_orders_menu == '1':
                print(orders_list)

            elif input_orders_menu == '2':
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

            elif input_orders_menu == '3':
                for index, orders in enumerate(orders_list):
                    print(f'{index}: {orders}')
                input_customer_order_num = int(input("Which customer's order would you like to update? "))
                order_get_key = orders.keys('status')
                print(f'{orders_list['status']}')
                #for index_orders, order_keys in enumerate(order_get_key):
                #    print(f'{index_orders}: {order_keys}')
        else:
            print("Invalid input. Please enter the appropriate number.\n")




