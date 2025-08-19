import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import logging
from typing import Dict, Any

logger = logging.getLogger(__name__)

async def send_contact_notification(contact_data: Dict[str, Any]):
    """Send email notification when contact form is submitted"""
    try:
        # Get SMTP configuration from environment
        smtp_host = os.getenv("SMTP_HOST", "localhost")
        smtp_port = int(os.getenv("SMTP_PORT", "587"))
        smtp_user = os.getenv("SMTP_USER", "")
        smtp_pass = os.getenv("SMTP_PASS", "")
        admin_email = os.getenv("ADMIN_EMAIL", "info@mabratech.co.id")
        
        if not smtp_user or not smtp_pass:
            logger.warning("SMTP credentials not configured, skipping email notification")
            return
        
        # Create message
        msg = MIMEMultipart()
        msg['From'] = smtp_user
        msg['To'] = admin_email
        msg['Subject'] = f"New Contact Form Submission - {contact_data.get('service', 'General Inquiry')}"
        
        # Create email body
        body = f"""
New contact form submission received from the Mabratech website:

Name: {contact_data.get('name', 'N/A')}
Email: {contact_data.get('email', 'N/A')}
Phone: {contact_data.get('phone', 'N/A')}
Company: {contact_data.get('company', 'N/A')}
Service Interest: {contact_data.get('service', 'N/A')}

Message:
{contact_data.get('message', 'N/A')}

Submission Details:
- Time: {contact_data.get('created_at', 'N/A')}
- IP Address: {contact_data.get('ip_address', 'N/A')}
- User Agent: {contact_data.get('user_agent', 'N/A')}

Please respond to this inquiry at your earliest convenience.

Best regards,
Mabratech Website System
        """
        
        msg.attach(MIMEText(body, 'plain'))
        
        # Connect to server and send email
        server = smtplib.SMTP(smtp_host, smtp_port)
        server.starttls()
        server.login(smtp_user, smtp_pass)
        text = msg.as_string()
        server.sendmail(smtp_user, admin_email, text)
        server.quit()
        
        logger.info(f"Contact notification email sent for submission from {contact_data.get('email')}")
        
        # Send auto-reply to customer
        await send_auto_reply(contact_data, smtp_host, smtp_port, smtp_user, smtp_pass)
        
    except Exception as e:
        logger.error(f"Error sending contact notification email: {e}")

async def send_auto_reply(contact_data: Dict[str, Any], smtp_host: str, smtp_port: int, smtp_user: str, smtp_pass: str):
    """Send auto-reply to customer"""
    try:
        customer_email = contact_data.get('email')
        if not customer_email:
            return
            
        # Create auto-reply message
        msg = MIMEMultipart()
        msg['From'] = smtp_user
        msg['To'] = customer_email
        msg['Subject'] = "Terima kasih atas minat Anda - PT Mabra Technology Solutions"
        
        # Create auto-reply body
        body = f"""
Halo {contact_data.get('name', '')},

Terima kasih telah menghubungi PT Mabra Technology Solutions!

Kami telah menerima pesan Anda mengenai {contact_data.get('service', 'layanan kami')} dan akan segera menindaklanjutinya. Tim kami akan menghubungi Anda dalam waktu 1x24 jam untuk membahas kebutuhan teknologi perusahaan Anda.

Ringkasan pesan Anda:
- Layanan yang diminati: {contact_data.get('service', 'N/A')}
- Perusahaan: {contact_data.get('company', 'N/A')}

Sementara menunggu respons dari tim kami, Anda dapat:
- Melihat portofolio proyek kami di website
- Menghubungi kami langsung di (022) 20668716
- Mengunjungi kantor kami di Jl. Canon No. 5 A-6 Cipageran Cimahi

Hormat kami,
Tim PT Mabra Technology Solutions

---
PT Mabra Technology Solutions
Jl. Canon No. 5 A-6 Cipageran Cimahi
Phone: (022) 20668716
Email: info@mabratech.co.id
Website: www.mabratech.co.id

"Penyedia solusi teknologi informasi yang inovatif, handal, dan terpercaya"
        """
        
        msg.attach(MIMEText(body, 'plain'))
        
        # Send auto-reply
        server = smtplib.SMTP(smtp_host, smtp_port)
        server.starttls()
        server.login(smtp_user, smtp_pass)
        text = msg.as_string()
        server.sendmail(smtp_user, customer_email, text)
        server.quit()
        
        logger.info(f"Auto-reply sent to {customer_email}")
        
    except Exception as e:
        logger.error(f"Error sending auto-reply email: {e}")