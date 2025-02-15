import { supabase } from "../supabaseClient";

// ✅ Sign Up User
export async function signUp(email: string, password: string) {
    const { data, error } = await supabase.auth.signUp({ email, password });

    if (error) {
        console.error("Sign-up error:", error.message);
        return null;
    }

    return data.user;
}

// ✅ Login User
export async function signIn(email: string, password: string) {
    const { data, error } = await supabase.auth.signInWithPassword({ email, password });

    if (error) {
        console.error("Login error:", error.message);
        return null;
    }

    return data.user;
}

// ✅ Logout User
export async function signOut() {
    const { error } = await supabase.auth.signOut();

    if (error) {
        console.error("Logout error:", error.message);
    }
}
