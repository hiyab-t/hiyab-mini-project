from week_2.source import app

try:
        with open("../data/products.txt", 'r') as products_file:
                products_content = products_file.read()

        for line_products in products_content:
                print(line_products, end='')      
except FileNotFoundError:
        print('Failed to open file.')

try:
        with open('../data/couriers.txt', 'r') as couriers_file:
                couriers_content = couriers_file.read()
        
        for line_couriers in couriers_content:
                print(line_couriers, end='')
except FileNotFoundError:
        print('Failed to open.')


app.main_menu_opt()

if app.main_menu_input == '0':
        with open('../data/products.txt', 'r') as write_products_file:
                updated_products_content = write_products_file.write()

        for updated_line_products in updated_products_content:
                print(updated_line_products, end='')

        with open('../data/couriers.txt', 'w') as write_couriers_file:
                updated_couriers_content = write_couriers_file.write()

        for updated_line_couriers in write_couriers_file:
                print(updated_line_couriers, end='')

        exit("Exitting the app. Don't be a stanger!")
else:
        print('test')


