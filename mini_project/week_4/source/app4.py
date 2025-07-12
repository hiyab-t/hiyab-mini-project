import csv
import os

#tobe imported
def get_int_input():
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

def get_float_input():
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
        "customer_address": "Main Street, LONDON",
        "customer_phone": "07987654321",
        "courier": 1,
        "status": "Preparing",
        "items": "1, 4"
        },
        {
        "customer_name": "Hiyab Tewelde",
        "customer_address": "Antrim road, Belfast",
        "customer_phone": "07404313229",
        "courier": 2, #courier index
        "status": "Delivered",
        "items": "1, 3, 4" #product indexes
        }]

order_status = ['Preparing', 'Out-for-delivery', 'Delivered']

#to be imported to util
def get_validated_int_input_order_items():
    while True:
        try:
            list_order_items = [int(product) for product in input("Enter the number representations of the items you would like to order(Please separate them by comma):\n").split(',')]
            access_order_items_list = [products[product_item_index] for product_item_index in (list_order_items)] 
            print(f'Ordered list of items: {list_order_items}')
            for product_item in access_order_items_list:
                print(f'{product_item['name']} - Price: {product_item['price']}')
            break
        except ValueError as v_oops:
            print(f'{v_oops}. Please enter a valid number or numbers.')
        except IndexError as i_oops:
            print(f'{i_oops}. Please enter a valid number or numbers.')
        except Exception as err:
            print(f"Unexpected {err=}, {type(err)=}. Please enter a valid number or numbers.")

def clear_scroll():
    if os.name == 'nt':
        os.system('clr')
    else:
        os.system('clear')

def main_menu_opt():
    print("__________________________\n")
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
    print("Orders menu\n" \
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
        print(f'{products_index} - {product['name']} .................... {product['price']}')
    print("__________________________\n")

def couriers_index_list():
    print("__________________________\n")
    print("Couriers List:\n")
    for couriers_index, courier in enumerate(couriers):
        print(f'{couriers_index} - {courier['name']}\n {courier['phone']}')
    print("__________________________\n")

def orders_index_list():
    print("__________________________\n")
    print('Orders list')
    for index_order, order in enumerate(orders):
            print(f'{index_order} - \n{order["customer_name"]}\n {order['customer_address']}\n{order['customer_phone']}\n{order['courier']}\n{order['status']}\n{order['items']}')
    print("__________________________\n")

def order_status_list_index():
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
            input_new_product_price = get_float_input()

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
            input_update_product_index = get_int_input()

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
                result = get_float_input()
                chosen_update_product.update({'price':input_updated_product_price})
                print(f'Here is the updated product.\n {chosen_update_product}') 
                continue

        elif input_product_opt == '4':

            products_index_list()

            print('Which product would you like to delete?\n')
            input_delete_product_index = get_int_input()

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

            couriers.append({'name':input_new_courier_name,
                            'phone':input_new_courier_phone})
            continue
            
        #update a courier
        elif input_courier_opt == '3':

            couriers_index_list()

            print('Enter the number of the courier you would like to update:\n')
            input_update_courier_index = get_int_input()

            chosen_update_courier = couriers[input_update_courier_index]

            input_update_courier_name = input("Enter updated courier name:\n")
            input_update_courier_phone = input("Enter updated courier's phone number:\n")
            input_update_courier_phone = input_update_courier_phone.replace(' ','')

            if input_update_courier_name == '':
                print(f"No changes were made to the chosen courier's name.\n{chosen_update_courier}")
            else:
                chosen_update_courier.update({'name':input_new_courier_name})

            while True:
                print('Please ensure to enter a valid phone number.')
                input_update_courier_phone = input('Enter courier phone number:\n')
                if input_update_courier_phone.isdigit() and len(input_update_courier_phone) == 11 or len(input_update_courier_phone):
                    break
            
            if input_update_courier_phone == '':
                print(f"No changed were made to the chosen courier's phone number.")
                continue
            else:
                chosen_update_courier.update({'phone':input_update_courier_phone})
                print(f'Here is the updated courier:\n{chosen_update_courier}')
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
            input_new_customer_phone = input_new_customer_phone.replace(' ', '')

            products_index_list()

            #get a validated string user input for ordered product index values
            input_new_customer_items = get_validated_int_input_order_items()

            couriers_index_list()

            input_new_customer_courier = get_int_input()

            order_status = 'Preparing'

            order = {
                'customer_name': input_new_courier_name,
                'customer_address': input_new_customer_address,
                'customer_phone': input_new_customer_phone,
                'courier': input_new_customer_courier,
                'status': order_status,
                'items': input_new_customer_items
            }

            orders.append(order)

            print('New Order successfully created!')
            for index_order in order:
                print(order)
            
            continue

        #update order status
        elif input_orders_opt == '3':
            
            






            



            

            
            


        

