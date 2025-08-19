#!/usr/bin/env python3
"""
Comprehensive Backend API Testing for PT Mabra Technology Solutions
Tests all implemented backend endpoints with realistic data
"""

import asyncio
import aiohttp
import json
import os
from datetime import datetime
from typing import Dict, Any

# Get backend URL from environment
BACKEND_URL = "https://tech-innovators-10.preview.emergentagent.com/api"

class BackendTester:
    def __init__(self):
        self.session = None
        self.test_results = []
        
    async def __aenter__(self):
        self.session = aiohttp.ClientSession()
        return self
        
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if self.session:
            await self.session.close()
    
    def log_result(self, test_name: str, success: bool, details: str = "", response_data: Any = None):
        """Log test result"""
        result = {
            "test": test_name,
            "success": success,
            "details": details,
            "timestamp": datetime.now().isoformat(),
            "response_data": response_data
        }
        self.test_results.append(result)
        status = "✅ PASS" if success else "❌ FAIL"
        print(f"{status} {test_name}: {details}")
        if response_data and not success:
            print(f"   Response: {response_data}")
    
    async def test_health_endpoint(self):
        """Test health check endpoint"""
        try:
            async with self.session.get(f"{BACKEND_URL}/health") as response:
                if response.status == 200:
                    data = await response.json()
                    if data.get("status") == "healthy":
                        self.log_result("Health Check", True, "Service is healthy", data)
                    else:
                        self.log_result("Health Check", False, "Unexpected health status", data)
                else:
                    self.log_result("Health Check", False, f"HTTP {response.status}", await response.text())
        except Exception as e:
            self.log_result("Health Check", False, f"Exception: {str(e)}")
    
    async def test_contact_form_valid_submission(self):
        """Test valid contact form submission"""
        contact_data = {
            "name": "Budi Santoso",
            "email": "budi.santoso@perusahaan.co.id",
            "phone": "081234567890",
            "company": "PT Teknologi Maju Bersama",
            "service": "ERP Systems",
            "message": "Kami tertarik dengan sistem ERP untuk mengintegrasikan operasional perusahaan kami. Mohon informasi lebih lanjut mengenai fitur dan harga yang tersedia."
        }
        
        try:
            async with self.session.post(
                f"{BACKEND_URL}/contacts/",
                json=contact_data,
                headers={"Content-Type": "application/json"}
            ) as response:
                if response.status == 200:
                    data = await response.json()
                    if data.get("success") and data.get("id"):
                        self.log_result("Contact Form - Valid Submission", True, "Contact created successfully", data)
                        return data.get("id")  # Return ID for further tests
                    else:
                        self.log_result("Contact Form - Valid Submission", False, "Invalid response format", data)
                else:
                    error_data = await response.text()
                    self.log_result("Contact Form - Valid Submission", False, f"HTTP {response.status}", error_data)
        except Exception as e:
            self.log_result("Contact Form - Valid Submission", False, f"Exception: {str(e)}")
        return None
    
    async def test_contact_form_validation(self):
        """Test contact form validation with invalid data"""
        # Test missing required fields
        invalid_data = {
            "name": "",  # Empty name
            "email": "invalid-email",  # Invalid email
            "service": "",  # Empty service
            "message": "Short"  # Too short message
        }
        
        try:
            async with self.session.post(
                f"{BACKEND_URL}/contacts/",
                json=invalid_data,
                headers={"Content-Type": "application/json"}
            ) as response:
                if response.status == 422:  # Validation error expected
                    data = await response.json()
                    self.log_result("Contact Form - Validation", True, "Validation errors caught correctly", data)
                else:
                    data = await response.text()
                    self.log_result("Contact Form - Validation", False, f"Expected 422, got {response.status}", data)
        except Exception as e:
            self.log_result("Contact Form - Validation", False, f"Exception: {str(e)}")
    
    async def test_get_contacts(self):
        """Test getting contacts list (admin endpoint)"""
        try:
            async with self.session.get(f"{BACKEND_URL}/contacts/") as response:
                if response.status == 200:
                    data = await response.json()
                    if "contacts" in data and "total" in data:
                        self.log_result("Get Contacts", True, f"Retrieved {data['total']} contacts", {"total": data["total"]})
                    else:
                        self.log_result("Get Contacts", False, "Invalid response format", data)
                else:
                    error_data = await response.text()
                    self.log_result("Get Contacts", False, f"HTTP {response.status}", error_data)
        except Exception as e:
            self.log_result("Get Contacts", False, f"Exception: {str(e)}")
    
    async def test_contact_stats(self):
        """Test contact statistics endpoint"""
        try:
            async with self.session.get(f"{BACKEND_URL}/contacts/stats") as response:
                if response.status == 200:
                    data = await response.json()
                    required_fields = ["totalSubmissions", "byService", "byMonth"]
                    if all(field in data for field in required_fields):
                        self.log_result("Contact Stats", True, f"Stats retrieved: {data['totalSubmissions']} total submissions", data)
                    else:
                        self.log_result("Contact Stats", False, "Missing required fields in response", data)
                else:
                    error_data = await response.text()
                    self.log_result("Contact Stats", False, f"HTTP {response.status}", error_data)
        except Exception as e:
            self.log_result("Contact Stats", False, f"Exception: {str(e)}")
    
    async def test_get_services(self):
        """Test services endpoint"""
        try:
            async with self.session.get(f"{BACKEND_URL}/services") as response:
                if response.status == 200:
                    data = await response.json()
                    if "services" in data and "total" in data:
                        services = data["services"]
                        if len(services) > 0:
                            # Check service structure
                            first_service = services[0]
                            required_fields = ["id", "title", "description", "features", "icon"]
                            if all(field in first_service for field in required_fields):
                                self.log_result("Get Services", True, f"Retrieved {len(services)} services with correct structure", {"total": len(services)})
                            else:
                                self.log_result("Get Services", False, "Service missing required fields", first_service)
                        else:
                            self.log_result("Get Services", True, "No services found (using fallback data)", data)
                    else:
                        self.log_result("Get Services", False, "Invalid response format", data)
                else:
                    error_data = await response.text()
                    self.log_result("Get Services", False, f"HTTP {response.status}", error_data)
        except Exception as e:
            self.log_result("Get Services", False, f"Exception: {str(e)}")
    
    async def test_get_products(self):
        """Test products endpoint"""
        try:
            async with self.session.get(f"{BACKEND_URL}/products") as response:
                if response.status == 200:
                    data = await response.json()
                    if "products" in data and "total" in data:
                        products = data["products"]
                        if len(products) > 0:
                            # Check product structure
                            first_product = products[0]
                            required_fields = ["id", "title", "subtitle", "description", "features", "icon", "color"]
                            if all(field in first_product for field in required_fields):
                                self.log_result("Get Products", True, f"Retrieved {len(products)} products with correct structure", {"total": len(products)})
                            else:
                                self.log_result("Get Products", False, "Product missing required fields", first_product)
                        else:
                            self.log_result("Get Products", True, "No products found (using fallback data)", data)
                    else:
                        self.log_result("Get Products", False, "Invalid response format", data)
                else:
                    error_data = await response.text()
                    self.log_result("Get Products", False, f"HTTP {response.status}", error_data)
        except Exception as e:
            self.log_result("Get Products", False, f"Exception: {str(e)}")
    
    async def test_get_projects(self):
        """Test projects endpoint"""
        try:
            async with self.session.get(f"{BACKEND_URL}/projects") as response:
                if response.status == 200:
                    data = await response.json()
                    if "projects" in data and "total" in data:
                        projects = data["projects"]
                        if len(projects) > 0:
                            # Check project structure
                            first_project = projects[0]
                            required_fields = ["id", "title", "client", "category", "description", "features", "technologies", "year", "status", "icon"]
                            if all(field in first_project for field in required_fields):
                                self.log_result("Get Projects", True, f"Retrieved {len(projects)} projects with correct structure", {"total": len(projects)})
                            else:
                                self.log_result("Get Projects", False, "Project missing required fields", first_project)
                        else:
                            self.log_result("Get Projects", True, "No projects found (using fallback data)", data)
                    else:
                        self.log_result("Get Projects", False, "Invalid response format", data)
                else:
                    error_data = await response.text()
                    self.log_result("Get Projects", False, f"HTTP {response.status}", error_data)
        except Exception as e:
            self.log_result("Get Projects", False, f"Exception: {str(e)}")
    
    async def test_analytics_page_view(self):
        """Test analytics page view tracking"""
        analytics_data = {
            "type": "page_view",
            "page": "/services",
            "metadata": {
                "referrer": "https://google.com",
                "user_type": "visitor"
            }
        }
        
        try:
            async with self.session.post(
                f"{BACKEND_URL}/analytics/page-view",
                json=analytics_data,
                headers={"Content-Type": "application/json"}
            ) as response:
                if response.status == 200:
                    data = await response.json()
                    if data.get("success"):
                        self.log_result("Analytics - Page View", True, "Page view tracked successfully", data)
                    else:
                        self.log_result("Analytics - Page View", False, "Analytics tracking failed", data)
                else:
                    error_data = await response.text()
                    self.log_result("Analytics - Page View", False, f"HTTP {response.status}", error_data)
        except Exception as e:
            self.log_result("Analytics - Page View", False, f"Exception: {str(e)}")
    
    async def test_analytics_dashboard(self):
        """Test analytics dashboard endpoint"""
        try:
            async with self.session.get(f"{BACKEND_URL}/analytics/dashboard") as response:
                if response.status == 200:
                    data = await response.json()
                    required_fields = ["total_page_views", "total_contacts", "top_pages", "contacts_by_service", "recent_activity"]
                    if all(field in data for field in required_fields):
                        self.log_result("Analytics - Dashboard", True, f"Dashboard data retrieved: {data['total_page_views']} page views, {data['total_contacts']} contacts", data)
                    else:
                        self.log_result("Analytics - Dashboard", False, "Missing required fields in dashboard", data)
                else:
                    error_data = await response.text()
                    self.log_result("Analytics - Dashboard", False, f"HTTP {response.status}", error_data)
        except Exception as e:
            self.log_result("Analytics - Dashboard", False, f"Exception: {str(e)}")
    
    async def test_invalid_endpoint(self):
        """Test error handling for invalid endpoints"""
        try:
            async with self.session.get(f"{BACKEND_URL}/nonexistent") as response:
                if response.status == 404:
                    self.log_result("Error Handling - Invalid Endpoint", True, "404 returned for invalid endpoint")
                else:
                    self.log_result("Error Handling - Invalid Endpoint", False, f"Expected 404, got {response.status}")
        except Exception as e:
            self.log_result("Error Handling - Invalid Endpoint", False, f"Exception: {str(e)}")
    
    async def run_all_tests(self):
        """Run all backend tests"""
        print(f"🚀 Starting Backend API Tests for PT Mabra Technology Solutions")
        print(f"📍 Backend URL: {BACKEND_URL}")
        print("=" * 80)
        
        # Test sequence based on priority
        test_sequence = [
            # High Priority Tests
            ("Health Check", self.test_health_endpoint),
            ("Contact Form - Valid Submission", self.test_contact_form_valid_submission),
            ("Contact Form - Validation", self.test_contact_form_validation),
            ("Get Contacts", self.test_get_contacts),
            ("Contact Stats", self.test_contact_stats),
            ("Get Services", self.test_get_services),
            ("Get Products", self.test_get_products),
            ("Get Projects", self.test_get_projects),
            
            # Medium Priority Tests
            ("Analytics - Page View", self.test_analytics_page_view),
            ("Analytics - Dashboard", self.test_analytics_dashboard),
            
            # Error Handling Tests
            ("Error Handling - Invalid Endpoint", self.test_invalid_endpoint),
        ]
        
        for test_name, test_func in test_sequence:
            print(f"\n🔍 Running: {test_name}")
            await test_func()
            await asyncio.sleep(0.5)  # Small delay between tests
        
        # Print summary
        print("\n" + "=" * 80)
        print("📊 TEST SUMMARY")
        print("=" * 80)
        
        passed = sum(1 for result in self.test_results if result["success"])
        failed = len(self.test_results) - passed
        
        print(f"✅ Passed: {passed}")
        print(f"❌ Failed: {failed}")
        print(f"📈 Success Rate: {(passed/len(self.test_results)*100):.1f}%")
        
        if failed > 0:
            print("\n🔍 FAILED TESTS:")
            for result in self.test_results:
                if not result["success"]:
                    print(f"   ❌ {result['test']}: {result['details']}")
        
        return self.test_results

async def main():
    """Main test runner"""
    async with BackendTester() as tester:
        results = await tester.run_all_tests()
        
        # Save results to file
        with open("/app/backend_test_results.json", "w") as f:
            json.dump(results, f, indent=2, default=str)
        
        print(f"\n💾 Test results saved to: /app/backend_test_results.json")
        
        return results

if __name__ == "__main__":
    asyncio.run(main())