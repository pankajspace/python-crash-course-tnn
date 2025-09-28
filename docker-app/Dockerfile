# Use official slim Python image (Debian-based, works on all host OS)
# python:3.11-slim = Python 3.11 + Debian 12 + optimized size (~45MB)
# Alternative options: python:3.11-alpine (smaller), python:3.11 (full version)
FROM python:3.11-slim

# Set working directory inside container
WORKDIR /app

# Prevent Python from writing .pyc and enable unbuffered logs
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install system dependencies (if needed)
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy dependencies and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code
COPY . .

# Expose app port
EXPOSE 5000

# Run the app
CMD ["python", "app.py"]
