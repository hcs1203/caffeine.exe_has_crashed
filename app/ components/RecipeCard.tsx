import React from "react";
import { View, Text, StyleSheet } from "react-native";

type RecipeCardProps = {
    title: string;
    description: string;
    ingredients: string[];
};

const RecipeCard: React.FC<RecipeCardProps> = ({ title, description, ingredients }) => {
    return (
        <View style={styles.card}>
            <Text style={styles.title}>{title}</Text>
            <Text style={styles.description}>{description}</Text>
            <Text style={styles.ingredientsTitle}>Ingredients:</Text>
            <View style={styles.ingredientsList}>
                {ingredients.map((ingredient, index) => (
                    <Text key={index} style={styles.ingredient}>
                        - {ingredient}
                    </Text>
                ))}
            </View>
        </View>
    );
};

export default RecipeCard;

const styles = StyleSheet.create({
    card: {
        backgroundColor: "#fff",
        borderRadius: 10,
        marginBottom: 20,
        shadowColor: "#000",
        shadowOffset: { width: 0, height: 2 },
        shadowOpacity: 0.1,
        shadowRadius: 6,
        elevation: 3,
        padding: 15,
        width: "100%",
    },
    title: {
        fontSize: 18,
        fontWeight: "bold",
        marginTop: 10,
    },
    description: {
        fontSize: 14,
        color: "#666",
        marginTop: 5,
    },
    ingredientsTitle: {
        fontSize: 16,
        fontWeight: "bold",
        marginTop: 15,
    },
    ingredientsList: {
        marginTop: 10,
    },
    ingredient: {
        fontSize: 14,
        color: "#444",
    },
});
