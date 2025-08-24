from library import file_handler, displays, util
from week_5.source import my_db_ap 
import os

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

order_status = ["Cancelled", "Preparing", "Out-for-delivery", "Delivered"]

def orders_index_list():
    print("__________________________\n")
    print("Orders List")
    for index_order, order in enumerate(orders):
        print(
            f"{index_order} - \nCustomer name: {order['customer_name']}\nCustomer address: {order['customer_address']}\nCustomer phone: {order['customer_phone']}\nCourier: {order['courier']}\nStatus: {order['status']}\nItems: {order['items']}\n"
        )
    print("__________________________\n")

def order_status_list_index():
    print("__________________________\n")
    print("Order Status List\n")
    for index_order_status, order in enumerate(order_status):
        print(f"{index_order_status} - {order}\n")
    print("__________________________\n")

#clear screen

def clear_scroll():
    if os.name == "nt":
        os.system("clr")
    else:
        os.system("clear")

#loading products from products table

my_db_ap.retrieve_products()

#laoding couriers from couriers table

my_db_ap.retrieve_couriers()

#loading orders from orders.csv

file_handler.read_orders_file()

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

            #retrieve products from product table
            my_db_ap.retrieve_products()

        #create new product
        elif input_product_opt == 2:
            clear_scroll()

            input_new_product_name = input("What would you like to add?\n")
            input_new_product_name = util.validate_str_input(input_new_product_name)

            print('Set the price:\n')
            input_new_product_price = util.validate_float_input()

            #create new product 
            my_db_ap.insert_product(input_new_product_name, input_new_product_price)

            #update products

        elif input_product_opt == 3:
            clear_scroll()

            #retrieve and print all product with ID

            my_db_ap.retrieve_products()

            print("Enter the ID of the product you would like to update:\n")
            input_chosen_update_product = util.validate_int_input()

            #update product name
            print('Enter updated product name:\n')
            input_update_product_name = input()

            if input_update_product_name == '':
                #input_update_product_name = '%s'
                print('No changes have been made to product name.\n')
            else:
                input_update_product_name = util.validate_str_input(input_update_product_name)
                my_db_ap.update_product_name(input_update_product_name, input_chosen_update_product)
                print('Product name successfully updated.')
            
            #update product price
            input_update_product_price = input('Set the price:\n')

            if input_update_product_price == '':
                #input_update_product_price = '%s'
                print('No changes have been made to product price.')
            else:
                print("Confirm the price by entering again:\n")
                input_update_product_price = util.validate_float_input()
                my_db_ap.update_product_price(input_update_product_price, input_chosen_update_product)
                print('Product price successfully updated.')
                
        #delete a product
        elif input_product_opt == 4:
            clear_scroll()

            #retrieve all products from product table
            my_db_ap.retrieve_products()

            print("Enter the ID of the product you would like to delete:\n")
            input_delete_product_id = util.validate_int_input()

            my_db_ap.delete_product(input_delete_product_id)

    #courier menu
    elif input_main_menu == 2:

        displays.couriers_menu_opt()

        #get courier opt input
        input_courier_opt = util.validate_int_input()

        #return to main menu
        if input_courier_opt == 0:
            continue

        #view courier list
        elif input_courier_opt == 1:
            clear_scroll()

            #retrieve all couriers from couriers table
            my_db_ap.retrieve_couriers()

        #create new courier
        elif input_courier_opt == 2:
            clear_scroll()

            input_new_courier_name = input("What would you like to add?\n")
            input_new_courier_name = util.validate_str_input(input_new_courier_name)

            input_new_courier_phone = input('Set courier phone number:\n')
            input_new_courier_phone = util.validate_phone_num(input_new_courier_phone)

            my_db_ap.insert_courier(input_new_courier_name, input_new_courier_phone)

        #update existing courier
        elif input_courier_opt == 3:

            my_db_ap.retrieve_couriers()

            #get input for the courier to update
            print('Enter the ID of the courier you would like to update:\n')
            input_chosen_update_courier = util.validate_int_input()

            #get input for update courier name
            input_update_courier_name = input("Enter updated courier name:\n")

            if input_update_courier_name == '':
                print("No changes have been made to courier name.")
            else:
                input_update_courier_name = util.validate_str_input(input_update_courier_name)
                my_db_ap.update_courier_name(input_update_courier_name, input_chosen_update_courier)

            #get input for update courier phone
            input_update_courier_phone = input("Enter updated courier phone number:\n")

            if input_update_courier_phone == '':
                print('No changes have been made to courier phone.')
            else:
                input_update_courier_phone = util.validate_phone_num(input_update_courier_phone)
                my_db_ap.update_courier_phone(input_update_courier_phone, input_chosen_update_courier)

        #delete courier
        elif input_courier_opt == 4:

            #retrieve couriers from couriers table
            my_db_ap.retrieve_couriers()

            print('Enter the ID of the courier you would like to delete:\n')
            input_delete_courier_id = util.validate_int_input()

            my_db_ap.delete_courier(input_delete_courier_id)


    elif input_main_menu == 3:

        displays.order_menu_opt()

        #get input for orders options
        input_orders_opt = util.validate_int_input()

        #return to main menu
        if input_orders_opt == 0:
            continue

        #view orders list
        elif input_orders_opt == 1:
            displays.orders_index_list()

        #create new order
        elif input_orders_opt == 2:

            #get input for new customer name and validate it
            input_new_customer_name = input()
            input_new_customer_name = util.validate_str_input(input_new_customer_name)

            #get input for new customer address and validate it
            input_new_customer_address = input()
            input_new_customer_address = util.validate_address_input(input_new_customer_address)

            #get input for new customer phone and validate it
            input_new_customer_phone = input()
            input_new_customer_phone = util.validate_phone_num(input_new_customer_phone)
            
            #view products from products table
            my_db_ap.retrieve_products()

            input_list_new_customer_items =  [int(product) for product in input().split(",")]

            input_str_new_customer_items = ",".join(str(index_item) for index_item in input_list_new_customer_items)

            #view couriers from couriers table
            my_db_ap.retrieve_couriers()

            input_new_customer_courier = util.validate_int_input()

            util.add_new_order(input_new_customer_name, input_new_customer_address, input_new_customer_phone, input_new_customer_courier, input_str_new_customer_items, orders)

        elif input_orders_opt == 3:
            clear_scroll()

            orders_index_list()

            input_update_order_id = util.validate_int_input()

            chosen_update_customer_order_status = orders[input_update_order_id]

            order_status_list_index()

            input_update_status_id = util.validate_int_input()

            chosen_status = order_status[input_update_status_id]

            chosen_update_customer_order_status.update({
                'status': chosen_status
            }
            )

        elif input_orders_opt == 4:
            clear_scroll()

            displays.orders_index_list()

            print("Which order would you like to update?\n")
            input_update_order_property_index = util.validate_int_input()

            chosen_update_order_property = orders[input_update_order_property_index]

            # get customer name 
            input_update_customer_name = input("Enter updated customer name:\n")

            # customer name update with feedback if no change

            if input_update_customer_name == "":
                print("No change has been made to customer name.")
            else:
                input_update_customer_name = util.validate_str_input(input_update_customer_name)
                chosen_update_order_property.update(
                    {"customer_name": input_update_customer_name}
                )

            # get updated customer address

            input_update_customer_address = input("Enter updated customer address:\n")

            # customer address update with feedback if no change

            if input_update_customer_address == "":
                print("No change has been made to customer address.")
            else:
                input_update_customer_address = util.validate_address_input(
                input_update_customer_address)

                chosen_update_order_property.update(
                    {"customer_address": input_update_customer_address}
                )

            #get customer phone update input

            input_update_customer_phone = input(
                "Enter updated customer phone number:\n"
            )

            #customer phone update with feedback if no change

            if input_update_customer_phone == "":
                print("No change has been made to customer phone number.")
            else:
                input_update_customer_phone = util.validate_phone_num(
                    input_update_customer_phone
                )

                chosen_update_order_property.update(
                    {"customer_phone": input_update_customer_phone}
                )

            #view courier list from courier table then get input

            my_db_ap.retrieve_couriers()

            print("Enter updated courier choice:\n")
            input_update_customer_courier = input()

            #customer courier phone update with feedback if no change

            if input_update_customer_courier == "":
                print("No change has been made to courier choice.")
            else:
                print('Confirm courier choice by entering again.')
                input_update_customer_courier = util.validate_int_input()

                chosen_update_order_property.update(
                    {"courier": input_update_customer_courier}
                )

            #view products for ordered items list then get input

            my_db_ap.retrieve_products()

            print("Enter the number representaion of the order items you would like to place order(Please separate multiple entries by comma):")
            input_update_customer_items = input()

            if input_update_customer_items == "":
                print("No change has been made to ordered items.")
            else:
                print('To confirm enter the number representaion of the items again:\n')
                input_list_updated_customer_items =  [int(product) for product in input().split(",")]

                input_str_updated_customer_items = ",".join(str(index_item) for index_item in input_list_updated_customer_items)

                chosen_update_order_property.update(
                    {"items": input_str_updated_customer_items}
                )

            print(
                "Notice: If enteries were left blank, no updates have been conducted.\n"
            )
            print(f"Here is the updated order:\n{chosen_update_order_property}")

            file_handler.save_orders(orders)

        elif input_orders_opt == 5:
            clear_scroll()

            displays.orders_index_list()

            input_delete_order_index = util.validate_int_input()

            orders.pop(input_delete_order_index)

            print("Order has been succeffuly deleted.")

            file_handler.save_orders()

    else:
        print('Invalid input. Please enter a valid number.')










            

            