import re

def add_new_product(new_product_name, new_product_price, products_list):
    product = {
                "name": new_product_name,
                "price": new_product_price,
            }
    products_list.append(product)
    
    return product

def add_new_order(new_customer_name, new_customer_address, new_customer_phone, new_customer_courier, new_customer_items, orders_list):
    order_status = "Preparing"

    order = {
        "customer_name": new_customer_name,
        "customer_address": new_customer_address,
        "customer_phone": new_customer_phone,
        "courier": new_customer_courier,
        "status": order_status,
        "items": new_customer_items,
    }
    
    orders_list.append(order)
    
    return order


def validate_int_input():
    while True:
        try:
            value = int(input())
            if value < 0:
                raise ValueError("Negative numbers are not allowed")
        except ValueError as v_oops:
            print(f"{v_oops}. Please enter a valid number.")
        except IndexError as i_oops:
            print(f"{i_oops}. Please enter a valid number.")
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
            print(f"{v_oops}. Please enter a valid number.")
        except OverflowError as o_oops:
            print(f"{o_oops}. Please enter a valid number.")
        else:
            return value


def validate_str_input(input_str):
    input_str = input_str.strip()
    while True:
        if re.fullmatch(r"[a-zA-Z\s'-]+", input_str):
            return input_str.title()
        else:
            print(
                "Special characters or numbers are not allowed. Please enter a valid input."
            )
            input_str = input()


def validate_address_input(input_address):
    while True:
        if re.fullmatch(r"[a-zA-Z0-9,\s'-]+", input_address):
            return input_address.title().strip()
        else:
            print("Special characters are not allowed. Please enter a valid input.")
            input_address = input()


def validate_phone_num(input_phone):
    while True:
        input_phone = re.sub(r"\s+", "", input_phone)
        if input_phone.isdigit() and (len(input_phone) == 11 or len(input_phone) == 10):
            return input_phone
        else:
            print("Invalid phone number. Please try again.")
            input_phone = input()


def validate_int_input_order_items(products):
    while True:
        try:
            list_order_items = [
                int(product)
                for product in input().split(",")
                ]
            
            access_order_items_list = [
                products[product_item_index]
                for product_item_index in (list_order_items)
            ]
            
            print(f"Ordered list of items: {list_order_items}\n")
            
            for product_item in access_order_items_list:
                print(f"{product_item['name']}\nPrice: {product_item['price']}\n")
            break
        except ValueError as v_oops:
            print(f"{v_oops}. Please enter a valid number or numbers.")
        except IndexError as i_oops:
            print(f"{i_oops}. Please enter a valid number or numbers.")
        except Exception as err:
            print(
                f"Unexpected {err=}, {type(err)=}. Please enter a valid number or numbers."
            )

    value = ",".join(str(index_item) for index_item in list_order_items)
    return value
