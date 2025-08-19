from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase
from pymongo import ASCENDING, DESCENDING
import os
from datetime import datetime
import logging

logger = logging.getLogger(__name__)

class Database:
    client: AsyncIOMotorClient = None
    database: AsyncIOMotorDatabase = None

db = Database()

async def get_database() -> AsyncIOMotorDatabase:
    return db.database

async def connect_to_mongo():
    """Create database connection"""
    try:
        db.client = AsyncIOMotorClient(os.environ["MONGO_URL"])
        db.database = db.client[os.environ["DB_NAME"]]
        
        # Test connection
        await db.client.admin.command('ping')
        logger.info("Successfully connected to MongoDB")
        
        # Create indexes for better performance
        await create_indexes()
        
    except Exception as e:
        logger.error(f"Could not connect to MongoDB: {e}")
        raise

async def close_mongo_connection():
    """Close database connection"""
    if db.client:
        db.client.close()
        logger.info("Disconnected from MongoDB")

async def create_indexes():
    """Create database indexes for optimal performance"""
    try:
        database = db.database
        
        # Contacts collection indexes
        await database.contacts.create_index([("email", ASCENDING)])
        await database.contacts.create_index([("created_at", DESCENDING)])
        await database.contacts.create_index([("status", ASCENDING)])
        
        # Services collection indexes
        await database.services.create_index([("is_active", ASCENDING), ("order", ASCENDING)])
        await database.services.create_index([("title", ASCENDING)])
        
        # Products collection indexes  
        await database.products.create_index([("is_active", ASCENDING), ("order", ASCENDING)])
        await database.products.create_index([("title", ASCENDING)])
        
        # Projects collection indexes
        await database.projects.create_index([("is_active", ASCENDING), ("order", ASCENDING)])
        await database.projects.create_index([("year", DESCENDING)])
        await database.projects.create_index([("client", ASCENDING)])
        
        # Analytics collection indexes
        await database.analytics.create_index([("timestamp", DESCENDING)])
        await database.analytics.create_index([("type", ASCENDING)])
        await database.analytics.create_index([("page", ASCENDING)])
        
        logger.info("Database indexes created successfully")
        
    except Exception as e:
        logger.error(f"Error creating indexes: {e}")

# Database utility functions
async def insert_one(collection_name: str, document: dict):
    """Insert a single document"""
    collection = db.database[collection_name]
    result = await collection.insert_one(document)
    return result

async def find_one(collection_name: str, filter_dict: dict):
    """Find a single document"""
    collection = db.database[collection_name]
    document = await collection.find_one(filter_dict)
    return document

async def find_many(collection_name: str, filter_dict: dict = None, sort_dict: dict = None, limit: int = None):
    """Find multiple documents"""
    collection = db.database[collection_name]
    
    cursor = collection.find(filter_dict or {})
    
    if sort_dict:
        cursor = cursor.sort(list(sort_dict.items()))
    
    if limit:
        cursor = cursor.limit(limit)
    
    documents = await cursor.to_list(length=None)
    return documents

async def update_one(collection_name: str, filter_dict: dict, update_dict: dict):
    """Update a single document"""
    collection = db.database[collection_name]
    
    # Add updated_at timestamp
    update_dict.setdefault("$set", {})["updated_at"] = datetime.utcnow()
    
    result = await collection.update_one(filter_dict, update_dict)
    return result

async def delete_one(collection_name: str, filter_dict: dict):
    """Delete a single document"""
    collection = db.database[collection_name]
    result = await collection.delete_one(filter_dict)
    return result

async def count_documents(collection_name: str, filter_dict: dict = None):
    """Count documents matching filter"""
    collection = db.database[collection_name]
    count = await collection.count_documents(filter_dict or {})
    return count

async def aggregate(collection_name: str, pipeline: list):
    """Run aggregation pipeline"""
    collection = db.database[collection_name]
    cursor = collection.aggregate(pipeline)
    results = await cursor.to_list(length=None)
    return results