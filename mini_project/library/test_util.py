import util

#test add new product will create a new product object

def test_add_new_product_will_create_new_product_from_valid_data():

    #arrange

    expected_product = {
        "name": 'Hot chocolate',
        "price": 2.50,
    }

    #act

    actual_product = util.add_new_product("Hot chocolate", 2.50, [])

    #assert 

    assert actual_product == expected_product, f'Expected product is {expected_product} but was {actual_product}.'

#test add new product will create a new product object

def test_add_new_product_will_create_new_product_object():

    #arrange

    products_list = []

    expected_product = {
        "name": 'Hot chocolate',
        "price": 2.50,
    }

    #act

    util.add_new_product("Hot chocolate", 2.50, products_list)

    #assert

    assert len(products_list) == 1, f'Expected 1 but got {len(products_list)}'

    assert products_list[0] == expected_product, f'Expected {expected_product} but got {products_list[0]}'

#test add new order will create a new order object

def test_add_new_order_will_create_new_order_from_valid_data():
    
    #arrange

    expected_order = {
        "customer_name": "John Jones",
        "customer_address": "Main Street,LONDON",
        "customer_phone": "07987654321",
        "courier": 1,
        "status": "Preparing",
        "items": "1,4",
    }


    #act

    actual_order = util.add_new_order("John Jones", "Main Street,LONDON", "07987654321", 1, "1,4", [])

    #assert

    assert actual_order == expected_order, f'Expected {expected_order} but was {actual_order}.'

#will add new order to the list

def test_add_new_order_will_add_new_object_to_the_list():
    
    #arrange

    orders_list = []

    expected_order = {
        "customer_name": "John Jones",
        "customer_address": "Main Street,LONDON",
        "customer_phone": "07987654321",
        "courier": 1,
        "status": "Preparing",
        "items": "1,4",
    }

    #act

    util.add_new_order("John Jones", "Main Street,LONDON", "07987654321", 1, "1,4", orders_list)

    #assert

    assert len(orders_list) == 1, f'Expected 1 but got {len(orders_list)}'

    assert orders_list[0] == expected_order, f'Expected {expected_order} but was {orders_list[0]}'
