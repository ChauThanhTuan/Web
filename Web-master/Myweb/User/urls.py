from django.urls import path
from User import views

urlpatterns = [
    #Home
    path('', views.homeView, name='home'),

    #Register and Login and About
    path('/register', views.register_view, name='register'),
    path('/login', views.login_view, name='login'),
    path('/about', views.about_view, name='about'),

    #Begin main page
    path('menu/HealthyMealPlans/WeightLossMealPlans/main.html', views.HealthyMealPlans_WeightLossMealPlans_view, name='HealthyMealPlans_WeightLoss'),
    path('menu/HealthyMealPlans/VeganMealPlans/main.html', views.HealthyMealPlans_VeganMealPlans_view, name='HealthyMealPlans_Vegan'),
    path('menu/HealthyMealPlans/DiabetesMealPlans/main.html', views.HealthyMealPlans_DiabetesMealPlans_view, name='HealthyMealPlans_Diabetes'),
    path('menu/HealthyMealPlans/CholesterolMealPlans/main.html', views.HealthyMealPlans_CholesterolMealPlans_view, name='HealthyMealPlans_Cholesterol'),
    path('menu/HealthyMealPlans/PregnancyMealPlans/main.html', views.HealthyMealPlans_PregnancyMealPlans_view, name='HealthyMealPlans_Pregnancy'),
    path('menu/HealthyMealPlans/HeartHealthyMealPlans/main.html', views.HealthyMealPlans_HeartHealthyMealPlans_view, name='HealthyMealPlans_HeartHealthy'),
    path('menu/HealthyMealPlans/WeightgainMealPlans/main.html', views.HealthyMealPlans_DinnerMealPlans_view, name='HealthyMealPlans_Dinner'),
    path('menu/HealthyMealPlans/HealthyKidMealPlans/main.html', views.HealthyMealPlans_HealthyKidMealPlans_view, name='HealthyMealPlans_HealthyKid'),
    #End main page

    #Begin WeightLoss Meal Plans
    path('menu/HealthyMealPlans/WeightLossMealPlans/id1.html', views.HealthyMealPlans_WeightLossMealPlans_id1_view, name='HealthyMealPlans_WeightLoss_id1'),
    path('menu/HealthyMealPlans/WeightLossMealPlans/id2.html', views.HealthyMealPlans_WeightLossMealPlans_id2_view, name='HealthyMealPlans_WeightLoss_id2'),
    path('menu/HealthyMealPlans/WeightLossMealPlans/id3.html', views.HealthyMealPlans_WeightLossMealPlans_id3_view, name='HealthyMealPlans_WeightLoss_id3'),
    path('menu/HealthyMealPlans/WeightLossMealPlans/id4.html', views.HealthyMealPlans_WeightLossMealPlans_id4_view, name='HealthyMealPlans_WeightLoss_id4'),
    #End WeightLoss Meal Plans
    
    #Begin Vegan Meal Plans
    path('menu/HealthyMealPlans/VeganMealPlans/id1.html', views.HealthyMealPlans_VeganMealPlans_id1_view, name='HealthyMealPlans_Vegan_id1'),
    path('menu/HealthyMealPlans/VeganMealPlans/id2.html', views.HealthyMealPlans_VeganMealPlans_id2_view, name='HealthyMealPlans_Vegan_id2'),
    path('menu/HealthyMealPlans/VeganMealPlans/id3.html', views.HealthyMealPlans_VeganMealPlans_id3_view, name='HealthyMealPlans_Vegan_id3'),
    path('menu/HealthyMealPlans/VeganMealPlans/id4.html', views.HealthyMealPlans_VeganMealPlans_id4_view, name='HealthyMealPlans_Vegan_id4'),
    #End Vegan Meal Plans

    #Begin Holiday Plans
    path('menu/Holidays/Holidays Recipes/main.html', views.Holiday_Recipes_View, name='Holiday_Recipes'),
    
    #Begin Holiday Recipes
    path('menu/Holidays/Holidays Recipes/tet.html', views.Holiday_Recipes_tetND_View, name='Tet_Nguyen_Dan'),

    #Begin Special Diets
    path('menu/SpecialDiets/main.html', views.Special_Diets_View, name='Special_Diets'),

    #Begin Food News
    path('menu/FoodNews/main.html', views.Food_News_View, name='Food_News'),
]