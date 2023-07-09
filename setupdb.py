from models import (db,User,Product,Tag, ProductTag,Webshop_Transaction)
import os

# def delete_database():
    # cwd = os.getcwd()
    # database_path = os.path.join(cwd, "betsy_webshop.db")
    # if os.path.exists(database_path):
    #     os.remove(database_path)

def populate_database():

    db.connect()

    db.create_tables([User,Product,Tag, ProductTag,Webshop_Transaction])

    User.create(name = 'Pietje Bell', adress='Stationstraat 1',postcode = '7481AA', town='Enschede', billing_info= 'SNS123456')
    User.create(name = 'Anna Jansen', adress='Dorpsplein 5',postcode = '3322HF', town='Groningen', billing_info= 'RABO123456')
    User.create(name = 'Jort Dijkstra', adress='Lelylaan 25',postcode = '4255ZX', town='Eindhoven', billing_info= 'ING123456')

    Product.create(name ="Sweater",description= 'Brown sweater with text Holiday',price_per_unit=24.95,stock=10,owner=1)
    Product.create(name ="Trousers",description= 'Blue trousers, size M',price_per_unit= 20,stock=10,owner=1)
    Product.create(name ="Socks",description= 'Blue socks, size 39-42',price_per_unit= 5,stock=10,owner=1)
    Product.create(name ="Sweater",description= 'Blue sweater,plain',price_per_unit=29.95,stock=5,owner=2)
    Product.create(name ="Jeans",description= 'Dark bleu jeans, size 30/32',price_per_unit= 35.95,stock=1,owner=2)
    Product.create(name ="Socks",description= 'Blue socks, size 39-42',price_per_unit= 7.50,stock=10,owner=2)
    Product.create(name ="Hand mixer",description= 'Hand mixer, Philips',price_per_unit= 37.95,stock=10,owner=2)
    Product.create(name ="Washing machine",description= 'Washing machine AEG',price_per_unit= 100,stock=2,owner=3)
    Product.create(name ="Suitcase",description= 'Suitcase, blue, 80x40x20cm',price_per_unit= 25,stock=2,owner=3)
    Product.create(name ="Suitcase",description= 'Suitcase, red, 80x40x20cm',price_per_unit= 25,stock=10,owner=3)
    Product.create(name ="Tennisracket",description= 'Tennisracket, adults, Dunlop',price_per_unit= 30,stock=2,owner=3)
    Product.create(name ="Tennisracket",description= 'Tennisracket, junior, Dunlop',price_per_unit= 25,stock=5,owner=1)
    Product.create(name ="Tennisshort",description= 'Tennisshort, white, size M',price_per_unit= 19.95,stock=10,owner=2)
    Product.create(name ="Sportsbag",description= 'Sportsbag, black, medium',price_per_unit= 21.95,stock=20,owner=3)
    Product.create(name ="Sportsbag",description= 'Sportsbag, black, large',price_per_unit= 31.95,stock=10,owner=3)

    Tag.create(name = 'Clothing')
    Tag.create(name = 'Travel')
    Tag.create(name = 'Appliance')
    Tag.create(name = 'Sports')

    ProductTag.create(product = 1, tag=1)
    ProductTag.create(product = 2, tag=1)
    ProductTag.create(product = 3, tag=1)
    ProductTag.create(product = 4, tag=1)
    ProductTag.create(product = 5, tag=1)
    ProductTag.create(product = 6, tag=1)        
    ProductTag.create(product = 7, tag=3)
    ProductTag.create(product = 8, tag=3)
    ProductTag.create(product = 9, tag=2)
    ProductTag.create(product = 10, tag=2)
    ProductTag.create(product = 11, tag=4)
    ProductTag.create(product = 12, tag=4)
    ProductTag.create(product = 13, tag=1)
    ProductTag.create(product = 13, tag=4)    
    ProductTag.create(product = 14, tag=2)
    ProductTag.create(product = 14, tag=4)   
    ProductTag.create(product = 15, tag=2)
    ProductTag.create(product = 15, tag=4)

    db.close()    