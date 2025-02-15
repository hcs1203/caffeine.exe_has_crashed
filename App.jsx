import React from "react";
import { NavigationContainer } from "@react-navigation/native";
import StackNavigator from "./app/navigation/StackNavigator";

export default function App() {
    return (
        <NavigationContainer>
            <StackNavigator />
        </NavigationContainer>
    );
}
