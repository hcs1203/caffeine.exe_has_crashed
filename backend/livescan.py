import torch
from transformers import CLIPProcessor, CLIPModel
from PIL import Image
import torch
#pip install transformers torch pillow
# Step 3: Load the Pre-trained CLIP Model
model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")

# Step 4: Upload an Image (We used Colab's upload feature or provide a path)
image = Image.open("/Users/riyamehta_2211/Desktop/caffeine.exe_has_crashed/assets/images/maggi.jpg")


# Step 5: Define Class Labels (Text descriptions)
#labels = ["perishable", "stable"]
food_ingredients = [
    "Milk", "Cheese", "Yogurt", "Butter", "Cream", "Sour Cream", "Eggs", "Ice Cream",
    "Apple", "Banana", "Orange", "Strawberry", "Blueberry", "Pineapple", "Mango", "Grapes", "Watermelon",
    "Tomato", "Carrot", "Spinach", "Lettuce", "Broccoli", "Garlic", "Onion", "Bell Pepper", "Potato",
    "Chicken", "Beef", "Pork", "Lamb", "Turkey", "Duck", "Fish", "Salmon", "Tuna", "Shrimp", "Crab", "Lobster",
    "Rice", "Wheat Flour", "Oats", "Pasta", "Quinoa", "Barley", "Cornmeal", "Bread", "Tortilla",
    "Lentils", "Chickpeas", "Black Beans", "Kidney Beans", "Peas", "Soybeans", "Tofu",
    "Almonds", "Peanuts", "Cashews", "Walnuts", "Hazelnuts", "Chia Seeds", "Flaxseeds", "Sunflower Seeds",
    "Olive Oil", "Vegetable Oil", "Coconut Oil", "Butter", "Ghee",
    "White Sugar", "Brown Sugar", "Honey", "Maple Syrup", "Molasses",
    "Baking Powder", "Baking Soda", "Yeast", "Cornstarch", "Cocoa Powder", "Vanilla Extract",
    "Canned Beans", "Canned Tomatoes", "Pickles", "Peanut Butter", "Jam", "Coconut Milk",
    "Ketchup", "Mustard", "Soy Sauce", "Vinegar", "Mayonnaise", "Salad Dressing", "Hot Sauce",
    "Frozen Peas", "Frozen Chicken", "Frozen Pizza", "Frozen Shrimp", "Frozen Berries",
    "Juice", "Coffee", "Tea", "Soda", "Wine", "Beer",
    "Salt", "Pepper", "Cinnamon", "Basil", "Oregano", "Cumin", "Nutmeg", "Turmeric",
    "Instant Noodles", "Granola", "Cereal", "Pasta Sauce", "Energy Bar"
]
# Step 6: Preprocess the Inputs
inputs = processor(text=food_ingredients, images=image, return_tensors="pt", padding=True)

# Step 7: Perform Zero-Shot Classification
outputs = model(**inputs)
logits_per_image = outputs.logits_per_image  # Similarity score
probs = logits_per_image.softmax(dim=1)      # Probability distribution

# Step 8: Get the Predicted Class
predicted_class = food_ingredients[probs.argmax()]
print(f"Predicted class: {predicted_class}")


    #ingredients = [label.description for label in labels if label.score > 0.6]

    #return ingredients

#file_name = "broccoli.jpeg"
#detect_ingredients(file_name)

