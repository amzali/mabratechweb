import React, { useState } from "react";
import { Menu, X } from "lucide-react";

const Header = () => {
  const [isMenuOpen, setIsMenuOpen] = useState(false);

  const scrollToSection = (sectionId) => {
    const element = document.getElementById(sectionId);
    if (element) {
      element.scrollIntoView({ behavior: 'smooth' });
      setIsMenuOpen(false);
    }
  };

  return (
    <header className="dark-header">
      <div className="flex items-center">
        <div className="flex items-center space-x-3">
          <img 
            src="https://customer-assets.emergentagent.com/job_tech-innovators-10/artifacts/xoh4wss1_logo_only_edited.png" 
            alt="Mabra Technology Solutions Logo" 
            className="h-10 w-10 object-contain"
          />
          <div className="flex flex-col">
            <h1 className="company-logo text-xl font-bold">MABRATECH</h1>
            <span className="company-tagline text-xs text-gray-400">Technology Solutions</span>
          </div>
        </div>
      </div>
      
      {/* Desktop Navigation */}
      <nav className="dark-nav hidden md:flex">
        <button onClick={() => scrollToSection('home')} className="dark-nav-link">
          Home
        </button>
        <button onClick={() => scrollToSection('about')} className="dark-nav-link">
          About
        </button>
        <button onClick={() => scrollToSection('services')} className="dark-nav-link">
          Services
        </button>
        <button onClick={() => scrollToSection('products')} className="dark-nav-link">
          Products
        </button>
        <button onClick={() => scrollToSection('projects')} className="dark-nav-link">
          Projects
        </button>
        <button onClick={() => scrollToSection('contact')} className="dark-nav-link">
          Contact
        </button>
      </nav>

      {/* Mobile Menu Button */}
      <button 
        className="md:hidden text-white p-2"
        onClick={() => setIsMenuOpen(!isMenuOpen)}
      >
        {isMenuOpen ? <X size={24} /> : <Menu size={24} />}
      </button>

      {/* Mobile Navigation */}
      {isMenuOpen && (
        <div className="absolute top-full left-0 right-0 bg-black border-t border-gray-800 md:hidden">
          <nav className="flex flex-col p-4 space-y-4">
            <button onClick={() => scrollToSection('home')} className="dark-nav-link text-left">
              Home
            </button>
            <button onClick={() => scrollToSection('about')} className="dark-nav-link text-left">
              About
            </button>
            <button onClick={() => scrollToSection('services')} className="dark-nav-link text-left">
              Services
            </button>
            <button onClick={() => scrollToSection('products')} className="dark-nav-link text-left">
              Products
            </button>
            <button onClick={() => scrollToSection('projects')} className="dark-nav-link text-left">
              Projects
            </button>
            <button onClick={() => scrollToSection('contact')} className="dark-nav-link text-left">
              Contact
            </button>
          </nav>
        </div>
      )}
    </header>
  );
};

export default Header;