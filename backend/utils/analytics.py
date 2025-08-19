from datetime import datetime
import logging
from typing import Optional, Dict, Any

from ..database import insert_one
from ..models import AnalyticsEvent

logger = logging.getLogger(__name__)

async def track_event(
    event_type: str,
    page: str,
    ip_address: Optional[str] = None,
    user_agent: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None
):
    """Track an analytics event"""
    try:
        event = AnalyticsEvent(
            type=event_type,
            page=page,
            ip_address=ip_address,
            user_agent=user_agent,
            metadata=metadata or {}
        )
        
        # Convert to dict for MongoDB
        event_dict = event.dict()
        event_dict["_id"] = event_dict.pop("id")
        
        await insert_one("analytics", event_dict)
        
        logger.debug(f"Tracked {event_type} event for page {page}")
        
    except Exception as e:
        logger.error(f"Error tracking analytics event: {e}")
        # Don't raise exception for analytics failures