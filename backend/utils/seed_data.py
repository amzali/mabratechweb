"""
Default data for services, products, and projects.
This data will be used when the database is empty or as fallback.
"""

from datetime import datetime

def get_default_services():
    """Get default services data"""
    return [
        {
            "id": "service-1",
            "icon": "Database",
            "title": "ERP Systems",
            "description": "Sistem perencanaan sumber daya perusahaan yang terintegrasi untuk mengoptimalkan operasional bisnis Anda.",
            "features": [
                "Manajemen Inventory",
                "Financial Management", 
                "CRM Integration",
                "Real-time Analytics"
            ],
            "is_active": True,
            "order": 1,
            "created_at": datetime.utcnow(),
            "updated_at": datetime.utcnow()
        },
        {
            "id": "service-2", 
            "icon": "DollarSign",
            "title": "Payroll Management",
            "description": "Solusi komprehensif untuk mengelola penggajian karyawan dengan akurasi dan efisiensi tinggi.",
            "features": [
                "Automated Calculations",
                "Tax Management",
                "Employee Self-Service", 
                "Compliance Reporting"
            ],
            "is_active": True,
            "order": 2,
            "created_at": datetime.utcnow(),
            "updated_at": datetime.utcnow()
        },
        {
            "id": "service-3",
            "icon": "Globe", 
            "title": "Web Development",
            "description": "Pengembangan website dan aplikasi web modern dengan teknologi terdepan dan desain responsif.",
            "features": [
                "Responsive Design",
                "Custom Development",
                "E-commerce Solutions",
                "SEO Optimization"
            ],
            "is_active": True,
            "order": 3,
            "created_at": datetime.utcnow(),
            "updated_at": datetime.utcnow()
        },
        {
            "id": "service-4",
            "icon": "Smartphone",
            "title": "Mobile Applications", 
            "description": "Aplikasi mobile native dan cross-platform untuk meningkatkan engagement dan produktivitas.",
            "features": [
                "iOS & Android",
                "Cross-platform",
                "UI/UX Design",
                "API Integration"
            ],
            "is_active": True,
            "order": 4,
            "created_at": datetime.utcnow(),
            "updated_at": datetime.utcnow()
        },
        {
            "id": "service-5",
            "icon": "Shield",
            "title": "System Integration",
            "description": "Integrasi sistem yang seamless untuk menghubungkan berbagai platform bisnis Anda.",
            "features": [
                "API Development",
                "Third-party Integration", 
                "Data Migration",
                "System Architecture"
            ],
            "is_active": True,
            "order": 5,
            "created_at": datetime.utcnow(),
            "updated_at": datetime.utcnow()
        },
        {
            "id": "service-6",
            "icon": "Users",
            "title": "IT Consulting",
            "description": "Konsultasi teknologi informasi untuk strategi digital dan transformasi bisnis perusahaan.", 
            "features": [
                "Digital Strategy",
                "Technology Assessment",
                "Process Optimization", 
                "Training & Support"
            ],
            "is_active": True,
            "order": 6,
            "created_at": datetime.utcnow(),
            "updated_at": datetime.utcnow()
        }
    ]

