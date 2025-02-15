import React from "react";
import { createNativeStackNavigator } from "@react-navigation/native-stack";
import CameraScreen from "../screen/camera";
import RecommendationScreen from "../screen/recommendation";
import HistoryScreen from "../screen/history";
import LoginScreen from "../auth/login";
import SignupScreen from "../auth/signup";
import { BottomTabNavigator } from "./TabNavigator"; // 👈 Import Bottom Tabs

export type RootStackParamList = {
    Login: undefined;
    Signup: undefined;
    App: undefined;
};

const Stack = createNativeStackNavigator<RootStackParamList>();

const StackNavigator = () => {
    return (
        <Stack.Navigator screenOptions={{ headerShown: false }}>
            <Stack.Screen name="Login" component={LoginScreen} />
            <Stack.Screen name="Signup" component={SignupScreen} />
            <Stack.Screen name="App" component={BottomTabNavigator} />
        </Stack.Navigator>
    );
};

export default StackNavigator;
