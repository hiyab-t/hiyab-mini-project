import csv
from pathlib import Path


# absolute path
product_file_path = (Path(__file__).parent / "../week_4/data/product.csv").resolve()
courier_file_path = (Path(__file__).parent / "../week_4/data/courier.csv").resolve()
order_file_path = (Path(__file__).parent / "../week_4/data/orders.csv").resolve()


# read products from product.csv
def read_products_file():
    try:
        with open(str(product_file_path), mode="r") as products_file:
            products_content = csv.DictReader(products_file)

            for products_row in products_content:
                print(products_row, end="\n")
    except FileNotFoundError as whoops:
        print(f"{whoops}. Failed to open file.")


# read couriers from couriers.csv
def read_couriers_file():
    try:
        with open(str(courier_file_path), mode="r") as couriers_file:
            couriers_content = csv.DictReader(couriers_file)

            print("\n__________________________\n")
            print("\nCourier List\n")
            for index, couriers_row in enumerate(couriers_content):
                print(
                    index,
                    "-",
                    couriers_row["name"],
                    "-",
                    couriers_row["phone"],
                    end="\n",
                )

    except FileNotFoundError as whoops:
        print(f"{whoops}. Failed to open file.")


# read orders from orders.csv
def read_orders_file():
    try:
        with open(str(order_file_path), mode="r") as orders_file:
            orders_content = csv.DictReader(orders_file)

            print("\n__________________________\n")
            print("\nOrders List\n")
            for orders_row in orders_content:
                print(orders_row, end="\n")

    except FileNotFoundError as whoops:
        print(f"{whoops}. Failed to open file.")


def save_products(products):
    try:
        with open(str(product_file_path), mode="w", newline="") as products_file:
            products_keys = ["name", "price"]
            updated_products = csv.DictWriter(products_file, fieldnames=products_keys)
            updated_products.writeheader()
            for product_write in products:
                updated_products.writerow(product_write)
    except FileNotFoundError as fail:
        print(f"{fail}. Failed to open file.")


def save_couriers(couriers):
    try:
        with open(str(courier_file_path), mode="w", newline="") as couriers_file:
            couriers_keys = ["name", "phone"]
            updated_couriers = csv.DictWriter(
                couriers_file, fieldnames=couriers_keys, delimiter=","
            )

            updated_couriers.writeheader()
            for courier_write in couriers:
                updated_couriers.writerow(courier_write)
    except FileNotFoundError as fail:
        print(f"{fail}. Failed to open file.")


def save_orders(orders):
    try:
        with open(str(order_file_path), newline="", mode="w") as orders_file:
            orders_keys = [
                "customer_name",
                "customer_address",
                "customer_phone",
                "courier",
                "status",
                "items",
            ]
            updated_orders = csv.DictWriter(
                orders_file, fieldnames=orders_keys, delimiter=","
            )
            updated_orders.writeheader()
            for order_write in orders:
                updated_orders.writerow(order_write)
    except FileNotFoundError as fail:
        print(f"{fail}. Failed to open file.")
