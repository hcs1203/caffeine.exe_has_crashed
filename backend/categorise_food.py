from api import client

def categorize_food(food_name):
    # use openai gpt models to categorise food
    prompt = f"There are 2 categories of food, perishable and stable, please categorise the food {food_name} accordingly according to its natural and storage properties. Return only the category of the food."

    completion = client.chat.completions.create(
        model="gpt-4o",
        store=True,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return completion.choices[0].message.content

if __name__ == "__main__":
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

    for food_ingredient in food_ingredients:
        print(f"{food_ingredient}: {categorize_food(food_ingredient)}")
