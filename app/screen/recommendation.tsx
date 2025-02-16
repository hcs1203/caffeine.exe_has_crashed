import React, { useState, useEffect } from "react";
import { View, Text, ScrollView, StyleSheet, TouchableOpacity } from "react-native";
import supabase from "../supabaseClient"; // Import Supabase client
import RecipeCard from "../components/RecipeCard"; // Assuming RecipeCard is in the components folder

type Recipe = {
    id: number;
    recipe: string;
    ingredients: string;
    steps: string;
};

const RecommendationScreen: React.FC = () => {
    const [recipes, setRecipes] = useState<Recipe[]>([]);
    const [selectedRecipe, setSelectedRecipe] = useState<Recipe | null>(null);

    useEffect(() => {
        // Fetch recipes from Supabase
        const fetchRecipes = async () => {
            try {
                const { data, error } = await supabase
                    .from("recipe")
                    .select("id, recipe, ingredients, steps");

                if (error) {
                    console.error("Error fetching recipes:", error);
                } else {
                    setRecipes(data);
                }
            } catch (error) {
                console.error("Error fetching data:", error);
            }
        };

        fetchRecipes();
    }, []);

    const handleCardClick = (recipe: Recipe) => {
        if (selectedRecipe?.id === recipe.id) {
            setSelectedRecipe(null); // Close the card if clicked again
        } else {
            setSelectedRecipe(recipe); // Open the clicked recipe card
        }
    };

    return (
        <View style={styles.container}>
            <Text style={styles.title}>Your Recommended Diet Plan</Text>
            <ScrollView contentContainerStyle={styles.scrollContainer}>
                {recipes.map((recipe) => (
                    <TouchableOpacity key={recipe.id} onPress={() => handleCardClick(recipe)}>
                        <RecipeCard
                            title={recipe.recipe}
                            description={`Ingredients: ${recipe.ingredients}`}
                            ingredients={recipe.ingredients.split(",")}
                        />
                        {selectedRecipe?.id === recipe.id && (
                            <View style={styles.stepsContainer}>
                                <Text style={styles.stepsTitle}>Cooking Steps:</Text>
                                <Text style={styles.steps}>{recipe.steps}</Text>
                            </View>
                        )}
                    </TouchableOpacity>
                ))}
            </ScrollView>
        </View>
    );
};

const styles = StyleSheet.create({
    container: {
        flex: 1,
        backgroundColor: "white",
        padding: 20,
    },
    title: {
        fontSize: 24,
        fontWeight: "bold",
        marginBottom: 20,
    },
    scrollContainer: {
        paddingBottom: 20,
    },
    stepsContainer: {
        marginTop: 15,
        padding: 10,
        backgroundColor: "#f8f8f8",
        borderRadius: 10,
    },
    stepsTitle: {
        fontSize: 18,
        fontWeight: "bold",
    },
    steps: {
        fontSize: 14,
        color: "#333",
        marginTop: 5,
    },
});

export default RecommendationScreen;
