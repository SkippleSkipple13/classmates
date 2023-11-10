from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from classmates.models import Classmate

class ClassmateList(ListView):
    model = Classmate

class ClassmateView(DetailView):
    model = Classmate

class ClassmateCreate(CreateView):
    model = Classmate
    fields = ['firstname', 'lastname', 'age', 'address', 'gender']
    success_url = reverse_lazy('classmate_list')

class ClassmateUpdate(UpdateView):
    model = Classmate
    fields = ['firstname', 'lastname', 'age', 'address', 'gender']
    success_url = reverse_lazy('classmate_list')

class ClassmateDelete(DeleteView):
    model = Classmate
    success_url = reverse_lazy('classmate_list')
