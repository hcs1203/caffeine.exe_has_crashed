import { View, Pressable, Text, ActivityIndicator, StyleSheet, Button } from "react-native";
import Checkbox from "expo-checkbox";
import React, { useEffect, useState } from "react";
import supabase from "../supabaseClient";

const HistoryScreen = () => {
    const [user, setUser] = useState<any>(null);
    const [dietaryPreferences, setDietaryPreferences] = useState({
        vegan: false,
        vegetarian: false,
        glutenFree: false,
        dairyFree: false,
        pescatarian: false,
    });
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        const fetchUser = async () => {
            const {
                data: { user },
                error,
            } = await supabase.auth.getUser();

            if (user) {
                setUser(user);
                fetchDietaryPreferences(user.id);
            } else {
                console.error("Error fetching user:", error?.message);
            }
        };

        const fetchDietaryPreferences = async (userId: string) => {
            const { data, error } = await supabase
                .from("dietary_preferences")
                .select("preferences")
                .eq("user_id", userId)
                .single();

            if (error) {
                console.error("Error fetching dietary preferences:", error.message);
            } else {
                const updatedPreferences = {
                    vegan: false,
                    vegetarian: false,
                    glutenFree: false,
                    dairyFree: false,
                    pescatarian: false,
                };

                if (data?.preferences) {
                    data.preferences.forEach((pref: string) => {
                        updatedPreferences[pref as keyof typeof updatedPreferences] = true;
                    });
                }

                setDietaryPreferences(updatedPreferences);
            }
            setLoading(false);
        };

        fetchUser();
    }, []);

    // Handle Checkbox Selection
    const handlePreferenceChange = (preference: keyof typeof dietaryPreferences) => {
        setDietaryPreferences((prev) => ({
            ...prev,
            [preference]: !prev[preference],
        }));
    };

    // Save Preferences to Supabase
    const saveDietaryPreferences = async () => {
        if (!user) return;
        const preferencesArray = Object.keys(dietaryPreferences).filter((key) => dietaryPreferences[key]);

        const { error } = await supabase.from("dietary_preferences").upsert([
            {
                user_id: user.id,
                preferences: preferencesArray,
            },
        ]);

        if (error) {
            console.error("Error saving preferences:", error.message);
            alert("Failed to save preferences.");
        } else {
            alert("Preferences updated successfully!");
        }
    };

    return (
        <View style={styles.container}>
            <Text style={styles.title}>Dietary Preferences</Text>

            {loading ? (
                <ActivityIndicator size="large" color="#6200EE" />
            ) : (
                <View style={styles.checkboxContainer}>
                    {(Object.keys(dietaryPreferences) as Array<keyof typeof dietaryPreferences>).map((pref) => (
                        <View key={pref} style={styles.preferenceRow}>
                            <Checkbox
                                style={styles.checkbox}
                                value={dietaryPreferences[pref]}
                                onValueChange={() => handlePreferenceChange(pref)}
                                color={dietaryPreferences[pref] ? "#6200EE" : undefined}
                            />
                            <Text style={styles.preferenceLabel}>{pref.charAt(0).toUpperCase() + pref.slice(1)}</Text>
                        </View>
                    ))}

                    <Pressable onPress={saveDietaryPreferences} style={styles.button}>
                        <Text style={{ color: "white" }}>Save prefrences</Text>
                    </Pressable>
                </View>
            )}
        </View>
    );
};

export default HistoryScreen;

const styles = StyleSheet.create({
    container: { flex: 1, justifyContent: "center", alignItems: "center", padding: 20 },
    title: { fontSize: 24, fontWeight: "bold", marginBottom: 20 },
    checkboxContainer: {},
    preferenceRow: { flexDirection: "row", alignItems: "center", marginVertical: 5 },
    preferenceLabel: { fontSize: 16, marginLeft: 10 },
    checkbox: { margin: 8 },
    button: {
        display: "flex",
        flexDirection: "row",
        justifyContent: "center",
        alignItems: "center",
        backgroundColor: "#6200EE",
        padding: 10,
        borderRadius: 5,
        marginTop: 10,
    },
});
