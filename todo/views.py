from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import TodoModel
from django.urls import reverse_lazy

# Create your views here.

class TodoList(ListView):
    template_name = "list.html"
    model = TodoModel
class TodoDetail(DetailView):
    template_name = "detail.html"
    model = TodoModel
    # success_url = reverse_lazy("list")
class TodoCreate(CreateView):
    template_name = "create.html"
    model = TodoModel
    fields = ("title","memo","priority","duedate")
    # createを行った後、どこのlinkに戻れば良いか指示するもの(urlsで各リンクに名前をつけて、指示を行う)
    success_url = reverse_lazy("list") #要チェック
class TodoDelete(DeleteView):
    template_name =  "delete.html"
    model = TodoModel
    success_url = reverse_lazy("list")
class TodoUpdate(UpdateView):
    template_name =  "update.html"
    model = TodoModel
    fields = ("title","memo","priority","duedate")
    success_url = reverse_lazy("list")
