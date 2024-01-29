from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# Create your views here.
from app.models import Employee
from django.views import generic
from django.contrib.auth.forms import UserCreationForm

class EmployeeTemplateView(TemplateView):
        template_name = "home.html"

class EmployeeList(ListView):
        model = Employee
        template_name = "list_employee.html"
        context_object_name = 'data'

class EmployeeDetail(DetailView):
        model = Employee
        template_name = "detailed_employee.html"
        context_object_name = 'data'


class EmployeeCreate(CreateView):
        model = Employee
        template_name = "create_employee.html"
        fields = "__all__"

class EmployeeUpdate(UpdateView):
        model = Employee
        template_name = "update_employee.html"
        fields = "__all__"
        # fields = ["first_name","second_name"]

class EmployeeDelete(DeleteView):
        model = Employee
        context_object_name = 'data'
        template_name = "delete.html"
        success_url = reverse_lazy('list')

class SignUpView (generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy ('home') #where it can redirect
    template_name='signup.html'








"""
<!--        <li><a href="{% url 'create' %}">Create</a></li>-->
        <td><button><a href="{% url 'update' i.id %}">update</a></button></td>
        <td><button><a href="{% url 'delete' i.id %}">delete</a></button></td>
 
"""
