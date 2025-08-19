from fastapi import APIRouter, HTTPException, Request, BackgroundTasks
from typing import List
import logging
from datetime import datetime

from models import Contact, ContactCreate, ContactResponse, ContactListResponse
from database import insert_one, find_many, find_one, update_one, count_documents
from utils.email import send_contact_notification
from utils.analytics import track_event

router = APIRouter(prefix="/api/contacts", tags=["contacts"])
logger = logging.getLogger(__name__)

@router.post("/", response_model=ContactResponse)
async def create_contact(
    contact_data: ContactCreate, 
    request: Request,
    background_tasks: BackgroundTasks
):
    """Submit a new contact form"""
    try:
        # Get client information
        client_ip = request.client.host
        user_agent = request.headers.get("user-agent", "")
        
        # Create contact document
        contact = Contact(
            **contact_data.dict(),
            ip_address=client_ip,
            user_agent=user_agent
        )
        
        # Insert into database
        contact_dict = contact.dict()
        contact_dict["_id"] = contact_dict.pop("id")  # MongoDB uses _id
        
        await insert_one("contacts", contact_dict)
        
        # Send email notification in background
        background_tasks.add_task(
            send_contact_notification,
            contact.dict()
        )
        
        # Track analytics event
        background_tasks.add_task(
            track_event,
            "contact_form",
            "contact",
            client_ip,
            user_agent,
            {"service": contact.service, "company": contact.company}
        )
        
        logger.info(f"New contact submission from {contact.email}")
        
        return ContactResponse(
            success=True,
            message="Terima kasih! Pesan Anda telah berhasil dikirim. Tim kami akan segera menghubungi Anda.",
            id=contact.id
        )
        
    except Exception as e:
        logger.error(f"Error creating contact: {e}")
        raise HTTPException(
            status_code=500, 
            detail="Terjadi kesalahan sistem. Silakan coba lagi atau hubungi kami langsung."
        )

@router.get("/", response_model=ContactListResponse)
async def get_contacts(
    status: str = None,
    limit: int = 50,
    offset: int = 0
):
    """Get all contacts (admin only - basic implementation)"""
    try:
        # Build filter
        filter_dict = {}
        if status:
            filter_dict["status"] = status
        
        # Get contacts with pagination
        contacts = await find_many(
            "contacts",
            filter_dict,
            sort_dict={"created_at": -1},
            limit=limit
        )
        
        # Convert MongoDB _id to id
        for contact in contacts:
            contact["id"] = contact.pop("_id")
        
        # Get total count
        total = await count_documents("contacts", filter_dict)
        
        return ContactListResponse(
            contacts=[Contact(**contact) for contact in contacts],
            total=total
        )
        
    except Exception as e:
        logger.error(f"Error fetching contacts: {e}")
        raise HTTPException(status_code=500, detail="Error fetching contacts")

@router.get("/stats")
async def get_contact_stats():
    """Get contact statistics"""
    try:
        # Total submissions
        total_submissions = await count_documents("contacts")
        
        # Submissions by service
        service_pipeline = [
            {"$group": {"_id": "$service", "count": {"$sum": 1}}},
            {"$sort": {"count": -1}}
        ]
        
        from ..database import aggregate
        by_service = await aggregate("contacts", service_pipeline)
        
        # Submissions by month (last 6 months)
        month_pipeline = [
            {
                "$group": {
                    "_id": {
                        "year": {"$year": "$created_at"},
                        "month": {"$month": "$created_at"}
                    },
                    "count": {"$sum": 1}
                }
            },
            {"$sort": {"_id.year": -1, "_id.month": -1}},
            {"$limit": 6}
        ]
        
        by_month = await aggregate("contacts", month_pipeline)
        
        return {
            "totalSubmissions": total_submissions,
            "byService": by_service,
            "byMonth": by_month
        }
        
    except Exception as e:
        logger.error(f"Error fetching contact stats: {e}")
        raise HTTPException(status_code=500, detail="Error fetching statistics")

@router.patch("/{contact_id}/status")
async def update_contact_status(contact_id: str, status: str):
    """Update contact status (admin only)"""
    try:
        valid_statuses = ["new", "contacted", "qualified", "closed"]
        if status not in valid_statuses:
            raise HTTPException(status_code=400, detail="Invalid status")
        
        result = await update_one(
            "contacts",
            {"_id": contact_id},
            {"$set": {"status": status}}
        )
        
        if result.matched_count == 0:
            raise HTTPException(status_code=404, detail="Contact not found")
        
        return {"success": True, "message": "Status updated successfully"}
        
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error updating contact status: {e}")
        raise HTTPException(status_code=500, detail="Error updating status")