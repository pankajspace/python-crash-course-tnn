# Docker App - Development Setup

This Flask application is containerized with Docker to avoid installing Python dependencies globally on your laptop. Everything runs inside Docker containers, keeping your system clean!

## Prerequisites

Before you start, make sure you have installed:

### Docker & Docker Compose
- **Docker**: [Install Docker](https://docs.docker.com/get-docker/)
- **Docker Compose**: Usually comes with Docker Desktop

#### OS-Specific Docker Installation:
- **Fedora 42**: `sudo dnf install docker docker-compose-plugin`
- **Ubuntu/Debian**: `sudo apt install docker.io docker-compose-plugin`
- **CentOS/RHEL**: `sudo yum install docker docker-compose-plugin`
- **macOS**: Download Docker Desktop
- **Windows**: Download Docker Desktop

### Make (Optional but Recommended)
- **Fedora**: `sudo dnf install make`
- **Ubuntu/Debian**: `sudo apt install make`
- **CentOS/RHEL**: `sudo yum install make`
- **macOS**: Comes with Xcode Command Line Tools (`xcode-select --install`)
- **Windows**: Use WSL2 or install via Chocolatey (`choco install make`)

### Start Docker Service (Linux only)
```bash
# For Fedora/CentOS/RHEL
sudo systemctl start docker
sudo systemctl enable docker

# Add your user to docker group (logout/login required)
sudo usermod -aG docker $USER
```

## 🚀 Getting Started

### 1. Clone and Navigate
```bash
cd /path/to/python-crash-course-tnn/docker-app
```

### 2. Build the Docker Environment
```bash
# Using Make (recommended)
make build

# OR using Docker Compose directly
docker-compose build
```

### 3. Run the Application
```bash
# Using Make
make run

# OR using Docker Compose directly
docker-compose up app
```

**🌐 Access your app at:** http://localhost:5000

### 4. Stop the Application
```bash
# Press Ctrl+C in the terminal, or in another terminal:
docker-compose down
```

## 📦 Managing Python Dependencies (No Global Installs!)

### Adding New Libraries

#### Method 1: Using Make Commands (Easiest)
```bash
# Add a single package
make install-package PACKAGE=requests

# Add multiple packages at once
make install-package PACKAGE="requests pandas numpy matplotlib"

# Add a specific version
make install-package PACKAGE="django==4.2.0"
```

#### Method 2: Using Docker Compose Directly
```bash
# Install a package
docker-compose run --rm dev pip install requests

# Update requirements.txt after installation
docker-compose run --rm dev pip freeze > requirements.txt
```

#### Method 3: Edit requirements.txt and Rebuild
1. Add your packages to `requirements.txt`:
   ```
   flask==3.0.3
   requests==2.31.0
   pandas==2.1.0
   ```
2. Rebuild the container:
   ```bash
   make build
   # OR
   docker-compose build
   ```

### Removing Libraries
```bash
# Using Make
make remove-package PACKAGE=requests

# Using Docker Compose directly
docker-compose run --rm dev pip uninstall -y requests
docker-compose run --rm dev pip freeze > requirements.txt
```

### Viewing Installed Packages
```bash
# See all installed packages
make list-packages

# OR
docker-compose run --rm dev pip list
```

## 🛠️ Development Commands

| Command               | Make         | Docker Compose                                  | Description                       |
| --------------------- | ------------ | ----------------------------------------------- | --------------------------------- |
| **Build**             | `make build` | `docker-compose build`                          | Build/rebuild the Docker image    |
| **Run App**           | `make run`   | `docker-compose up app`                         | Start the Flask application       |
| **Interactive Shell** | `make shell` | `docker-compose run --rm dev /bin/bash`         | Get a bash shell inside container |
| **View Logs**         | `make logs`  | `docker-compose logs -f app`                    | View application logs             |
| **Stop App**          | `Ctrl+C`     | `docker-compose down`                           | Stop the running application      |
| **Clean Up**          | `make clean` | `docker-compose down && docker system prune -f` | Remove containers and cleanup     |

### 🖥️ Interactive Development Shell
```bash
# Get inside the container for testing/debugging
make shell

# Now you can run Python commands with all your dependencies:
# python
# >>> import requests
# >>> import pandas
# >>> # Test your code interactively!
```

## 📁 Project Structure
```
docker-app/
├── app.py                 # Your Flask application
├── requirements.txt       # Python dependencies
├── Dockerfile            # Docker image definition (uses python:3.11-slim base)
├── docker-compose.yml    # Multi-container setup
├── Makefile             # Convenient commands
├── .dockerignore        # Files to ignore in Docker
└── README.md           # This file
```

## 🐳 Docker Base Image & Cross-Platform Compatibility

### Base Image Used
This project uses **`python:3.11-slim`** as the base image, which is:
- **OS**: Debian-based Linux (inside the container)
- **Python**: Version 3.11
- **Size**: Optimized slim version (~45MB vs ~380MB for full image)
- **Architecture**: Supports AMD64, ARM64 (works on Intel, AMD, Apple Silicon)

### Why This Works on All Operating Systems
🎯 **Key Point**: Your **host OS doesn't matter**! Docker containers are isolated.

| Your Host OS  | Container OS  | Works? | Notes                                |
| ------------- | ------------- | ------ | ------------------------------------ |
| **Fedora 42** | Debian (slim) | ✅ Yes  | Your case - works perfectly!         |
| **Ubuntu**    | Debian (slim) | ✅ Yes  | Same Linux family                    |
| **Windows**   | Debian (slim) | ✅ Yes  | Docker Desktop handles compatibility |
| **macOS**     | Debian (slim) | ✅ Yes  | Docker Desktop + virtualization      |
| **CentOS**    | Debian (slim) | ✅ Yes  | Different Linux distro, no problem   |

### Container vs Host OS
```bash
# Your Fedora 42 system
$ cat /etc/os-release
NAME="Fedora Linux"
VERSION="42"

# Inside the Docker container (python:3.11-slim)
$ docker run --rm python:3.11-slim cat /etc/os-release
NAME="Debian GNU/Linux"
VERSION="12 (bookworm)"
```

## 🔄 Typical Development Workflow

### Starting a New Feature
```bash
# 1. Make sure you have the latest image
make build

# 2. Need a new library? Add it
make install-package PACKAGE=requests

# 3. Start developing
make run

# 4. Open another terminal for interactive testing
make shell
```

### Daily Development
```bash
# 1. Start your app (auto-reloads on file changes)
make run

# 2. Edit your Python files normally
# 3. Changes are reflected immediately (volume mounting)
# 4. View logs if needed
make logs
```

### Debugging
```bash
# Get an interactive Python shell with all your packages
make shell
python

# Or run specific Python files
make shell
python your_script.py
```

## ⭐ Key Benefits

### ✅ Clean Development Environment
- **No Global Installs**: Python packages stay in Docker containers
- **System Protection**: Your laptop's Python environment stays untouched
- **Easy Cleanup**: Remove everything with `make clean`

### ✅ Consistent Environment
- **Same for Everyone**: Team members use identical environments
- **Version Control**: `requirements.txt` tracks exact package versions
- **Reproducible**: Works the same on any machine with Docker

### ✅ Easy Package Management
- **Automatic Updates**: `requirements.txt` updates automatically
- **Safe Experimentation**: Test packages without affecting your system
- **Quick Rollback**: Rebuild from `requirements.txt` anytime

## 🐛 Troubleshooting

### Container Won't Start?
```bash
# Check if port 5000 is already in use
sudo netstat -tlnp | grep :5000

# Use a different port if needed (edit docker-compose.yml)
# Change "5000:5000" to "5001:5000"
```

### Package Installation Fails?
```bash
# Try building with no cache
docker-compose build --no-cache

# Or check if you need system dependencies
# Edit Dockerfile to add: RUN apt-get install -y package-name
```

### Need to Reset Everything?
```bash
# Nuclear option - removes everything and starts fresh
make clean
make build
```

## 🚀 Advanced Usage

### Changing Docker Base Image (Optional)

Current Dockerfile uses `python:3.11-slim`. You can modify it if needed:

```dockerfile
# Current (Recommended for Flask)
FROM python:3.11-slim

# Alternatives:
FROM python:3.11-alpine    # Smaller (~15MB) but may need extra packages
FROM python:3.11           # Full version (~380MB) with more tools
FROM python:3.12-slim      # Newer Python version
FROM python:3.10-slim      # Older Python version for compatibility
```

**For Flask apps, `python:3.11-slim` is perfect because:**
- Small size (good for deployment)
- Has necessary libraries pre-installed
- Debian-based (easy package management)
- Well-tested and stable

### Custom Environment Variables
Edit `docker-compose.yml` to add environment variables:
```yaml
environment:
  - FLASK_ENV=development
  - DATABASE_URL=postgresql://...
  - API_KEY=your-secret-key
```

### Multiple Services
Add more services to `docker-compose.yml`:
```yaml
services:
  app:
    # ... existing app config

  database:
    image: postgres:13
    environment:
      POSTGRES_DB: myapp

  redis:
    image: redis:alpine
```