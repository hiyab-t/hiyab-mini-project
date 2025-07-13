import csv
import os
import re

#tobe imported
def validate_int_input():
    while True:
            try: 
                value = int(input())
                if value < 0:
                    raise ValueError('Negative numbers are not allowed')
            except ValueError as v_oops:
                print(f'{v_oops}. Please enter a valid number.')
            except IndexError as i_oops:
                print(f'{i_oops}. Please enter a valid number.')
            else:
                return value

def validate_float_input():
    while True:
        try:
            value = float(input())
            if value < 0:
                raise ValueError("Negative numbers are not allowed")
            elif value != round(value, 2):
                raise ValueError("Numbers must rounded up to two decimal numbers")
        except ValueError as v_oops:
                print(f'{v_oops}. Please enter a valid number.')
        except OverflowError as o_oops:
                print(f'{o_oops}. Please enter a valid number.')
        else:
            return value
        
def validate_phone_num(input_phone,**kwargs):
    while True:
        input_phone = re.sub(r'\s+', '', input_phone)
        if input_phone.isdigit() and (len(input_phone) == 11 or len(input_phone) == 10):
            return input_phone
        else:
            print('Invalid phone number. Please try again.')
            input_phone = input()

products = [{
        'name': 'Falafel burgers',
        'price': 3.65
        },
        {
        'name': 'Reuben sandwich',
        'price': 4
        },
        {'name': 'Chopped salad',
        'price': 3},
        {'name': 'Pasta House salad',
        'price': 5},
        {'name': 'Hot Chocolate',
        'price': 2}]

couriers = [{
        'name':'Uber Eats',
        'phone':'0789887889'
        },
        {
        'name':'Deliveroo',
        'phone':'0784897810'
        }]

orders = [{
        "customer_name": "John Jones",
        "customer_address": "Main Street,LONDON",
        "customer_phone": "07987654321",
        "courier": 1,
        "status": "Preparing",
        "items": "1,4"
        },
        {
        "customer_name": "Hiyab Tewelde",
        "customer_address": "Antrim road,Belfast",
        "customer_phone": "07404313229",
        "courier": 2, #courier index
        "status": "Delivered",
        "items": "1,3,4" #product indexes
        }]

order_status = ['Cancelled','Preparing', 'Out-for-delivery', 'Delivered']

#tget_ imported to util
def validate_int_input_order_items():
    while True:
        try:
            list_order_items = [int(product) for product in input("Enter the number representation of the items you would like to place order(Please separate them by comma):\n").split(',')]
            access_order_items_list = [products[product_item_index] for product_item_index in (list_order_items)] 
            print(f'Ordered list of items: {list_order_items}')
            for product_item in access_order_items_list:
                print(f'{product_item['name']}\nPrice: {product_item['price']}\n')
            break
        except ValueError as v_oops:
            print(f'{v_oops}. Please enter a valid number or numbers.')
        except IndexError as i_oops:
            print(f'{i_oops}. Please enter a valid number or numbers.')
        except Exception as err:
            print(f"Unexpected {err=}, {type(err)=}. Please enter a valid number or numbers.")

    value = ','.join(str(index_item) for index_item in list_order_items)
    return value

def clear_scroll():
    if os.name == 'nt':
        os.system('clr')
    else:
        os.system('clear')

def main_menu_opt():
    print("\n__________________________\n")
    print('Main Menu\n')
    print('0 - Exit the App\n' \
    '1 - Product Menu\n' \
    '2 - Couriers Menu\n' \
    '3 - Orders Menu\n')
    print("__________________________\n")

def products_menu_opt():
    print("__________________________\n")
    print('Products Menu\n')
    print("0 - Return to Main Menu\n" \
        "1 - Products List.\n" \
        "2 - Create New Product.\n" \
        "3 - Update Existing Product.\n" \
        "4 - Delete Product.\n")
    print("__________________________\n")

