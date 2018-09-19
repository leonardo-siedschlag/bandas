from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import render
from bandasApp.forms import CadastroBandasForm

def index(request):

    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage is the same as {{ boldmessage }} in the template!
    context_dict = {'boldmessage': "I am bold font from the context"}

    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.

    return render(request, 'bandasHtml/index.html', context_dict)

def about(request):

    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage is the same as {{ boldmessage }} in the template!
    context_dict = {'boldmessage': "I am bold font from the context"}

    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.

    return render(request, 'bandasHtml/about.html', context_dict)

def addBandas(request):
   if request.method == 'POST':
        form = CadastroBandasForm(request.POST)
        print(form.errors)
        if form.is_valid():
           form.save()
           return index(request)
        else:
             print (form.errors)
   else:

    form = CadastroBandasForm()
    return render(request, 'bandasHtml/addBandas.html', {'form': form})


