# 🔒 Security Policy

## 🛡️ Aqualyx AI Security Commitment

Aqualyx AI is committed to maintaining secure, reliable, and responsible software practices.  
We prioritize data protection, secure model inference, and responsible AI deployment.

---

## 📢 Reporting a Vulnerability

If you discover a security vulnerability, please report it responsibly:

📧 Email: ankitkumarforall@gmail.com  
Subject: [Security Vulnerability] Aqualyx AI  

Please include:

- Description of the issue
- Steps to reproduce
- Potential impact
- Screenshots (if applicable)

We aim to respond within **48 hours**.

---

## 🔐 Security Measures Implemented

### Backend Security
- Input validation via **Pydantic schemas**
- Strict type enforcement
- Error handling without exposing internal stack traces
- CORS configuration restrictions
- Environment-based configuration management

### Model Security
- Model file stored server-side only
- No client-side ML exposure
- Inference sandboxed inside backend service

### Infrastructure Security
- Docker containerization
- Isolated backend/frontend services
- Environment variables for sensitive configs
- Production deployment via HTTPS (Render/Vercel)

---

## 🔎 Dependency Management

We use:
- `pip freeze` for locked Python versions
- `npm audit` for frontend dependency scanning
- Regular dependency updates

---

## ⚠️ Responsible Disclosure

We request that researchers:
- Do not exploit vulnerabilities
- Do not access or modify user data
- Allow time for patching before public disclosure

---

Thank you for helping keep Aqualyx AI secure.
