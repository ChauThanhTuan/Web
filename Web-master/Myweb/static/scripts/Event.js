let list = {
    "optionsMealsCooking": "MealsCooking",
    "optionsFoodNews": "FoodNews",
    "optionsHolidays": "Holidays",
    "optionsSpecialDiets": "SpecialDiets",
    "optionsHealthyMealPlans": "HealthyMealPlans",
    "optionsHealthyLifestyle": "HealthyLifestyle"
}

let menuIcon = document.querySelector("#header #nav-menu");
let menu = document.querySelector("#header .menu");
let body = document.querySelector("body");
let subOptions = document.querySelectorAll("#header .sub-options div")
let mealplansTypes = document.querySelectorAll("#header .mealplansType")

menuIcon.onclick = function() {
    menu.style.display = "block";
    body.style.backgroundColor = "#ccc";
}


for (var mealplansType of mealplansTypes) {
    mealplansType.onclick = function() {
        for (var subOption of subOptions) {
            subOption.className = "hidden";
        }
        document.getElementById(list[this.id]).classList.remove("hidden");
    }
}