#product list
products = ['Mocha', 'Hot chocolate']

#order list
orders_list =[{
    "customer_name": "John Jones",
    "customer_address": "Main Street, LONDON",
    "customer_phone": "07987654321",
    "status": "Preparing"
    },
    {
    "customer_name": "Hiyab Tewelde",
    "customer_address": "Antrim road, Belfast",
    "customer_phone": "07404313229",
    "status": "Delivered"
    }]

#order status list
order_status_list = ['preparing', 'out-for-delivery', 'delivered']

#print main menu 
def main_menu_opt():
    print("\nMain menu options\n" \
    "0 - Exit App.\n" \
    "1 - Products Menu.\n" \
    "2 - Order menu.\n")

#func to get products list with index
def products_index_list():
    print('Products list')
    for index_product, product in enumerate(products):
        print(f'{index_product} - {product}')

#func to print orders list with index
def orders_index_list():
    print('Orders list')
    for index, orders in enumerate(orders_list):
        print(f'{index} - {orders}')

def main():
    pass

if __name__ == "__main__":

    #main menu 
    while True:
            main_menu_opt()
            main_menu_input = input()
    
            if main_menu_input == '0':
                quit("Exitting the app. Don't be a stanger!")
    
            #get input for product menu
            elif main_menu_input == '1':
                user_input_product_opt = input(
                    "Product Menu\n"
                    "0 - Return to Main Menu\n" \
                    "1 - Print Products List.\n" \
                    "2 - Create New Product.\n" \
                    "3 - Update Existing Product.\n" \
                    "4 - Delete Product.\n")
    
                #product menu
                if user_input_product_opt == '0':
                    continue
            
                elif user_input_product_opt == '1':
                        products_index_list()
        
                elif user_input_product_opt == '2':
                    print(products.append(input("What would you like to add?\n")))
    
                elif user_input_product_opt == '3':
                    products_index_list()
                    user_input_index = input("Enter the number of the product you would like to update:\n")
                    user_input_product_name = input("What product would you like to add?\n")
                    products[int(user_input_index)] = user_input_product_name.title()
    
                elif user_input_product_opt == '4':
                    print(products_index_list())
                    user_input_index_pop = input("Please enter the number of the product you want to delete:\n")
                    products.pop(int(user_input_index_pop))
    
            #orders menu
            elif main_menu_input == '2':
                input_orders_menu = input(
                    "Orders menu\n" \
                    "0 - Return to main menu.\n" \
                    "1 - Orders list.\n" \
                    "2 - Create New Order.\n" \
                    "3 - Update Existing Order Status.\n" \
                    "4 - Update Existing Order.\n" \
                    "5 - Delete Order.\n")
                
                if input_orders_menu == '0':
                    continue
    
                elif input_orders_menu == '1':
                    orders_index_list()
    
                #get user input to update existing order
                elif input_orders_menu == '2':
                    user_input_name = input("Enter customer full name: ")
                    user_input_address = input("Enter customer address: ")
                    user_input_phone_num = input("Enter customer phone number: ")
                    while True:
                        print('Please ensure to enter a valid phone number and no blank spaces.')
                        user_input_phone_num = input('Enter customer phone number:\n')
                        if user_input_phone_num.isdigit() and len(user_input_phone_num) == 11 or len(user_input_phone_num) == 10:
                            break
                    order_status = 'PREPARING'
                    order = {
                        'customer_name': user_input_name,
                        'customer_address': user_input_address,
                        'Customer_phone number': user_input_phone_num,
                        'Status': order_status
                    }
                    orders_list.append(order)
                    print(order)
    
                #printed order status list with index
                elif input_orders_menu == '3':
                    orders_index_list()
    
                    input_order_status_num = input("Which order's status would you like to update?\n") 
                    
                    chosen_order = orders_list[int(input_order_status_num)]
                    
                    print('Order status list')
                    for index_status, orders_to_list in enumerate(order_status_list):
                        print(f'{index_status}: {orders_to_list}')
                    input_status_index = input('What would you like to update the order status to?\n')
                    
                    chosen_order.update({'status': order_status_list[int(input_status_index)]})
                    print(f'Order status update successful!\n{chosen_order}')
    
                    try:
                        input_order_status_num = input()
                    except IndexError: 
                        print('Invalid input. Please enter a valid number.')
                    else:
                        print(f'{input_order_status_num} accepted.')

                #get user input to update order
                elif input_orders_menu == '4':
                    orders_index_list()
        
                    input_order_num = input("Which order would you like to update?\n")
        
                    chosen_order_property_update = orders_list[int(input_order_num)]
        
                    input_update_name = input("Enter updated customer name:\n")
                    input_update_address = input('Enter updated customer address:\n')
                    input_update_phone = input('Enter updated customer phone number:\n')
                    input_update_phone.replace(' ', '')
    
                    #utilized while loop to handle empty input and other requirements for customer number
                    while True:
                            if input_update_phone.isdigit() and len(input_update_phone) == 11 or len(input_update_phone) == 10:
                                break
                            else:
                                print('Please ensure to enter a valid phone number.')
                                input_update_phone = input('Enter updated customer phone number:\n')
                            
                    if input_update_name == '':
                        break
                    elif input_update_address == '':
                        break
                    elif input_update_phone == '':
                        print(f'No update was conducted. Order information will remain the same.\n{chosen_order_property_update}')
                        continue
                    else:
                        chosen_order_property_update.update({'customer_name': input_update_name, 
                                                            'customer_address': input_update_address,
                                                            'customer_phone': input_update_phone})
                        print(f'Order properties update successful!\n {chosen_order_property_update}')
                elif input_orders_menu == '5':
                    orders_index_list()
    
                    input_delete_order_index = input('Which order would you like to delete?\n')
    
                    orders_list.pop(int(input_delete_order_index))
                    print(f'Order has been successfuly deleted. Remaining orders:\n {orders_index_list()}')
            else:
                print("Invalid input. Please enter a valid number.\n")
    
    