def couriers_menu_opt():
    print("__________________________\n")
    print("Couriers Menu\n"
            "0 - Return to Main Menu\n"
            "1 - Couriers List\n"
            "2 - Create New Courier\n"
            "3 - Update Existing Courier\n"
            "4 - Delete Courier")
    print("__________________________\n")

def order_menu_opt():
    print("__________________________\n")
    print("Orders Menu\n" \
            "0 - Return to main menu.\n" \
            "1 - Orders list.\n" \
            "2 - Create New Order.\n" \
            "3 - Update Existing Order Status.\n" \
            "4 - Update Existing Order.\n" \
            "5 - Delete Order.\n")
    print('__________________________\n')

def products_index_list():
    print("__________________________\n")
    print("Products List:\n")
    for products_index, product in enumerate(products):
        print(f'{products_index} - {product['name']}\nPrice - {product['price']}\n')
    print("__________________________\n")

def couriers_index_list():
    print("__________________________\n")
    print("Couriers List:\n")
    for couriers_index, courier in enumerate(couriers):
        print(f'{couriers_index} - {courier['name']}\n{courier['phone']}\n')
    print("__________________________\n")

def orders_index_list():
    print("__________________________\n")
    print('Orders List')
    for index_order, order in enumerate(orders):
            print(f'{index_order} - \nCustomer name: {order["customer_name"]}\nCustomer address: {order['customer_address']}\nCustomer phone: {order['customer_phone']}\nCourier: {order['courier']}\nStatus: {order['status']}\nItems: {order['items']}\n')
    print("__________________________\n")

def order_status_list_index():
    print("__________________________\n")
    print('Order Status List\n')
    for index_order_status, order in enumerate(order_status):
        print(f'{index_order_status} - {order}\n')
    print("__________________________\n")

#persisting data
try:
    with open('week_4/data/products.csv', mode='r') as products_file:
        products_content = csv.DictReader(products_file)

        for products_row in products_file:
            print(products_row, end='')
except FileNotFoundError as whoops:
    print('Failed to open file.')

try:
    with open('week_4/data/couriers.csv', 'r') as couriers_file:
        couriers_content = csv.DictReader(couriers_file)

        for couriers_row in couriers_file:
            print(couriers_row, end='')

except FileNotFoundError as whoops:
    print('Failed to open file.')

try:
    with open('week_4/data/orders.csv', 'r') as orders_file:
        orders_content = csv.DictReader(orders_file)
        
        for orders_row in orders_content:
            print(orders_row, end='')

except FileNotFoundError as whoops:
    print('File failed to open.')
    
#loop main menu opt

