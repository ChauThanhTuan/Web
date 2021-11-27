from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.homeView, name='home'),
    path('name', views.get_name, name='name'),
    path('result', views.result, name='result'),

    #Register, Login, About, Service, Contact
    path('about', views.about_view, name='about'),
    path('service', views.service_view, name='service'),
    #path('contact', views.contact_view, name='contact'),

    #Begin menu
    path('menu', views.menu_view, name='menu'),
    #Begin loss gain
    path('menu/LossGain', views.loss_gain_view, name='lossgain'),
    path('menu/lossgain/1000calo', views.loss_gain_paper_1_view, name='paper_lg(1)'),
    path('menu/lossgain/lowcarbs', views.loss_gain_paper_2_view, name='paper_lg(2)'),
    path('menu/lossgain/lowcalo', views.loss_gain_paper_3_view, name='paper_lg(3)'),

    #Begin Vegan
    path('menu/Vegan', views.vegan_view, name='vegan'),
    path('menu/Vegan/VeganHealthy', views.vegan_paper_1_view, name='vegan_paper(1)'),
    # weight gain
    path('menu/weight gain', views.weight_gain, name='weightgain'),
    path('menu/weight gain/weight gain paper', views.weight_gain_paper, name='weightgainpaper'),
]
