from django.urls import path

from .views import (NewUserView, UpdateUserView, RemoveUserView,AllUserView,
                LoginUserView,LogoutUserView)

app_name = 'user_permission'

urlpatterns = [
    path('all_user/', AllUserView.as_view(), name='all_user'),
    path('new_user/', NewUserView.as_view(), name='new_user'),
    path('update_user/<int:pk>/', UpdateUserView.as_view(), name='update_user'),
    path('remove_user/<int:pk>/', RemoveUserView.as_view(), name='remove_user'),
    path('login/', LoginUserView.as_view(),name='login'),
    path('logout/',LogoutUserView.as_view(),name='logout')
]