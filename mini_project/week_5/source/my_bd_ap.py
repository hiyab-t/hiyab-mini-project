import os
import psycopg2 as psycopg
from dotenv import load_dotenv

load_dotenv(
)
host_name = os.environ.get("POSTGRES_HOST")
database_name = os.environ.get("POSTGRES-DB")
user_name = os.environ.get("POSTGRES_USER")
user_password = os.environ.get("POSTGRES_PASSWORD")

def retrieve_products():    
    try:

        with psycopg.connect(f'''host
                host={host_name}'
                dbname={database_name}
                user={user_name}
                password={user_password}''') as connection:

            cursor = connection.cursor()

            cursor.execute('SELECT name, prcie FROM products ORDER BY id ASC')
            
            rows = cursor.fetchall()
            
            print('Products list')

            for row in rows:
                print(f'Name: {row[0]}, Price: {row[1]}')

                cursor.close()

    except Exception as ex:
        print('Failed to:', ex)

retrieve_products()

def insert_product(input_new_product_name, input_new_product_price):
    try:
        with psycopg.connect(f'''host
                    host={host_name}'
                    dbname={database_name}
                    user={user_name}
                    password={user_password}''') as connection:
                
                cursor = connection.cursor()

                sql = """
                    INSERT INTO product (name, price)
                    VALUES (%s, %s)
                    RETURNING product_id, name, price
                """

                data_values = (input_new_product_name, input_new_product_price)

                cursor.execute(sql, data_values)
                rows = cursor.fetchall()
                
                print(f'id:{rows[0]}, Name: {rows[1]}, Price: {rows[2]}')

                connection.commit()

                cursor.close()
        
    except Exception as ex:
        print('Failed to:', ex)

#def update_product():
#    try:
#        with psycopg.connect(f'''host
#                    host={host_name}'
#                    dbname={database_name}
#                    user={user_name}
#                    password={user_password}''') as connection:
#                
#                cursor = connection.cursor()
#
#                sql = """
#                    
#                """
