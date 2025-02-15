from fastapi import FastAPI
from routes import router  # Import routes

app = FastAPI()

# Include the routes from routes.py
app.include_router(router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)


