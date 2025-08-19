import React from "react";
import Header from "./Header";
import HeroSection from "./HeroSection";
import AboutSection from "./AboutSection";
import ServicesSection from "./ServicesSection";
import ProductsSection from "./ProductsSection";
import ProjectsSection from "./ProjectsSection";
import ContactSection from "./ContactSection";
import Footer from "./Footer";
import { usePageTracking } from "../hooks/useApi";

const HomePage = () => {
  // Track page views
  usePageTracking();

  return (
    <div className="dark-container">
      <Header />
      <HeroSection />
      <AboutSection />
      <ServicesSection />
      <ProductsSection />
      <ProjectsSection />
      <ContactSection />
      <Footer />
    </div>
  );
};

export default HomePage;