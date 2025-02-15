module.exports = {
    presets: ["babel-preset-expo"],
    plugins: [
        [
            "module:react-native-dotenv",
            {
                moduleName: "@env",
                path: ".env",
                safe: true,
                allowUndefined: false,
            },
        ],
        ["react-native-reanimated/plugin"],
    ],
};
