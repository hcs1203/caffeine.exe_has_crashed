import livescan  # Import your function
import io

# Load an image file
#with open("assets/images/broccoli.jpeg", "rb") as image_file:

    #image_bytes = image_file.read()
# Call the function
detected_ingredients = livescan.detect_ingredients("assets/images/broccoli.jpeg")

# Print the detected ingredients
print("Detected Ingredients:", detected_ingredients)