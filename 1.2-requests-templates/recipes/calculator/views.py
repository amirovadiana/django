from django.shortcuts import render
from django.http import HttpResponse


DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
}

name_dish = DATA.keys()


def recipes_list(request):
    context = {
        'name_dish': name_dish
    }
    template_name = 'calculator/recipes_list.html'
    return render(request, template_name, context)


def calculate_recipes(request, dish):
    servings = int(request.GET.get('servings', 1))
    recipes = {}
    for food, description in DATA.items():
        if food == dish:
            for ingredient, amount in description.items():
                recipes[ingredient] = float(amount * servings)

    context = {
        'recipes': recipes
    }
    return render(request, 'calculator/index.html', context)
