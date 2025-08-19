import React from "react";
import { Database, DollarSign, Globe, Smartphone, Shield, Users } from "lucide-react";
import { useServices } from "../hooks/useApi";

// Icon mapping for dynamic icons
const iconMap = {
  Database,
  DollarSign,
  Globe,
  Smartphone,
  Shield,
  Users
};

const ServicesSection = () => {
  const { services, loading, error } = useServices();

  // Fallback services data in case API fails
  const fallbackServices = [
    {
      icon: "Database",
      title: "ERP Systems",
      description: "Sistem perencanaan sumber daya perusahaan yang terintegrasi untuk mengoptimalkan operasional bisnis Anda.",
      features: ["Manajemen Inventory", "Financial Management", "CRM Integration", "Real-time Analytics"]
    },
    {
      icon: "DollarSign", 
      title: "Payroll Management",
      description: "Solusi komprehensif untuk mengelola penggajian karyawan dengan akurasi dan efisiensi tinggi.",
      features: ["Automated Calculations", "Tax Management", "Employee Self-Service", "Compliance Reporting"]
    },
    {
      icon: "Globe",
      title: "Web Development",
      description: "Pengembangan website dan aplikasi web modern dengan teknologi terdepan dan desain responsif.",
      features: ["Responsive Design", "Custom Development", "E-commerce Solutions", "SEO Optimization"]
    },
    {
      icon: "Smartphone",
      title: "Mobile Applications",
      description: "Aplikasi mobile native dan cross-platform untuk meningkatkan engagement dan produktivitas.", 
      features: ["iOS & Android", "Cross-platform", "UI/UX Design", "API Integration"]
    },
    {
      icon: "Shield",
      title: "System Integration",
      description: "Integrasi sistem yang seamless untuk menghubungkan berbagai platform bisnis Anda.",
      features: ["API Development", "Third-party Integration", "Data Migration", "System Architecture"]
    },
    {
      icon: "Users",
      title: "IT Consulting",
      description: "Konsultasi teknologi informasi untuk strategi digital dan transformasi bisnis perusahaan.",
      features: ["Digital Strategy", "Technology Assessment", "Process Optimization", "Training & Support"]
    }
  ];

  const displayServices = services.length > 0 ? services : fallbackServices;

  if (loading) {
    return (
      <section id="services" className="py-32 relative">
        <div className="dark-content-container">
          <div className="text-center">
            <div className="display-large text-white mb-6">Loading Services...</div>
            <div className="animate-pulse grid md:grid-cols-2 lg:grid-cols-3 gap-8">
              {[...Array(6)].map((_, i) => (
                <div key={i} className="bg-secondary border border-subtle p-8 h-80"></div>
              ))}
            </div>
          </div>
        </div>
      </section>
    );
  }

  return (
    <section id="services" className="py-32 relative">
      <div className="absolute inset-0 opacity-3">
        <div className="grid-pattern"></div>
      </div>
      
      <div className="dark-content-container relative z-10">
        {/* Section Header */}
        <div className="text-center space-y-6 mb-20">
          <h2 className="display-large text-white">Our Services</h2>
          <p className="body-large text-secondary max-w-3xl mx-auto">
            Kami menyediakan berbagai layanan teknologi informasi yang dirancang untuk memenuhi 
            kebutuhan bisnis modern dan mendorong transformasi digital perusahaan Anda.
          </p>
          
          {error && (
            <div className="text-yellow-400 body-small">
              Using cached services data (API temporarily unavailable)
            </div>
          )}
        </div>

        {/* Services Grid */}
        <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
          {displayServices.map((service, index) => {
            const IconComponent = iconMap[service.icon] || Database;
            
            return (
              <div 
                key={service.id || index}
                className="bg-secondary border border-subtle p-8 dark-hover group cursor-pointer"
              >
                {/* Service Icon */}
                <div className="w-16 h-16 bg-overlay border border-brand-primary mb-6 flex items-center justify-center group-hover:bg-brand-primary transition-colors duration-300">
                  <IconComponent className="w-8 h-8 text-brand-primary group-hover:text-black" />
                </div>

                {/* Service Content */}
                <h3 className="heading-3 text-white mb-4">{service.title}</h3>
                <p className="body-medium text-secondary mb-6">
                  {service.description}
                </p>

                {/* Features List */}
                <ul className="space-y-2">
                  {service.features?.map((feature, featureIndex) => (
                    <li key={featureIndex} className="flex items-center text-muted body-small">
                      <div className="w-1 h-1 bg-brand-primary mr-3 flex-shrink-0"></div>
                      {feature}
                    </li>
                  ))}
                </ul>

                {/* Hover Effect */}
                <div className="mt-6 opacity-0 group-hover:opacity-100 transition-opacity duration-300">
                  <div className="w-full h-1 bg-gradient-to-r from-brand-primary to-transparent"></div>
                </div>
              </div>
            );
          })}
        </div>

        {/* CTA Section */}
        <div className="text-center mt-20">
          <div className="bg-overlay p-12 border border-subtle">
            <h3 className="heading-2 text-white mb-6">
              Ready to Transform Your Business?
            </h3>
            <p className="body-large text-secondary mb-8 max-w-2xl mx-auto">
              Hubungi kami untuk konsultasi gratis dan temukan bagaimana teknologi kami 
              dapat membantu mengoptimalkan operasional bisnis Anda.
            </p>
            <button 
              onClick={() => {
                const element = document.getElementById('contact');
                if (element) {
                  element.scrollIntoView({ behavior: 'smooth' });
                }
              }}
              className="btn-primary"
            >
              Get Free Consultation
            </button>
          </div>
        </div>
      </div>
    </section>
  );
};

export default ServicesSection;