spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    return [name["name"] for name in spicy_foods ]

def get_spiciest_foods(spicy_foods):
    return[name for name in spicy_foods if name["heat_level"] > 5 ]

def print_spicy_foods(spicy_foods):
    food_strings = [f'{name["name"]} ({name["cuisine"]}) | Heat Level: {"🌶"* name["heat_level"]}' for name in spicy_foods]
    for food_string in food_strings:
        print(food_string)

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    result = [food for food in spicy_foods if food["cuisine"].lower() == cuisine.lower()]
    return result[0] if result else None 

def print_spiciest_foods(spicy_foods):
    spiciest_foods = [f'{food["name"]} ({food["cuisine"]}) | Heat Level: {"🌶" * food["heat_level"]}' 
                      for food in spicy_foods if food["heat_level"] > 5]
    
    for food in spiciest_foods:
        print(food)

def get_average_heat_level(spicy_foods):
    total_heat_level = sum(food["heat_level"] for food in spicy_foods)
    
    num_foods = len(spicy_foods)
    
    if num_foods > 0:
        return total_heat_level // num_foods
    else:
        return 0 
def create_spicy_food(spicy_foods, spicy_food):

    spicy_foods.append(spicy_food)
    return spicy_foods



