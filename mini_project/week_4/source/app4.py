import csv
import os

def clear_scroll():
    if os.name == 'nt':
        os.system('clr')
    else:
        os.system('clear')



products =[{
        'name': 'Falafel burgers',
        'price': 3.65
        },
        {
        'name': 'Reuben sandwich',
        'price': 4
        }]

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
        "status": "Preparing"
        },
        {
        "customer_name": "Hiyab Tewelde",
        "customer_address": "Antrim road, Belfast",
        "customer_phone": "07404313229",
        "status": "Delivered"
        }]

order_status = ['Preparing', 'Out-for-delivery', 'Delivered']

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
    print("Here's products List:\n")
    for products_index, product in enumerate(products):
        print(f'{products_index} - {product}')
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

        exit("Exitting the app. Don't be a stranger.")

    #print product menu and get user input
    elif main_menu_input == '1':

        products_menu_opt()

        input_product_opt = input()

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
            input_product_price = input('Set the price:\n') 
            input_product_price.replace(' ', '')

            #validate price input and add new product to product list
            while True:
                if input_product_price.isdigit():
                    break
                else:
                    ('Please enter a valid price number.')
                    input_product_price = input()

            add_product = {
                'name': input_product_name,
                'price': input_product_price
            }
            products.append(add_product)
            print(f'Product has been successfully added!\n{products}')
        





