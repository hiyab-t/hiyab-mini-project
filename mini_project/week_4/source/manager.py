class ProductsManager:
    def __init__(self, name_product, price_product):
        self.name_product = name_product
        self.price_product = price_product

    def products_display(self):
        print("__________________________\n")
        print("Here's products List:\n")
        for products_index, self.name_product in enumerate(products):
            print(f'{products_index} - {product}')
        print("__________________________\n")
    
    def create_product()

def get_int_input(prompt, **kwargs):
    while True:
        if int(input(prompt)) < 0:
            print('no negative. revise')
        else:
            try: 
                int(input(prompt))
                break
            except ValueError as whoops:
                print(f'{whoops}. Please enter a valid number.')
            except IndexError as oops:
                print(f'{oops}. Please enter a valid number.')
        

            

input_something = get_int_input('what number?\n')
    
