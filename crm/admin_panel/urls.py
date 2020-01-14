from django.urls import path

from .views import (NewClothesView, UpdateClothesView, 
                    AllClothesView, AllOrderView, 
                    CompleteOrderView,RemoveClothesView)

app_name = 'admin_panel'

urlpatterns = [
    path('new_clothes/', NewClothesView.as_view(), name='new_clothes'),
    path('update_clohes/<int:pk>/', UpdateClothesView.as_view(), name='update_clothes'),
    path('remove_clothes/<int:pk>/', RemoveClothesView.as_view(), name='remove_clothes'),
    path('all_clothes/', AllClothesView.as_view(), name='all_clothes'),
    path('all_order/',AllOrderView.as_view(), name='all_order'),
    path('all_order/<int:filter>/',AllOrderView.as_view(), name='all_order_with_param'),
    path('complete_order/', CompleteOrderView.as_view(), name='complete_order'),
]