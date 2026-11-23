from fastapi import FastAPI
from contextlib import asynccontextmanager
from database import test_conn, engine



@asynccontextmanager
async def lifespan(app: FastAPI):
    await test_conn()
    yield
    await engine.dispose()
    
app = FastAPI(lifespan=lifespan)
@app.get("/health")
def health_check():
    return{
          "status": "healthy",
        "message": "Booking Engine API is running"
    }