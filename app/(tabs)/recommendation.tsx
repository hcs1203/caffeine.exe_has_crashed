import React from "react";
import { View, Text, Image, StyleSheet } from "react-native";
import { RouteProp } from "@react-navigation/native";
import { RootStackParamList } from "../navigation/types"; // Import the type

type RecommendationScreenProps = {
    route: RouteProp<RootStackParamList, "Recommendation">;
};

const RecommendationScreen: React.FC<RecommendationScreenProps> = ({ route }) => {
    const image = route?.params?.image || "";
    console.log("Received Image URI:", image);

    return (
        <View style={styles.container}>
            <Text style={styles.title}>Your Recommended Diet Plan</Text>

            {image ? (
                <Image source={{ uri: image }} style={styles.image} resizeMode="contain" />
            ) : (
                <Text style={styles.error}>No image available</Text>
            )}
        </View>
    );
};

export default RecommendationScreen;

const styles = StyleSheet.create({
    container: {
        flex: 1,
        justifyContent: "center",
        alignItems: "center",
        backgroundColor: "white",
        padding: 20,
    },
    title: {
        fontSize: 20,
        fontWeight: "bold",
        marginBottom: 20,
    },
    image: {
        width: "90%",
        height: 300,
        borderRadius: 10,
    },
    error: {
        fontSize: 16,
        color: "red",
    },
});
