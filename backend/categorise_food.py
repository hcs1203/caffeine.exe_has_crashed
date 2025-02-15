from api import client
from supabase_connection import SupabaseSingleton  # Import the Singleton

# Get the Supabase client from the Singleton
supabase = SupabaseSingleton.get_instance()

'''
def categorise_food(food_name):
    # use openai gpt models to categorise food
    prompt = ""#f"There are 2 categories of food, perishable and stable, please categorise the food {food_name} accordingly according to its natural and storage properties. Return only the category of the food in a list of tuples (ingredient, category)"

    completion = client.chat.completions.create(
        model="gpt-4o",
        store=True,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return completion.choices[0].message.content
'''
def get_current_user():
    user = supabase.auth.get_user()
    if user and user.user:
        return user.user.id
    return None

def get_user_preferences(user_id):
    if not user_id:
        return "Error: No authenticated user found"
    
    response = supabase.table("dietary_preferences").select("preferences").eq("user_id", user_id).single().execute()
    
    if response.data:
        return response.data["preferences"]
    return "No preferences found for this user"
    
# ingredients = [
#      "broccoli", "instant noodles", "potato", "carrot", "onion", "tomato", "cucumber", "spinach", "lettuce",
#      "bell pepper", "cauliflower", "garlic", "ginger", "eggplant", "zucchini", "cabbage", "radish", 
#      "mushroom", "peas", "asparagus", "okra", "celery", "beetroot", "fennel", "brussels sprouts",
#      "artichoke", "turnip", "parsnip", "kale", "swiss chard", "bok choy", "leek", "scallion",
#      "apple", "banana", "orange", "mango", "pineapple", "strawberry", "blueberry", "raspberry", 
#      "blackberry", "cranberry", "avocado", "watermelon", "grape", "papaya", "cherry", "pear", 
#      "peach", "pomegranate", "kiwi", "lemon", "lime", "plum", "fig", "apricot", "coconut", 
#      "lychee", "guava", "dragon fruit", "persimmon", "mulberry", "starfruit",
#      "rice", "wheat", "oats", "quinoa", "barley", "corn", "millet", "rye", "buckwheat",
#      "sorghum", "amaranth", "couscous", "farro", "bulgur", "wild rice", "teff",
#     "lentils", "chickpeas", "kidney beans", "black beans", "green gram", "soybeans", 
#     "pinto beans", "white beans", "navy beans", "adzuki beans", "mung beans",
#     "chicken", "beef", "pork", "fish", "salmon", "tuna", "shrimp", "lobster", "crab",
#     "mussels", "clams", "oysters", "squid", "octopus", "duck", "turkey", "lamb", 
#     "venison", "rabbit", "quail", "goat meat",
#     "egg", "milk", "cheese", "yogurt", "butter", "cream", "sour cream", "ghee",
#     "tofu", "tempeh", "paneer", "cottage cheese", "halloumi", "mozzarella", "cheddar",
#     "parmesan", "feta", "ricotta",
#     "salt", "pepper", "turmeric", "cumin", "coriander", "cardamom", "cinnamon", "cloves", 
#     "nutmeg", "mustard seeds", "bay leaf", "basil", "oregano", "thyme", "rosemary", 
#     "paprika", "chili powder", "cayenne", "saffron", "tarragon", "dill", "chives",
#     "star anise", "fenugreek", "lemongrass", "sumac", "caraway", "marjoram",
#     "olive oil", "vegetable oil", "butter", "vinegar", "balsamic vinegar", "red wine vinegar",
#     "soy sauce", "ketchup", "mayonnaise", "mustard", "honey", "sugar", "maple syrup",
#     "molasses", "coconut oil", "sesame oil", "peanut oil", "avocado oil", "ghee",
#     "bread", "pasta", "noodles", "cereal", "oatmeal", "granola", "pita", "tortilla", 
#     "baguette", "croissant", "donut", "muffin", "biscotti", "sourdough", "focaccia",
#     "chips", "chocolate", "biscuits", "cake", "ice cream", "brownies", "cookies", "candy",
#     "pudding", "popcorn", "marshmallow", "pretzels", "crackers", "cheesecake", "pastry",
#     "coffee", "tea", "green tea", "black tea", "herbal tea", "matcha", "chai", "cocoa powder",
#     "hot chocolate", "energy drink", "soda", "lemonade", "smoothie", "milkshake", "kombucha",
#     "wine", "beer", "whiskey", "vodka", "rum", "gin", "tequila", "brandy", "cider", "sake",
#     "peanut butter", "jam", "jelly", "marmalade", "tahini", "almond butter", "hazelnut spread",
#     "cream cheese", "hummus", "guacamole", "salsa", "pesto", "barbecue sauce", "soybean paste",
#     "fish sauce", "hoisin sauce", "wasabi", "horseradish",
#     "yogurt drink", "kefir", "buttermilk", "coconut milk", "almond milk", "soy milk",
#     "oat milk", "rice milk", "cashew milk", "macadamia milk",
#     "tofu skin", "seitan", "jackfruit", "textured vegetable protein", "miso", "natto",
#     "seaweed", "nori", "wakame", "kelp", "dulse", "spirulina", "chlorella",
#     "caviar", "anchovies", "sardines", "eel", "tilapia", "haddock", "halibut", "trout", "cod",
#     "miso paste", "kimchi", "sauerkraut", "pickles", "fermented black beans",
#     "chili flakes", "coconut flakes", "dried fruits", "raisins", "prunes",
#     "cranberries", "goji berries", "apricots",
#     "tamarind", "yuzu", "lotus root", "edamame", "wasabi peas",
#     "plantain", "cassava", "taro", "yam", "sweet potato", "jicama",
#     "gelatin", "agar-agar", "xanthan gum", "guar gum", "cornstarch", "potato starch", "arrowroot powder",
#     "vanilla extract", "almond extract", "rose water", "orange blossom water",
#     "safflower oil", "grapeseed oil", "walnut oil", "hazelnut oil", "pumpkin seed oil",
#     "vegemite", "marmite", "nutritional yeast", "tempeh bacon",
#     "beef jerky", "salami", "prosciutto", "chorizo", "bacon",
#     "flaxseeds", "chia seeds", "hemp seeds", "sunflower seeds", "pumpkin seeds", "poppy seeds",
#     "cashews", "almonds", "walnuts", "pecans", "hazelnuts", "macadamia nuts", "brazil nuts", "pistachios",
#     "cottage cheese", "creme fraiche", "mascarpone", "gorgonzola", "brie", "camembert"
# ]
# FOOD_CATEGORIES = {
#     "broccoli": "perishable", 
#     "instant noodles": "stable", 
#     "potato": "perishable", 
#     "carrot": "perishable", 
#     "onion": "perishable", 
#     "tomato": "perishable", 
#     "cucumber": "perishable", 
#     "spinach": "perishable", 
#     "lettuce": "perishable", 
#     "bell pepper": "perishable", 
#     "cauliflower": "perishable", 
#     "garlic": "perishable", 
#     "ginger": "perishable", 
#     "eggplant": "perishable", 
#     "zucchini": "perishable", 
#     "cabbage": "perishable", 
#     "radish": "perishable", 
#     "mushroom": "perishable", 
#     "peas": "perishable", 
#     "asparagus": "perishable", 
#     "okra": "perishable", 
#     "celery": "perishable", 
#     "beetroot": "perishable", 
#     "fennel": "perishable", 
#     "brussels sprouts": "perishable", 
#     "artichoke": "perishable", 
#     "turnip": "perishable", 
#     "parsnip": "perishable", 
#     "kale": "perishable", 
#     "swiss chard": "perishable", 
#     "bok choy": "perishable", 
#     "leek": "perishable", 
#     "scallion": "perishable", 
#     "apple": "perishable", 
#     "banana": "perishable", 
#     "orange": "perishable", 
#     "mango": "perishable", 
#     "pineapple": "perishable", 
#     "strawberry": "perishable", 
#     "blueberry": "perishable", 
#     "raspberry": "perishable", 
#     "blackberry": "perishable", 
#     "cranberry": "perishable", 
#     "avocado": "perishable", 
#     "watermelon": "perishable", 
#     "grape": "perishable", 
#     "papaya": "perishable", 
#     "cherry": "perishable", 
#     "pear": "perishable", 
#     "peach": "perishable", 
#     "pomegranate": "perishable", 
#     "kiwi": "perishable", 
#     "lemon": "perishable", 
#     "lime": "perishable", 
#     "plum": "perishable", 
#     "fig": "perishable", 
#     "apricot": "perishable", 
#     "coconut": "perishable", 
#     "lychee": "perishable", 
#     "guava": "perishable", 
#     "dragon fruit": "perishable", 
#     "persimmon": "perishable", 
#     "mulberry": "perishable", 
#     "starfruit": "perishable", 
#     "rice": "stable", 
#     "wheat": "stable", 
#     "oats": "stable", 
#     "quinoa": "stable", 
#     "barley": "stable", 
#     "corn": "stable", 
#     "millet": "stable", 
#     "rye": "stable", 
#     "buckwheat": "stable", 
#     "sorghum": "stable", 
#     "amaranth": "stable", 
#     "couscous": "stable", 
#     "farro": "stable", 
#     "bulgur": "stable", 
#     "wild rice": "stable", 
#     "teff": "stable", 
#     "lentils": "stable", 
#     "chickpeas": "stable", 
#     "kidney beans": "stable", 
#     "black beans": "stable", 
#     "green gram": "stable", 
#     "soybeans": "stable", 
#     "pinto beans": "stable", 
#     "white beans": "stable", 
#     "navy beans": "stable", 
#     "adzuki beans": "stable", 
#     "mung beans": "stable", 
#     "chicken": "perishable", 
#     "beef": "perishable", 
#     "pork": "perishable", 
#     "fish": "perishable", 
#     "salmon": "perishable", 
#     "tuna": "perishable", 
#     "shrimp": "perishable", 
#     "lobster": "perishable", 
#     "crab": "perishable", 
#     "mussels": "perishable", 
#     "clams": "perishable", 
#     "oysters": "perishable", 
#     "squid": "perishable", 
#     "octopus": "perishable", 
#     "duck": "perishable", 
#     "turkey": "perishable", 
#     "lamb": "perishable", 
#     "venison": "perishable", 
#     "rabbit": "perishable", 
#     "quail": "perishable", 
#     "goat meat": "perishable", 
#     "egg": "perishable", 
#     "milk": "perishable", 
#     "cheese": "perishable", 
#     "yogurt": "perishable", 
#     "butter": "perishable", 
#     "cream": "perishable", 
#     "sour cream": "perishable", 
#     "ghee": "perishable", 
#     "tofu": "perishable", 
#     "tempeh": "perishable", 
#     "paneer": "perishable", 
#     "cottage cheese": "perishable", 
#     "halloumi": "perishable", 
#     "mozzarella": "perishable", 
#     "cheddar": "perishable", 
#     "parmesan": "perishable", 
#     "feta": "perishable", 
#     "ricotta": "perishable"
# }

# def build_priority_queue():
#     pq = []
#     for ingredient in ingredients:
#         priority = 0 if FOOD_CATEGORIES.get(ingredient, "stable") == "perishable" else 1
#         heapq.heappush(pq, (priority, ingredient)) 
#     return pq
# if __name__ == "__main__":
    #print(build_priority_queue())
    # print(get_user_preferences(get_current_user()))
    #print(categorize_food(food_ingredients))