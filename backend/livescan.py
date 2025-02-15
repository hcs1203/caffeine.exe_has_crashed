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
labels = [
    "broccoli", "maggi", "potato", "carrot", "onion", "tomato", "cucumber", "spinach", "lettuce", 
    "bell pepper", "cauliflower", "garlic", "ginger", "eggplant", "zucchini", "cabbage", "radish", 
    "mushroom", "peas", "asparagus", "apple", "banana", "orange", "mango", "pineapple", "strawberry", 
    "blueberry", "raspberry", "avocado", "watermelon", "grape", "papaya", "cherry", "pear", "peach", 
    "pomegranate", "kiwi", "lemon", "lime", "rice", "wheat", "oats", "quinoa", "barley", "corn", 
    "lentils", "chickpeas", "kidney beans", "black beans", "green gram", "soybeans", "chicken", "beef", 
    "pork", "fish", "salmon", "tuna", "shrimp", "egg", "milk", "cheese", "yogurt", "butter", "tofu", 
    "tempeh", "paneer", "salt", "pepper", "turmeric", "cumin", "coriander", "cardamom", "cinnamon", 
    "cloves", "nutmeg", "mustard seeds", "bay leaf", "basil", "oregano", "thyme", "rosemary", 
    "paprika", "chili powder", "olive oil", "vegetable oil", "butter", "vinegar", "soy sauce", 
    "ketchup", "mayonnaise", "mustard", "honey", "sugar", "bread", "pasta", "noodles", "cereal", 
    "chips", "chocolate", "biscuits", "cake", "ice cream"
]

# Step 6: Preprocess the Inputs
inputs = processor(text=labels, images=image, return_tensors="pt", padding=True)

# Step 7: Perform Zero-Shot Classification
outputs = model(**inputs)
logits_per_image = outputs.logits_per_image  # Similarity score
probs = logits_per_image.softmax(dim=1)      # Probability distribution

# Step 8: Get the Predicted Class
predicted_class = labels[probs.argmax()]
print(f"Predicted class: {predicted_class}")


    #ingredients = [label.description for label in labels if label.score > 0.6]

    #return ingredients

#file_name = "broccoli.jpeg"
#detect_ingredients(file_name)

