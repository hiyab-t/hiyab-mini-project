from week_2.source import app2


products = ["Falafel burgers", "Reuben sandwich", 'Chopped salad', "Pasta House salad", 
                "Special spicy chicken & avocado wraps", "Hot chocolate", "Mocha", "coffee",
                "Americano", "Flat white", "Cappuccino"]

#order list
orders_list = [{
        "customer_name": "John Jones",
        "customer_address": "Main Street, LONDON",
        "customer_phone": "07987654321",
        "status": "Preparing"
        },
        {
        "customer_name": "Hiyab Tewelde",
        "customer_address": "Antrim road, Belfast",
        "customer_phone": "07404313229",
        "status": "Delivered"
        }]

couriers = ['Uber', 'Deliveroo']


def products_menu_opt():
        print("__________________________\n")
        print("Product Menu\n")
        print("__________________________\n")
        print("0 - Return to Main Menu\n" \
        "1 - Print Products List.\n" \
        "2 - Create New Product.\n" \
        "3 - Update Existing Product.\n" \
        "4 - Delete Product.\n")
        print("__________________________\n")

def couriers_menu_opt():
        print("__________________________\n")
        print("Couriers Menu\n"
                "0 - Return to Main Menu\n"
                "1 - Couriers List\n"
                "2 - Create New Courier\n"
                "3 - Update Existing Courier\n"
                "4 - Delete Courier")
        print("__________________________\n")

def orders_menu_opt():
        print("__________________________\n")
        print("Orders menu\n" \
                "0 - Return to main menu.\n" \
                "1 - Orders list.\n" \
                "2 - Create New Order.\n" \
                "3 - Update Existing Order Status.\n" \
                "4 - Update Existing Order.\n" \
                "5 - Delete Order.\n")
        print('__________________________\n')

#functions to list couriers with index

def couriers_index_list():
        print('Courier list')
        for index_courier, courier in enumerate(couriers):
                print(f'{index_courier} - {courier}')

#function to prevent this module from running in where it is imported
def main():
        pass

