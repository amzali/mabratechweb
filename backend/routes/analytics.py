from fastapi import APIRouter, HTTPException, Request
from datetime import datetime, timedelta
import logging

from ..models import AnalyticsEvent, AnalyticsEventCreate, AnalyticsStats
from ..database import insert_one, aggregate, count_documents, find_many
from ..utils.analytics import track_event

router = APIRouter(prefix="/api/analytics", tags=["analytics"])
logger = logging.getLogger(__name__)

@router.post("/page-view")
async def track_page_view(
    event_data: AnalyticsEventCreate,
    request: Request
):
    """Track a page view event"""
    try:
        client_ip = request.client.host
        user_agent = request.headers.get("user-agent", "")
        
        await track_event(
            event_data.type,
            event_data.page,
            client_ip,
            user_agent,
            event_data.metadata
        )
        
        return {"success": True}
        
    except Exception as e:
        logger.error(f"Error tracking page view: {e}")
        # Don't throw error for analytics, just log
        return {"success": False}

@router.get("/dashboard", response_model=AnalyticsStats)
async def get_analytics_dashboard():
    """Get analytics dashboard data"""
    try:
        # Get date range (last 30 days)
        end_date = datetime.utcnow()
        start_date = end_date - timedelta(days=30)
        
        # Total page views
        total_page_views = await count_documents(
            "analytics",
            {
                "type": "page_view",
                "timestamp": {"$gte": start_date}
            }
        )
        
        # Total contacts
        total_contacts = await count_documents("contacts")
        
        # Top pages
        top_pages_pipeline = [
            {
                "$match": {
                    "type": "page_view",
                    "timestamp": {"$gte": start_date}
                }
            },
            {
                "$group": {
                    "_id": "$page",
                    "views": {"$sum": 1}
                }
            },
            {"$sort": {"views": -1}},
            {"$limit": 5}
        ]
        
        top_pages = await aggregate("analytics", top_pages_pipeline)
        
        # Contacts by service
        contacts_by_service_pipeline = [
            {
                "$group": {
                    "_id": "$service",
                    "count": {"$sum": 1}
                }
            },
            {"$sort": {"count": -1}}
        ]
        
        contacts_by_service = await aggregate("contacts", contacts_by_service_pipeline)
        
        # Recent activity (last 10 events)
        recent_activity = await find_many(
            "analytics",
            filter_dict={},
            sort_dict={"timestamp": -1},
            limit=10
        )
        
        return AnalyticsStats(
            total_page_views=total_page_views,
            total_contacts=total_contacts,
            top_pages=[{"page": item["_id"], "views": item["views"]} for item in top_pages],
            contacts_by_service=[{"service": item["_id"], "count": item["count"]} for item in contacts_by_service],
            recent_activity=recent_activity
        )
        
    except Exception as e:
        logger.error(f"Error fetching analytics dashboard: {e}")
        raise HTTPException(status_code=500, detail="Error fetching analytics data")