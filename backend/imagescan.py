import torch
from transformers import CLIPProcessor, CLIPModel
import torch
model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")

#labels = ["perishable", "stable"]
labels = [
    "broccoli", "instant noodles", "potato", "carrot", "onion", "tomato", "cucumber", "spinach", "lettuce", "date",
    "bell pepper", "cauliflower", "garlic", "ginger", "eggplant", "zucchini", "cabbage", "radish", 
    "mushroom", "peas", "asparagus", "okra", "celery", "beetroot", "fennel", "brussels sprouts",
    "artichoke", "turnip", "parsnip", "kale", "swiss chard", "bok choy", "leek", "scallion",
    "apple", "banana", "orange", "mango", "pineapple", "strawberry", "blueberry", "raspberry", 
    "blackberry", "cranberry", "avocado", "watermelon", "grape", "papaya", "cherry", "pear", 
    "peach", "pomegranate", "kiwi", "lemon", "lime", "plum", "fig", "apricot", "coconut", 
    "lychee", "guava", "dragon fruit", "persimmon", "mulberry", "starfruit",
    "rice", "wheat", "oats", "quinoa", "barley", "corn", "millet", "rye", "buckwheat",
    "sorghum", "amaranth", "couscous", "farro", "bulgur", "wild rice", "teff",
    "lentils", "chickpeas", "kidney beans", "black beans", "green gram", "soybeans", 
    "pinto beans", "white beans", "navy beans", "adzuki beans", "mung beans",
    "chicken", "beef", "pork", "fish", "salmon", "tuna", "shrimp", "lobster", "crab",
    "mussels", "clams", "oysters", "squid", "octopus", "duck", "turkey", "lamb", 
    "venison", "rabbit", "quail", "goat meat",
    "egg", "milk", "cheese", "yogurt", "butter", "cream", "sour cream", "ghee",
    "tofu", "tempeh", "paneer", "cottage cheese", "halloumi", "mozzarella", "cheddar",
    "parmesan", "feta", "ricotta",
    "salt", "pepper", "turmeric", "cumin", "coriander", "cardamom", "cinnamon", "cloves", 
    "nutmeg", "mustard seeds", "bay leaf", "basil", "oregano", "thyme", "rosemary", 
    "paprika", "chili powder", "cayenne", "saffron", "tarragon", "dill", "chives",
    "star anise", "fenugreek", "lemongrass", "sumac", "caraway", "marjoram",
    "olive oil", "vegetable oil", "butter", "vinegar", "balsamic vinegar", "red wine vinegar",
    "soy sauce", "ketchup", "mayonnaise", "mustard", "honey", "sugar", "maple syrup",
    "molasses", "coconut oil", "sesame oil", "peanut oil", "avocado oil", "ghee",
    "bread", "pasta", "noodles", "cereal", "oatmeal", "granola", "pita", "tortilla", 
    "baguette", "croissant", "donut", "muffin", "biscotti", "sourdough", "focaccia",
    "chips", "chocolate", "biscuits", "cake", "ice cream", "brownies", "cookies", "candy",
    "pudding", "popcorn", "marshmallow", "pretzels", "crackers", "cheesecake", "pastry",
    "coffee", "tea", "green tea", "black tea", "herbal tea", "matcha", "chai", "cocoa powder",
    "hot chocolate", "energy drink", "soda", "lemonade", "smoothie", "milkshake", "kombucha",
    "wine", "beer", "whiskey", "vodka", "rum", "gin", "tequila", "brandy", "cider", "sake",
    "peanut butter", "jam", "jelly", "marmalade", "tahini", "almond butter", "hazelnut spread",
    "cream cheese", "hummus", "guacamole", "salsa", "pesto", "barbecue sauce", "soybean paste",
    "fish sauce", "hoisin sauce", "wasabi", "horseradish",
    "yogurt drink", "kefir", "buttermilk", "coconut milk", "almond milk", "soy milk",
    "oat milk", "rice milk", "cashew milk", "macadamia milk",
    "tofu skin", "seitan", "jackfruit", "textured vegetable protein", "miso", "natto",
    "seaweed", "nori", "wakame", "kelp", "dulse", "spirulina", "chlorella",
    "caviar", "anchovies", "sardines", "eel", "tilapia", "haddock", "halibut", "trout", "cod",
    "miso paste", "kimchi", "sauerkraut", "pickles", "fermented black beans",
    "chili flakes", "coconut flakes", "dried fruits", "raisins", "prunes",
    "cranberries", "goji berries", "apricots",
    "tamarind", "yuzu", "lotus root", "edamame", "wasabi peas",
    "plantain", "cassava", "taro", "yam", "sweet potato", "jicama",
    "gelatin", "agar-agar", "xanthan gum", "guar gum", "cornstarch", "potato starch", "arrowroot powder",
    "vanilla extract", "almond extract", "rose water", "orange blossom water",
    "safflower oil", "grapeseed oil", "walnut oil", "hazelnut oil", "pumpkin seed oil",
    "vegemite", "marmite", "nutritional yeast", "tempeh bacon",
    "beef jerky", "salami", "prosciutto", "chorizo", "bacon",
    "flaxseeds", "chia seeds", "hemp seeds", "sunflower seeds", "pumpkin seeds", "poppy seeds",
    "cashews", "almonds", "walnuts", "pecans", "hazelnuts", "macadamia nuts", "brazil nuts", "pistachios",
    "cottage cheese", "creme fraiche", "mascarpone", "gorgonzola", "brie", "camembert"
]
def image_to_food(image):
    inputs = processor(text=labels, images=image, return_tensors="pt", padding=True)
    outputs = model(**inputs)
    logits_per_image = outputs.logits_per_image
    probs = logits_per_image.softmax(dim=1)

    predicted_class = labels[probs.argmax()]
    #print(f"Predicted class: {predicted_class}")
    return predicted_class