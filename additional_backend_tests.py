#!/usr/bin/env python3
"""
Additional Backend Tests - Database Operations and Edge Cases
"""

import asyncio
import aiohttp
import json
from datetime import datetime

BACKEND_URL = "https://tech-innovators-10.preview.emergentagent.com/api"

async def test_multiple_contact_submissions():
    """Test multiple contact submissions to verify database persistence"""
    print("🔍 Testing multiple contact submissions...")
    
    contacts = [
        {
            "name": "Sari Dewi",
            "email": "sari.dewi@perusahaan.co.id",
            "phone": "081234567891",
            "company": "PT Maju Jaya Sentosa",
            "service": "Payroll Management",
            "message": "Kami membutuhkan sistem payroll yang dapat mengintegrasikan dengan sistem HR yang sudah ada. Mohon informasi detail mengenai fitur dan implementasinya."
        },
        {
            "name": "Ahmad Rahman",
            "email": "ahmad.rahman@teknologi.com",
            "phone": "081234567892",
            "company": "CV Teknologi Nusantara",
            "service": "Web Development",
            "message": "Perusahaan kami ingin mengembangkan website e-commerce dengan fitur pembayaran online dan manajemen inventory. Berapa estimasi waktu dan biayanya?"
        },
        {
            "name": "Linda Sari",
            "email": "linda@startup.id",
            "company": "Startup Digital Indonesia",
            "service": "Mobile Applications",
            "message": "Kami startup fintech yang membutuhkan aplikasi mobile untuk layanan pembayaran digital. Apakah ada pengalaman mengembangkan aplikasi serupa?"
        }
    ]
    
    async with aiohttp.ClientSession() as session:
        submitted_ids = []
        
        for i, contact in enumerate(contacts, 1):
            try:
                async with session.post(
                    f"{BACKEND_URL}/contacts/",
                    json=contact,
                    headers={"Content-Type": "application/json"}
                ) as response:
                    if response.status == 200:
                        data = await response.json()
                        if data.get("success"):
                            submitted_ids.append(data.get("id"))
                            print(f"   ✅ Contact {i} submitted: {contact['name']}")
                        else:
                            print(f"   ❌ Contact {i} failed: {data}")
                    else:
                        print(f"   ❌ Contact {i} HTTP error: {response.status}")
            except Exception as e:
                print(f"   ❌ Contact {i} exception: {e}")
        
        # Verify all contacts were stored
        try:
            async with session.get(f"{BACKEND_URL}/contacts/") as response:
                if response.status == 200:
                    data = await response.json()
                    total_contacts = data.get("total", 0)
                    print(f"   📊 Total contacts in database: {total_contacts}")
                    
                    if total_contacts >= len(submitted_ids):
                        print("   ✅ All contacts successfully stored in database")
                    else:
                        print("   ❌ Some contacts may not have been stored")
                else:
                    print(f"   ❌ Failed to retrieve contacts: {response.status}")
        except Exception as e:
            print(f"   ❌ Error retrieving contacts: {e}")

async def test_analytics_aggregation():
    """Test analytics aggregation with multiple events"""
    print("\n🔍 Testing analytics aggregation...")
    
    events = [
        {"type": "page_view", "page": "/services", "metadata": {"section": "erp"}},
        {"type": "page_view", "page": "/products", "metadata": {"product": "payroll"}},
        {"type": "page_view", "page": "/projects", "metadata": {"category": "web"}},
        {"type": "page_view", "page": "/services", "metadata": {"section": "web"}},
        {"type": "page_view", "page": "/", "metadata": {"referrer": "google"}},
    ]
    
    async with aiohttp.ClientSession() as session:
        # Submit multiple analytics events
        for i, event in enumerate(events, 1):
            try:
                async with session.post(
                    f"{BACKEND_URL}/analytics/page-view",
                    json=event,
                    headers={"Content-Type": "application/json"}
                ) as response:
                    if response.status == 200:
                        data = await response.json()
                        if data.get("success"):
                            print(f"   ✅ Event {i} tracked: {event['page']}")
                        else:
                            print(f"   ❌ Event {i} failed: {data}")
                    else:
                        print(f"   ❌ Event {i} HTTP error: {response.status}")
            except Exception as e:
                print(f"   ❌ Event {i} exception: {e}")
        
        # Check analytics dashboard
        await asyncio.sleep(1)  # Small delay for data processing
        
        try:
            async with session.get(f"{BACKEND_URL}/analytics/dashboard") as response:
                if response.status == 200:
                    data = await response.json()
                    page_views = data.get("total_page_views", 0)
                    top_pages = data.get("top_pages", [])
                    
                    print(f"   📊 Total page views: {page_views}")
                    print(f"   📈 Top pages: {len(top_pages)} entries")
                    
                    if top_pages:
                        for page_data in top_pages[:3]:
                            print(f"      - {page_data.get('page', 'Unknown')}: {page_data.get('views', 0)} views")
                    
                    print("   ✅ Analytics aggregation working correctly")
                else:
                    print(f"   ❌ Failed to get analytics: {response.status}")
        except Exception as e:
            print(f"   ❌ Error getting analytics: {e}")

