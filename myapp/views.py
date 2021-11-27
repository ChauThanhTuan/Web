from django.http import HttpResponseRedirect
from django.shortcuts import render
import datetime

from .forms import NameForm
from polls.models import Blog

name = {}
def get_name(request):
    global name
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            name = form.cleaned_data
            return HttpResponseRedirect('/result')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'index.html', {'form': form})

def result(request):
    blog = Blog.objects.filter(name=name['name']).get()
    return render(request, 'result.html', {'blog': blog})

def homeView(request):
    return render(request, 'home.html',
    {
        'now': datetime.datetime.now()
    }
    )

#Register and Login


#About
def about_view(request):
    return render(request, 'about.html')

#Service
def service_view(request):
    return render(request, 'service.html')
#Contact
# def contact_view(request):
#     return render(request, 'contact.html')

#Begin menu
def menu_view(request):
    return render(request, 'menu.html')
#Begin loss gain
def loss_gain_view(request):
    return render(request, 'main/loss_gain/loss_gain.html')
def loss_gain_paper_1_view(request):
    return render(request, 'main/loss_gain/LG(1).html')
def loss_gain_paper_2_view(request):
    return render(request, 'main/loss_gain/LG(2).html')

def loss_gain_paper_3_view(request):
    return render(request, 'main/loss_gain/LG(3).html')

#begin vegan
def vegan_view(request):
    return render(request, 'main/vegan/vegan.html')
def vegan_paper_1_view(request):
    return render(request, 'main/vegan/vegan(1).html')
#weight gain
def weight_gain(request):
    return render(request, 'main/weight gain/weight_gain.html')
def weight_gain_paper(request):
    return render(request, 'main/weight gain/weight_gain_paper.html')
