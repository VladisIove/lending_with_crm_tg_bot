import json 

from aiohttp import web , ClientSession
import aiohttp_jinja2

from sqlalchemy import create_engine
import sqlalchemy as db
from sqlalchemy.orm import sessionmaker
from settings import MEDIA_PATH, MEDIA_URL, DEFAULT_MEDIA_PATH
from settings import config

from db import ClothesView, ChooceClothes, Order

DSN = "postgresql://{user}:{password}@{host}:{port}/{database}"
db_url = DSN.format(**config['postgres'])
engine = create_engine(db_url)
connection = engine.connect()
Session = sessionmaker(bind=engine)
session = Session()

class LendingView(web.View):
    
    @aiohttp_jinja2.template('lending.html')
    async def get(self):
        return {'clothes': session.query(ClothesView).filter_by(enabled=True).order_by(ClothesView.type_clothes.desc())}

class CreateFastOrderView(web.View):
    
    async def post(self):
        try:
            data = await self.request.post()   
            order = Order(type_order=data['type_order'],name=data['name'],phone=data['phone'], price=data['price'])
            chooce_clothes = ChooceClothes(clothes_id=data['id_clothes'], price=data['price'])
            session.add(order,chooce_clothes)
            order.chooce_clothes.append(chooce_clothes)
            session.commit()
            return web.json_response({'created': True}, status=200)
        except:
            return web.json_response({'created': False}, status=500)
class CreateOrderByCartView(web.View):

    async def post(self):
        data = await self.request.post()
        order = Order(**data['order'])
        session.add(order)
        async for fields in data['chooce_clothes']:
            order.chooce_clothes.append(ChooceClothes(**fields))
        session.commit()
        return web.json_response({'created': True}, status=200)
