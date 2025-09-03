from api import IngredientApi
import random


def get_ingredient_list_id():
    response = IngredientApi.get_ingredients()
    ingredients = response.json()['data']
    list_id = []
    for ingredient in ingredients:
        list_id.append(ingredient['_id'])
        if len(list_id) >= random.randint(1, 5):
            break
    return list_id
