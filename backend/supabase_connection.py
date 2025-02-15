import os
from supabase import create_client, Client
from dotenv import load_dotenv

load_dotenv()  # Load environment variables

class SupabaseSingleton:
    _instance = None  # Store the single instance of Supabase Client

    @classmethod
    def get_instance(cls):
        """Returns a single instance of the Supabase client."""
        if cls._instance is None:
            url: str = os.getenv("SUPABASE_URL")
            key: str = os.getenv("SUPABASE_API_KEY")
            
            if not url or not key:
                raise ValueError("❌ Supabase URL or API key is missing! Check your .env file.")
            
            cls._instance = create_client(url, key)  # Initialize once
        
        return cls._instance

