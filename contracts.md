# API Contracts - PT Mabra Technology Solutions Website

## Overview
This document defines the API contracts and integration plan for transitioning from mock data to a fully functional backend system.

## Current Frontend Mock Data
Currently all data is hardcoded in the frontend components. The following components need backend integration:

### 1. Contact Form (ContactSection.js)
- **Current**: Form submission shows alert, no data persistence
- **Mock Data**: Form validation only, no actual submission
- **Integration Needed**: Contact form submissions, email notifications

### 2. Services Data (ServicesSection.js)
- **Current**: Hardcoded services array in component
- **Mock Data**: Static services list with features
- **Integration Needed**: Dynamic services management

### 3. Products Data (ProductsSection.js)
- **Current**: Hardcoded products array in component  
- **Mock Data**: Static products with features and descriptions
- **Integration Needed**: Dynamic products management

### 4. Projects Data (ProjectsSection.js)
- **Current**: Hardcoded projects array in component
- **Mock Data**: Static project portfolio
- **Integration Needed**: Dynamic projects/portfolio management

## Backend API Endpoints

### 1. Contact Management
```
POST /api/contacts
- Purpose: Submit contact form
- Body: { name, email, phone, company, service, message }
- Response: { success: boolean, message: string, id?: string }

GET /api/contacts (Admin only)
- Purpose: Retrieve all contact submissions
- Response: { contacts: Contact[], total: number }

GET /api/contacts/stats
- Purpose: Get contact form analytics
- Response: { totalSubmissions, byService, byMonth }
```

### 2. Content Management
```
GET /api/services
- Purpose: Get all services
- Response: { services: Service[] }

GET /api/products  
- Purpose: Get all products
- Response: { products: Product[] }

GET /api/projects
- Purpose: Get all projects
- Response: { projects: Project[] }

POST/PUT/DELETE /api/admin/services/:id (Admin only)
- Purpose: CRUD operations for services

POST/PUT/DELETE /api/admin/products/:id (Admin only)
- Purpose: CRUD operations for products

POST/PUT/DELETE /api/admin/projects/:id (Admin only)
- Purpose: CRUD operations for projects
```

### 3. Analytics & Tracking
```
POST /api/analytics/page-view
- Purpose: Track page views and user behavior
- Body: { page, userAgent, timestamp }

GET /api/analytics/dashboard (Admin only)
- Purpose: Get website analytics
- Response: { pageViews, topPages, contactSubmissions, trends }
```

### 4. Email Notifications
```
POST /api/email/contact-notification
- Purpose: Send email notification on contact form submission
- Internal API, triggered by contact submission
```

## Database Schema

### Collections

#### 1. contacts
```javascript
{
  _id: ObjectId,
  name: String,
  email: String,
  phone: String,
  company: String,
  service: String,
  message: String,
  status: String, // "new", "contacted", "qualified", "closed"
  createdAt: Date,
  updatedAt: Date,
  ipAddress: String,
  userAgent: String
}
```

#### 2. services
```javascript
{
  _id: ObjectId,
  icon: String, // lucide icon name
  title: String,
  description: String,
  features: [String],
  isActive: Boolean,
  order: Number,
  createdAt: Date,
  updatedAt: Date
}
```

#### 3. products
```javascript
{
  _id: ObjectId,
  icon: String, // lucide icon name
  title: String,
  subtitle: String,
  description: String,
  features: [Mixed], // Can be string or {icon, text}
  color: String, // gradient colors
  isActive: Boolean,
  order: Number,
  createdAt: Date,
  updatedAt: Date
}
```

#### 4. projects
```javascript
{
  _id: ObjectId,
  title: String,
  client: String,
  category: String,
  description: String,
  features: [String],
  technologies: [String],
  duration: String,
  year: String,
  status: String,
  icon: String, // lucide icon name
  isActive: Boolean,
  order: Number,
  createdAt: Date,
  updatedAt: Date
}
```

#### 5. analytics
```javascript
{
  _id: ObjectId,
  type: String, // "page_view", "contact_form", "button_click"
  page: String,
  userAgent: String,
  ipAddress: String,
  metadata: Object, // additional data
  timestamp: Date
}
```

## Frontend Integration Plan

### Phase 1: Contact Form Integration
1. Create contact API endpoint
2. Update ContactSection.js to use actual API
3. Add loading states and success/error handling
4. Remove mock alert, add proper feedback

### Phase 2: Content Management Integration  
1. Create content APIs (services, products, projects)
2. Create React hooks for data fetching (useServices, useProducts, useProjects)
3. Update components to use API data instead of hardcoded arrays
4. Add loading states and error handling

### Phase 3: Analytics Integration
1. Add page view tracking
2. Add form submission tracking  
3. Add button click analytics
4. Create analytics dashboard (optional)

### Phase 4: Admin Panel (Optional)
1. Create admin authentication
2. Build admin dashboard for content management
3. Add CRUD interfaces for services/products/projects
4. Add contact management interface

## Environment Variables Needed
```
# Email Configuration (for contact notifications)
SMTP_HOST=smtp.gmail.com
SMTP_PORT=587
SMTP_USER=your-email@gmail.com
SMTP_PASS=your-app-password

# Admin Configuration
ADMIN_EMAIL=admin@mabratech.co.id
```

## Error Handling
- All API endpoints return consistent error format
- Frontend displays user-friendly error messages
- Server logs all errors for debugging
- Graceful fallback to cached/default data when API fails

## Security Considerations
- Rate limiting on contact form submissions
- Input validation and sanitization
- CORS configuration
- IP address logging for analytics
- Basic admin authentication (if admin panel implemented)

## Performance Optimizations
- Caching for content APIs (services, products, projects)
- Image optimization for uploaded content
- Database indexing on frequently queried fields
- Pagination for large datasets (contacts, analytics)

## Testing Strategy
- API endpoint testing with automated tests
- Frontend integration testing
- Contact form submission testing
- Error handling testing
- Performance testing under load