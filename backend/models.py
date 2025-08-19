from pydantic import BaseModel, Field, EmailStr
from typing import List, Optional, Union, Any
from datetime import datetime
import uuid

# Contact Models
class ContactCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    email: EmailStr
    phone: Optional[str] = Field(None, max_length=20)
    company: Optional[str] = Field(None, max_length=100)
    service: str = Field(..., min_length=1)
    message: str = Field(..., min_length=10, max_length=1000)

class Contact(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    name: str
    email: str
    phone: Optional[str] = None
    company: Optional[str] = None
    service: str
    message: str
    status: str = "new"  # new, contacted, qualified, closed
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
    ip_address: Optional[str] = None
    user_agent: Optional[str] = None

class ContactResponse(BaseModel):
    success: bool
    message: str
    id: Optional[str] = None

# Service Models
class Service(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    icon: str  # lucide icon name
    title: str
    description: str
    features: List[str]
    is_active: bool = True
    order: int = 0
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

class ServiceCreate(BaseModel):
    icon: str
    title: str = Field(..., min_length=1, max_length=100)
    description: str = Field(..., min_length=10, max_length=500)
    features: List[str]
    is_active: bool = True
    order: int = 0

# Product Models  
class ProductFeature(BaseModel):
    icon: Optional[str] = None
    text: str

class Product(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    icon: str  # lucide icon name
    title: str
    subtitle: str
    description: str
    features: List[Union[str, ProductFeature]]
    color: str  # gradient colors
    is_active: bool = True
    order: int = 0
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

class ProductCreate(BaseModel):
    icon: str
    title: str = Field(..., min_length=1, max_length=100)
    subtitle: str = Field(..., min_length=1, max_length=200)
    description: str = Field(..., min_length=10, max_length=500)
    features: List[Union[str, ProductFeature]]
    color: str
    is_active: bool = True
    order: int = 0

# Project Models
class Project(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    title: str
    client: str
    category: str
    description: str
    features: List[str]
    technologies: List[str]
    duration: str
    year: str
    status: str
    icon: str  # lucide icon name
    is_active: bool = True
    order: int = 0
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

class ProjectCreate(BaseModel):
    title: str = Field(..., min_length=1, max_length=100)
    client: str = Field(..., min_length=1, max_length=100)
    category: str = Field(..., min_length=1, max_length=100)
    description: str = Field(..., min_length=10, max_length=500)
    features: List[str]
    technologies: List[str]
    duration: str
    year: str
    status: str
    icon: str
    is_active: bool = True
    order: int = 0

# Analytics Models
class AnalyticsEvent(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    type: str  # page_view, contact_form, button_click
    page: str
    user_agent: Optional[str] = None
    ip_address: Optional[str] = None
    metadata: Optional[dict] = None
    timestamp: datetime = Field(default_factory=datetime.utcnow)

class AnalyticsEventCreate(BaseModel):
    type: str
    page: str
    metadata: Optional[dict] = None

class AnalyticsStats(BaseModel):
    total_page_views: int
    total_contacts: int
    top_pages: List[dict]
    contacts_by_service: List[dict]
    recent_activity: List[dict]

# Response Models
class ServiceListResponse(BaseModel):
    services: List[Service]
    total: int

class ProductListResponse(BaseModel):
    products: List[Product]
    total: int

class ProjectListResponse(BaseModel):
    projects: List[Project]
    total: int

class ContactListResponse(BaseModel):
    contacts: List[Contact]
    total: int