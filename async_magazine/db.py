from tortoise.models import Model
from tortoise import fields

class SizeClothes(Model):
    class Meta:
        table='sizes_clothes'

    id = fields.IntField(pk=True)
    name_size = fields.CharField(max_length=120)

    def __str__(self):
        return '{}'.format(self.name_size)

class ColorClothes(Model):
    class Meta:
        table='colors_clothes'

    id = fields.IntField(pk=True)
    name_color = fields.CharField(max_length=120)

    def __str__(self):
        return '{}'.format(self.name_color)

class ClothesView(Model):
    class Meta:
        table='clothes_views'

    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=120) 
    description = fields.CharField(max_length=500)
    type_clothes = fields.SmallIntField()
    enabled = fields.BooleanField()
    old_price = fields.SmallIntField()
    price = fields.SmallIntField()
    count = fields.SmallIntField()
    img = fields.CharField(max_length=500) 
    size = fields.ManyToManyField('models.SizeClothes', related_name='clothes')
    color = fields.ManyToManyField('models.ColorClothes', related_name='clothes')

    def __str__(self):
        return 'ID: {}, name: {}'.format(self.id, self.name)

class ChooceClothes(Model):
    class Meta:
        table='chooces_clothes'

    id = fields.IntField(pk=True)
    datetime = fields.DatetimeField(auto_now_add=True)
    clothes = fields.ManyToManyField('models.ClothesView', related_name='chooce_clothes')
    price = fields.SmallIntField()

    def __str__(self):
        return 'ID: {}, price: {}'.format(self.id, self.price)

class Order(Model):
    class Meta:
        table='orders'

    id = fields.IntField(pk=True)
    phone = fields.CharField(max_length=20) 
    name = fields.CharField(max_length=120)
    surname = fields.CharField(max_length=120)
    city = fields.CharField(max_length=120)
    address_novoi_poshti = fields.CharField(max_length=120)
    datetime = fields.DatetimeField(auto_now_add=True)
    chooce_clothes = fields.ManyToManyField('models.ChooceClothes', related_name='order')
    price = fields.DecimalField(decimal_places=2)
    type_order = fields.IntField()

    def __str__(self):
        return 'ID: {}, price: {}'.format(self.id, self.price)