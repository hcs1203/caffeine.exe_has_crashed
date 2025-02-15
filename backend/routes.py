from fastapi import APIRouter, UploadFile, File
from PIL import Image
from imagescan import image_to_food  # Function to classify food
from categorise_food import categorise_food  # Function to categorize food
from supabase_connection import SupabaseSingleton  # Supabase functions

# Create a router
router = APIRouter()

@router.post("/upload-image/")
async def upload_image(file: UploadFile = File(...)):
    """Receives an image, classifies it as food, determines perishable/stable, and stores it in Supabase."""
    
    # Open the image using PIL
    image = Image.open(file.file)

    # Convert the image into a food label (e.g., "Instant Noodles", "Milk")
    food_label = image_to_food(image)

    # Determine if the food is Perishable or Stable
    food_category = categorise_food(food_label)


    return {
        "message": "Image processed successfully",
        "food_label": food_label,
        "category": food_category
    }




