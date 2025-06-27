from week_2.source import app




#try:
with open("../data/products.txt", 'r') as products_file:
        products_list = products_file.read()
        print('file contents=', products)
#except:
#    print('Failed to open file.')

with open('../data/couriers.txt') as couriers_file:
        couriers_list = couriers_file.read()
        print

