import React, { useState } from "react";
import {
    View,
    Text,
    TextInput,
    StyleSheet,
    KeyboardAvoidingView,
    ScrollView,
    Platform,
    TouchableOpacity,
    ActivityIndicator,
} from "react-native";
import { NativeStackScreenProps } from "@react-navigation/native-stack";
import  supabase  from "../supabaseClient"; 
import { RootStackParamList } from "../navigation/types";

type Props = NativeStackScreenProps<RootStackParamList, "Signup">;

const SignupScreen = ({ navigation }: Props) => {
    const [username, setUsername] = useState("");
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");
    const [loading, setLoading] = useState(false);

    async function handleSignup() {
        if (!username || !email || !password) {
            alert("All fields are required.");
            return;
        }

        setLoading(true);

        try {
            // Sign up the user with Supabase Auth
            const { data, error } = await supabase.auth.signUp({
                email,
                password,
            });

            if (error) throw error;
            if (!data.user) throw new Error("User creation failed.");

            // Save user ID & username to Supabase Database
            const { error: dbError } = await supabase
                .from("users") // Ensure this matches your table name
                .insert([{ id: data.user.id, username }]);

            if (dbError) throw dbError;

            alert("Sign-up successful! Please log in.");
            navigation.navigate("Login");
        } catch (error: any) {
            alert(error.message || "Sign-up failed.");
        } finally {
            setLoading(false);
        }
    }

    return (
        <KeyboardAvoidingView behavior={Platform.OS === "ios" ? "padding" : "height"} style={styles.container}>
            <ScrollView contentContainerStyle={styles.scrollContainer}>
                <View style={styles.innerContainer}>
                    <Text style={styles.title}>Sign Up</Text>

                    <TextInput
                        placeholder="Username"
                        placeholderTextColor="#888"
                        value={username}
                        onChangeText={setUsername}
                        style={styles.input}
                        autoCapitalize="none"
                    />
                    <TextInput
                        placeholder="Email"
                        placeholderTextColor="#888"
                        value={email}
                        onChangeText={(text) => setEmail(text.toLowerCase())}
                        style={styles.input}
                        keyboardType="email-address"
                        autoCapitalize="none"
                    />
                    <TextInput
                        placeholder="Password"
                        placeholderTextColor="#888"
                        value={password}
                        onChangeText={setPassword}
                        secureTextEntry
                        style={styles.input}
                    />

                    <TouchableOpacity onPress={handleSignup} style={styles.button} disabled={loading}>
                        {loading ? <ActivityIndicator color="white" /> : <Text style={styles.buttonText}>Sign Up</Text>}
                    </TouchableOpacity>

                    <TouchableOpacity onPress={() => navigation.navigate("Login")}>
                        <Text style={styles.switchText}>Already have an account? Log in</Text>
                    </TouchableOpacity>
                </View>
            </ScrollView>
        </KeyboardAvoidingView>
    );
};

export default SignupScreen;

const styles = StyleSheet.create({
    container: { flex: 1 },
    scrollContainer: { flexGrow: 1, justifyContent: "center", alignItems: "center", padding: 20 },
    innerContainer: { width: "100%", maxWidth: 400 },
    title: { fontSize: 24, fontWeight: "bold", marginBottom: 20, textAlign: "center" },
    input: { width: "100%", padding: 12, borderWidth: 1, borderRadius: 5, marginBottom: 10, borderColor: "#ccc" },
    button: { backgroundColor: "#6200EE", padding: 12, borderRadius: 5, alignItems: "center", marginTop: 10 },
    buttonText: { color: "white", fontSize: 16, fontWeight: "bold" },
    switchText: { marginTop: 15, color: "#6200EE", textAlign: "center" },
});
