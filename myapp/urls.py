from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.homeView, name='home'),
    path('blog', views.get_search, name='blog'),
    path('result', views.result, name='result'),
    path('propose', views.propose, name='propose'),
    path('test', views.test_view, name='test'),

    #Register, Login, About, Service, Contact
    path('about', views.about_view, name='about'),
    path('service', views.get_info, name='service'),
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


    #Begin other
    path('menu/knowledge', views.other_view, name='other'),
    path('menu/knowledge/calo', views.other_paper_1_view, name='other_paper(1)'),
    path('menu/knowledge/taller', views.other_paper_2_view, name='other_paper(2)'),
    path('menu/knowledge/cheap_food', views.other_paper_3_view, name='other_paper(3)'),
    path('menu/knowledge/fruit', views.other_paper_4_view, name='other_paper(4)'),

    # weight gain
    path('menu/WeightGain', views.weight_gain, name='weightgain'),
    path('menu/WeightGain/WeightGain_paper', views.weight_gain_paper, name='weightgainpaper'),
    path('menu/weight gain/WeightGain_Food', views.weight_gain_paper_1, name='weightgainpaper(1)'),
    path('menu/weight gain/WeightGain', views.weight_gain_paper_2, name='weightgainpaper(2)'),
]

