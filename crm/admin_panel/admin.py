from django.contrib import admin

from .models import Image, SizeClothes, ColorClothes, ClothesView, ChooceClothes,Order

# Register your models here.

admin.site.register(Image)
admin.site.register(SizeClothes)
admin.site.register(ColorClothes)
#admin.site.register(Clothes)
admin.site.register(ClothesView)
admin.site.register(ChooceClothes)
admin.site.register(Order)
