import React from "react";
import { createBottomTabNavigator } from "@react-navigation/bottom-tabs";
import CameraScreen from "../screen/camera";
import RecommendationScreen from "../screen/recommendation";
import HistoryScreen from "../screen/history";

import SettingsScreen from "../screen/settings";

import { MaterialIcons } from "@expo/vector-icons";

export type TabParamList = {
    Camera: undefined;
    Recommendation: { image?: string };
    History: undefined;
    // Settings: undefined;
};

const Tab = createBottomTabNavigator<TabParamList>();

export const BottomTabNavigator = () => {
    return (
        <Tab.Navigator screenOptions={{ headerShown: false }}>
            <Tab.Screen
                name="Camera"
                component={CameraScreen}
                options={{
                    title: "Scan",
                    tabBarIcon: ({ color, size }) => <MaterialIcons name="camera" size={size} color={color} />,
                }}
            />
            <Tab.Screen
                name="Recommendation"
                component={RecommendationScreen}
                options={{
                    title: "Recommendation",
                    tabBarIcon: ({ color, size }) => <MaterialIcons name="recommend" size={size} color={color} />,
                }}
            />
            <Tab.Screen
                name="History"
                component={HistoryScreen}
                options={{
                    title: "Settings",
                    tabBarIcon: ({ color, size }) => <MaterialIcons name="settings" size={size} color={color} />,
                }}
            />

        </Tab.Navigator>
    );
};
