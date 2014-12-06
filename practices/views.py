from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views import generic
from practices.models import Practice

class IndexView(generic.ListView):
    model = Practice

class DetailView(generic.DetailView):
    model = Practice

class UpdateView(generic.UpdateView):
    model = Practice

class CreateView(generic.CreateView):
    model = Practice
    success_url = reverse_lazy("practices:index")

class DeleteView(generic.DeleteView):
    model = Practice
    success_url = reverse_lazy("practices:index")
