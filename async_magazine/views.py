from aiohttp import web 
import aiohttp_jinja2

class LendingView(web.View):
    
    @aiohttp_jinja2.template('lending.html')
    async def get(self):
        return {'clothes': []}


class CreateOrderView(web.View):
    pass