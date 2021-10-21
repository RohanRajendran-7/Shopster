from django.db import models
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView,DeleteView
from django.contrib.auth.views import LoginView 
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Employee, Visitors

# Create your views here.
class UserLogin(LoginView):
    template_name = 'employee/login.html'
    fields = '__all__'
    redirect_authenticated_user = True
    # success_url = reverse_lazy('home')
    def success_url(self):
        return reverse_lazy('home')

class Home(LoginRequiredMixin, ListView):
    model =  Employee
class VisitorHome(LoginRequiredMixin, ListView):
    model =  Visitors
    
class EmployeeDetail(LoginRequiredMixin,DetailView):
    model = Employee
class VisitorDetail(LoginRequiredMixin,DetailView):
    model = Visitors

class CreateEmployee(LoginRequiredMixin, CreateView):
    model = Employee
    fields = '__all__'
    success_url = reverse_lazy('home')

class CreateVisitor(LoginRequiredMixin, CreateView):
    model = Visitors
    fields = '__all__'
    success_url = reverse_lazy('visitor')
 
class UpdateEmployee(LoginRequiredMixin,UpdateView):
    model = Employee
    fields = '__all__'
    success_url = reverse_lazy('home')

class UpdateVisitor(LoginRequiredMixin,UpdateView):
    model = Visitors
    fields = '__all__'
    success_url = reverse_lazy('visitor')


class DeleteEmployee(LoginRequiredMixin,DeleteView):
    model = Employee
    template_name = 'employee/delete_employee.html'
    success_url = reverse_lazy('home')

class DeleteVisitor(LoginRequiredMixin,DeleteView):
    model = Visitors
    template_name = 'employee/delete_employee.html'
    success_url = reverse_lazy('visitor')