from django.shortcuts import render
from rango.models import Category
from django.http import HttpResponse

def index(request):
    context_dict = {'boldmessage': "I am bold font from the context"}

    return render(request, 'rango/index.html', context_dict)#criar uma no about

def about(request):
    context_dict = {'boldmessage': "I am bold font from the context"}

    return render(request, 'rango/about.html', context_dict)#criar uma no about

def index(request):
    #variavel criada
    category_list = Category.objects.order_by('-views')[:5]#category_list = puxando da models e ordenando por likes
    context_dict = {'categories': category_list}#passando um dicionario

    # Render the response and send it back!

    return render (request,'rango/index.html',context_dict)
