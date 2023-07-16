# Models go here
from peewee import *


db = SqliteDatabase("betsy_webshop.db")


class BaseModel(Model):
    class Meta:
        database = db


class User(BaseModel):
    name = CharField()
    adress = CharField()
    postcode = CharField()
    town = CharField()
    billing_info = CharField()


class Product(BaseModel):
    name = CharField(index=True)
    description = CharField()
    price_per_unit = DecimalField(decimal_places=2, auto_round=True)
    stock = IntegerField()
    owner = ForeignKeyField(User, backref="productlist")


class Tag(BaseModel):
    name = CharField(unique=True)


class ProductTag(BaseModel):
    product = ForeignKeyField(Product, backref="producttags")
    tag = ForeignKeyField(Tag, backref="producttags")


class WebshopTransaction(BaseModel):
    buyer = ForeignKeyField(User)
    product = ForeignKeyField(Product)
    quantity = IntegerField()
