from views import LendingView, CreateFastOrderView, CreateOrderByCartView
import os


def setup_routes(app):
    cwd = os.getcwd()
    app.router.add_get('', LendingView, name='lending')
    app.router.add_post('/create_fast_order/', CreateFastOrderView, name='create_fast_order')
    app.router.add_post('/create_order_by_cart/', CreateOrderByCartView, name='crete_order_by_cart')
    app.router.add_static('/static/', path=str('{}/static'.format(cwd)),  name='static')