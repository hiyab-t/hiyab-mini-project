import os
from library import util, file_handler

""" Welcome to Maria's cafe! This is a fully functional CLI based cafe application 
to manage and configure customer, courier and order information, and settings. """

products = [
    {"name": "Falafel burgers", "price": 3.65},
    {"name": "Reuben sandwich", "price": 4},
    {"name": "Chopped salad", "price": 3},
    {"name": "Pasta House salad", "price": 5},
    {"name": "Hot Chocolate", "price": 2},
]

couriers = [
    {"name": "Uber Eats", "phone": "0789887889"},
    {"name": "Deliveroo", "phone": "0784897810"},
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
        "courier": 2,  # courier index
        "status": "Delivered",
        "items": "1,3,4",  # product indexes
    },
]

order_status = ["Cancelled", "Preparing", "Out-for-delivery", "Delivered"]


def clear_scroll():
    if os.name == "nt":
        os.system("clr")
    else:
        os.system("clear")


def main_menu_opt():
    print("\n__________________________\n")
    print("Main Menu\n")
    print(
        "0 - Exit the App\n"
        "1 - Product Menu\n"
        "2 - Couriers Menu\n"
        "3 - Orders Menu\n"
    )
    print("__________________________\n")


def products_menu_opt():
    print("__________________________\n")
    print("Products Menu\n")
    print(
        "0 - Return to Main Menu\n"
        "1 - Products List.\n"
        "2 - Create New Product.\n"
        "3 - Update Existing Product.\n"
        "4 - Delete Product.\n"
    )
    print("__________________________\n")


def couriers_menu_opt():
    print("__________________________\n")
    print(
        "Couriers Menu\n"
        "0 - Return to Main Menu\n"
        "1 - Couriers List\n"
        "2 - Create New Courier\n"
        "3 - Update Existing Courier\n"
        "4 - Delete Courier"
    )
    print("__________________________\n")


def order_menu_opt():
    print("__________________________\n")
    print(
        "Orders Menu\n"
        "0 - Return to main menu.\n"
        "1 - Orders list.\n"
        "2 - Create New Order.\n"
        "3 - Update Existing Order Status.\n"
        "4 - Update Existing Order.\n"
        "5 - Delete Order.\n"
    )
    print("__________________________\n")


def products_index_list():
    print("__________________________\n")
    print("Products List:\n")
    for products_index, product in enumerate(products):
        print(f'{products_index} - {product["name"]}\nPrice - {product["price"]}\n')
    print("__________________________\n")


def couriers_index_list():
    print("__________________________\n")
    print("Couriers List:\n")
    for couriers_index, courier in enumerate(couriers):
        print(f"{couriers_index} - {courier['name']}\n{courier['phone']}\n")
    print("__________________________\n")


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


def return_main_menu_after_pause():
    while True:
        return_main_menu_after_pause = input('\nEnter "R" to return to main menu.\n')
        break
    if return_main_menu_after_pause.capitalize() == "r":
        main_menu_opt()
    else:
        print('Invalid input. Please enter "R" to return to main menu.')


print("Welcome to Maria's Cafe!\n")

# print products,courier,orders from their csv files

file_handler.read_products_file()
file_handler.read_couriers_file()
file_handler.read_orders_file()

# loop main menu opt

