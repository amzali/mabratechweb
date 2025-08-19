import React, { useState } from "react";
import { MapPin, Phone, Mail, Clock, Send, MessageCircle } from "lucide-react";
import { useContactForm } from "../hooks/useApi";

const ContactSection = () => {
  const [formData, setFormData] = useState({
    name: '',
    email: '',
    phone: '',
    company: '',
    service: '',
    message: ''
  });

  const { submitContact, submitting, submitResult, clearResult } = useContactForm();

  const handleInputChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value
    });
    
    // Clear previous result when user starts typing
    if (submitResult) {
      clearResult();
    }
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    
    try {
      await submitContact(formData);
      
      // Reset form on success
      setFormData({
        name: '',
        email: '',
        phone: '',
        company: '',
        service: '',
        message: ''
      });
    } catch (error) {
      // Error is handled by the hook
      console.error('Form submission error:', error);
    }
  };

  const contactInfo = [
    {
      icon: MapPin,
      title: "Address",
      details: "Jl. Canon No. 5 A-6 Cipageran Cimahi",
      description: "Visit our office for direct consultation"
    },
    {
      icon: Phone,
      title: "Phone",
      details: "(022) 20668716",
      description: "Call us during business hours"
    },
    {
      icon: Mail,
      title: "Email",
      details: "info@mabratech.co.id",
      description: "Send us your inquiry anytime"
    },
    {
      icon: Clock,
      title: "Business Hours",
      details: "Mon - Fri: 9AM - 6PM",
      description: "We're here to help you"
    }
  ];

  const services = [
    "ERP Systems",
    "Payroll Management", 
    "Web Development",
    "Mobile Applications",
    "System Integration",
    "IT Consulting",
    "General Inquiry"
  ];

  return (
    <section id="contact" className="py-32 relative">
      <div className="absolute inset-0 opacity-3">
        <div className="grid-pattern"></div>
      </div>
      
      <div className="dark-content-container relative z-10">
        {/* Section Header */}
        <div className="text-center space-y-6 mb-20">
          <h2 className="display-large text-white">Contact Us</h2>
          <p className="body-large text-secondary max-w-3xl mx-auto">
            Siap memulai proyek teknologi Anda? Hubungi kami untuk konsultasi gratis dan 
            temukan solusi terbaik untuk kebutuhan bisnis Anda.
          </p>
        </div>

        <div className="grid lg:grid-cols-2 gap-16">
          {/* Contact Information */}
          <div className="space-y-12">
            <div>
              <h3 className="heading-2 text-white mb-8">Get in Touch</h3>
              <p className="body-large text-secondary mb-12">
                Tim ahli kami siap membantu Anda menemukan solusi teknologi yang tepat. 
                Jangan ragu untuk menghubungi kami melalui berbagai channel yang tersedia.
              </p>
            </div>

            {/* Contact Cards */}
            <div className="space-y-6">
              {contactInfo.map((info, index) => (
                <div key={index} className="flex items-start space-x-4 p-6 bg-overlay border border-subtle dark-hover">
                  <div className="w-12 h-12 bg-brand-primary flex items-center justify-center">
                    <info.icon className="w-6 h-6 text-black" />
                  </div>
                  <div>
                    <h4 className="heading-3 text-white mb-2">{info.title}</h4>
                    <p className="body-medium text-brand-primary mb-1">{info.details}</p>
                    <p className="body-small text-muted">{info.description}</p>
                  </div>
                </div>
              ))}
            </div>

            {/* Quick Actions */}
            <div className="space-y-4">
              <h4 className="heading-3 text-white">Quick Actions</h4>
              <div className="flex flex-wrap gap-4">
                <a 
                  href="tel:+622220668716"
                  className="btn-secondary flex items-center space-x-2"
                >
                  <Phone className="w-5 h-5" />
                  <span>Call Now</span>
                </a>
                <a 
                  href="https://wa.me/622220668716"
                  target="_blank"
                  rel="noopener noreferrer"
                  className="btn-secondary flex items-center space-x-2"
                >
                  <MessageCircle className="w-5 h-5" />
                  <span>WhatsApp</span>
                </a>
              </div>
            </div>
          </div>

          {/* Contact Form */}
          <div className="bg-secondary border border-subtle p-12">
            <h3 className="heading-2 text-white mb-8">Send us a Message</h3>
            
            {/* Success/Error Message */}
            {submitResult && (
              <div className={`p-4 border mb-6 ${
                submitResult.success 
                  ? 'bg-green-900/20 border-green-500 text-green-400' 
                  : 'bg-red-900/20 border-red-500 text-red-400'
              }`}>
                {submitResult.message}
              </div>
            )}
            
            <form onSubmit={handleSubmit} className="space-y-6">
              <div className="grid md:grid-cols-2 gap-6">
                <div>
                  <label className="block body-medium text-secondary mb-2">Full Name *</label>
                  <input
                    type="text"
                    name="name"
                    value={formData.name}
                    onChange={handleInputChange}
                    required
                    disabled={submitting}
                    className="w-full px-4 py-3 bg-primary border border-subtle text-white placeholder-muted focus:border-brand-primary focus:outline-none transition-colors disabled:opacity-50"
                    placeholder="Your full name"
                  />
                </div>
                <div>
                  <label className="block body-medium text-secondary mb-2">Email Address *</label>
                  <input
                    type="email"
                    name="email"
                    value={formData.email}
                    onChange={handleInputChange}
                    required
                    disabled={submitting}
                    className="w-full px-4 py-3 bg-primary border border-subtle text-white placeholder-muted focus:border-brand-primary focus:outline-none transition-colors disabled:opacity-50"
                    placeholder="your@email.com"
                  />
                </div>
              </div>

              <div className="grid md:grid-cols-2 gap-6">
                <div>
                  <label className="block body-medium text-secondary mb-2">Phone Number</label>
                  <input
                    type="tel"
                    name="phone"
                    value={formData.phone}
                    onChange={handleInputChange}
                    disabled={submitting}
                    className="w-full px-4 py-3 bg-primary border border-subtle text-white placeholder-muted focus:border-brand-primary focus:outline-none transition-colors disabled:opacity-50"
                    placeholder="Your phone number"
                  />
                </div>
                <div>
                  <label className="block body-medium text-secondary mb-2">Company Name</label>
                  <input
                    type="text"
                    name="company"
                    value={formData.company}
                    onChange={handleInputChange}
                    disabled={submitting}
                    className="w-full px-4 py-3 bg-primary border border-subtle text-white placeholder-muted focus:border-brand-primary focus:outline-none transition-colors disabled:opacity-50"
                    placeholder="Your company name"
                  />
                </div>
              </div>

              <div>
                <label className="block body-medium text-secondary mb-2">Service Interested *</label>
                <select
                  name="service"
                  value={formData.service}
                  onChange={handleInputChange}
                  required
                  disabled={submitting}
                  className="w-full px-4 py-3 bg-primary border border-subtle text-white focus:border-brand-primary focus:outline-none transition-colors disabled:opacity-50"
                >
                  <option value="">Select a service</option>
                  {services.map((service, index) => (
                    <option key={index} value={service}>{service}</option>
                  ))}
                </select>
              </div>

              <div>
                <label className="block body-medium text-secondary mb-2">Message *</label>
                <textarea
                  name="message"
                  value={formData.message}
                  onChange={handleInputChange}
                  required
                  disabled={submitting}
                  rows={6}
                  className="w-full px-4 py-3 bg-primary border border-subtle text-white placeholder-muted focus:border-brand-primary focus:outline-none transition-colors resize-vertical disabled:opacity-50"
                  placeholder="Tell us about your project requirements..."
                ></textarea>
              </div>

              <button
                type="submit"
                disabled={submitting}
                className={`btn-primary w-full group ${submitting ? 'opacity-50 cursor-not-allowed' : ''}`}
              >
                {submitting ? (
                  <span>Sending...</span>
                ) : (
                  <>
                    <span>Send Message</span>
                    <Send className="w-5 h-5 group-hover:translate-x-1 transition-transform" />
                  </>
                )}
              </button>
            </form>

            <p className="body-small text-muted mt-6 text-center">
              * Required fields. We'll respond within 24 hours.
            </p>
          </div>
        </div>
      </div>
    </section>
  );
};

export default ContactSection;