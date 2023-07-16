__winc_id__ = "d7b474e9b3a54d23bca54879a4f1855b"
__human_name__ = "Betsy Webshop"

from models import Product, Tag, ProductTag, WebshopTransaction
import os
from setupdb import populate_database
from peewee import fn
from spellchecker import SpellChecker


def main():
    # search("sweter")
    # list_products_per_tag(2)
    add_product_to_catalog(3, "badmintonset")
    # remove_product(10)
    # update_stock(11, 200)
    # purchase_product(2, 3, 2)


def check_file():
    check_file = os.path.isfile("betsy_webshop.db")
    if check_file:
        pass
    else:
        populate_database()


def search(term):
    check_file()
    # om spelling van zoekterm te checken en alternatieven te zoeken wordt
    # SpellChecker gebruikt. Met candidates wordt lijst samengesteld
    # van mogelijk bedoelde zoektermen
    spell = SpellChecker()
    likely_options = spell.candidates(term)
    if not likely_options:
        # als er teveel spelfouten inzitten kan geen alternatief
        # worden gevonden en is de lijst leeg.
        print("item not found")
    else:
        # anders wordt voor ieder woord in de lijst met alternatieven
        # gezocht of deze in productnaam of -beshrijving voorkomen
        for word in likely_options:
            word_query = Product.select().where(
                fn.Lower(Product.name.contains(word))
                | (Product.description.contains(word))
            )
            for product in word_query:
                print(
                    product.name,
                    product.description,
                    product.price_per_unit,
                    product.stock,
                    product.owner,
                )


def list_user_products(user_id):
    check_file()
    for product in Product.select().where(Product.owner == user_id):
        print(
            product.name,
            product.description,
            product.price_per_unit,
            product.stock,
            product.owner,
        )
    exit()


def list_products_per_tag(tag_id):
    check_file()
    for product in (
        Product.select().join(ProductTag).where(ProductTag.tag == tag_id)
    ):
        print(
            product.name,
            product.description,
            product.price_per_unit,
            product.stock,
            product.owner,
        )
    exit()


def add_product_to_catalog(user_id, product):
    check_file()
    product = str.capitalize(product)
    print("Enter description:")
    d = input()
    print("Enter product price per unit:")
    p = input()
    print("Enter quantity:")
    q = int(input())
    prod_add = Product.create(
        name=product, description=d, price_per_unit=p, stock=q, owner=user_id
    )
    prod_id = prod_add.id

    def add_tag(prod_id):
        print("Enter Tag:")
        t = str.capitalize(input())
        check = Tag.get_or_none(name=t)
        if check is None:
            tag = Tag.create(name=t)
            tagid = tag.id
            ProductTag.create(product_id=prod_id, tag_id=tagid)
            user_input = input("add another tag? y for yes, n for no:")
            if user_input == "y":
                add_tag(prod_id)
            else:
                exit()
        else:
            tag = Tag.select().where(Tag.name == t)
            tagid = tag.get()
            ProductTag.create(product_id=prod_id, tag_id=tagid)
            user_input = input("add another tag? y for yes, n for no:")
            if user_input == "y":
                add_tag(prod_id)
            else:
                exit()

    add_tag(prod_id)


def update_stock(product_id, new_quantity):
    check_file()
    query = Product.update(stock=new_quantity).where(Product.id == product_id)
    query.execute()
    for product in Product.select().where(Product.id == product_id):
        if product.stock == 0:
            remove_product(product_id)
        else:
            print(str(product.stock) + " item(s) left")


def purchase_product(product_id, buyer_id, quantity):
    check_file()
    for product in Product.select().where(Product.id == product_id):
        if product.owner_id == buyer_id:
            print("not possible to buy your own products")
            exit()
        if product.stock < quantity:
            print("not enough items in stock")
        if product.stock >= quantity:
            new_quantity = (product.stock) - quantity
            query = WebshopTransaction.select().where(
                (WebshopTransaction.product == product_id)
                & (WebshopTransaction.buyer == buyer_id)
            )
            if query.exists():
                row = WebshopTransaction.get(
                    (WebshopTransaction.product == product_id)
                    & (WebshopTransaction.buyer == buyer_id)
                )
                row.quantity = row.quantity + quantity
                row.save()
            else:
                WebshopTransaction.create(
                    buyer=buyer_id, product=product_id, quantity=quantity
                )
            update_stock(product_id, new_quantity)


def remove_product(product_id):
    check_file()
    obj = Product.get(Product.id == product_id)
    obj.delete_instance()


if __name__ == "__main__":
    main()
