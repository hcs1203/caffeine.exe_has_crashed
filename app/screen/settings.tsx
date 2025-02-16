import { View, Text, CheckBox, Button } from "react-native";
import React, { useEffect, useState } from "react";
import { useNavigation } from "@react-navigation/native"; 
import supabase from "../supabaseClient";

const SettingsScreen = () => {
    const [user, setUser] = useState(null);

    // State to manage dietary preferences
    const [dietaryPreferences, setDietaryPreferences] = useState({
        vegan: false,
        vegetarian: false,
        glutenFree: false,
        dairyFree: false,
        pescatarian: false,
    });

    const navigation = useNavigation(); // Get the navigation prop

    // Fetch current user on component mount
    useEffect(() => {
        const fetchUser = async () => {
            const currentUser = supabase.auth.user(); // Get current authenticated user
            setUser(currentUser);
        };

        fetchUser();
    }, []);

    // Function to handle changes in dietary preference checkboxes
    const handleDietaryChange = (preference) => {
        setDietaryPreferences((prevState) => ({
            ...prevState,
            [preference]: !prevState[preference],
        }));
    };

    // Save dietary preferences to Supabase
    const saveDietaryPreferences = async () => {
        if (user) {
            const preferencesArray = Object.keys(dietaryPreferences)
                .filter((key) => dietaryPreferences[key])
                .map((key) => key);

            // Insert preferences into Supabase
            const { data, error } = await supabase
                .from("dietary_preferences")
                .insert([
                    {
                        user_id: user.id, // Get the user's ID from the auth
                        preferences: preferencesArray,
                    },
                ]);

            if (error) {
                console.error("Error inserting dietary preferences:", error.message);
            } else {
                console.log("Dietary preferences saved:", data);
                alert("Dietary preferences saved successfully!");
            }
        }
    };

    return (
        <View style={{ padding: 20 }}>
            {/* Display Username if available */}
            {user ? (
                <Text>Welcome, {user.username || user.email}</Text>
            ) : (
                <Text>Loading...</Text>
            )}

            <Text style={{ fontSize: 18, marginVertical: 20 }}>Settings</Text>

            {/* Dietary Preferences Section */}
            <Text style={{ fontSize: 16, fontWeight: "bold", marginVertical: 10 }}>
                Dietary Preferences
            </Text>

            <View>
                {/* Vegan Preference */}
                <View style={{ flexDirection: "row", alignItems: "center", marginVertical: 5 }}>
                    <CheckBox
                        value={dietaryPreferences.vegan}
                        onValueChange={() => handleDietaryChange("vegan")}
                    />
                    <Text>Vegan</Text>
                </View>

                {/* Vegetarian Preference */}
                <View style={{ flexDirection: "row", alignItems: "center", marginVertical: 5 }}>
                    <CheckBox
                        value={dietaryPreferences.vegetarian}
                        onValueChange={() => handleDietaryChange("vegetarian")}
                    />
                    <Text>Vegetarian</Text>
                </View>

                {/* Gluten-Free Preference */}
                <View style={{ flexDirection: "row", alignItems: "center", marginVertical: 5 }}>
                    <CheckBox
                        value={dietaryPreferences.glutenFree}
                        onValueChange={() => handleDietaryChange("glutenFree")}
                    />
                    <Text>Gluten-Free</Text>
                </View>

                {/* Dairy-Free Preference */}
                <View style={{ flexDirection: "row", alignItems: "center", marginVertical: 5 }}>
                    <CheckBox
                        value={dietaryPreferences.dairyFree}
                        onValueChange={() => handleDietaryChange("dairyFree")}
                    />
                    <Text>Dairy-Free</Text>
                </View>

                {/* Pescatarian Preference */}
                <View style={{ flexDirection: "row", alignItems: "center", marginVertical: 5 }}>
                    <CheckBox
                        value={dietaryPreferences.pescatarian}
                        onValueChange={() => handleDietaryChange("pescatarian")}
                    />
                    <Text>Pescatarian</Text>
                </View>
            </View>

            {/* Save Button */}
            <Button title="Save Preferences" onPress={saveDietaryPreferences} />

            {/* Button to navigate to History */}
            <Button
                title="View History"
                onPress={() => navigation.navigate("History")}
            />
        </View>
    );
};

export default SettingsScreen;
