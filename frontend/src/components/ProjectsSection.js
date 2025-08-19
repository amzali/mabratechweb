import React, { useState } from "react";
import { Building, Users, Calculator, ExternalLink } from "lucide-react";
import { useProjects } from "../hooks/useApi";

// Icon mapping for dynamic icons
const iconMap = {
  Building, Users, Calculator
};

const ProjectsSection = () => {
  const [selectedProject, setSelectedProject] = useState(0);
  const { projects, loading, error } = useProjects();

  // Fallback projects data
  const fallbackProjects = [
    {
      id: 1,
      title: "Payroll Application",
      client: "PT Sansan Saudaratex Jaya",
      category: "Human Resource Management",
      description: "Pengembangan aplikasi payroll komprehensif untuk mengelola penggajian karyawan PT Sansan Saudaratex Jaya. Sistem ini mengotomatisasi perhitungan gaji, tunjangan, dan potongan dengan akurasi tinggi.",
      features: [
        "Automated salary calculations",
        "Tax deduction management",
        "Employee attendance integration",
        "Comprehensive reporting system",
        "Multi-department support"
      ],
      technologies: ["React.js", "Node.js", "MySQL", "Express.js"],
      duration: "6 months",
      year: "2022",
      status: "Completed",
      icon: "Calculator"
    },
    {
      id: 2,
      title: "Website & Online Recruitment",
      client: "PT Andalan Multi Kencana (AllMakes)",
      category: "Web Development & HR Tech",
      description: "Pengembangan website corporate dan sistem rekrutmen online terintegrasi untuk PT Andalan Multi Kencana. Platform ini memungkinkan proses rekrutmen yang lebih efisien dan modern.",
      features: [
        "Corporate website with CMS",
        "Online job application system",
        "Candidate tracking system",
        "Interview scheduling",
        "Document management",
        "Automated email notifications"
      ],
      technologies: ["WordPress", "PHP", "MySQL", "JavaScript", "Bootstrap"],
      duration: "4 months",
      year: "2021",
      status: "Completed",
      icon: "Users"
    },
    {
      id: 3,
      title: "Accounting Application",
      client: "PT Sinar Panca Mitra Indonesia",
      category: "Financial Management System",
      description: "Implementasi sistem akuntansi digital untuk PT Sinar Panca Mitra Indonesia yang mencakup pencatatan transaksi, laporan keuangan, dan manajemen aset perusahaan.",
      features: [
        "General ledger management",
        "Accounts payable & receivable",
        "Financial reporting",
        "Budget planning & tracking",
        "Asset management",
        "Tax calculation & reporting"
      ],
      technologies: ["Java", "Spring Boot", "PostgreSQL", "Angular", "Bootstrap"],
      duration: "8 months",
      year: "2023",
      status: "Completed",
      icon: "Building"
    }
  ];

  const displayProjects = projects.length > 0 ? projects : fallbackProjects;

  // Ensure selectedProject index is valid
  const validSelectedIndex = selectedProject < displayProjects.length ? selectedProject : 0;
  const currentProject = displayProjects[validSelectedIndex] || displayProjects[0];

  const partners = [
    {
      name: "PT Sansan Saudaratex Jaya",
      industry: "Textile Manufacturing",
      description: "Leading textile manufacturer specializing in high-quality fabrics and garments for both domestic and international markets."
    },
    {
      name: "PT Sinar Panca Mitra Indonesia",
      industry: "Trading & Distribution",
      description: "Established trading company with extensive distribution network across Indonesia, focusing on industrial supplies and equipment."
    }
  ];

  if (loading) {
    return (
      <section id="projects" className="py-32 relative">
        <div className="dark-content-container">
          <div className="text-center">
            <div className="display-large text-white mb-6">Loading Projects...</div>
            <div className="animate-pulse">
              <div className="bg-secondary border border-subtle p-12 h-96"></div>
            </div>
          </div>
        </div>
      </section>
    );
  }

  return (
    <section id="projects" className="py-32 relative">
      <div className="absolute inset-0 opacity-3">
        <div className="grid-pattern"></div>
      </div>
      
      <div className="dark-content-container relative z-10">
        {/* Section Header */}
        <div className="text-center space-y-6 mb-20">
          <h2 className="display-large text-white">Our Projects</h2>
          <p className="body-large text-secondary max-w-3xl mx-auto">
            Beberapa proyek unggulan yang telah kami selesaikan dengan tingkat kepuasan klien yang tinggi 
            dan implementasi teknologi terdepan.
          </p>
          
          {error && (
            <div className="text-yellow-400 body-small">
              Using cached projects data (API temporarily unavailable)
            </div>
          )}
        </div>

        {/* Project Navigation */}
        <div className="flex flex-wrap justify-center gap-4 mb-16">
          {displayProjects.map((project, index) => {
            const IconComponent = iconMap[project.icon] || Calculator;
            
            return (
              <button
                key={project.id || index}
                onClick={() => setSelectedProject(index)}
                className={`flex items-center space-x-3 px-6 py-3 border transition-all duration-300 ${
                  validSelectedIndex === index
                    ? 'bg-brand-hover text-brand-primary border-brand-primary font-semibold'
                    : 'bg-transparent text-secondary border-subtle hover:border-brand-primary hover:text-brand-primary'
                }`}
              >
                <IconComponent className="w-5 h-5" />
                <span className="button-text">{project.title}</span>
              </button>
            );
          })}
        </div>

        {/* Selected Project Details */}
        {currentProject && (
          <div className="bg-secondary border border-subtle p-12 mb-20">
            <div className="grid lg:grid-cols-3 gap-12">
              {/* Project Info */}
              <div className="lg:col-span-2 space-y-8">
                <div className="flex items-start space-x-4">
                  <div className="w-16 h-16 bg-brand-primary flex items-center justify-center">
                    {React.createElement(iconMap[currentProject.icon] || Calculator, {
                      className: "w-8 h-8 text-black"
                    })}
                  </div>
                  <div>
                    <h3 className="heading-2 text-white">{currentProject.title}</h3>
                    <p className="body-medium text-brand-primary mb-2">{currentProject.client}</p>
                    <p className="body-small text-muted">{currentProject.category}</p>
                  </div>
                </div>

                <p className="body-large text-secondary">
                  {currentProject.description}
                </p>

                {/* Key Features */}
                <div>
                  <h4 className="heading-3 text-white mb-6">Key Features</h4>
                  <div className="grid md:grid-cols-2 gap-4">
                    {currentProject.features?.map((feature, index) => (
                      <div key={index} className="flex items-center space-x-3 p-4 bg-overlay border border-subtle">
                        <div className="w-2 h-2 bg-brand-primary flex-shrink-0"></div>
                        <span className="body-medium text-secondary">{feature}</span>
                      </div>
                    ))}
                  </div>
                </div>
              </div>

              {/* Project Meta */}
              <div className="space-y-8">
                <div className="bg-overlay p-6 border border-subtle">
                  <h4 className="heading-3 text-white mb-6">Project Details</h4>
                  <div className="space-y-4">
                    <div className="flex justify-between items-center">
                      <span className="body-medium text-muted">Duration:</span>
                      <span className="body-medium text-secondary">{currentProject.duration}</span>
                    </div>
                    <div className="flex justify-between items-center">
                      <span className="body-medium text-muted">Year:</span>
                      <span className="body-medium text-secondary">{currentProject.year}</span>
                    </div>
                    <div className="flex justify-between items-center">
                      <span className="body-medium text-muted">Status:</span>
                      <span className="body-medium text-brand-primary">{currentProject.status}</span>
                    </div>
                  </div>
                </div>

                <div className="bg-overlay p-6 border border-subtle">
                  <h4 className="heading-3 text-white mb-6">Technologies</h4>
                  <div className="flex flex-wrap gap-2">
                    {currentProject.technologies?.map((tech, index) => (
                      <span 
                        key={index}
                        className="px-3 py-1 bg-brand-hover text-brand-primary body-small border border-brand-primary"
                      >
                        {tech}
                      </span>
                    ))}
                  </div>
                </div>

                <button 
                  onClick={() => {
                    const element = document.getElementById('contact');
                    if (element) {
                      element.scrollIntoView({ behavior: 'smooth' });
                    }
                  }}
                  className="btn-primary w-full"
                >
                  <span>View Case Study</span>
                  <ExternalLink className="w-5 h-5" />
                </button>
              </div>
            </div>
          </div>
        )}

        {/* Partners Section */}
        <div className="space-y-12">
          <div className="text-center">
            <h3 className="heading-2 text-white mb-6">Trusted Partners</h3>
            <p className="body-large text-secondary max-w-2xl mx-auto">
              Perusahaan-perusahaan terpercaya yang telah mempercayakan kebutuhan teknologi mereka kepada kami.
            </p>
          </div>

          <div className="grid md:grid-cols-2 gap-8">
            {partners.map((partner, index) => (
              <div key={index} className="bg-overlay p-8 border border-subtle dark-hover">
                <h4 className="heading-3 text-white mb-2">{partner.name}</h4>
                <p className="body-medium text-brand-primary mb-4">{partner.industry}</p>
                <p className="body-medium text-secondary">{partner.description}</p>
              </div>
            ))}
          </div>
        </div>
      </div>
    </section>
  );
};

export default ProjectsSection;