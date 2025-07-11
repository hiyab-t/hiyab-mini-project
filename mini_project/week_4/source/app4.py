import csv
import os

#tobe imported
def get_int_input(prompt_int, **kwargs):
    while True:
            try: 
                value1 = int(input(prompt_int))
                if value1 < 0:
                    raise ValueError('Negative numbers are not allowed')
            except ValueError as whoops:
                print(f'{whoops}. Please enter a valid number.')
            except IndexError as oops:
                print(f'{oops}. Please enter a valid number.')
            else:
                return value1

def get_float_input(prompt_float, **kwargs):
    while True:
        try:
            value = float(input(prompt_float))
            if value < 0:
                raise ValueError("Negative numbers are not allowed")
            elif value != round(value, 2):
                raise ValueError("Numbers must rounded up to two decimal numbers")
        except ValueError as whoops:
                print(f'{whoops}. Please enter a valid number.')
        except OverflowError as ouou:
                print(f'{ouou}. Please enter a valid number.')
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

def products_index_list():
    print("__________________________\n")
    print("Products List:\n")
    for products_index, product in enumerate(products):
        print(f'{products_index} - {product['name']} .................... {product['price']}')
    print("__________________________\n")

def couriers_index_list():
    print("__________________________\n")
    print("Here's Couriers List:\n")
    for couriers_index, courier in enumerate(couriers):
        print(f'{couriers_index} - {courier}')
    print("__________________________\n")

def orders_index_list():
    print("__________________________\n")
    print('Orders List\n')
    for orders_index, order in enumerate(orders):
        print(f'{orders_index} - {order}')
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

    main_menu_input = input()
    main_menu_input = main_menu_input.strip()

    if main_menu_input == '0':

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
    elif main_menu_input == '1':

        products_menu_opt()

        input_product_opt = input()
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

            input_product_name = input("What would you like to add?\n")
            input_product_name = input_product_name.strip() 
            
            input_product_price = get_float_input('Set the price:\n')

            #create new product 

            create_product = {
                'name': input_product_name,
                'price': input_product_price
            }
            products.append(create_product)
            print(f'Product has been successfully added!\n{products}')

        elif input_product_opt == '3':

            products_index_list()

            input_update_product_index = get_int_input('Enter the number of the product you would like to update:\n')

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
                result = get_float_input(f'Enter the price again to confirm:\n')
                chosen_update_product.update({'price':input_updated_product_price})
                print(f'Here is the updated product.\n {chosen_update_product}') 

        elif input_product_opt == '4':

            products_index_list()

            input_delete_product_index = get_int_input('Which product would you like to delete?\n')

            products.pop(input_delete_product_index)
            print(f'Product has been succeessfully deleted. Remainining products:\n{products}')
            

            
            


        





