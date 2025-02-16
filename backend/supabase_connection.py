import os
from supabase import create_client, Client
from dotenv import load_dotenv
import re
load_dotenv()  # Load environment variables

class SupabaseSingleton:
    _instance = None  # Store the single instance of Supabase Client

    @classmethod
    def get_instance(cls):
        """Returns a single instance of the Supabase client."""
        if cls._instance is None:
            url: str = os.getenv("SUPABASE_URL")
            key: str = os.getenv("SUPABASE_API_KEY")
            
            if not url or not key:
                raise ValueError("❌ Supabase URL or API key is missing! Check your .env file.")
            
            cls._instance = create_client(url, key)  # Initialize once
        
        return cls._instance

    @classmethod
    def insert_recipe_recommendation(cls, recipes_list):
        """Insert a row into the dietary_preferences table."""
        supabase = cls.get_instance()
        dish_names = []
        ingredients_list = []
        steps_list = []
        for i in range(len(recipes_list)):  
            #dish_names = []
            #ingredients_list = []
            #steps_list = []
            for dish in recipes_list:
                dish_name_match = re.search(r'\d+\.\sDish Name:\s(.+?)\s+Ingredients:', dish, re.DOTALL)
                dish_name = dish_name_match.group(1).strip() if dish_name_match else ""
                dish_names.append(dish_name)


                ingredients_match = re.search(r'Ingredients:\s(.+?)\s+Steps:', dish, re.DOTALL)
                ingredients = [ing.strip() for ing in ingredients_match.group(1).split(",")] if ingredients_match else []
                ingredients_list.append(ingredients)

                steps_match = re.search(r'Steps:\s+(.+)', dish, re.DOTALL)
                steps = [step.strip() for step in re.split(r'\d+\.\s', steps_match.group(1)) if step] if steps_match else []
                steps_list.append(steps)
        for i in range(len(dish_names)):
            response = supabase.table("recipe").insert({
                "recipe": dish_names[i], "ingredients": ingredients_list[i], "steps": steps_list[i][0]
            }).execute()
            print("Response:", response)
