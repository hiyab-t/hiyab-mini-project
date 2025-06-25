#from week_2.source import app




#try:
with open("../data/products.txt", 'r') as products_file:
        products = products_file.read()
        print('file contents=', products)
#except:
 #   print('Failed to open file.')