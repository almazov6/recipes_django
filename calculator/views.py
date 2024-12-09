from django.shortcuts import render

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


def recipe_view(request, rec):
    servings = request.GET.get('servings')
    if servings == None:
        servings = 1
    try:
        recipe = DATA[rec]
    except KeyError:
        recipe = None
    context = {
        'recipe': recipe,
        'servings': int(servings)
    }
    return render(request, 'calculator/index.html', context)
