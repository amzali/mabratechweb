import React, { useState } from "react";
import { DollarSign, Home, Shield, Users, ChevronRight, Eye, Monitor, Fan, Thermometer, Terminal, Calendar, Droplets, MapPin, QrCode, Wifi, Bluetooth } from "lucide-react";
import { useProducts } from "../hooks/useApi";

// Icon mapping for dynamic icons
const iconMap = {
  DollarSign, Home, Shield, Users, Eye, Monitor, Fan, Thermometer, 
  Terminal, Calendar, Droplets, MapPin, QrCode, Wifi, Bluetooth
};

const ProductsSection = () => {
  const [selectedProduct, setSelectedProduct] = useState(0);
  const { products, loading, error } = useProducts();

  // Fallback products data
  const fallbackProducts = [
    {
      icon: "DollarSign",
      title: "Mabra Payroll",
      subtitle: "Employee Payroll Management System",
      description: "Aplikasi lengkap yang dikembangkan khusus untuk membantu perusahaan dalam mengelola penggajian karyawan dengan akurat dan efisien.",
      features: [
        "Automated salary calculations",
        "Tax management & compliance",
        "Employee attendance integration",
        "Detailed payroll reports",
        "Multi-company support",
        "Bank integration for payments"
      ],
      color: "from-green-500 to-emerald-600"
    },
    {
      icon: "Home",
      title: "DYRECS Vatriot",
      subtitle: "Dynamic Residential Control System",
      description: "Aplikasi canggih yang dapat mengendalikan berbagai peralatan rumah dari perumahan-perumahan dengan satu aplikasi terintegrasi dan data yang dinamis.",
      features: [
        { icon: "Eye", text: "Realtime CCTV Monitoring" },
        { icon: "Monitor", text: "Kontrol Lampu" },
        { icon: "Fan", text: "Kontrol Kipas Angin" },
        { icon: "Thermometer", text: "Monitoring Suhu & Kelembaban" },
        { icon: "Terminal", text: "Kontrol Terminal" },
        { icon: "Calendar", text: "Autofeeder dan Scheduler" },
        { icon: "Droplets", text: "Pengisian Air Otomatis" }
      ],
      color: "from-blue-500 to-cyan-600"
    },
    {
      icon: "Shield",
      title: "Patrol System",
      subtitle: "Mobile Security Patrol Application",
      description: "Aplikasi mobile yang dirancang khusus untuk personel keamanan/security dalam melakukan patroli, baik di dalam gedung maupun di lapangan dengan berbagai metode tracking.",
      features: [
        { icon: "MapPin", text: "GPS Location Tracking" },
        { icon: "QrCode", text: "QR Code Scanning" },
        { icon: "Wifi", text: "NFC Scanning" },
        { icon: "Bluetooth", text: "Beacon Scanning" },
        "Real-time reporting",
        "Route optimization",
        "Incident management",
        "Historical patrol data"
      ],
      color: "from-red-500 to-orange-600"
    },
    {
      icon: "Users",
      title: "RTRW-Online",
      subtitle: "Neighborhood Management System",
      description: "Aplikasi komprehensif untuk pengolahan data warga pada tingkat Rukun Tetangga dan Rukun Warga, memudahkan administrasi kependudukan di tingkat grassroot.",
      features: [
        "Citizen data management",
        "Family card processing",
        "Document requests",
        "Community announcements",
        "Financial management",
        "Event organization",
        "Digital archive system",
        "Mobile accessibility"
      ],
      color: "from-purple-500 to-indigo-600"
    }
  ];

  const displayProducts = products.length > 0 ? products : fallbackProducts;

  // Ensure selectedProduct index is valid
  const validSelectedIndex = selectedProduct < displayProducts.length ? selectedProduct : 0;
  const currentProduct = displayProducts[validSelectedIndex] || displayProducts[0];

  if (loading) {
    return (
      <section id="products" className="py-32 relative">
        <div className="dark-content-container">
          <div className="text-center">
            <div className="display-large text-white mb-6">Loading Products...</div>
            <div className="animate-pulse">
              <div className="bg-secondary border border-subtle p-12 h-96"></div>
            </div>
          </div>
        </div>
      </section>
    );
  }

  return (
    <section id="products" className="py-32 relative">
      <div className="absolute inset-0 opacity-3">
        <div className="grid-pattern"></div>
      </div>
      
      <div className="dark-content-container relative z-10">
        {/* Section Header */}
        <div className="text-center space-y-6 mb-20">
          <h2 className="display-large text-white">Our Products</h2>
          <p className="body-large text-secondary max-w-3xl mx-auto">
            Produk-produk inovatif yang telah kami kembangkan untuk memberikan solusi 
            teknologi terdepan bagi berbagai kebutuhan industri dan masyarakat.
          </p>
          
          {error && (
            <div className="text-yellow-400 body-small">
              Using cached products data (API temporarily unavailable)
            </div>
          )}
        </div>

        {/* Product Navigation */}
        <div className="flex flex-wrap justify-center gap-4 mb-16">
          {displayProducts.map((product, index) => {
            const IconComponent = iconMap[product.icon] || DollarSign;
            
            return (
              <button
                key={product.id || index}
                onClick={() => setSelectedProduct(index)}
                className={`flex items-center space-x-3 px-6 py-3 border transition-all duration-300 ${
                  validSelectedIndex === index
                    ? 'bg-brand-hover text-brand-primary border-brand-primary font-semibold'
                    : 'bg-transparent text-secondary border-subtle hover:border-brand-primary hover:text-brand-primary'
                }`}
              >
                <IconComponent className="w-5 h-5" />
                <span className="button-text">{product.title}</span>
              </button>
            );
          })}
        </div>

        {/* Selected Product Details */}
        {currentProduct && (
          <div className="bg-secondary border border-subtle p-12">
            <div className="grid lg:grid-cols-2 gap-12 items-center">
              {/* Product Info */}
              <div className="space-y-8">
                <div className="flex items-center space-x-4">
                  <div className={`w-16 h-16 bg-gradient-to-br ${currentProduct.color || 'from-cyan-500 to-blue-600'} flex items-center justify-center`}>
                    {React.createElement(iconMap[currentProduct.icon] || DollarSign, {
                      className: "w-8 h-8 text-white"
                    })}
                  </div>
                  <div>
                    <h3 className="heading-2 text-white">{currentProduct.title}</h3>
                    <p className="body-medium text-brand-primary">{currentProduct.subtitle}</p>
                  </div>
                </div>

                <p className="body-large text-secondary">
                  {currentProduct.description}
                </p>

                <div className="flex space-x-4">
                  <button 
                    onClick={() => {
                      const element = document.getElementById('contact');
                      if (element) {
                        element.scrollIntoView({ behavior: 'smooth' });
                      }
                    }}
                    className="btn-primary"
                  >
                    Learn More
                  </button>
                  <button 
                    onClick={() => {
                      const element = document.getElementById('contact');
                      if (element) {
                        element.scrollIntoView({ behavior: 'smooth' });
                      }
                    }}
                    className="btn-secondary"
                  >
                    Request Demo
                  </button>
                </div>
              </div>

              {/* Features List */}
              <div className="space-y-6">
                <h4 className="heading-3 text-white mb-6">Key Features</h4>
                <div className="grid gap-4">
                  {currentProduct.features?.map((feature, index) => (
                    <div key={index} className="flex items-center space-x-4 p-4 bg-overlay border border-subtle">
                      {typeof feature === 'object' && feature.icon ? (
                        <>
                          {React.createElement(iconMap[feature.icon] || ChevronRight, {
                            className: "w-5 h-5 text-brand-primary flex-shrink-0"
                          })}
                          <span className="body-medium text-secondary">{feature.text}</span>
                        </>
                      ) : (
                        <>
                          <ChevronRight className="w-5 h-5 text-brand-primary flex-shrink-0" />
                          <span className="body-medium text-secondary">
                            {typeof feature === 'string' ? feature : feature.text || 'Feature'}
                          </span>
                        </>
                      )}
                    </div>
                  ))}
                </div>
              </div>
            </div>
          </div>
        )}

        {/* Product Stats */}
        <div className="grid md:grid-cols-4 gap-8 mt-20">
          <div className="text-center p-8 bg-overlay border border-subtle">
            <div className="display-medium text-brand-primary">4+</div>
            <div className="body-small text-muted">Products Developed</div>
          </div>
          <div className="text-center p-8 bg-overlay border border-subtle">
            <div className="display-medium text-brand-primary">1000+</div>
            <div className="body-small text-muted">Active Users</div>
          </div>
          <div className="text-center p-8 bg-overlay border border-subtle">
            <div className="display-medium text-brand-primary">99.9%</div>
            <div className="body-small text-muted">Uptime Guarantee</div>
          </div>
          <div className="text-center p-8 bg-overlay border border-subtle">
            <div className="display-medium text-brand-primary">24/7</div>
            <div className="body-small text-muted">Technical Support</div>
          </div>
        </div>
      </div>
    </section>
  );
};

export default ProductsSection;