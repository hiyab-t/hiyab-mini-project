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


def products_index_list(products):
    print("__________________________\n")
    print("Products List:\n")
    for products_index, product in enumerate(products):
        print(f'{products_index} - {product["name"]}\nPrice - {product["price"]}\n')
    print("__________________________\n")


def couriers_index_list(couriers):
    print("__________________________\n")
    print("Couriers List:\n")
    for couriers_index, courier in enumerate(couriers):
        print(f"{couriers_index} - {courier['name']}\n{courier['phone']}\n")
    print("__________________________\n")


def orders_index_list(orders):
    print("__________________________\n")
    print("Orders List")
    for index_order, order in enumerate(orders):
        print(
            f"{index_order} - \nCustomer name: {order['customer_name']}\nCustomer address: {order['customer_address']}\nCustomer phone: {order['customer_phone']}\nCourier: {order['courier']}\nStatus: {order['status']}\nItems: {order['items']}\n"
        )
    print("__________________________\n")


def order_status_list_index(order_status):
    print("__________________________\n")
    print("Order Status List\n")
    for index_order_status, order in enumerate(order_status):
        print(f"{index_order_status} - {order}\n")
    print("__________________________\n")