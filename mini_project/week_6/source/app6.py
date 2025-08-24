from library.utils import util
from library import displays
from week_5.source import my_db_ap
import os

def clear_scroll():
    if os.name == "nt":
        os.system("clr")
    else:
        os.system("clear")

print("Welcome to Maria's cafe!")

my_db_ap.retrieve_products()

my_db_ap.retrieve_couriers()

my_db_ap.retrieve_orders()

while True:

    #print main menu options
    displays.main_menu_opt()

    #get input for main menu options
    input_main_menu = input()
    input_main_menu = util.validate_int_input(input_main_menu)

    if input_main_menu == 0:   
    
        exit("Exitting the app. Don't be a stranger!")

    elif input_main_menu == 1:

        displays.products_menu_opt()

        input_product_opt = input()
        input_product_opt = util.validate_int_input(input_product_opt)

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
            input_new_product_name = util.validate_name_input(input_new_product_name)

            input_new_product_price = input('Set the price:\n')
            input_new_product_price = util.validate_float_input(input_new_product_price)

            #create new product 
            my_db_ap.insert_product(input_new_product_name, input_new_product_price)

            #update products

        elif input_product_opt == 3:
            clear_scroll()

            #retrieve and print all product with ID

            my_db_ap.retrieve_products()

            input_chosen_update_product = input("Enter the ID of the product you would like to update:\n")
            input_chosen_update_product = util.validate_int_input(input_chosen_update_product)

            #update product name

            input_update_product_name = input('Enter updated product name:\n')
            input_update_product_name = util.validate_name_input(input_update_product_name)

            if input_update_product_name == '':
                print('No changes have been made to product name.\n')
            else:
                my_db_ap.update_product_name(input_update_product_name, input_chosen_update_product)
                print('Product name successfully updated.')
            
            #update product price
            input_update_product_price = input('Set the price:\n')

            if input_update_product_price == '':
                print('No changes have been made to product price.')
            else:
                input_update_product_price = util.validate_float_input(input_update_product_price)
                my_db_ap.update_product_price(input_update_product_price, input_chosen_update_product)
                print('Product price successfully updated.')
                
        #delete a product
        elif input_product_opt == 4:
            clear_scroll()

            #retrieve all products from product table
            my_db_ap.retrieve_products()

            input_delete_product_id = input("Enter the ID of the product you would like to delete:\n")
            input_delete_product_id = util.validate_int_input(input_delete_product_id)

            my_db_ap.delete_product(input_delete_product_id)

    #courier menu
    elif input_main_menu == 2:

        displays.couriers_menu_opt()

        #get courier opt input
        input_courier_opt = input()
        input_courier_opt = util.validate_int_input(input_courier_opt)

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
            input_new_courier_name = util.validate_name_input(input_new_courier_name)

            input_new_courier_phone = input('Set courier phone number:\n')
            input_new_courier_phone = util.validate_phone_num(input_new_courier_phone)

            my_db_ap.insert_courier(input_new_courier_name, input_new_courier_phone)

        #update existing courier
        elif input_courier_opt == 3:
            clear_scroll()

            my_db_ap.retrieve_couriers()

            #get input for the courier to update
            input_chosen_update_courier = input('Enter the ID of the courier you would like to update:\n')
            input_chosen_update_courier = util.validate_int_input(input_chosen_update_courier)

            #get input for update courier name
            input_update_courier_name = input("Enter updated courier name:\n")

            if input_update_courier_name == '':
                print("No changes have been made to courier name.")
            else:
                input_update_courier_name = util.validate_name_input(input_update_courier_name)
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
            clear_scroll()

            #retrieve couriers from couriers table
            my_db_ap.retrieve_couriers()

            input_delete_courier_id = input('Enter the ID of the courier you would like to delete:\n')
            input_delete_courier_id = util.validate_int_input(input_delete_courier_id)

            my_db_ap.delete_courier(input_delete_courier_id)

    #orders menu
    elif input_main_menu == 3:
        clear_scroll()

        #print orders menu
        displays.order_menu_opt()

        #get input for orders menu
        input_order_opt = input()
        input_order_opt = util.validate_int_input(input_order_opt)

        #return to main menu
        if input_order_opt == 0:
            continue
        
        elif input_order_opt == 1:
            clear_scroll()

            my_db_ap.retrieve_orders()

        elif input_order_opt == 2:
            clear_scroll()

            my_db_ap.retrieve_orders_by_status()

        elif input_order_opt == 3:
            clear_scroll()

            #get customer name
            input_new_customer_name = input("Enter Customer name:\n")
            input_new_customer_name = util.validate_name_input(input_new_customer_name)

            #get customer address
            input_new_customer_address = input("Enter Customer address:\n")
            input_new_customer_address = util.validate_address_input(input_new_customer_address)

            #get customer phone
            input_new_customer_phone = input("Enter Customer phone number:\n")
            input_new_customer_phone = util.validate_phone_num(input_new_customer_phone)

            my_db_ap.retrieve_couriers()

            #get customer courier
            input_new_customer_courier = input("Enter Customer Courier choice:\n")
            input_new_customer_courier = util.validate_int_input(input_new_customer_courier)

            my_db_ap.retrieve_products()

            print("Enter")

            #get customer order items
            input_list_new_customer_items =  [int(product) for product in input().split(",")]

            input_str_new_customer_items = ",".join(str(index_item) for index_item in input_list_new_customer_items)

            my_db_ap.insert_customer(input_new_customer_name, input_new_customer_address, input_new_customer_phone, input_new_customer_courier, input_str_new_customer_items)

        elif input_order_opt == 4:
            clear_scroll()

            #read orders with ID
            my_db_ap.retrieve_orders()

            #get input for order to update its order status
            input_update_order = input("Enter the order ID to update order status:\n")
            input_update_order = util.validate_int_input(input_update_order)

            #read order status with ID
            my_db_ap.retrieve_order_status()

            input_update_order_status_id = input("Enter the ID of the order status you would like to update into:\n")
            input_update_order_status_id = util.validate_int_input(input_update_order_status_id)

            input_update_order_status = f"{my_db_ap.get_order_status(input_update_order_status_id)}"

            my_db_ap.update_customer_order_status(input_update_order_status, input_update_order)

        elif input_order_opt == 5:
            clear_scroll()

            #read orders with ID
            my_db_ap.retrieve_orders()

            input_update_customer_property_id = input("Which Customer Order ID would you like to update?")
            input_update_customer_property_id = util.validate_int_input(input_update_customer_property_id)

            input_update_customer_name = input("Enter updated customer name:\n")

            if input_update_customer_name == '':
                print('No changes have been made to customer name.')
            else:
                input_update_customer_name = util.validate_name_input(input_update_customer_name)
                my_db_ap.update_customer_name(input_update_customer_name, input_update_customer_property_id)

            input_update_customer_address = input("Enter updated customer address:\n")

            if input_update_customer_address == '':
                print('No changes have been made to customer address.')
            else:
                input_update_customer_address = util.validate_address_input(input_update_customer_address)
                my_db_ap.update_customer_address(input_update_customer_address, input_update_customer_property_id)

            input_update_customer_phone = input("Enter updated customer phone:\n")

            if input_update_customer_phone == '':
                print('No changes have been made to customer phone.')
            else:
                input_update_customer_phone = util.validate_phone_num(input_update_customer_phone)
                my_db_ap.update_customer_phone(input_update_customer_phone, input_update_customer_property_id)

            my_db_ap.retrieve_products()

            print("Enter updated items and separate them by comma:\n")
            input_update_list_customer_items = [int(product) for product in input().split(",")]

            input_update_str_customer_items = ",".join(str(index_item) for index_item in input_update_list_customer_items)

            if input_update_str_customer_items == '':
                print('No changes have been made to customer item choices.')
            else:
                my_db_ap.update_customer_order_items(input_update_str_customer_items, input_update_customer_property_id)

            my_db_ap.retrieve_couriers()

            print("Which courier would you like? Enter its ID:\n\n")    
            input_update_customer_courier = input()

            if input_update_customer_courier == '':
                print('No changes have been made to customer courier.')
            else:
                input_update_customer_courier = util.validate_int_input(input_update_customer_courier)
                my_db_ap.update_customer_courier(input_update_customer_courier, input_update_customer_property_id)

        elif input_order_opt == 6:
            clear_scroll()

            my_db_ap.retrieve_orders()

            input_delete_order_id = input('Which order would you like to delete? Enter its ID\n')
            input_delete_order_id = util.validate_int_input(input_delete_order_id)

            my_db_ap.delete_order(input_delete_order_id)
        
    elif input_main_menu == 4:
        clear_scroll()

        displays.customer_menu_opt()

        input_customer_opt = input()
        input_customer_opt = util.validate_int_input(input_customer_opt)

        if input_customer_opt == 0:
            continue

        elif input_customer_opt == 1:

            my_db_ap.retrieve_customers()

        elif input_customer_opt == 2:

            input_new_customer_name = input('Enter new customer name:\n')
            input_new_customer_name = util.validate_name_input(input_new_customer_name)

            input_new_customer_address = input('Enter new customer address:\n')
            input_new_customer_address = util.validate_address_input(input_new_customer_address)

            input_new_customer_phone = input('Enter a new customer phone number:\n')
            input_new_customer_phone = util.validate_phone_num(input_new_customer_phone)

            my_db_ap.insert_customer(input_new_customer_name, input_new_customer_address, input_new_customer_phone)

        elif input_customer_opt == 3:

            my_db_ap.retrieve_customers()

            input_update_customer_property_id = input("Which Customer would you like to update? Enter ID:\n")
            input_update_customer_property_id = util.validate_int_input(input_update_customer_property_id)

            input_update_customer_name = input("Enter updated customer name:\n")

            if input_update_customer_name == '':
                print('No changes have been made to customer name.')
            else:
                input_update_customer_name = util.validate_name_input(input_update_customer_name)
                my_db_ap.update_customer_name(input_update_customer_name, input_update_customer_property_id)

            input_update_customer_address = input("Enter updated customer address:\n")

            if input_update_customer_address == '':
                print('No changes have been made to customer address.')
            else:
                input_update_customer_address = util.validate_address_input(input_update_customer_address)
                my_db_ap.update_customer_address(input_update_customer_address, input_update_customer_property_id)

            input_update_customer_phone = input("Enter updated customer phone:\n")

            if input_update_customer_phone == '':
                print('No changes have been made to customer phone.')
            else:
                input_update_customer_phone = util.validate_phone_num(input_update_customer_phone)
                my_db_ap.update_customer_phone(input_update_customer_phone, input_update_customer_property_id)

        elif input_customer_opt == 4:

            my_db_ap.retrieve_customers()

            input_delete_customer_id = input('Which customer would you like to delete? Enter ID:\n')
            input_delete_customer_id = util.validate_int_input(input_delete_customer_id)

            my_db_ap.delete_customer(input_delete_customer_id)

    else:
        clear_scroll()
        print("Invalid input. Please try again.\n")

            

            



            










