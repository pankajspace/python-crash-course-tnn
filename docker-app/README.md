### Build image
docker build -t docker-app .

### Run container
docker run -p 5000:5000 docker-app

### Access the app
```
Open your web browser and navigate to http://localhost:5000
You should see "Hello from Dockerized Python app!" displayed on the page.
```