def get_default_products():
    """Get default products data"""
    return [
        {
            "id": "product-1",
            "icon": "DollarSign",
            "title": "Mabra Payroll",
            "subtitle": "Employee Payroll Management System",
            "description": "Aplikasi lengkap yang dikembangkan khusus untuk membantu perusahaan dalam mengelola penggajian karyawan dengan akurat dan efisien.",
            "features": [
                "Automated salary calculations",
                "Tax management & compliance", 
                "Employee attendance integration",
                "Detailed payroll reports",
                "Multi-company support",
                "Bank integration for payments"
            ],
            "color": "from-green-500 to-emerald-600",
            "is_active": True,
            "order": 1,
            "created_at": datetime.utcnow(),
            "updated_at": datetime.utcnow()
        },
        {
            "id": "product-2",
            "icon": "Home",
            "title": "DYRECS Vatriot", 
            "subtitle": "Dynamic Residential Control System",
            "description": "Aplikasi canggih yang dapat mengendalikan berbagai peralatan rumah dari perumahan-perumahan dengan satu aplikasi terintegrasi dan data yang dinamis.",
            "features": [
                {"icon": "Eye", "text": "Realtime CCTV Monitoring"},
                {"icon": "Monitor", "text": "Kontrol Lampu"},
                {"icon": "Fan", "text": "Kontrol Kipas Angin"},
                {"icon": "Thermometer", "text": "Monitoring Suhu & Kelembaban"},
                {"icon": "Terminal", "text": "Kontrol Terminal"},
                {"icon": "Calendar", "text": "Autofeeder dan Scheduler"},
                {"icon": "Droplets", "text": "Pengisian Air Otomatis"}
            ],
            "color": "from-blue-500 to-cyan-600",
            "is_active": True,
            "order": 2,
            "created_at": datetime.utcnow(),
            "updated_at": datetime.utcnow()
        },
        {
            "id": "product-3",
            "icon": "Shield",
            "title": "Patrol System",
            "subtitle": "Mobile Security Patrol Application", 
            "description": "Aplikasi mobile yang dirancang khusus untuk personel keamanan/security dalam melakukan patroli, baik di dalam gedung maupun di lapangan dengan berbagai metode tracking.",
            "features": [
                {"icon": "MapPin", "text": "GPS Location Tracking"},
                {"icon": "QrCode", "text": "QR Code Scanning"},
                {"icon": "Wifi", "text": "NFC Scanning"},
                {"icon": "Bluetooth", "text": "Beacon Scanning"},
                "Real-time reporting",
                "Route optimization", 
                "Incident management",
                "Historical patrol data"
            ],
            "color": "from-red-500 to-orange-600",
            "is_active": True,
            "order": 3,
            "created_at": datetime.utcnow(),
            "updated_at": datetime.utcnow()
        },
        {
            "id": "product-4",
            "icon": "Users",
            "title": "RTRW-Online",
            "subtitle": "Neighborhood Management System",
            "description": "Aplikasi komprehensif untuk pengolahan data warga pada tingkat Rukun Tetangga dan Rukun Warga, memudahkan administrasi kependudukan di tingkat grassroot.",
            "features": [
                "Citizen data management",
                "Family card processing",
                "Document requests",
                "Community announcements",
                "Financial management",
                "Event organization",
                "Digital archive system",
                "Mobile accessibility"
            ],
            "color": "from-purple-500 to-indigo-600",
            "is_active": True,
            "order": 4,
            "created_at": datetime.utcnow(),
            "updated_at": datetime.utcnow()
        }
    ]

def get_default_projects():
    """Get default projects data"""
    return [
        {
            "id": "project-1",
            "title": "Payroll Application",
            "client": "PT Sansan Saudaratex Jaya",
            "category": "Human Resource Management",
            "description": "Pengembangan aplikasi payroll komprehensif untuk mengelola penggajian karyawan PT Sansan Saudaratex Jaya. Sistem ini mengotomatisasi perhitungan gaji, tunjangan, dan potongan dengan akurasi tinggi.",
            "features": [
                "Automated salary calculations",
                "Tax deduction management",
                "Employee attendance integration", 
                "Comprehensive reporting system",
                "Multi-department support"
            ],
            "technologies": ["React.js", "Node.js", "MySQL", "Express.js"],
            "duration": "6 months",
            "year": "2022",
            "status": "Completed",
            "icon": "Calculator",
            "is_active": True,
            "order": 1,
            "created_at": datetime.utcnow(),
            "updated_at": datetime.utcnow()
        },
        {
            "id": "project-2", 
            "title": "Website & Online Recruitment",
            "client": "PT Andalan Multi Kencana (AllMakes)",
            "category": "Web Development & HR Tech",
            "description": "Pengembangan website corporate dan sistem rekrutmen online terintegrasi untuk PT Andalan Multi Kencana. Platform ini memungkinkan proses rekrutmen yang lebih efisien dan modern.",
            "features": [
                "Corporate website with CMS",
                "Online job application system",
                "Candidate tracking system",
                "Interview scheduling",
                "Document management",
                "Automated email notifications"
            ],
            "technologies": ["WordPress", "PHP", "MySQL", "JavaScript", "Bootstrap"],
            "duration": "4 months",
            "year": "2021", 
            "status": "Completed",
            "icon": "Users",
            "is_active": True,
            "order": 2,
            "created_at": datetime.utcnow(),
            "updated_at": datetime.utcnow()
        },
        {
            "id": "project-3",
            "title": "Accounting Application", 
            "client": "PT Sinar Panca Mitra Indonesia",
            "category": "Financial Management System",
            "description": "Implementasi sistem akuntansi digital untuk PT Sinar Panca Mitra Indonesia yang mencakup pencatatan transaksi, laporan keuangan, dan manajemen aset perusahaan.",
            "features": [
                "General ledger management",
                "Accounts payable & receivable",
                "Financial reporting",
                "Budget planning & tracking", 
                "Asset management",
                "Tax calculation & reporting"
            ],
            "technologies": ["Java", "Spring Boot", "PostgreSQL", "Angular", "Bootstrap"],
            "duration": "8 months",
            "year": "2023",
            "status": "Completed",
            "icon": "Building",
            "is_active": True,
            "order": 3,
            "created_at": datetime.utcnow(),
            "updated_at": datetime.utcnow()
        }
    ]