while True:
    # print main menu and get user input

    main_menu_opt()

    input_main_menu = util.validate_int_input()

    if input_main_menu == 0:
        # persist data to their csv files

        file_handler.save_products(products)

        file_handler.save_couriers(couriers)

        file_handler.save_orders(orders)

        clear_scroll()

        exit("Exitting the app. Don't be a stranger!")

    # print product menu and get user input

    elif input_main_menu == 1:
        products_menu_opt()

        input_product_opt = util.validate_int_input()

        # return to main menu

        if input_product_opt == 0:
            continue

        # products list

        elif input_product_opt == 1:
            products_index_list()

            return_main_menu_after_pause()

        # print products list and get user input for a new product to create

        elif input_product_opt == 2:
            products_index_list()

            input_new_product_name = input("What product would you like to add?\n")
            input_new_product_name = util.validate_str_input(input_new_product_name)

            print("Set the price:\n")
            input_new_product_price = util.validate_float_input()

            # create new product

            create_product = {
                "name": input_new_product_name,
                "price": input_new_product_price,
            }
            products.append(create_product)
            print("Product has been successfully added!")

            return_main_menu_after_pause()

        elif input_product_opt == 3:
            products_index_list()

            print("Enter the number of the product you would like to update:\n")
            input_update_product_index = util.validate_int_input()

            chosen_update_product = products[input_update_product_index]

            input_updated_product_name = input("Enter updated product name:\n")
            input_updated_product_name = util.validate_str_input(
                input_updated_product_name
            )
            input_updated_product_price = input("Set the price:\n")

            # update product name and feedback if no change
            if input_updated_product_name == "":
                print("No changes were conducted to the product name.\n")
            else:
                chosen_update_product.update({"name": input_updated_product_name})

            # update product price and feedback if no change
            if input_updated_product_price == "":
                result = None
                print("No changes were been made to product price.\n ")
                print(f"{chosen_update_product}")
            else:
                print("Enter the price again to confirm:\n")
                result = util.validate_float_input()
                chosen_update_product.update({"price": input_updated_product_price})
                print(f"Here is the updated product.\n {chosen_update_product}")

            return_main_menu_after_pause()

        elif input_product_opt == 4:
            products_index_list()

            print("Which product would you like to delete?\n")
            input_delete_product_index = util.validate_int_input()

            products.pop(input_delete_product_index)
            print("Product has been succeessfully deleted. Remainining products:\n")

            return_main_menu_after_pause()

    # couriers menu
    elif input_main_menu == 2:
        couriers_menu_opt()

        # get input for courier option
        input_courier_opt = util.validate_int_input()

        # return to main menu
        if input_courier_opt == 0:
            continue

        # print courier list
        elif input_courier_opt == 1:
            couriers_index_list()

            return_main_menu_after_pause()

        # create a new courier
        elif input_courier_opt == 2:
            # get courier name and validate input
            input_new_courier_name = input("What courier would you like to add?\n")
            input_new_courier_name = util.validate_str_input(input_new_courier_name)

            # get courier phone and validate input
            input_new_courier_phone = input("Enter courier phone number:\n")
            input_new_courier_phone = util.validate_phone_num(input_new_courier_phone)

            couriers.append(
                {"name": input_new_courier_name, "phone": input_new_courier_phone}
            )

            print("New courier successfully created!")

            return_main_menu_after_pause()

        # update a courier
        elif input_courier_opt == 3:
            couriers_index_list()

            # get index of the courier to update
            print("Enter the number of the courier you would like to update:\n")
            input_update_courier_index = util.validate_int_input()

            chosen_update_courier = couriers[input_update_courier_index]

            # get updated courier name and validate input
            input_update_courier_name = input("Enter updated courier name:\n")
            input_update_courier_name = util.validate_str_input(
                input_update_courier_name
            )

            if input_update_courier_name == "":
                print("\nNo changes were made to the chosen courier's name.")
                get_courier_name = chosen_update_courier.get("name")
                print(f"Courier name remains {get_courier_name}.\n")
            else:
                chosen_update_courier.update({"name": input_update_courier_name})
                get_courier_name = chosen_update_courier.get("name")
                print(f"Courier name has been updated to {get_courier_name}")

            # get courier phone and validate input
            input_update_courier_phone = input(
                "Enter updated courier's phone number:\n"
            )

            if input_update_courier_phone == "":
                print("No changed were made to the chosen courier's phone number.")
                get_courier_phone = chosen_update_courier.get("phone")
                print(f"Courier phone number reamins {get_courier_phone}.\n")
            else:
                input_update_courier_phone = util.validate_phone_num(
                    input_update_courier_phone
                )
                chosen_update_courier.update({"phone": input_update_courier_phone})
                get_courier_phone = chosen_update_courier.get("phone")
                print(
                    f"\nCourier phone number has been updated to {get_courier_phone}.\n"
                )

            print("\nAction completed. Returning to Main Menu.")

            return_main_menu_after_pause()

        # delete courier
        elif input_courier_opt == 4:
            couriers_index_list()

            input_delete_courier_index = input(
                "Enter the number of the courier you would like to delete:\n"
            )

            couriers.pop(input_delete_courier_index)

            return_main_menu_after_pause()

    # orders menu
    elif input_main_menu == 3:
        order_menu_opt()

        input_orders_opt = util.validate_int_input()

        # return to main menu
        if input_orders_opt == 0:
            continue

        # print orders menu
        elif input_orders_opt == 1:
            orders_index_list()

            return_main_menu_after_pause()

        # create new order
        elif input_orders_opt == 2:
            # get new customer name and validate input
            input_new_customer_name = input("Enter customer name:\n")
            input_new_customer_name = util.validate_str_input(input_new_customer_name)

            # get customer address and validate input
            input_new_customer_address = input("Enter customer address:\n")
            input_new_customer_address = util.validate_address_input(
                input_new_customer_address
            )

            # get customer phone and validate input
            input_new_customer_phone = input("Enter customer phone:\n")
            input_new_customer_phone = util.validate_phone_num(input_new_customer_phone)

            # print product list with index
            products_index_list()

            # get a validated string input for ordered items index values
            input_new_customer_items = util.validate_int_input_order_items(products)

            # print courier list with index
            couriers_index_list()

            # get customer courier choice and validate input
            input_new_customer_courier = util.validate_int_input()

            order_status = "Preparing"

            order = {
                "customer_name": input_new_customer_name,
                "customer_address": input_new_customer_address,
                "customer_phone": input_new_customer_phone,
                "courier": input_new_customer_courier,
                "status": order_status,
                "items": input_new_customer_items,
            }

            orders.append(order)

            print("New Order has  been successfully created!\n")
            for order_key, order_value in order.items():
                print(f"{order_key}: {order_value}")

            return_main_menu_after_pause()

        # update order status
        elif input_orders_opt == 3:
            orders_index_list()

            input_update_status_index = util.validate_int_input()

            chosen_update_order = orders[input_update_status_index]

            order_status_list_index()

            input_update_status_index = util.validate_int_input()

            chosen_update_order.update({"status": input_update_status_index})
            print(f"Order Status has been successfully updated!\n{chosen_update_order}")

            return_main_menu_after_pause()

        # update order property
        elif input_orders_opt == 4:
            orders_index_list()

            print("Which order would you like to update?\n")
            input_update_order_property_index = util.validate_int_input()

            chosen_update_order_property = orders[input_update_order_property_index]

            # get customer name and validate input
            input_update_customer_name = input("Enter updated customer name:\n")
            input_update_customer_name = util.validate_str_input(
                input_update_customer_name
            )

            # get updated customer address and validate input
            input_update_customer_address = input("Enter updated customer address:\n")
            input_update_customer_address = util.validate_address_input(
                input_update_customer_address
            )

            input_update_customer_phone = input(
                "Enter updated customer phone number:\n"
            )

            couriers_index_list()
            print("Enter updated courier choice:\n")
            input_update_customer_courier = input()

            products_index_list()

            # get a validated string user input for ordered product index values
            input_update_customer_items = input()

            # customer name update with feedback if no change
            if input_update_customer_name == "":
                print("No change has been made to customer name.")
            else:
                chosen_update_order_property.update(
                    {"customer_name": input_update_customer_name}
                )
                get_customer_name = chosen_update_order_property.get("customer_name")
                print(f"Customer name has been updated to {get_customer_name}")

            # customer address update with feedback if no change
            if input_update_customer_address == "":
                print("No change has been made to customer address.")
            else:
                chosen_update_order_property.update(
                    {"customer_address": input_update_customer_address}
                )
                get_customer_address = chosen_update_order_property.get(
                    "customer_address"
                )
                print(f"Customer address has been updated to {get_customer_address}")

            if input_update_customer_phone == "":
                print("No change has been made to customer phone number.")
            else:
                input_update_customer_phone = util.validate_phone_num(
                    input_update_customer_phone
                )

                chosen_update_order_property.update(
                    {"customer_phone": input_update_customer_phone}
                )
                get_customer_phone = chosen_update_order_property.get("customer_phone")
                print(
                    f"Customer phone number has been updated to {get_customer_phone}."
                )

            if input_update_customer_courier == "":
                print("No change has been made to courier choice.")
            else:
                input_update_customer_courier = util.validate_int_input()
                chosen_update_order_property.update(
                    {"courier": input_update_customer_courier}
                )
                get_customer_courier = chosen_update_order_property.get(
                    "customer_phone"
                )
                print(f"Courier choice has been updated to {get_customer_courier}")

            if input_update_customer_items == "":
                print("No change has been made to ordered items.")
            else:
                input_update_customer_items = util.validate_int_input_order_items(
                    products
                )
                chosen_update_order_property.update(
                    {"items": input_update_customer_items}
                )
                print(
                    "Notice: If enteries were left blank, no updates have been conducted.\n"
                )
                print(f"Here is the updated order:\n{chosen_update_order_property}")

                return_main_menu_after_pause()

        elif input_orders_opt == 5:
            orders_index_list()

            input_delete_order_index = util.validate_int_input()

            orders.pop(input_delete_order_index)

            print("Order has been succeffuly deleted.")

            return_main_menu_after_pause()

    else:
        print("Invalid input. Please enter a valid number.")
        input_main_menu = util.validate_int_input()
