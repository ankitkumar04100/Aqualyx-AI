# 🚀 Deployment Guide – Aqualyx AI

---

## 🐳 Docker Deployment

Build Image:

docker build -t aqualyx-backend .

Run Container:

docker run -p 8000:8000 aqualyx-backend

---

## ☁️ Backend Deployment (Render)

1. Connect GitHub repository
2. Select backend folder
3. Add environment variables
4. Deploy
5. Use generated public URL

---

## 🌐 Frontend Deployment (Vercel)

1. Connect repository
2. Select frontend directory
3. Set API base URL
4. Deploy

---

## 🔐 Environment Variables

Create `.env` file:

DATABASE_URL=sqlite:///./aqualyx.db
MODEL_PATH=ml/model.pkl
SECRET_KEY=your_secret_key

---

## 🧪 Testing After Deployment

Visit:

/health → Verify service status  
/predict → Send test payload  
/metrics → Validate model performance  

---

## 📈 Production Recommendations

- Switch SQLite → PostgreSQL
- Enable HTTPS
- Add rate limiting
- Use CI/CD pipeline
- Enable monitoring (Prometheus)

---

## 🌍 Scaling Strategy

Phase 1: Campus Deployment  
Phase 2: Multi-building monitoring  
Phase 3: Smart City Integration  
Phase 4: IoT Sensor Integration
