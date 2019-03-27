from django.shortcuts import render
from django.http import *
from models import *

# Create your views here.

def index(request):
    context = {'list': 'list'}
    return render(request, 'booktest/index.html', context)


def show(request, id):
    book = BookInfo.objects.get(pk=id)
    herobook = book.heroinfo_set.all()

    context = {'list': herobook}
    return render(request, 'booktest/show.html', context)

