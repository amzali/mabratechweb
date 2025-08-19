from fastapi import APIRouter, HTTPException
from typing import List
import logging

from models import (
    Service, ServiceListResponse, 
    Product, ProductListResponse,
    Project, ProjectListResponse
)
from database import find_many
from utils.seed_data import get_default_services, get_default_products, get_default_projects

router = APIRouter(prefix="/api", tags=["content"])
logger = logging.getLogger(__name__)

@router.get("/services", response_model=ServiceListResponse)
async def get_services():
    """Get all active services"""
    try:
        # Try to get from database first
        services = await find_many(
            "services",
            filter_dict={"is_active": True},
            sort_dict={"order": 1, "created_at": 1}
        )
        
        # If no services in DB, use default data
        if not services:
            services = get_default_services()
            logger.info("Using default services data")
        else:
            # Convert MongoDB _id to id
            for service in services:
                service["id"] = service.pop("_id", service.get("id"))
        
        return ServiceListResponse(
            services=[Service(**service) for service in services],
            total=len(services)
        )
        
    except Exception as e:
        logger.error(f"Error fetching services: {e}")
        # Fallback to default data on error
        services = get_default_services()
        return ServiceListResponse(
            services=[Service(**service) for service in services],
            total=len(services)
        )

@router.get("/products", response_model=ProductListResponse)
async def get_products():
    """Get all active products"""
    try:
        # Try to get from database first
        products = await find_many(
            "products",
            filter_dict={"is_active": True},
            sort_dict={"order": 1, "created_at": 1}
        )
        
        # If no products in DB, use default data
        if not products:
            products = get_default_products()
            logger.info("Using default products data")
        else:
            # Convert MongoDB _id to id
            for product in products:
                product["id"] = product.pop("_id", product.get("id"))
        
        return ProductListResponse(
            products=[Product(**product) for product in products],
            total=len(products)
        )
        
    except Exception as e:
        logger.error(f"Error fetching products: {e}")
        # Fallback to default data on error
        products = get_default_products()
        return ProductListResponse(
            products=[Product(**product) for product in products],
            total=len(products)
        )

@router.get("/projects", response_model=ProjectListResponse)
async def get_projects():
    """Get all active projects"""
    try:
        # Try to get from database first
        projects = await find_many(
            "projects",
            filter_dict={"is_active": True},
            sort_dict={"year": -1, "order": 1}
        )
        
        # If no projects in DB, use default data
        if not projects:
            projects = get_default_projects()
            logger.info("Using default projects data")
        else:
            # Convert MongoDB _id to id
            for project in projects:
                project["id"] = project.pop("_id", project.get("id"))
        
        return ProjectListResponse(
            projects=[Project(**project) for project in projects],
            total=len(projects)
        )
        
    except Exception as e:
        logger.error(f"Error fetching projects: {e}")
        # Fallback to default data on error  
        projects = get_default_projects()
        return ProjectListResponse(
            projects=[Project(**project) for project in projects],
            total=len(projects)
        )