from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.base import View 
from django.views.generic.edit import FormView
from .models import  Order,ClothesView
from .forms import ClothesForm

# Create your views here.


class NewClothesView(CreateView, LoginRequiredMixin):
    model = ClothesView
    fields = ['name', 'description', 'type_clothes', 'enabled',
                'old_price', 'price', 'count', 'img', 'size', 'color']
    #form_class = ClothesForm
    template_name = 'clothes_pages/form_clothes.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_anonymous:
            return redirect('admin_panel:all_clothes')
        if request.user.permission_user == 3:
            return super(NewClothesView,self).dispatch(request, *args, **kwargs)
        return redirect('admin_panel:all_clothes')

    def get_success_url(self):
        return reverse('admin_panel:all_clothes')
    

class UpdateClothesView(UpdateView, LoginRequiredMixin):
    model = ClothesView 
    fields = ['name', 'description', 'type_clothes', 'enabled',
                'old_price', 'price', 'count', 'img', 'size', 'color']
    template_name = 'clothes_pages/form_clothes.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_anonymous:
            return redirect('admin_panel:all_clothes')
        if request.user.is_anonymous or request.user.permission_user == 3:
            return super(UpdateClothesView,self).dispatch(request, *args, **kwargs)
        return redirect('admin_panel:all_clothes')
    
    def get_success_url(self):
        return reverse('admin_panel:all_clothes')

class RemoveClothesView(View):
    model = ClothesView 
    
    def get(self,request,*args,**kwargs):
        try:
            self.model.objects.get(pk=kwargs['pk']).delete()
        except:
           return redirect('admin_panel:all_clothes') 
        return redirect('admin_panel:all_clothes')


class AllClothesView(ListView, LoginRequiredMixin):
    model = ClothesView
    context_object_name ='clothes_views'
    template_name = 'clothes_pages/all_clothes.html'

class AllOrderView(ListView, LoginRequiredMixin):
    model = Order
    template_name = 'orders_pages/order_page.html'

    def get_queryset(self,*args,**kwargs):
        qs = super().get_queryset()
        try:
            if kwargs['filter'] == 1 or kwargs['filter'] == 2:
                return qs.filter(type_order=kwargs['filter'])
            if kwargs['filter'] == 3:
                return qs.filter(complete=True)
        except:
            return qs

class CompleteOrderView(View, LoginRequiredMixin):

    def get(self,*args,**kwargs):
        Order.objects.filter(id=kwargs['pk']).update(complete=kwargs['complete']) 
    