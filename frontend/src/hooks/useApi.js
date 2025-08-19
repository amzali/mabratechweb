import { useState, useEffect } from 'react';
import axios from 'axios';

const BACKEND_URL = process.env.REACT_APP_BACKEND_URL;
const API = `${BACKEND_URL}/api`;

// Create axios instance with default config
const api = axios.create({
  baseURL: API,
  timeout: 10000,
  headers: {
    'Content-Type': 'application/json',
  },
});

// Custom hook for API calls
export const useApi = (url, options = {}) => {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    if (!url) return;

    const fetchData = async () => {
      try {
        setLoading(true);
        setError(null);
        
        const response = await api.get(url, options);
        setData(response.data);
      } catch (err) {
        setError(err.response?.data?.detail || err.message || 'An error occurred');
        console.error('API Error:', err);
      } finally {
        setLoading(false);
      }
    };

    fetchData();
  }, [url]);

  return { data, loading, error, refetch: () => window.location.reload() };
};

// Hook for services
export const useServices = () => {
  const { data, loading, error } = useApi('/services');
  return {
    services: data?.services || [],
    loading,
    error
  };
};

// Hook for products  
export const useProducts = () => {
  const { data, loading, error } = useApi('/products');
  return {
    products: data?.products || [],
    loading,
    error
  };
};

// Hook for projects
export const useProjects = () => {
  const { data, loading, error } = useApi('/projects');
  return {
    projects: data?.projects || [],
    loading,
    error
  };
};

// Hook for contact form submission
export const useContactForm = () => {
  const [submitting, setSubmitting] = useState(false);
  const [submitResult, setSubmitResult] = useState(null);

  const submitContact = async (contactData) => {
    try {
      setSubmitting(true);
      setSubmitResult(null);

      const response = await api.post('/contacts', contactData);
      
      setSubmitResult({
        success: true,
        message: response.data.message
      });

      // Track analytics
      await trackEvent('contact_form', 'contact', {
        service: contactData.service,
        company: contactData.company
      });

      return response.data;
    } catch (err) {
      const errorMessage = err.response?.data?.detail || 'Terjadi kesalahan. Silakan coba lagi.';
      
      setSubmitResult({
        success: false,
        message: errorMessage
      });

      throw new Error(errorMessage);
    } finally {
      setSubmitting(false);
    }
  };

  return {
    submitContact,
    submitting,
    submitResult,
    clearResult: () => setSubmitResult(null)
  };
};

// Analytics tracking
export const trackEvent = async (eventType, page, metadata = {}) => {
  try {
    await api.post('/analytics/page-view', {
      type: eventType,
      page: page,
      metadata: metadata
    });
  } catch (err) {
    // Don't throw error for analytics failures
    console.warn('Analytics tracking failed:', err);
  }
};

// Track page views
export const usePageTracking = () => {
  useEffect(() => {
    const trackPageView = async () => {
      const page = window.location.pathname;
      await trackEvent('page_view', page, {
        title: document.title,
        referrer: document.referrer
      });
    };

    trackPageView();
  }, []);
};

export default api;