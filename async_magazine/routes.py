from views import LendingView, CreateOrderView

def setup_routes(app):
    app.router.add_get('', LendingView, name='lending')
    app.router.add_post('/create_order/', CreateOrderView, name='create_order')