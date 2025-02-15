from api import client

# Example format: (works, faster)
    # 1. Dish Name: 

# def generate_menus(ingredients):
#     # Generate the prompt to ask OpenAI to generate dish names based on ingredients
#     prompt = f"Based on the following ingredients, generate 5 unique dish names:\n\n{', '.join(ingredients)}\n\nDish Names:"

#     # Make the API call to OpenAI to generate dish names
#     completion = client.chat.completions.create(
#         model="gpt-4",  # Correct model version (you had "gpt-4o", which is invalid)
#         messages=[
#             {
#                 "role": "user",
#                 "content": prompt
#             }
#         ],
#         temperature=0.7
#     )

#     # Extract dish names from the OpenAI response
#     response_message = completion.choices[0].message.content.strip()

#     # Return the list of dish names (splitting by newlines)
#     return response_message.split("\n")


# Example format: (works, slower)
    # 1. Dish Name: 
    #    Ingredients: [List of ingredients]
    #    Steps: [Step-by-step cooking instructions]

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
