from week_2.source import app2
from week_3.source import app3
import csv

products = [{
        'name': 'Falafel burgers',
        'price': 3.65
        },
        {
        'name': 'Reuben sandwich',
        'price': 4
        }]

courier = [
    {
        'name':'Uber Eats',
        'phone':'0789887889'
    },
    {
        'name':'Deliveroo',
        'phone':'0784897810'
    }
]

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

#persisting

#try:
with open('week_4/data/products.csv', mode='r') as products_file:
        products_content = csv.DictReader(products_file)

        for row in products_file:
            print(row)
#except FileNotFoundError as whoops:
#    print('Failed to open file.')

