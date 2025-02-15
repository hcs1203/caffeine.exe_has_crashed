import { Camera, CameraView, CameraType, useCameraPermissions } from "expo-camera";
import { useRef, useState } from "react";
import { Button, StyleSheet, Text, TouchableOpacity, View, SafeAreaView, Image, Pressable } from "react-native";
import { MaterialIcons, MaterialCommunityIcons } from "@expo/vector-icons";
import { useNavigation } from "@react-navigation/native";
import * as ImagePicker from "expo-image-picker";

const CameraScreen = () => {
    const [facing, setFacing] = useState<CameraType>("back");
    const [permission, requestPermission] = useCameraPermissions();
    const [image, setImage] = useState<string | undefined>("");
    const cameraRef = useRef<CameraView | null>(null);
    const navigation = useNavigation();

    if (!permission) {
        // Camera permissions are still loading.
        return <View />;
    }

    if (!permission.granted) {
        // Camera permissions are not granted yet.
        return (
            <View style={styles.container}>
                <Text style={styles.message}>We need your permission to show the camera</Text>
                <Button onPress={requestPermission} title="grant permission" />
            </View>
        );
    }

    async function takePhoto() {
        if (cameraRef.current) {
            const photo = await cameraRef.current.takePictureAsync();
            setImage(photo?.uri); // Fallback
        }
    }

    const pickImage = async () => {
        // No permissions request is necessary for launching the image library
        let result = await ImagePicker.launchImageLibraryAsync({
            mediaTypes: ["images", "videos"],
            allowsEditing: true,
            aspect: [4, 3],
            quality: 1,
        });

        console.log(result);

        if (!result.canceled) {
            setImage(result.assets[0].uri);
        }
    };

    function toggleCameraFacing() {
        setFacing((current) => (current === "back" ? "front" : "back"));
    }

    return (
        <SafeAreaView style={styles.container}>
            {image ? (
                <View style={styles.previewContainer}>
                    <Image source={{ uri: image }} style={styles.previewImage} />
                    <View style={styles.previewButtons}>
                        <Pressable style={({ pressed }) => [styles.actionButton]} onPress={() => setImage("")}>
                            <Text style={styles.buttonText}>Retake</Text>
                        </Pressable>

                        <Pressable
                            style={({ pressed }) => [styles.actionButton]}
                            onPress={() => navigation.navigate("Recommendation", { image: image })}
                        >
                            <Text style={styles.buttonText}>Use Photo</Text>
                        </Pressable>
                    </View>
                </View>
            ) : (
                <CameraView style={styles.camera} facing={facing} ref={cameraRef}>
                    <View style={styles.buttonContainer}>
                        <TouchableOpacity style={styles.button} onPress={pickImage}>
                            <MaterialCommunityIcons name="view-gallery-outline" color="white" size={50} />
                        </TouchableOpacity>
                        <TouchableOpacity style={styles.button} onPress={takePhoto}>
                            <MaterialIcons name="photo-camera" color="white" size={50} />
                        </TouchableOpacity>
                        <TouchableOpacity style={styles.button} onPress={toggleCameraFacing}>
                            <MaterialIcons name="cameraswitch" color="white" size={50} />
                        </TouchableOpacity>
                    </View>
                </CameraView>
            )}
        </SafeAreaView>
    );
};

export default CameraScreen;

const styles = StyleSheet.create({
    container: {
        flex: 1,
        justifyContent: "center",
    },
    message: {
        textAlign: "center",
        paddingBottom: 10,
    },
    camera: { flex: 1 },
    buttonContainer: {
        flex: 1,
        flexDirection: "row",
        justifyContent: "space-between",
        backgroundColor: "transparent",
        marginBottom: 20,
    },
    button: {
        flex: 1,
        alignSelf: "flex-end",
        alignItems: "center",
    },
    previewContainer: {
        flex: 1,
        justifyContent: "center",
        alignItems: "center",
        backgroundColor: "black",
    },
    previewImage: { width: "100%", height: "90%" },
    previewButtons: {
        width: "100%",
        flexDirection: "row",
        justifyContent: "space-between",
        padding: 10,
    },
    actionButton: {
        paddingVertical: 15,
        paddingHorizontal: 30,
        borderRadius: 10,
        alignItems: "center",
    },
    buttonText: {
        fontSize: 18,
        fontWeight: "bold",
        color: "white",
    },
});
