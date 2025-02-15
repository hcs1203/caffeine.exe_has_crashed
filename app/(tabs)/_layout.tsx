import { Tabs } from "expo-router";
import React from "react";
import { Platform } from "react-native";

import { HapticTab } from "@/components/HapticTab";
import { MaterialIcons } from "@expo/vector-icons";
import TabBarBackground from "@/components/ui/TabBarBackground";
import { Colors } from "@/constants/Colors";
import { useColorScheme } from "@/hooks/useColorScheme";

export default function TabLayout() {
    const colorScheme = useColorScheme();

    return (
        <Tabs
            screenOptions={{
                tabBarActiveTintColor: Colors[colorScheme ?? "light"].tint,
                headerShown: false,
                tabBarButton: HapticTab,
                tabBarBackground: TabBarBackground,
                tabBarStyle: Platform.select({
                    ios: {
                        // Use a transparent background on iOS to show the blur effect
                        position: "absolute",
                    },
                    default: {},
                }),
            }}
        >
            <Tabs.Screen
                name="index"
                options={{
                    title: "Home",
                    tabBarIcon: ({ color }) => <MaterialIcons size={28} name="house" color={color} />,
                }}
            />
            <Tabs.Screen
                name="camera"
                options={{
                    title: "Scan",
                    tabBarIcon: ({ color }) => <MaterialIcons size={28} name="camera" color={color} />,
                }}
            />
            <Tabs.Screen
                name="recommendation"
                options={{
                    title: "Recommendations",
                    tabBarIcon: ({ color }) => <MaterialIcons size={28} name="recommend" color={color} />,
                }}
            />
        </Tabs>
    );
}
