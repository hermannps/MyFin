from django.shortcuts import render
from .models import item_orcamento,Todo

# Create your views here.
def index(request):
    todos = Todo.objects.all()
    return render(request,"base.url", {"itens_orcamento": item_orcamento})
