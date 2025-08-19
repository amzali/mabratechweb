import React from "react";
import { ArrowRight, Code, Database, Globe } from "lucide-react";

const HeroSection = () => {
  const scrollToSection = (sectionId) => {
    const element = document.getElementById(sectionId);
    if (element) {
      element.scrollIntoView({ behavior: 'smooth' });
    }
  };

  return (
    <section id="home" className="min-h-screen flex items-center justify-center relative overflow-hidden pt-20">
      {/* Background Pattern */}
      <div className="absolute inset-0 opacity-5">
        <div className="absolute inset-0 bg-gradient-to-br from-cyan-400 via-transparent to-transparent"></div>
        <div className="grid-pattern"></div>
      </div>
      
      <div className="dark-content-container relative z-10">
        <div className="text-center space-y-8">
          {/* Main Title */}
          <div className="space-y-4">
            <h1 className="display-huge text-white leading-tight">
              PT Mabra Technology
              <br />
              <span className="text-brand-primary">Solutions</span>
            </h1>
            <p className="body-large text-secondary max-w-3xl mx-auto">
              Penyedia solusi teknologi informasi yang inovatif, handal, dan terpercaya sejak 2016
            </p>
          </div>

          {/* Service Icons */}
          <div className="flex justify-center space-x-8 md:space-x-12 my-12">
            <div className="flex flex-col items-center space-y-2">
              <div className="w-16 h-16 bg-brand-hover rounded-full flex items-center justify-center">
                <Database className="w-8 h-8 text-brand-primary" />
              </div>
              <span className="body-small text-muted">ERP Systems</span>
            </div>
            <div className="flex flex-col items-center space-y-2">
              <div className="w-16 h-16 bg-brand-hover rounded-full flex items-center justify-center">
                <Code className="w-8 h-8 text-brand-primary" />
              </div>
              <span className="body-small text-muted">Payroll Apps</span>
            </div>
            <div className="flex flex-col items-center space-y-2">
              <div className="w-16 h-16 bg-brand-hover rounded-full flex items-center justify-center">
                <Globe className="w-8 h-8 text-brand-primary" />
              </div>
              <span className="body-small text-muted">Web Development</span>
            </div>
          </div>

          {/* CTA Buttons */}
          <div className="flex flex-col sm:flex-row gap-6 justify-center items-center mt-12">
            <button 
              onClick={() => scrollToSection('services')}
              className="btn-primary group"
            >
              <span>Explore Our Services</span>
              <ArrowRight className="w-5 h-5 group-hover:translate-x-1 transition-transform" />
            </button>
            <button 
              onClick={() => scrollToSection('contact')}
              className="btn-secondary"
            >
              Get In Touch
            </button>
          </div>

          {/* Stats */}
          <div className="grid grid-cols-3 gap-8 mt-20 pt-12 border-t border-subtle">
            <div className="text-center">
              <div className="display-medium text-brand-primary">9+</div>
              <div className="body-small text-muted">Years Experience</div>
            </div>
            <div className="text-center">
              <div className="display-medium text-brand-primary">50+</div>
              <div className="body-small text-muted">Projects Completed</div>
            </div>
            <div className="text-center">
              <div className="display-medium text-brand-primary">100%</div>
              <div className="body-small text-muted">Client Satisfaction</div>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
};

export default HeroSection;