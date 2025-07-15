from library import file_handler, displays, util
import os

products = [
    {"id": 0, "name": "Falafel burgers", "price": 3.65},
    {"id": 1, "name": "Reuben sandwich", "price": 4},
    {"id": 2, "name": "Chopped salad", "price": 3},
    {"id": 3, "name": "Pasta House salad", "price": 5.40},
    {"id": 4, "name": "Hot Chocolate", "price": 2},
]

couriers = [
    {"id":1, "name": "Uber Eats", "phone": "0789887889"},
    {"id":2, "name": "Deliveroo", "phone": "0784897810"},
]

orders = [
    {
        "customer_name": "John Jones",
        "customer_address": "Main Street,LONDON",
        "customer_phone": "07987654321",
        "courier": 1,
        "status": "Preparing",
        "items": "1,4",
    },
    {
        "customer_name": "Hiyab Tewelde",
        "customer_address": "Antrim road,Belfast",
        "customer_phone": "07404313229",
        "courier": 2,  # courier id
        "status": "Delivered",
        "items": "1,3,4",  # product id
    },
]

#clear screen

def clear_scroll():
    if os.name == "nt":
        os.system("clr")
    else:
        os.system("clear")

#loading orders from orders.csv

file_handler.read_orders_file(orders)

while True:

    #print main menu

    displays.main_menu_opt()

    input_main_menu = util.validate_int_input()

    if input_main_menu == 0:

        #save orders to order.csv
    
        file_handler.save_orders(orders)
    
        exit("Exitting the app. Don't be a stranger!")

    elif input_main_menu == 1:

        displays.products_menu_opt()

        input_product_opt = util.validate_int_input()

        # return to main menu

        if input_product_opt == 0:
            continue

        # products list

        elif input_product_opt == 1:

        #place holder import 

