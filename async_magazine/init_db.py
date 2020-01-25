from sqlalchemy import create_engine, MetaData

from settings import config
from db import clothes_views_color, clothes_views_size, orders_chooce_clothes, Base

DSN = "postgresql://{user}:{password}@{host}:{port}/{database}"
db_url = DSN.format(**config['postgres'])

def create_tables(engine):
    meta = MetaData()
    Base.metadata.create_all(bind=engine)
    meta.create_all(bind=engine, tables=[orders_chooce_clothes, clothes_views_size, clothes_views_color])

if __name__ == '__main__':
    db_url = DSN.format(**config['postgres'])
    engine = create_engine(db_url)

    create_tables(engine)