if __name__ == "__main__":

        #print welcome message

        print("Welcome to Maria's cafe! \n")

        #loading products list from products.txt

        try:
                with open("week_3/data/products.txt", 'r') as products_file:
                        products_content = products_file.read()
        
                for line_products in products_content:
                        print(line_products, end='')      
        except FileNotFoundError:
                print('Failed to open file.')
        
        #loading couriers list from couriers.txt
        
        try:
                with open('week_3/data/couriers.txt', 'r') as couriers_file:
                        couriers_content = couriers_file.read()
                
                for line_couriers in couriers_content:
                        print(line_couriers, end='')
        except FileNotFoundError:
                print('Failed to open file.')

        #imported function from app2 to print main menu options

        app2.main_menu_opt()

        #main menu 

        while True:
                main_menu_input = input()
                if main_menu_input == '0':
        
                        #save products list to products.txt
                        try:
                                with open('week_3/data/products.txt', 'w') as write_products_file:
                                        for updated_line_products in products:
                                                write_products_file.write(updated_line_products + '\n')
                        except FileNotFoundError as welp:
                                print('Failed to open file.')
                
                        #save couriers list to couriers.txt
                        try:
                                with open('week_3/data/couriers.txt', 'w') as write_couriers_file:
                                        for updated_line_couriers in couriers:
                                                write_couriers_file.write(updated_line_couriers + '\n')
                        except FileNotFoundError as welp_2:
                                print('Failed to open file.')
                
                        exit("Exitting the app. Don't be a stanger!")
        
                elif main_menu_input == '1':
                        
                        products_menu_opt()
                        input_product_opt = input()
        
                        #product menu
                        if input_product_opt == '0':
                                continue
        
                        elif input_product_opt == '1':
                                app2.products_index_list()
                
                        elif input_product_opt == '2':
                                print(products.append(input("What would you like to add?\n")))
        
                        elif input_product_opt == '3':
                                app2.products_index_list()
                                user_input_index = input("Enter the number of the product you would like to update:\n")
                                user_input_product_name = input("What product would you like to add instead?\n")
                                products[int(user_input_index)] = user_input_product_name.title()
        
                        elif input_product_opt == '4':
                                print(app2.products_index_list())
                                user_input_index_pop = input("Please enter the number of the product you want to delete:\n")
                                products.pop(int(user_input_index_pop))
                
                #couriers menu
                elif main_menu_input == '2':
                        
                        couriers_menu_opt()
                        
                        input_courier = input()
        
                        if input_courier == '0':
                                continue
        
                        elif input_courier == '1':
                                couriers_index_list()
        
                        elif input_courier == '2':
        
                                couriers.append(input('What courier would you like to add?\n'))
                                print(f'New Courier successfully created!\n {couriers}')
        
                        elif input_courier == '3':
        
                                couriers_index_list()
                                input_index_courier_update = input('Enter the number of the courier you would like to update:\n')
                                input_updated_courier = input('What courier would you like to add instead?\n')
        
                                couriers[int(input_index_courier_update)] = input_updated_courier.title()
        
                        elif input_courier == '4':
        
                                couriers_index_list()
                                input_delete_courier = input("Please enter the number of the product you would like to delete:\n")
        
                                couriers.pop(int(input_delete_courier))
                                print(f'Courier has been successfuly deleted!\n {couriers_index_list}')
        
                elif main_menu_input == '3':
        
                        orders_menu_opt()

                        input_orders_menu = input()
                        
                        if input_orders_menu == '0':
                                continue
        
                        elif input_orders_menu == '1':
                                
                                app2.orders_index_list()
        
                        #get user input to update existing order
                        elif input_orders_menu == '2':
                                user_input_name = input("Enter customer full name: ")
                                user_input_address = input("Enter customer address: ")
                                user_input_phone_num = input("Enter customer phone number: ")
                                while True:
                                        print('Please ensure to enter a valid phone number and no blank spaces.')
                                        user_input_phone_num = input('Enter customer phone number:\n')
                                        if user_input_phone_num.isdigit() and len(user_input_phone_num) == 11 or len(user_input_phone_num) == 10:
                                                break
                                order_status = 'PREPARING'
                                order = {
                                'customer_name': user_input_name,
                                'customer_address': user_input_address,
                                'customer_phone number': user_input_phone_num,
                                'status': order_status
                                }
                                orders_list.append(order)
                                print(order)
        
                        #printed order status list with index
                        elif input_orders_menu == '3':
                                app2.orders_index_list()
                
                                input_order_status_num = input("Which order's status would you like to update?\n") 
        
                                chosen_order = orders_list[int(input_order_status_num)]
        
                                print('Order status list')
                                for index_status, orders_to_list in enumerate(app2.order_status_list):
                                        print(f'{index_status}: {orders_to_list}')
                                input_status_index = input('What would you like to update the order status to?\n')
        
                                chosen_order.update({'status': app2.order_status_list[int(input_status_index)]})
                                print(f'Order status update successful!\n{chosen_order}')
                
                                try:
                                        input_order_status_num = input()
                                except IndexError: 
                                        print('Invalid input. Please enter a valid number.')
                                else:
                                        print(f'{input_order_status_num} accepted.')
                                
                        #get user input to update order
                        elif input_orders_menu == '4':
                                app2.orders_index_list()
        
                                input_order_num = input("Which order would you like to update?\n")
        
                                chosen_order_property_update = orders_list[int(input_order_num)]
        
                                input_update_name = input("Enter updated customer name:\n")
                                input_update_address = input('Enter updated customer address:\n')
                                input_update_phone = input('Enter updated customer phone number:\n')
                                input_update_phone.replace(' ', '')
                
                                #utilized while loop to handle empty input and other requirements for customer number
                                while True:
                                        if input_update_phone == '' or input_update_phone.isdigit() and len(input_update_phone) == 11 or len(input_update_phone) == 10:
                                                break
                                        else:
                                                print('Please ensure to enter a valid phone number.')
                                                input_update_phone = input('Enter updated customer phone number:\n')
        
                                if input_update_name or input_update_address or input_update_phone == '':
                                        print(f'No update was conducted. Order information will remain the same.\n {chosen_order_property_update}')
                                        continue
                                else:
                                        chosen_order_property_update.update({'customer_name': input_update_name, 
                                                                        'customer_address': input_update_address,
                                                                        'customer_phone': input_update_phone})
                                print(f'Order properties update successful!\n {chosen_order_property_update}')
                        elif input_orders_menu == '5':
                                app2.orders_index_list()
                
                                input_delete_order_index = input('Which order would you like to delete?\n')
                
                                orders_list.pop(int(input_delete_order_index))
                                print(f'Order has been successfuly deleted. Remaining orders:\n {app2.orders_index_list()}')
                else:
                        print("Invalid input. Please enter a valid number.\n")
        
        
        
                
        
        


