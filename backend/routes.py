# from fastapi import APIRouter, UploadFile, File
# from PIL import Image
# import os
# from detect_food import image_to_food  # Function to classify food
# # from categorise_food import categorise_food  # Function to categorize food
# from prioritize_food import prioritize_food  # Function to prioritize food
# from generate_menu import generate_menus  # Function to generate menus
# from constant import FOOD_CATEGORIES  # Dictionary of food categories
# from supabase_connection import SupabaseSingleton  # Supabase functions


# # Get the directory of the current script
# script_dir = os.path.dirname(os.path.abspath(__file__))

# # Correctly construct the path to the image in the root 'assets/images' folder
# image_filename = 'broccoli.jpeg'
# image_path = os.path.join(script_dir, '..', 'assets', 'images', image_filename)

# # Normalize the path
# image_path = os.path.abspath(image_path)

# # Create a router
# router = APIRouter()

# @router.post("/upload-image/")
# async def upload_image(file: UploadFile = File(...)):
#     """Receives an image, classifies it as food, determines perishable/stable, and stores it in Supabase."""
    
#     # Open the image using PIL
#     image = Image.open(file.file)

#     # Convert the image into a food label (e.g., "Instant Noodles", "Milk")
#     food_label = image_to_food(image)
#     print(f"Food Label: {food_label}")

#     # # Determine if the food is Perishable or Stable
#     # food_category = categorise_food(food_label)
#     # Look up the category from the FOOD_CATEGORIES dictionary
#     food_category = FOOD_CATEGORIES.get(food_label.lower(), "Unknown")  # Default to "Unknown" if not found
#     print(f"Food Category: {food_category}")

#     if food_category == "Unknown":
#         return {"message": f"Food category for '{food_label}' not found in the database."}

#     prioritized_food = prioritize_food(food_label, food_category)
#     print(f"Prioritized Food: {prioritized_food}")

#     generate_menu = generate_menus(prioritized_food)
#     print(f"Generated Menu: {generate_menu}")

#     return {
#         "message": "Image processed successfully",
#         "food_label": food_label,
#         "category": food_category,
#         "prioritized_food": prioritized_food,
#         "generate_menu": generate_menu
#     }


# # Route for testing with predefined image
# if os.path.exists(image_path):
#     # Load the image
#     image = Image.open(image_path)

#     # Get prediction
#     predicted_food = image_to_food(image)
#     print(f"Predicted Food: {predicted_food}")

#     # Get food category
#     food_category = FOOD_CATEGORIES.get(predicted_food.lower(), "Unknown")
#     print(f"Food Category: {food_category}")
# else:
#     print(f"Image not found: {image_path}")



from fastapi import APIRouter, UploadFile, File
from PIL import Image
import os
from detect_food import image_to_food  # Function to classify food
from prioritize_food import prioritize_food  # Function to prioritize food
from generate_menu import generate_menus # Function to generate menus
from constant import FOOD_CATEGORIES  # Dictionary of food categories
from supabase_connection import SupabaseSingleton  # Supabase functions

# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Correctly construct the path to the image in the root 'assets/images' folder
image_filename = 'broccoli.jpeg'
image_path = os.path.join(script_dir, '..', 'assets', 'images', image_filename)

# Normalize the path
image_path = os.path.abspath(image_path)

# Create a router
router = APIRouter()

@router.post("/upload-image/")
async def upload_image(file: UploadFile = File(...)):
    """Receives an image, classifies it as food, determines perishable/stable, and stores it in Supabase."""
    
    # Open the image using PIL
    image = Image.open(file.file)

    # Convert the image into a food label (e.g., "Instant Noodles", "Milk")
    food_label = image_to_food(image)
    print(f"Food Label: {food_label}")

    # Look up the category from the FOOD_CATEGORIES dictionary
    food_category = FOOD_CATEGORIES.get(food_label.lower(), "Unknown")  # Default to "Unknown" if not found
    print(f"Food Category: {food_category}")

    if food_category == "Unknown":
        return {"message": f"Food category for '{food_label}' not found in the database."}

    # Call prioritize_food to determine priority of the food
    prioritized_food = prioritize_food(food_label, food_category)
    print(f"Prioritized Food: {prioritized_food}")

    # Generate the menu based on the prioritized food
    generate_menu = generate_menus(prioritized_food) 
    print(f"Generated Menu: {generate_menu}")

    return {
        "message": "Image processed successfully",
        "food_label": food_label,
        "category": food_category,
        "prioritized_food": prioritized_food,
        "generate_menu": generate_menu
    }

# Route for testing with predefined image
if os.path.exists(image_path):
    # Load the image
    image = Image.open(image_path)

    # Get prediction
    predicted_food = image_to_food(image)
    print(f"Predicted Food: {predicted_food}")

    # Get food category
    food_category = FOOD_CATEGORIES.get(predicted_food.lower(), "Unknown")
    print(f"Food Category: {food_category}")

    # Proceed to prioritize food
    prioritized_food = prioritize_food(predicted_food, food_category)
    print(f"Prioritized Food: {prioritized_food}")

    # Generate menu
    generate_menu = generate_menus(prioritized_food)
    print(f"Generated Menu: {generate_menu}")

else:
    print(f"Image not found: {image_path}")









