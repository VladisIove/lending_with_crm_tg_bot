from views import LendingView, CreateOrderView
import os


def setup_routes(app):
    cwd = os.getcwd()
    app.router.add_get('', LendingView, name='lending')
    app.router.add_post('/create_order/', CreateOrderView, name='create_order')
    app.router.add_static('/static/', path=str('{}/static'.format(cwd)),  name='static')