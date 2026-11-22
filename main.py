from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
def health_check():
    return{
          "status": "healthy",
        "message": "Booking Engine API is running"
    }