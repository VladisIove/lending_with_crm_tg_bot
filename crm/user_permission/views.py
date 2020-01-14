from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import logout
from django.contrib.auth.views import  LoginView, LogoutView
from django.views.generic.base import View 
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView, DeletionMixin
from django.views.generic.list import ListView

from .models import User
# Create your views here.

class LogoutUserView(LogoutView):
    pass

class LoginUserView(LoginView):
    template_name = 'user/login.html'

class NewUserView(CreateView, LoginRequiredMixin):
    model = User
    template_name='user/form_user.html' 
    fields = ['name','surname','email','permission_user','password']

    def get_success_url(self):
        return reverse('user_permission:all_user')

    def dispatch(self, request, *args, **kwargs):
        if request.user.permission_user == 3:
            return super(NewUserView,self).dispatch(request, *args, **kwargs)
        return redirect('admin_panel:all_clothes')
    
    def get_context_data(self, **kwards):
        context = super(NewUserView, self).get_context_data(**kwards)
        context['name_button'] = 'Создать юзера'
        context['class_button'] = 'btn btn-primary'
        return context

class UpdateUserView(UpdateView, LoginRequiredMixin):
    model = User
    template_name='user/form_user.html'
    fields = ['name','surname','email','permission_user','password']
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.permission_user == 3:
            return super(UpdateUserView,self).dispatch(request, *args, **kwargs)
        return redirect('admin_panel:all_clothes')
    
    def get_context_data(self, **kwards):
        context = super(UpdateUserView, self).get_context_data(**kwards)
        context['name_button'] = 'Обновить юзера'
        context['class_button'] = 'btn btn-primary'
        return context

class RemoveUserView(View, LoginRequiredMixin):
    model = User 
    template_name='user/form_user.html'
    def dispatch(self, request, *args, **kwargs):
        if request.user.permission_user == 3:
            return super(RemoveUserView,self).dispatch(request, *args, **kwargs)
        return redirect('admin_panel:all_clothes')

    def get(self,request,*args,**kwargs):
        print(kwargs)
        try:
            self.model.objects.get(pk=kwargs['pk']).delete()
        except:
           return redirect('user_permission:all_user') 
        return redirect('user_permission:all_user')

    def get_success_url(self):
        return reverse('user_permission:all_user')

class AllUserView(ListView, LoginRequiredMixin):
    model = User
    context_object_name ='users'
    template_name='user/all_user.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.permission_user == 3:
            return super(AllUserView,self).dispatch(request, *args, **kwargs)
        return redirect('admin_panel:all_clothes')