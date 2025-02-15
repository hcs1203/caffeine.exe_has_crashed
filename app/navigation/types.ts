import { NavigatorScreenParams } from "@react-navigation/native";
import { NativeStackScreenProps } from "@react-navigation/native-stack";
import { BottomTabScreenProps } from "@react-navigation/bottom-tabs";

/**
 * Type definition for the navigation stack.
 */
export type RootStackParamList = {
    Camera: undefined; // No params needed for Camera screen
    Recommendation: { image?: string }; // Pass `image` as a prop
    History: undefined;
    Login: undefined;
    Signup: undefined;
    App: NavigatorScreenParams<TabParamList>;
};

export type TabParamList = {
    Camera: undefined;
    Recommendation: { image?: string };
    History: undefined;
};

export type StackNavigationProps<T extends keyof RootStackParamList> = NativeStackScreenProps<RootStackParamList, T>;

export type TabNavigationProps<T extends keyof TabParamList> = BottomTabScreenProps<TabParamList, T>;
