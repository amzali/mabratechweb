import React from "react";
import { Target, Eye, Users } from "lucide-react";

const AboutSection = () => {
  return (
    <section id="about" className="py-32 relative">
      <div className="absolute inset-0 opacity-3">
        <div className="grid-pattern"></div>
      </div>
      
      <div className="dark-content-container relative z-10">
        {/* Section Header */}
        <div className="text-center space-y-6 mb-20">
          <h2 className="display-large text-white">Tentang Mabratech</h2>
          <p className="body-large text-secondary max-w-4xl mx-auto">
            Mabra Technology Solutions adalah perusahaan yang bergerak di bidang teknologi informatika 
            dengan kegiatan usaha meliputi jasa di bidang telematika, perencanaan perakitan dan 
            pengembangan software aplikasi komputer dan perdagangan.
          </p>
        </div>

        {/* Company Overview */}
        <div className="bg-secondary p-12 rounded-none mb-20 border border-subtle">
          <div className="grid md:grid-cols-2 gap-12">
            <div>
              <h3 className="heading-2 text-white mb-6">Company Overview</h3>
              <p className="body-medium text-secondary mb-6">
                Didirikan pada tanggal 27 April 2016, meskipun baru berdiri Mabratech memiliki 
                sumber daya manusia yang punya kapabilitas serta pengalaman dalam berbagai 
                pengembangan software.
              </p>
              <p className="body-medium text-secondary">
                Mabratech lahir dengan semangat membagi solusi teknologi yang dapat memberikan 
                nilai tambah maksimal bagi semua pemangku kepentingan baik perseorangan atau perusahaan.
              </p>
            </div>
            <div className="space-y-8">
              <div className="border-l-4 border-brand-primary pl-6">
                <div className="heading-3 text-brand-primary mb-2">Founded</div>
                <div className="body-medium text-secondary">27 April 2016</div>
              </div>
              <div className="border-l-4 border-brand-primary pl-6">
                <div className="heading-3 text-brand-primary mb-2">Legal Entity</div>
                <div className="body-medium text-secondary">
                  Akta Pendirian Nomor 04 oleh Notaris Fetty Siti Savitri, SH
                </div>
              </div>
              <div className="border-l-4 border-brand-primary pl-6">
                <div className="heading-3 text-brand-primary mb-2">NPWP</div>
                <div className="body-medium text-secondary">76.241.770.7.428.000</div>
              </div>
            </div>
          </div>
        </div>

        {/* Vision & Mission */}
        <div className="grid lg:grid-cols-2 gap-16">
          {/* Vision */}
          <div className="space-y-8">
            <div className="flex items-center space-x-4 mb-8">
              <div className="w-12 h-12 bg-brand-primary flex items-center justify-center">
                <Eye className="w-6 h-6 text-black" />
              </div>
              <h3 className="heading-2 text-white">Visi</h3>
            </div>
            <div className="bg-overlay p-8 border border-subtle">
              <p className="body-large text-white mb-4">
                Menjadi penyedia solusi teknologi informasi yang inovatif, handal, dan terpercaya.
              </p>
              <p className="body-medium text-secondary italic">
                "To be provider of information technology solutions that are innovative, 
                reliable, and trustworthy."
              </p>
            </div>
          </div>

          {/* Mission */}
          <div className="space-y-8">
            <div className="flex items-center space-x-4 mb-8">
              <div className="w-12 h-12 bg-brand-primary flex items-center justify-center">
                <Target className="w-6 h-6 text-black" />
              </div>
              <h3 className="heading-2 text-white">Misi</h3>
            </div>
            <div className="space-y-6">
              <div className="bg-overlay p-6 border-l-4 border-brand-primary">
                <p className="body-medium text-secondary">
                  Menciptakan inovasi teknologi berkualitas dan bermanfaat bagi semua pelanggan
                </p>
              </div>
              <div className="bg-overlay p-6 border-l-4 border-brand-primary">
                <p className="body-medium text-secondary">
                  Memberikan kemudahan dalam proses kerja semua pemangku kepentingan pada sebuah perusahaan
                </p>
              </div>
              <div className="bg-overlay p-6 border-l-4 border-brand-primary">
                <p className="body-medium text-secondary">
                  Membangun suasana nyaman dalam bekerja demi terlahirnya kreatifitas yang orisinil
                </p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
};

export default AboutSection;