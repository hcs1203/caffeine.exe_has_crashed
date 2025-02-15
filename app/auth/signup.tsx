import React, { useState } from "react";
import { View, Text, TextInput, TouchableOpacity, StyleSheet } from "react-native";
import { signUp } from "./authHelpers";
import { RootStackParamList, StackNavigationProps } from "../navigation/types";
import { NativeStackScreenProps } from "@react-navigation/native-stack";

type Props = NativeStackScreenProps<RootStackParamList, "Signup">;

const SignupScreen = ({ navigation }: Props) => {
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");

    async function handleSignup() {
        const user = await signUp(email, password);
        if (user) {
            alert("Sign-up successful! Please log in.");
            navigation.navigate("Login"); // ✅ Redirect to Login
        }
    }

    return (
        <View style={styles.container}>
            <Text style={styles.title}>Sign Up</Text>
            <TextInput placeholder="Email" value={email} onChangeText={setEmail} style={styles.input} />
            <TextInput
                placeholder="Password"
                value={password}
                onChangeText={setPassword}
                secureTextEntry
                style={styles.input}
            />
            <TouchableOpacity onPress={handleSignup} style={styles.button}>
                <Text style={styles.buttonText}>Sign Up</Text>
            </TouchableOpacity>
            <TouchableOpacity onPress={() => navigation.navigate("Login")}>
                <Text style={styles.switchText}>Already have an account? Log in</Text>
            </TouchableOpacity>
        </View>
    );
};

export default SignupScreen;

const styles = StyleSheet.create({
    container: { flex: 1, justifyContent: "center", alignItems: "center", padding: 20 },
    title: { fontSize: 24, fontWeight: "bold", marginBottom: 20 },
    input: { width: "100%", padding: 10, borderWidth: 1, borderRadius: 5, marginBottom: 10 },
    button: { backgroundColor: "#6200EE", padding: 10, borderRadius: 5, marginTop: 10 },
    buttonText: { color: "white", fontSize: 16 },
    switchText: { marginTop: 15, color: "#6200EE" },
});
