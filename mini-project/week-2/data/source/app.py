#product list

products = ['Mocha', 'Hot chocolate']

#order list

orders_list = [{
    "customer_name": "John Jones",
    "customer_address": "Main Street, LONDON",
    "customer_phone": "07987654321",
    "status": "Preparing"
}, {
    'customer_name': 'Hiyab Tewelde',
    'customer_address': 'Antrim road, Belfast',
    'customer_phone': '07404313229',
    'status': 'Delivered'
}]

#order status list

order_status_list = ['preparing', 'out-for-delivery', 'delivered']

#print main menu options

def main_menu_opt():
    print("Main menu options\n" \
    "0 - Exit App.\n" \
    "1 - Print Products Menu.\n" \
    "2 - Print Orders Menu.\n")

#func to get products list with index

def product_index_list():
    return enumerate(products)

#main menu opt

while True:
        main_menu_opt()
        main_menu_input = input()

        if main_menu_input == '0':
            quit("Exitting the app. Don't be a stanger!")

        #get input for product options

        elif main_menu_input == '1':
            user_input_product_opt = input(
                "Product Menu\n"
                "0 - Return to Main Menu\n" \
                "1 - Print Products List.\n" \
                "2 - Create New Product.\n" \
                "3 - Update Existing Product.\n" \
                "4 - Delete Product.\n")

            #product options

            if user_input_product_opt == '0':
                continue

            elif user_input_product_opt == '1':
                print(products)

            elif user_input_product_opt == '2':
                print(products.append(input("What would you like to add?\n")))

            elif user_input_product_opt == '3':
                print(product_index_list())
                user_input_index = int(input("Enter the number of the product you would like to update:\n"))
                user_input_product_name = input("What product would you like to add?\n")
                products[user_input_index] = user_input_product_name.title()

            elif user_input_product_opt == '4':
                print(product_index_list())
                user_input_index_pop = int(input("Please enter the number of the product you want to delete:\n"))
                products.pop(user_input_index_pop)
                user_input_product_opt = (input())
            else:
                print('Invalid input. Please enter a valid number.\n')
                
        elif main_menu_input == '2':
            input_orders_menu = input(
                "Orders menu\n" \
                "0 - Return to main menu.\n" \
                "1 - Print Orders Dictionary.\n" \
                "2 - Create New Order.\n" \
                "3 - Update Existing Order Status.\n" \
                "4 - Update Existing Order.\n" \
                "5 - Delete Order.\n")
            
            if input_orders_menu == '0':
                continue

            elif input_orders_menu == '1':
                print(orders_list)

            elif input_orders_menu == '2':
                user_input_name = input("Enter customer full name: ")
                user_input_address = input("Enter customer address: ")
                user_input_number = int(input("Enter customer phone number: "))
                while True:
                    print('Please ensure to enter a valid phone number and no blank spaces.')
                    user_input_number = input('Enter customer phone number:\n')
                    if user_input_number.isdigit() and len(user_input_number) == 11 or len(user_input_number) == 10:
                        break
                order_status = 'PREPARING'
                order = {
                    'customer_name': user_input_name,
                    'customer_address': user_input_address,
                    'Customer_phone number': user_input_number,
                    'Status': order_status
                }
                orders_list.append(order)
                print(order)

            elif input_orders_menu == '3':
                print('Orders list')

                for index, orders in enumerate(orders_list):
                    orders_index = (f'{index}: {orders}')
                    print(orders_index)

                input_order_status_num = int(input("Which order's status would you like to update?\n")) #TRY EXCEPT MIGHT BE NECESSARY bc of "int"
                
                chosen_order = orders_list[input_order_status_num]
                
                for index_status, orders_to_list in enumerate(order_status_list):
                    print(f'{index_status}: {orders_to_list}')
                input_status_index = int(input('What would you like to update the order status to?\n')) #try-except for same as #118
                
                orders.update({'status': order_status_list[input_status_index]})
                print(f'Update successful!\n{chosen_order}')
        elif input_orders_menu == '4':
            print('Orders list')

            for index, orders in enumerate(orders_list):
                orders_index = (f'{index}: {orders}')
                print(orders_index)

            input_order_num = int(input("Which order would you like to update?\n"))

            input_update_name = input("Enter updated customer name:\n")
            input_update_address = input('Enter updated customer address:\n')
            input_update_phone = input('Enter updated customer phone number:\n')
            while True:
                    print('Please ensure to enter a valid phone number and no blank spaces.')
                    user_input_number = input('Enter customer phone number:\n')
                    if user_input_number.isdigit() and len(user_input_number) == 11 or len(user_input_number) == 10:
                        break
            
            orders.update({'customer_name': order})

        else:
            print("Invalid input. Please enter a valid number.\n")




