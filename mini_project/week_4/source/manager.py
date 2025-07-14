products = []


class ProductsManager:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def products_display(self):
        print("__________________________\n")
        print("Products List:\n")
        for products_index, product in enumerate(products):
            print(
                f"{products_index} - {product[{self.name}]}    \n{product[{self.price}]}"
            )
        print(f" I like {self.name}, price is {self.price}")
        print("__________________________\n")


product = ProductsManager("Hot chocolate", 2)


product.products_display()


def products_index_list():
    print("__________________________\n")
    print("Here's products List:\n")
    for products_index, product in enumerate(products):
        print(f"{products_index} - {product}")
    print("__________________________\n")


def get_int_input(prompt_int, **kwargs):
    while True:
        if int(input(prompt_int)) < 0:
            print("Negative numbers are not allowed. Please enter a valid number.")
        else:
            try:
                int(input(prompt_int))
                break
            except ValueError as whoops:
                print(f"{whoops}. Please enter a valid number.")
            except IndexError as oops:
                print(f"{oops}. Please enter a valid number.")


def get_float_input(prompt_float, **kwargs):
    while True:
        if float(input(prompt_float)) < 0:
            print("No negative numbers. Please enter a valid number.")
        elif "e" in float(input(prompt_float)):
            print("No scitentific notations please.")
