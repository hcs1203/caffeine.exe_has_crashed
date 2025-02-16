from api import client
from supabase_connection import SupabaseSingleton  # Import the Singleton

# Get the Supabase client from the Singleton
supabase = SupabaseSingleton.get_instance()
def generate_menus(ingredients):
    # Generate the prompt to ask OpenAI to generate dish names with clear recipes
    prompt = f"""
    Based on the following ingredients, generate 5 unique dish names with their full recipes:

    Ingredients: {', '.join(ingredients)}

    For each dish, provide:
    - Dish Name
    - Full Recipe with ingredients and steps

    Example format:
    1. Dish Name: 
       Ingredients: [List of ingredients]
       Steps: [Step-by-step cooking instructions]
    2. Dish Name: 
       Ingredients: [List of ingredients]
       Steps: [Step-by-step cooking instructions]
    """

    # Make the API call to OpenAI to generate dish names with full recipes
    completion = client.chat.completions.create(
        model="gpt-4",  # Correct model version
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.7
    )

    # Extract dish names and recipes from the OpenAI response
    response_message = completion.choices[0].message.content.strip()

    # Return the list of dish names with recipes
    return response_message.split("\n")
