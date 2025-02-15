import React, { useState } from "react";
import { View, Text, TextInput, TouchableOpacity, StyleSheet } from "react-native";
import { useNavigation } from "@react-navigation/native";
import { signIn } from "./authHelpers";
import { StackNavigationProp } from "@react-navigation/stack";
import { RootStackParamList } from "../navigation/types";

type Props = StackNavigationProp<RootStackParamList, "Login">;

const LoginScreen = () => {
    const navigation = useNavigation<Props>();

    const [email, setEmail] = useState("");

    const [password, setPassword] = useState("");

    async function handleLogin() {
        const user = await signIn(email, password);
        if (user) {
            alert("Login successful!");
            navigation.replace("App", { screen: "Camera" });
        }
    }

    return (
        <View style={styles.container}>
            <Text style={styles.title}>Log In</Text>
            <TextInput placeholder="Email" value={email} onChangeText={setEmail} style={styles.input} />
            <TextInput
                placeholder="Password"
                value={password}
                onChangeText={setPassword}
                secureTextEntry
                style={styles.input}
            />
            <TouchableOpacity onPress={handleLogin} style={styles.button}>
                <Text style={styles.buttonText}>Log In</Text>
            </TouchableOpacity>
            <TouchableOpacity onPress={() => navigation.navigate("Signup")}>
                <Text style={styles.switchText}>Don't have an account? Sign up</Text>
            </TouchableOpacity>
        </View>
    );
};

export default LoginScreen;

const styles = StyleSheet.create({
    container: { flex: 1, justifyContent: "center", alignItems: "center", padding: 20 },
    title: { fontSize: 24, fontWeight: "bold", marginBottom: 20 },
    input: { width: "100%", padding: 10, borderWidth: 1, borderRadius: 5, marginBottom: 10 },
    button: { backgroundColor: "#6200EE", padding: 10, borderRadius: 5, marginTop: 10 },
    buttonText: { color: "white", fontSize: 16 },
    switchText: { marginTop: 15, color: "#6200EE" },
});
