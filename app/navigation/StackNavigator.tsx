import React from "react";
import { createBottomTabNavigator } from "@react-navigation/bottom-tabs";
import { createStackNavigator } from "@react-navigation/stack";
// import { NavigationContainer } from "@react-navigation/native";
import CameraScreen from "../(tabs)/camera";
import RecommendationScreen from "../(tabs)/recommendation";
import HistoryScreen from "../(tabs)/history";
import LoginScreen from "../auth/login";
import SignupScreen from "../auth/signup";
import { MaterialIcons } from "@expo/vector-icons";
import { RootStackParamList } from "./types";

// ✅ Bottom Tab Navigator (App Pages)
const Tab = createBottomTabNavigator<RootStackParamList>();
const AppTabs = () => (
    <Tab.Navigator>
        <Tab.Screen
            name="Camera"
            component={CameraScreen}
            options={{
                title: "Scan",
                tabBarIcon: ({ color }) => <MaterialIcons size={28} name="camera" color={color} />,
            }}
        />
        <Tab.Screen
            name="Recommendation"
            component={RecommendationScreen}
            options={{
                title: "Recommendation",
                tabBarIcon: ({ color }) => <MaterialIcons size={28} name="recommend" color={color} />,
            }}
        />
        <Tab.Screen
            name="History"
            component={HistoryScreen}
            options={{
                title: "History",
                tabBarIcon: ({ color }) => <MaterialIcons size={28} name="history" color={color} />,
            }}
        />
    </Tab.Navigator>
);

// ✅ Stack Navigator (Manages Auth & App Navigation)
const Stack = createStackNavigator();

const StackNavigator = () => {
    return (
        <Stack.Navigator initialRouteName="Login">
            {/* 🔐 Authentication Screens */}
            <Stack.Screen name="Login" component={LoginScreen} options={{ headerShown: false }} />
            <Stack.Screen name="Signup" component={SignupScreen} options={{ headerShown: false }} />

            {/* 🚀 Main App (Bottom Tab Navigator) */}
            <Stack.Screen name="App" component={AppTabs} options={{ headerShown: false }} />
        </Stack.Navigator>
    );
};

export default StackNavigator;