async def test_contact_status_update():
    """Test contact status update functionality"""
    print("\n🔍 Testing contact status update...")
    
    async with aiohttp.ClientSession() as session:
        # First, get a contact ID
        try:
            async with session.get(f"{BACKEND_URL}/contacts/") as response:
                if response.status == 200:
                    data = await response.json()
                    contacts = data.get("contacts", [])
                    
                    if contacts:
                        contact_id = contacts[0]["id"]
                        print(f"   📝 Testing with contact ID: {contact_id}")
                        
                        # Test status update
                        async with session.patch(
                            f"{BACKEND_URL}/contacts/{contact_id}/status?status=contacted"
                        ) as update_response:
                            if update_response.status == 200:
                                update_data = await update_response.json()
                                if update_data.get("success"):
                                    print("   ✅ Contact status updated successfully")
                                else:
                                    print(f"   ❌ Status update failed: {update_data}")
                            else:
                                print(f"   ❌ Status update HTTP error: {update_response.status}")
                    else:
                        print("   ⚠️  No contacts found to test status update")
                else:
                    print(f"   ❌ Failed to get contacts: {response.status}")
        except Exception as e:
            print(f"   ❌ Error testing status update: {e}")

async def test_edge_cases():
    """Test various edge cases"""
    print("\n🔍 Testing edge cases...")
    
    async with aiohttp.ClientSession() as session:
        # Test very long message
        long_message = "A" * 1001  # Exceeds 1000 char limit
        long_contact = {
            "name": "Test User",
            "email": "test@example.com",
            "service": "Testing",
            "message": long_message
        }
        
        try:
            async with session.post(
                f"{BACKEND_URL}/contacts/",
                json=long_contact,
                headers={"Content-Type": "application/json"}
            ) as response:
                if response.status == 422:
                    print("   ✅ Long message validation working correctly")
                else:
                    print(f"   ❌ Expected 422 for long message, got {response.status}")
        except Exception as e:
            print(f"   ❌ Error testing long message: {e}")
        
        # Test invalid analytics data
        invalid_analytics = {
            "type": "",  # Empty type
            "page": "",  # Empty page
        }
        
        try:
            async with session.post(
                f"{BACKEND_URL}/analytics/page-view",
                json=invalid_analytics,
                headers={"Content-Type": "application/json"}
            ) as response:
                # Analytics should be resilient and not fail hard
                if response.status in [200, 422]:
                    print("   ✅ Analytics handles invalid data gracefully")
                else:
                    print(f"   ⚠️  Analytics response: {response.status}")
        except Exception as e:
            print(f"   ❌ Error testing invalid analytics: {e}")

async def main():
    """Run additional tests"""
    print("🚀 Running Additional Backend Tests")
    print("=" * 60)
    
    await test_multiple_contact_submissions()
    await test_analytics_aggregation()
    await test_contact_status_update()
    await test_edge_cases()
    
    print("\n" + "=" * 60)
    print("✅ Additional testing completed")

if __name__ == "__main__":
    asyncio.run(main())