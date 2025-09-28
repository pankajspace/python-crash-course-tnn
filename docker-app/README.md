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

### Node.js & npm (For Task Management)
- **Node.js**: [Install Node.js](https://nodejs.org/) (includes npm)
- **Fedora**: `sudo dnf install nodejs npm`
- **Ubuntu/Debian**: `sudo apt install nodejs npm`
- **CentOS/RHEL**: `sudo yum install nodejs npm`
- **macOS**: Download from nodejs.org or use Homebrew (`brew install node`)
- **Windows**: Download from nodejs.org

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

### 2. Install npm Dependencies (One-time setup)
```bash
npm install
```

### 3. Build the Docker Environment
```bash
# Using npm scripts (recommended)
npm run build

# OR using Docker Compose directly
docker-compose build
```

### 4. Run the Application
```bash
# Using npm scripts
npm start

# OR using Docker Compose directly
docker-compose up app
```

**🌐 Access your app at:** http://localhost:5000

### 5. Stop the Application
```bash
# Press Ctrl+C in the terminal, or in another terminal:
docker-compose down
```

## 📦 Managing Python Dependencies (No Global Installs!)

### Adding New Libraries

#### Method 1: Using npm Scripts (Easiest)
```bash
# Add a single package
npm run install-package requests

# Add multiple packages at once
npm run install-package "requests pandas numpy matplotlib"

# Add a specific version
npm run install-package "django==4.2.0"
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
   npm run build
   # OR
   docker-compose build
   ```

### Removing Libraries
```bash
# Using npm scripts
npm run remove-package requests

# Using Docker Compose directly
docker-compose run --rm dev pip uninstall -y requests
docker-compose run --rm dev pip freeze > requirements.txt
```

### Viewing Installed Packages
```bash
# See all installed packages
npm run list-packages

# OR
docker-compose run --rm dev pip list
```

## 🛠️ Development Commands

| Command               | npm Scripts     | Docker Compose                                  | Description                       |
| --------------------- | --------------- | ----------------------------------------------- | --------------------------------- |
| **Build**             | `npm run build` | `docker-compose build`                          | Build/rebuild the Docker image    |
| **Run App**           | `npm start`     | `docker-compose up app`                         | Start the Flask application       |
| **Interactive Shell** | `npm run shell` | `docker-compose run --rm dev /bin/bash`         | Get a bash shell inside container |
| **View Logs**         | `npm run logs`  | `docker-compose logs -f app`                    | View application logs             |
| **Stop App**          | `Ctrl+C`        | `docker-compose down`                           | Stop the running application      |
| **Clean Up**          | `npm run clean` | `docker-compose down && docker system prune -f` | Remove containers and cleanup     |
| **Help**              | `npm run help`  | -                                               | Show all available commands       |

### 🖥️ Interactive Development Shell
```bash
# Get inside the container for testing/debugging
npm run shell

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
├── package.json          # npm scripts and project metadata
├── scripts/              # Helper scripts for npm commands
│   ├── install-package.js # Script to install Python packages
│   └── remove-package.js  # Script to remove Python packages
├── Dockerfile            # Docker image definition (uses python:3.11-slim base)
├── docker-compose.yml    # Multi-container setup
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
npm run build

# 2. Need a new library? Add it
npm run install-package requests

# 3. Start developing
npm start

# 4. Open another terminal for interactive testing
npm run shell
```

### Daily Development
```bash
# 1. Start your app (auto-reloads on file changes)
npm start

# 2. Edit your Python files normally
# 3. Changes are reflected immediately (volume mounting)
# 4. View logs if needed
npm run logs
```

### Debugging
```bash
# Get an interactive Python shell with all your packages
npm run shell
python

# Or run specific Python files
npm run shell
python your_script.py
```

## ⭐ Key Benefits

### ✅ Clean Development Environment
- **No Global Installs**: Python packages stay in Docker containers
- **System Protection**: Your laptop's Python environment stays untouched
- **Easy Cleanup**: Remove everything with `npm run clean`

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
npm run clean
npm run build
```

## 📋 Available npm Commands

Run `npm run help` to see all available commands, or use these directly:

```bash
npm run build              # Build Docker image
npm start                  # Run the application
npm run dev                # Run in development mode
npm run shell              # Interactive container shell
npm run logs               # View application logs
npm run clean              # Clean up containers and images
npm run list-packages      # Show installed packages
npm run install-requirements  # Install all requirements
npm run install-package <package>  # Install a specific package
npm run remove-package <package>   # Remove a specific package
npm run help               # Show this help message
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