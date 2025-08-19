from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os
import logging
from pathlib import Path
from contextlib import asynccontextmanager

# Import database connection
from database import connect_to_mongo, close_mongo_connection

# Import routes
from routes.contacts import router as contacts_router
from routes.content import router as content_router
from routes.analytics import router as analytics_router

ROOT_DIR = Path(__file__).parent
load_dotenv(ROOT_DIR / '.env')

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    logger.info("Starting up Mabratech API server...")
    await connect_to_mongo()
    yield
    # Shutdown
    logger.info("Shutting down Mabratech API server...")
    await close_mongo_connection()

# Create the main app
app = FastAPI(
    title="Mabratech API",
    description="API for PT Mabra Technology Solutions website",
    version="1.0.0",
    lifespan=lifespan
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify exact origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(contacts_router)
app.include_router(content_router) 
app.include_router(analytics_router)

# Health check endpoint
@app.get("/api/health")
async def health_check():
    return {
        "status": "healthy",
        "service": "Mabratech API",
        "version": "1.0.0"
    }

# Root endpoint (legacy support)
@app.get("/api/")
async def root():
    return {
        "message": "Welcome to Mabratech API",
        "version": "1.0.0",
        "docs": "/docs"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)