from imagescan import image_to_food
from categorise_food import categorise_food
from PIL import Image

image = Image.open("assets/images/maggi.jpg")
# This is the main app
def main():
    predicted_class = image_to_food(image)
    food_category = categorise_food(predicted_class)
    print(f"The food {predicted_class} is categorised as {food_category}")

__main__ = main()