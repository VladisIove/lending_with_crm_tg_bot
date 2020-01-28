import datetime
import base64
import time
import re
import uuid
import aiofiles

from sqlalchemy import (MetaData, Table, 
                        Column, ForeignKey, 
                        Integer, Boolean, 
                        String, Float,
                        DateTime, ARRAY, JSON)

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import relationship, backref

try:
    from settings import MEDIA_PATH, MEDIA_URL
except:
    from .settings import MEDIA_PATH, MEDIA_URL

Base = declarative_base()
meta = MetaData()


clothes_views_size = Table('clothes_views_size', Base.metadata,
    Column('clothesview_id', Integer, ForeignKey('clothes_views.id', ondelete='CASCADE')),
    Column('sizeclothes_id', Integer, ForeignKey('sizes_clothes.id', ondelete='CASCADE')),
)


orders_chooce_clothes = Table('orders_chooce_clothes', Base.metadata,
    Column('chooceclothes_id', Integer, ForeignKey('chooces_clothes.id', ondelete='CASCADE')),
    Column('order_id', Integer, ForeignKey('orders.id', ondelete='CASCADE')),
)

class SizeClothes(Base):
    __tablename__='sizes_clothes'

    id = Column(Integer, primary_key=True)
    name_size = Column( String(200), nullable=False)

    def __str__(self):
        return '{}'.format(self.name_size)


clothes_views_color = Table('clothes_views_color', Base.metadata,
    Column('clothesview_id', Integer, ForeignKey('clothes_views.id', ondelete='CASCADE')),
    Column('colorclothes_id', Integer, ForeignKey('colors_clothes.id', ondelete='CASCADE')),
)

class ColorClothes(Base):
    __tablename__='colors_clothes'
    id = Column(Integer, primary_key=True)
    name_color = Column( String(200), nullable=False)

    def __str__(self):
        return '{}'.format(self.name_color)

class ClothesView(Base):
    __tablename__='clothes_views'

    id = Column(Integer, primary_key=True)
    name = Column( String(200), nullable=False)
    description = Column( String(500), nullable=False)
    type_clothes = Column(Integer, nullable=False)
    enabled = Column(Boolean, default=True)
    old_price = Column(Float, nullable=False)
    price = Column(Float, nullable=False)
    count = Column(Integer, nullable=False)
    img = Column(String(500), nullable=False)
    size = relationship('SizeClothes', secondary=clothes_views_size)
    color = relationship('ColorClothes', secondary=clothes_views_color)
    type_clothes = Column(Integer, nullable=False)

    def __str__(self):
        return 'ID: {}, name: {}, color: {}'.format(self.id, self.name, [x for x in self.color])

class ChooceClothes(Base):
    __tablename__='chooces_clothes'
  
    id = Column(Integer, primary_key=True)
    datetime = Column(DateTime, default=datetime.datetime.utcnow)
    clothes_id = Column(Integer, nullable=False)
    price = Column(Float, nullable=False)

    def __str__(self):
        return 'ID: {}, price: {}'.format(self.id, self.price)

class Order(Base):
    __tablename__='orders'

    id = Column(Integer, primary_key=True)
    phone = Column( String(200))
    name = Column( String(200))
    surname = Column( String(200))
    city = Column( String(200))
    address_novoi_poshti = Column( String(200))
    datetime = Column(DateTime, default=datetime.datetime.utcnow)
    chooce_clothes = relationship("ChooceClothes",
                    secondary=orders_chooce_clothes,
                    backref="orders")
    price = Column(Float)
    type_order = Column(Integer)

    def __str__(self):
        return 'ID: {}, price: {}'.format(self.id, self.price)