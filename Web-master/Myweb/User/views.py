from django.shortcuts import render
import datetime

def homeView(request):
    return render(
        request,
        'home.html',
        {
            'now': datetime.datetime.now()
        }
    )

#Register and login
def register_view(request):
    return render(request, 'register.html',)
def login_view(request):
    return render(request, 'login.html',)

def about_view(request):
    return render(request,'about.html')

#Begin main page
def HealthyMealPlans_WeightLossMealPlans_view(request):
    return render(request, 'menu/HealthyMealPlans/WeightLossMealPlans/main.html',)

def HealthyMealPlans_VeganMealPlans_view(request):
    return render(request, 'menu/HealthyMealPlans/VeganMealPlans/main.html',)

def HealthyMealPlans_DiabetesMealPlans_view(request):
    return render(request, 'menu/HealthyMealPlans/DiabetesMealPlans/main.html',)
    
def HealthyMealPlans_CholesterolMealPlans_view(request):
    return render(request, 'menu/HealthyMealPlans/CholesterolMealPlans/main.html',)

def HealthyMealPlans_PregnancyMealPlans_view(request):
    return render(request, 'menu/HealthyMealPlans/PregnancyMealPlans/main.html',)

def HealthyMealPlans_HeartHealthyMealPlans_view(request):
    return render(request, 'menu/HealthyMealPlans/HeartHealthyMealPlans/main.html',)

def HealthyMealPlans_DinnerMealPlans_view(request):
    return render(request, 'menu/HealthyMealPlans/DinnerMealPlans/main.html',)
    
def HealthyMealPlans_HealthyKidMealPlans_view(request):
    return render(request, 'menu/HealthyMealPlans/HealthyKidMealPlans/main.html',)
#End main page

#Begin WeightLoss Meal Plans
def HealthyMealPlans_WeightLossMealPlans_id1_view(request):
    return render(request, 'menu/HealthyMealPlans/WeightLossMealPlans/id1.html',)

def HealthyMealPlans_WeightLossMealPlans_id2_view(request):
    return render(request, 'menu/HealthyMealPlans/WeightLossMealPlans/id2.html',)
    
def HealthyMealPlans_WeightLossMealPlans_id3_view(request):
    return render(request, 'menu/HealthyMealPlans/WeightLossMealPlans/id3.html',)
    
def HealthyMealPlans_WeightLossMealPlans_id4_view(request):
    return render(request, 'menu/HealthyMealPlans/WeightLossMealPlans/id4.html',)
#End WeightLoss Meal Plans

#Begin Vegan Meal Plans
def HealthyMealPlans_VeganMealPlans_id1_view(request):
    return render(request, 'menu/HealthyMealPlans/VeganMealPlans/id1.html',)

def HealthyMealPlans_VeganMealPlans_id2_view(request):
    return render(request, 'menu/HealthyMealPlans/VeganMealPlans/id2.html',)
    
def HealthyMealPlans_VeganMealPlans_id3_view(request):
    return render(request, 'menu/HealthyMealPlans/VeganMealPlans/id3.html',)
    
def HealthyMealPlans_VeganMealPlans_id4_view(request):
    return render(request, 'menu/HealthyMealPlans/VeganMealPlans/id4.html',)
#End Vegan Meal Plans

#begin Holidays Recipes
def Holiday_Recipes_View(request):
    return render(request,'menu/Holidays/Holidays Recipes/main.html')

def Holiday_Recipes_tetND_View(request):
    return render(request,'menu/Holidays/Holidays Recipes/tet.html')

#Begin Special Diets
def Special_Diets_View(request):
    return render(request,'menu/SpecialDiets/main.html')

#Begin Food News
def Food_News_View(request):
    return render(request,'menu/FoodNews/main.html')