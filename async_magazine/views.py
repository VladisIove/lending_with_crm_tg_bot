from aiohttp import web 
import aiohttp_jinja2

from sqlalchemy import create_engine
import sqlalchemy as db
from sqlalchemy.orm import sessionmaker
from settings import MEDIA_PATH, MEDIA_URL, DEFAULT_MEDIA_PATH
from settings import config

from db import ClothesView

DSN = "postgresql://{user}:{password}@{host}:{port}/{database}"
db_url = DSN.format(**config['postgres'])
engine = create_engine(db_url)
connection = engine.connect()
Session = sessionmaker(bind=engine)
session = Session()

class LendingView(web.View):
    
    @aiohttp_jinja2.template('lending.html')
    async def get(self):
        for i in session.query(ClothesView).filter_by(enabled=True):
            for k in i.size:
                print(k)
        return {'clothes': session.query(ClothesView).filter_by(enabled=True)}


class CreateOrderView(web.View):
    pass