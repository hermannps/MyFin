from django.shortcuts import render
from .models import item_orcamento

# Create your views here.
def index(request):
    return render(request,"base.url", {"itens_orcamento": item_orcamento})
