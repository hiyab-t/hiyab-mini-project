from library import app2_copied, app3_copied
import csv

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

orders_list = [{
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

#persisting

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
    

#print main menu

app2_copied.main_menu_opt()

main_menu_input = input()

while True:
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

        exit("Exitting the app. Don't be a stranger.")

    elif main_menu_input == '1':
        print("__________________________\n")
        print("Product Menu\n")
        print("__________________________\n")
        print("0 - Return to Main Menu\n" \
        "1 - Print Products List.\n" \
        "2 - Create New Product.\n" \
        "3 - Update Existing Product.\n" \
        "4 - Delete Product.\n")
        input_product_opt = input("__________________________\n")


        #product menu
        if input_product_opt == '0':
            continue

        elif input_product_opt == '1':

            app2_copied.products_index_list()

        #get user input to create a new order

        elif input_product_opt == '2':

            input_product_name = input("What would you like to add?")
            input_product_price = input('Set the price: ') 

            add_product = {
                'name': input_product_name,
                'price': input_product_price
            }
            products.append(add_product)
            print(f'Product has been successfully added!\n{products}')

        elif input_product_opt == '3':

            input_product_name = input('What would you like to add?')
            input_product_price = input('Set the price: ')
            input_product_price.replace(' ', '')

            while True:
                ('Please ensure to enter a valid price number.')
                input_product_price = input()
                if input_product_price.isdigit():
                    break

                product = {
                    'name': input_product_name,
                    'price': input_product_price
                }

                products.append(product)
                print(f'Your product has been successfuly added.\n{product}')

        elif input_product_opt == '3':
            app2_copied.products_index_list()

            input_update_product_num = input('Which product would you like to update?')

            chosen_product_update = products[int(input_update_product_num)]

            input_update_product_name = input("Enter updated product name:\n")
            input_update_product_price = input("Enter updated price:\n")
            input_update_product_price.replace(' ', '')

            while True:
                ('Please ensure to enter a valid price number.')
                input_update_product_price = input()

                if input_update_product_price.isdigit():
                    break
            
            if input_update_product_name == '':
                break
            elif input_update_product_price == '':
                (f'No changes have been made.\n{chosen_product_update}')
                continue
            else:
                chosen_product_update.update({
                                            'name': input_update_product_name,
                                            'price': input_update_product_price
                                            })
            print(f'Update successful!\n{chosen_product_update}')





