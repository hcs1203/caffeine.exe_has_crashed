import React, { useEffect, useState } from "react";
import { View, Text, Image, StyleSheet, ActivityIndicator, ScrollView } from "react-native";
import { RouteProp } from "@react-navigation/native";
import { RootStackParamList } from "../navigation/types";
import supabase from "../supabaseClient";
import { SafeAreaView } from "react-native-safe-area-context";

type RecommendationScreenProps = {
    route: RouteProp<RootStackParamList, "Recommendation">;
};

const RecommendationScreen: React.FC<RecommendationScreenProps> = ({ route }) => {
    const image = route?.params?.image || "";
    const [recipe, setRecipe] = useState<{
        recipe: string;
        ingredients: string[];
        steps: string[];
    } | null>(null);
    const [loading, setLoading] = useState(false);
    const [isTakingPhoto, setIsTakingPhoto] = useState(image !== ""); // Show loading when taking a photo

    useEffect(() => {
        const fetchRecipe = async () => {
            if (!image) return;

            try {
                setLoading(true);
                let { data, error } = await supabase
                    .from("recipe")
                    .select("recipe, ingredients, steps")
                    .order("id", { ascending: false }) // Get the latest recipe
                    .limit(1)
                    .single();

                if (error) {
                    console.error("Error fetching recipe:", error.message);
                    setRecipe(null);
                } else {
                    if (data) {
                        setRecipe({
                            recipe: data.recipe,
                            ingredients: data.ingredients
                                ? data.ingredients
                                      .split(/",\s*"/)
                                      .map((item: string) => item.replace(/[\[\]"]+/g, "").trim()) // Splitting string into an array
                                : [],
                            steps: data.steps
                                ? data.steps.split(/-\s+/).map((item: string) => item.trim()) // Splitting steps on `-`
                                : [],
                        });
                    } else {
                        setRecipe(null);
                    }
                }
            } catch (error) {
                console.error("Unexpected error:", error);
                setRecipe(null);
            } finally {
                setLoading(false);
            }
        };

        fetchRecipe();
    }, [image]);

    return (
        <ScrollView style={styles.container}>
            <SafeAreaView>
                <Text style={styles.title}>Your Recommended Diet Plan</Text>

                {image ? (
                    <Image source={{ uri: image }} style={styles.image} resizeMode="contain" />
                ) : (
                    <Text style={styles.error}>No image available</Text>
                )}

                {isTakingPhoto ? (
                    <ActivityIndicator size="large" color="#6200EE" style={styles.loadingIndicator} />
                ) : loading ? (
                    <ActivityIndicator size="large" color="#6200EE" style={styles.loadingIndicator} />
                ) : recipe ? (
                    <View style={styles.recipeContainer}>
                        <Text style={styles.recipeTitle}>{recipe.recipe}</Text>
                        <Text style={styles.sectionTitle}>Ingredients</Text>
                        {recipe.ingredients.length > 0 ? (
                            recipe.ingredients.map((ingredient, index) => (
                                <Text key={index} style={styles.ingredientItem}>
                                    • {ingredient}
                                </Text>
                            ))
                        ) : (
                            <Text style={styles.error}>No ingredients available</Text>
                        )}

                        <Text style={styles.sectionTitle}>Steps</Text>
                        {recipe.steps.length > 0 ? (
                            recipe.steps.map((step, index) => (
                                <Text key={index} style={styles.stepItem}>
                                    {index + 1}. {step}
                                </Text>
                            ))
                        ) : (
                            <Text style={styles.error}>No steps available</Text>
                        )}
                    </View>
                ) : (
                    <Text style={styles.error}>No recipe available</Text>
                )}
            </SafeAreaView>
        </ScrollView>
    );
};

export default RecommendationScreen;

const styles = StyleSheet.create({
    container: {
        flex: 1,
        backgroundColor: "white",
        padding: 20,
    },
    title: {
        fontSize: 20,
        fontWeight: "bold",
        textAlign: "center",
        marginBottom: 20,
    },
    image: {
        width: "90%",
        height: 300,
        borderRadius: 10,
        alignSelf: "center",
        marginBottom: 20,
    },
    loadingIndicator: {
        marginTop: 20,
    },
    recipeContainer: {
        backgroundColor: "#F3F3F3",
        padding: 15,
        borderRadius: 10,
        marginTop: 20,
    },
    recipeTitle: {
        fontSize: 22,
        fontWeight: "bold",
        marginBottom: 10,
        textAlign: "center",
    },
    sectionTitle: {
        fontSize: 18,
        fontWeight: "bold",
        marginTop: 15,
    },
    ingredientItem: {
        fontSize: 16,
        marginLeft: 10,
    },
    stepItem: {
        fontSize: 16,
        marginLeft: 10,
        marginTop: 5,
    },
    error: {
        fontSize: 16,
        color: "red",
        textAlign: "center",
    },
});