while True:

    #print main menu and get user input

    main_menu_opt()

    input_main_menu = input()
    input_main_menu = input_main_menu.strip()

    if input_main_menu == '0':

        try: 
            with open('week_4/data/products.csv', mode='w') as products_file:
                products_keys = ['name', 'price']
                updated_products = csv.DictWriter(products_file, fieldnames=products_keys)

                updated_products.writeheader()
                updated_products.writerows(products)
        except FileNotFoundError:
            print('Failed to open file.')

        try:
            with open('week_4/source/couriers.csv', mode='w') as couriers_file:
                couriers_keys = ['name', 'phone']
                updated_couriers = csv.DictWriter(couriers_file, fieldnames=couriers_keys)
                
                updated_couriers.writeheader()
                updated_couriers.writerows(couriers)
        except FileNotFoundError:
            print('Failed to open file.')
        
        clear_scroll()

        exit("Exitting the app. Don't be a stranger!")

    #print product menu and get user input

    elif input_main_menu == '1':

        products_menu_opt()

        input_product_opt = input()
        input_product_opt = input_product_opt.title()
        input_product_opt = input_product_opt.strip()

        #return to main menu

        if input_product_opt == '0':
            continue
        
        #products list

        elif input_product_opt == '1':

            products_index_list()

        #print products list and get user input for a new product to create

        elif input_product_opt == '2':

            products_index_list()

            input_new_product_name = input("What product would you like to add?\n")
            input_new_product_name = input_new_product_name.strip() 
            
            print('Set the price:\n')
            input_new_product_price = validate_float_input()

            #create new product 

            create_product = {
                'name': input_new_product_name,
                'price': input_new_product_price
            }
            products.append(create_product)
            print(f'Product has been successfully added!\n{products}')

        elif input_product_opt == '3':

            products_index_list()

            print('Enter the number of the product you would like to update:\n')
            input_update_product_index = validate_int_input()

            chosen_update_product = products[input_update_product_index]

            input_updated_product_name = input('Enter updated product name:\n')
            input_updated_product_price = input("Set the price:\n")

            if input_updated_product_name == '':
                print(f'No changes were conducted to the product name.\n {chosen_update_product}')
            else:
                chosen_update_product.update({'name': input_updated_product_name})
            if input_updated_product_price == '':
                result = None
                print('No changes were been made to product price.\n ')
                print(f'{chosen_update_product}')    
            else:
                print('Enter the price again to confirm:\n')
                result = validate_float_input()
                chosen_update_product.update({'price':input_updated_product_price})
                print(f'Here is the updated product.\n {chosen_update_product}') 
                continue

        elif input_product_opt == '4':

            products_index_list()

            print('Which product would you like to delete?\n')
            input_delete_product_index = validate_int_input()

            products.pop(input_delete_product_index)
            print(f'Product has been succeessfully deleted. Remainining products:\n{products}')
            continue

    #couriers menu
    elif input_main_menu == '2':

        couriers_menu_opt()

        #get input for courier option
        input_courier_opt = input()

        #return to main menu
        if input_courier_opt == '0':
            continue
        
        #print courier list
        elif input_courier_opt == '1':
            couriers_index_list()

        #create a new courier
        elif input_courier_opt == '2':
            
            input_new_courier_name = input("What courier would you like to add?\n")
            input_new_courier_name = input_new_courier_name.title()
            input_new_courier_name = input_new_courier_name.strip()
            input_new_courier_phone = input("Enter courier phone number:\n")

            #validate phone number input
            input_new_courier_phone = validate_phone_num(input_new_courier_phone)

            couriers.append({'name':input_new_courier_name,
                            'phone':input_new_courier_phone})
            continue
            
        #update a courier
        elif input_courier_opt == '3':

            couriers_index_list()

            print('Enter the number of the courier you would like to update:\n')
            input_update_courier_index = validate_int_input()

            chosen_update_courier = couriers[input_update_courier_index]

            input_update_courier_name = input("Enter updated courier name:\n")

            if input_update_courier_name == '':
                print(f"\nNo changes were made to the chosen courier's name.")
                get_courier_name = chosen_update_courier.get('name')
                print(f'Courier name remains {get_courier_name}.\n')
            else:
                chosen_update_courier.update({'name':input_update_courier_name})
                get_courier_name = chosen_update_courier.get('name')
                print(f'Courier name has been updated to {get_courier_name}')

            #get courier phone 
            input_update_courier_phone = input("Enter updated courier's phone number:\n")

            #validate courier phone
            if input_update_courier_phone == '':
                print(f"No changed were made to the chosen courier's phone number.")
                get_courier_phone = chosen_update_courier.get('phone')
                print(f'Courier phone number reamins {get_courier_phone}.\n')
            else:
                input_update_courier_phone = validate_phone_num(input_update_courier_phone)
                chosen_update_courier.update({'phone':input_update_courier_phone})
                get_courier_phone = chosen_update_courier.get('phone')
                print(f'\nCourier phone number has been updated to {get_courier_phone}.\n')         
            
            print('\nAction completed. Returning to Main Menu.')
            continue

        #delete courier
        elif input_courier_opt == '4':

            couriers_index_list()

            input_delete_courier_index = input('Enter the number of the courier you would like to delete:\n')

            couriers.pop(input_delete_courier_index)
            continue
    
    #orders menu
    elif input_main_menu == '3':

        order_menu_opt()

        input_orders_opt = input()

        #return to main menu
        if input_orders_opt == '0':
            continue
        
        #print orders menu
        elif input_orders_opt == '1':

            orders_index_list()

        #create new order
        elif input_orders_opt == '2':

            input_new_customer_name = input("Enter customer name:\n")
            input_new_customer_address = input('Enter customer address:\n')
            input_new_customer_phone = input('Enter customer phone:\n')

            input_new_customer_phone = validate_phone_num(input_new_customer_phone)

            products_index_list()

            #get a validated string user input for ordered product index values
            input_new_customer_items = validate_int_input_order_items()

            couriers_index_list()

            input_new_customer_courier = validate_int_input()

            order_status = 'Preparing'

            order = {
                'customer_name': input_new_customer_name,
                'customer_address': input_new_customer_address,
                'customer_phone': input_new_customer_phone,
                'courier': input_new_customer_courier,
                'status': order_status,
                'items': input_new_customer_items
            }

            orders.append(order)

            print('New Order has  been successfully created!\n')
            for order_key, order_value in order.items():
                print(f'{order_key}, {order_value}')
            
            continue

        #update order status
        elif input_orders_opt == '3':

            orders_index_list()

            input_update_status_index = validate_int_input()

            chosen_update_order = orders[input_update_status_index]
        
            order_status_list_index()

            input_update_status_index = validate_int_input()

            chosen_update_order.update({
                'status': input_update_status_index
                })
            print(f'Order Status has been successfully updated!\n{chosen_update_order}')

            continue

        #update order property
        elif input_orders_opt == '4':

            orders_index_list()

            print('Which order would you like to update?\n')
            input_update_order_property_index = validate_int_input()

            chosen_update_order_property = orders[input_update_order_property_index]

            input_update_customer_name = input("Enter updated customer name:\n")
            
            input_update_customer_address = input('Enter updated customer address:\n')
            input_update_customer_phone = input('Enter updated customer phone number:\n')

            couriers_index_list()
            print('Enter updated courier choice:\n')
            input_update_customer_courier = input()

            products_index_list()

            #get a validated string user input for ordered product index values
            input_update_customer_items = input()
            
            #customer name update with feedback if no change
            if input_update_customer_name == '':
                print('No change has been made to customer name.')
            else:
                chosen_update_order_property.update({
                    'customer_name': input_update_customer_name
                    })
                get_customer_name = chosen_update_order_property.get('customer_name')
                print(f'Customer name has been updated to {get_customer_name}')

            #customer address update with feedback if no change
            if input_update_customer_address == '':
                print('No change has been made to customer address.')
            else:
                chosen_update_order_property.update({
                    'customer_address': input_update_customer_address
                    })
                get_customer_address = chosen_update_order_property.get('customer_address')
                print(f'Customer address has been updated to {get_customer_address}')

            if input_update_customer_phone == '':
                print('No change has been made to customer phone number.')
            else:
                input_update_customer_phone = validate_phone_num(input_update_customer_phone)

                chosen_update_order_property.update({
                    'customer_phone': input_update_customer_phone
                })
                get_customer_phone = chosen_update_order_property.get('customer_phone')
                print(f'Customer phone number has been updated to {get_customer_phone}.')

            if input_update_customer_courier == '':
                print('No change has been made to courier choice.')
            else:
                input_update_customer_courier = validate_int_input()
                chosen_update_order_property.update({
                    'courier': input_update_customer_courier
                })
                get_customer_courier = chosen_update_order_property.get('customer_phone')
                print(f'Courier choice has been updated to {get_customer_courier}')

            if input_update_customer_items == '':
                print('No change has been made to ordered items.')
            else:
                input_update_customer_items = validate_int_input_order_items()
                chosen_update_order_property.update({
                    'items': input_update_customer_items
                })
                print(f'Notice: If enteries were left blank, no updates have been conducted.\n')
                print(f'Here is the updated order:\n{chosen_update_order_property}')

        elif input_orders_opt == '5':

            orders_index_list()

            input_delete_order_index = validate_int_input()

            orders.pop(input_delete_order_index)

            print('Order has been succeffuly deleted.')

            continue


                


        








            



            

