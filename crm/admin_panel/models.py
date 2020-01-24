from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Image(models.Model):
    class Meta:
        db_table='images'

    img = models.ImageField(upload_to = 'media/', verbose_name='Фотография профиля', default='../static/img/noimage.jpg', null=False,blank=False)

class SizeClothes(models.Model):
    class Meta:
        db_table='sizes_clothes'
    
    name_size = models.CharField(max_length=120, null=False,blank=False)
    datetime = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return '{}'.format(self.name_size)

class ColorClothes(models.Model):
    class Meta:
        db_table='colors_clothes'

    name_color = models.CharField(max_length=120,null=False, blank=False)

    def __str__(self):
        return '{}'.format(self.name_color)

class ClothesView(models.Model):
    class Meta:
        db_table ='clothes_views'
        ordering = ('datetime', 'enabled',)

    class TYPE_CLOTHES:
        TSHIRT=1
        HOODIE=2
        SHIRT=3
    
    CHOICE_TYPE_CLOTHES = (
        (TYPE_CLOTHES.TSHIRT, 'Футболка'),
        (TYPE_CLOTHES.HOODIE, 'Толстовка'),
        (TYPE_CLOTHES.SHIRT, 'Майка')
    )
    name = models.CharField(max_length=120, null=False,blank=False)
    description = models.CharField(max_length=500,null=False,blank=False)
    datetime = models.DateTimeField(auto_now_add=True, auto_now=False)
    type_clothes = models.PositiveSmallIntegerField(choices=CHOICE_TYPE_CLOTHES, default=TYPE_CLOTHES.TSHIRT)
    enabled = models.BooleanField(default=True)
    #clothes = models.ManyToManyField(Clothes, related_name='clothes_view')
    old_price = models.FloatField(validators=[MinValueValidator(0),], default=0, blank=True, null=True)
    price = models.FloatField(validators=[MinValueValidator(0),],null=False,blank=False)
    count = models.PositiveSmallIntegerField()
    #img = models.ForeignKey(Image,on_delete=models.CASCADE)
    img = models.ImageField(upload_to = 'media/', verbose_name='Фотография одежды', null=False,blank=False)
    size = models.ManyToManyField(SizeClothes,related_name='clothes')
    color = models.ManyToManyField(ColorClothes,related_name='clothes')

    def __str__(self):
        return 'ID: {}, name: {}'.format(self.id, self.name)
class ChooceClothes(models.Model):
    class Meta:
        db_table='chooces_clothes'

    datetime = models.DateTimeField(auto_now_add=True, auto_now=False)
    clothes = models.OneToOneField(ClothesView,related_name='chooce_clothes',null=True, on_delete=models.SET_NULL)
    price = models.FloatField(validators=[MinValueValidator(0),],null=False,blank=False)

class Order(models.Model):
    class Meta:
        db_table='orders'
        ordering=('-datetime',)

    class TYPE_ORDER:
        FAST = 1
        FULL = 2

    CHOICES_TYPE_ORDER = (
        (TYPE_ORDER.FAST, 'Быстрый заказ'),
        (TYPE_ORDER.FULL, 'Полный заказ'),
    )
    
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    name = models.CharField(max_length=120)
    surname = models.CharField(max_length=120)
    city = models.CharField(max_length=120)
    address_novoi_poshti = models.CharField(max_length=500)
    datetime = models.DateTimeField(auto_now_add=True, auto_now=False)
    chooce_clothes = models.ManyToManyField(ChooceClothes, related_name='order')
    complete = models.BooleanField()
    price = models.FloatField(validators=[MinValueValidator(0),],null=False,blank=False, default=0)
    type_order = models.PositiveSmallIntegerField(choices=CHOICES_TYPE_ORDER, default=TYPE_ORDER.FAST)

    def __str__(self):
        return 'ID: {}, datetime: {}'.format(self.id, self.datetime)

