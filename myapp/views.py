from django.http import HttpResponseRedirect
from django.shortcuts import render
import datetime

from polls.models import Blog

# Test xem có lấy đươc thông tin hay k
import win32api

# Search feature
search = ""
def get_search(request):
    global search
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        search = request.POST['search']
        search = search.upper()

        # Test xem có lấy đươc thông tin hay k
        
        # check whether it's valid:
        if search:
            # win32api.MessageBox(0, search, 'title')
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/result')
        else:
            win32api.MessageBox(0, "Giá trị không hợp lệ", 'error')
            return HttpResponseRedirect(request.path)

    return render(request, 'home.html')

def result(request):
    blog = Blog.objects.filter(title__contains=search).all()
    return render(request, 'blog.html', {'blog': blog})

# Chức năng đề xuất
def get_info(request):
    global search
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        name = request.POST['name']
        age = int(request.POST['age'])
        high = int(request.POST['high']) / 100
        weight = int(request.POST['weight'])
        BMI = weight / (2 * high)
        # Tính BMR cho nam
        BMR = (66.5 + (13.75 * weight) + (5.003 * high) - (6.755 * age))
        # Tính BMR cho nữ
        # Test xem có lấy đươc thông tin hay k
        # win32api.MessageBox(0, "BMI: " + str(BMI) + " BMR: " + str(BMR), 'BMI and BMR')
        
        if BMI < 18.5:
            search = "weight_gain"
        elif BMI >= 25:
            search = "loss_gain"
        else:
            search = "other"

        return HttpResponseRedirect('/propose')
        # check whether it's valid:
        # if search:
        #     # win32api.MessageBox(0, search, 'title')
        #     # process the data in form.cleaned_data as required
        #     # ...
        #     # redirect to a new URL:
        #     return HttpResponseRedirect('/bmi')
        # else:
        #     win32api.MessageBox(0, "Giá trị không hợp lệ", 'error')

    return render(request, 'service.html')

def propose(request):
    blog = Blog.objects.filter(topic__contains=search).all()
    return render(request, 'blog.html', {'blog': blog})

#
def homeView(request):
    return render(request, 'home.html',
    {
        'now': datetime.datetime.now()
    }
)

# Test
def test_view(request):
    return render(request, 'result.html')

#About
def about_view(request):
    return render(request, 'about.html')

# #Service
# def service_view(request):
#     return render(request, 'service.html')
#Contact
# def contact_view(request):
#     return render(request, 'contact.html')

#Begin menu
def service_view(request):
    return render(request, 'service.html')

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
def loss_gain_paper_4_view(request):
    return render(request, 'main/loss_gain/LG(4).html')
def loss_gain_paper_5_view(request):
    return render(request, 'main/loss_gain/LG(5).html')
def loss_gain_paper_6_view(request):
    return render(request, 'main/loss_gain/LG(6).html')

#begin vegan
def vegan_view(request):
    return render(request, 'main/vegan/vegan.html')
def vegan_paper_1_view(request):
    return render(request, 'main/vegan/vegan(1).html')
def vegan_paper_2_view(request):
    return render(request, 'main/vegan/vegan(2).html')
def vegan_paper_3_view(request):
    return render(request, 'main/vegan/vegan(3).html')

#Begin other
def other_view(request):
    return render(request, 'main/other/other.html')
def other_paper_1_view(request):
    return render(request, 'main/other/other(1).html')
def other_paper_2_view(request):
    return render(request, 'main/other/other(2).html')
def other_paper_3_view(request):
    return render(request, 'main/other/other(3).html')
def other_paper_4_view(request):
    return render(request, 'main/other/other(4).html')
def other_paper_5_view(request):
    return render(request, 'main/other/other(5).html')
def other_paper_6_view(request):
    return render(request, 'main/other/other(6).html')
def other_paper_7_view(request):
    return render(request, 'main/other/other(7).html')


#weight gain
def weight_gain(request):
    return render(request, 'main/weight gain/weight_gain.html')
def weight_gain_paper(request):
    return render(request, 'main/weight gain/weight_gain_paper.html')
def weight_gain_paper_1(request):
    return render(request, 'main/weight gain/weight_gain_paper(1).html')
def weight_gain_paper_2(request):
    return render(request, 'main/weight gain/weight_gain_paper(2).html')


