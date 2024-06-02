# EcoTrack_app
# Task: RESTful API for Sensor Goods Monitoring

**Customer:** EcoTrack

## Task Description

EcoTrack develops a platform for monitoring and managing environmental data from various sensors and devices. Currently, the company needs a system to manage data on air quality.
Task is to develop a RESTful API based on the provided specification to manage a list of air quality sensors. The API should allow sensors to be created, read, updated, and deleted. The API specification should be well documented using tools such as Swagger or OpenAPI.
Provide support for standard HTTP methods (GET, POST, PUT, DELETE) for each resource.
Implement error handling and return appropriate HTTP statuses and messages.

## Requirements

- **API Documentation:** Swagger
- **HTTP Methods:** GET, POST, PUT, DELETE
- **Authentication:** Access Tokens
- **Error Handling:** Appropriate HTTP statuses and messages
- **Data Format:** JSON
- **Data Consistency:** Transaction mechanisms

## Restrictions

- Must use Django REST Framework and PostgreSQL for Backend Track.

## Q&A

- **Security:** Access Tokens for authentication and role-based access.
- **Performance:** Data caching, query optimization, and horizontal scaling.
- **Testing:** Unit and integration testing using unittest.
- **Data Format:** JSON for data exchange.
- **Data Consistency:** Database transactions for integrity.

## Screenshots

1. **API Endpoints Overview:**
   ![API Endpoints Overview](/screenshots/Screenshot2024-06-01at19.11.10.png)
   ![API Endpoints Overview]()
   ![API Endpoints Overview]()
   ![API Endpoints Overview]()


2. **Tests:**
   ![Tests](/screenshots/Screenshot2024-06-01at17.47.30.png)


3. **Project configs:**
   Docker-compose
   ![Docker-compose](/screenshots/Screenshot2024-06-01at18.10.31.png)
   ![Docker-compose](/screenshots/Screenshot2024-06-01at18.10.47.png)
   ![Docker-compose](/screenshots/Screenshot2024-06-01at18.10.54.png)


4. **Database Schema:**
   ![Database Schema]()

## Video Presentation

For a detailed demonstration of the project, please refer to the video linked below. This video walks through the setup, key features, and functionalities of the API:
https://drive.google.com/drive/folders/1BR_qLzhz5P1JVFfpLAKOqZHvO-NuY4hR?usp=sharing

## Deploy on Free Cloud Server (Render):
(Since it's a free server, it could work very slow. Sorry for that T_T)
https://ecotrack-izrf.onrender.com
Credentials to log in to admin panel are
'admin' for username and
'1' for password.