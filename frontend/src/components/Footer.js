import React from "react";
import { MapPin, Phone, Mail, Globe, Facebook, Twitter, Instagram, Linkedin } from "lucide-react";

const Footer = () => {
  const scrollToSection = (sectionId) => {
    const element = document.getElementById(sectionId);
    if (element) {
      element.scrollIntoView({ behavior: 'smooth' });
    }
  };

  const quickLinks = [
    { label: "Home", action: () => scrollToSection('home') },
    { label: "About", action: () => scrollToSection('about') },
    { label: "Services", action: () => scrollToSection('services') },
    { label: "Products", action: () => scrollToSection('products') },
    { label: "Projects", action: () => scrollToSection('projects') },
    { label: "Contact", action: () => scrollToSection('contact') }
  ];

  const services = [
    "ERP Systems",
    "Payroll Management",
    "Web Development", 
    "Mobile Applications",
    "System Integration",
    "IT Consulting"
  ];

  const products = [
    "Mabra Payroll",
    "DYRECS Vatriot",
    "Patrol System",
    "RTRW-Online"
  ];

  return (
    <footer className="bg-primary border-t border-subtle">
      {/* Main Footer Content */}
      <div className="dark-content-container py-20">
        <div className="grid lg:grid-cols-4 gap-12">
          {/* Company Info */}
          <div className="lg:col-span-2 space-y-8">
            <div>
              <h2 className="display-medium text-white mb-4">MABRATECH</h2>
              <p className="body-large text-secondary mb-6">
                PT Mabra Technology Solutions - Penyedia solusi teknologi informasi yang inovatif, 
                handal, dan terpercaya sejak 2016.
              </p>
              <p className="body-medium text-muted">
                Kami berkomitmen memberikan nilai tambah maksimal bagi semua pemangku kepentingan 
                melalui inovasi teknologi berkualitas tinggi.
              </p>
            </div>

            {/* Contact Info */}
            <div className="space-y-4">
              <div className="flex items-start space-x-3">
                <MapPin className="w-5 h-5 text-brand-primary mt-1 flex-shrink-0" />
                <div>
                  <p className="body-medium text-secondary">
                    Jl. Canon No. 5 A-6 Cipageran Cimahi
                  </p>
                </div>
              </div>
              <div className="flex items-center space-x-3">
                <Phone className="w-5 h-5 text-brand-primary flex-shrink-0" />
                <p className="body-medium text-secondary">(022) 20668716</p>
              </div>
              <div className="flex items-center space-x-3">
                <Mail className="w-5 h-5 text-brand-primary flex-shrink-0" />
                <p className="body-medium text-secondary">info@mabratech.co.id</p>
              </div>
            </div>

            {/* Social Media */}
            <div>
              <h4 className="heading-3 text-white mb-4">Follow Us</h4>
              <div className="flex space-x-4">
                <button className="w-10 h-10 bg-overlay border border-subtle hover:bg-brand-primary hover:border-brand-primary group transition-all duration-300">
                  <Facebook className="w-5 h-5 text-brand-primary group-hover:text-black mx-auto" />
                </button>
                <button className="w-10 h-10 bg-overlay border border-subtle hover:bg-brand-primary hover:border-brand-primary group transition-all duration-300">
                  <Twitter className="w-5 h-5 text-brand-primary group-hover:text-black mx-auto" />
                </button>
                <button className="w-10 h-10 bg-overlay border border-subtle hover:bg-brand-primary hover:border-brand-primary group transition-all duration-300">
                  <Instagram className="w-5 h-5 text-brand-primary group-hover:text-black mx-auto" />
                </button>
                <button className="w-10 h-10 bg-overlay border border-subtle hover:bg-brand-primary hover:border-brand-primary group transition-all duration-300">
                  <Linkedin className="w-5 h-5 text-brand-primary group-hover:text-black mx-auto" />
                </button>
              </div>
            </div>
          </div>

          {/* Quick Links */}
          <div>
            <h4 className="heading-3 text-white mb-6">Quick Links</h4>
            <ul className="space-y-3">
              {quickLinks.map((link, index) => (
                <li key={index}>
                  <button 
                    onClick={link.action}
                    className="body-medium text-muted hover:text-brand-primary transition-colors duration-300"
                  >
                    {link.label}
                  </button>
                </li>
              ))}
            </ul>

            <div className="mt-8">
              <h4 className="heading-3 text-white mb-6">Services</h4>
              <ul className="space-y-3">
                {services.slice(0, 4).map((service, index) => (
                  <li key={index}>
                    <span className="body-medium text-muted hover:text-brand-primary cursor-pointer transition-colors duration-300">
                      {service}
                    </span>
                  </li>
                ))}
              </ul>
            </div>
          </div>

          {/* Products & Legal */}
          <div>
            <h4 className="heading-3 text-white mb-6">Our Products</h4>
            <ul className="space-y-3">
              {products.map((product, index) => (
                <li key={index}>
                  <span className="body-medium text-muted hover:text-brand-primary cursor-pointer transition-colors duration-300">
                    {product}
                  </span>
                </li>
              ))}
            </ul>

            <div className="mt-8">
              <h4 className="heading-3 text-white mb-6">Legal</h4>
              <ul className="space-y-3">
                <li>
                  <span className="body-medium text-muted">Established: April 27, 2016</span>
                </li>
                <li>
                  <span className="body-medium text-muted">NPWP: 76.241.770.7.428.000</span>
                </li>
                <li>
                  <button className="body-medium text-muted hover:text-brand-primary transition-colors duration-300">
                    Privacy Policy
                  </button>
                </li>
                <li>
                  <button className="body-medium text-muted hover:text-brand-primary transition-colors duration-300">
                    Terms of Service
                  </button>
                </li>
              </ul>
            </div>
          </div>
        </div>
      </div>

      {/* Bottom Footer */}
      <div className="border-t border-subtle">
        <div className="dark-content-container py-8">
          <div className="flex flex-col md:flex-row justify-between items-center space-y-4 md:space-y-0">
            <p className="body-medium text-muted text-center md:text-left">
              © 2025 PT Mabra Technology Solutions. All rights reserved.
            </p>
            <div className="flex items-center space-x-6">
              <span className="body-small text-muted">Powered by</span>
              <div className="flex items-center space-x-2">
                <Globe className="w-4 h-4 text-brand-primary" />
                <span className="body-small text-brand-primary">Mabratech</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </footer>
  );
};

export default Footer;