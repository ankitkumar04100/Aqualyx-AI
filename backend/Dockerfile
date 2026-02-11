# ===============================
# Base Image
# ===============================
FROM python:3.11-slim

# ===============================
# Environment Variables
# ===============================
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PORT=8000

# ===============================
# Set Work Directory
# ===============================
WORKDIR /app

# ===============================
# Install System Dependencies
# ===============================
RUN apt-get update && apt-get install -y \
    build-essential \
    gcc \
    curl \
    && rm -rf /var/lib/apt/lists/*

# ===============================
# Install Python Dependencies
# ===============================
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# ===============================
# Copy Application Code
# ===============================
COPY . .

# ===============================
# Expose Port
# ===============================
EXPOSE 8000

# ===============================
# Run Application (Production)
# ===============================
CMD ["gunicorn", "main:app", \
     "-k", "uvicorn.workers.UvicornWorker", \
     "--bind", "0.0.0.0:8000", \
     "--workers", "2"]
