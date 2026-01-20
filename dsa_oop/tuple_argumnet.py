
favorite_foods = ("Pizza", "Burger", "Pasta")

def food_items(*foods):
    return foods
result = food_items(*favorite_foods,'sandwich')
print(result)
