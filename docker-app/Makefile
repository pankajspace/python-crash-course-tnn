# Docker Development Commands

.PHONY: build run dev install-package remove-package shell logs clean

# Build the Docker image
build:
	docker-compose build

# Run the application
run:
	docker-compose up app

# Run in development mode with file watching
dev:
	docker-compose up app

# Install a new package (usage: make install-package PACKAGE=requests)
install-package:
	@echo "Installing $(PACKAGE)..."
	docker-compose run --rm dev pip install $(PACKAGE)
	docker-compose run --rm dev pip freeze > requirements.txt
	@echo "$(PACKAGE) installed and requirements.txt updated!"

# Remove a package (usage: make remove-package PACKAGE=requests)
remove-package:
	@echo "Removing $(PACKAGE)..."
	docker-compose run --rm dev pip uninstall -y $(PACKAGE)
	docker-compose run --rm dev pip freeze > requirements.txt
	@echo "$(PACKAGE) removed and requirements.txt updated!"

# Get an interactive shell inside the container
shell:
	docker-compose run --rm dev /bin/bash

# Show application logs
logs:
	docker-compose logs -f app

# Clean up containers and images
clean:
	docker-compose down
	docker system prune -f

# Show installed packages
list-packages:
	docker-compose run --rm dev pip list

# Install all requirements
install-requirements:
	docker-compose run --rm dev pip install -r requirements.txt