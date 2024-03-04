Certainly! Here's the API documentation incorporating all the provided routes, models, and services, along with dependencies, schema definitions, error handling, and success messages:

```markdown
# API Documentation

## Authentication

### Verify Token [GET]

- **URL:** `/verify-token`
- **Description:** Verifies the validity of a JWT token.
- **Request Headers:**
  - `Authorization`: Bearer Token
- **Responses:**
  - `200 OK`: Token is valid.
  - `401 Unauthorized`: Token is missing, invalid, or expired.

### Verify Asset [GET]

- **URL:** `/verify-asset/{asset_id}`
- **Description:** Verifies the ownership of an asset for a given user.
- **Request Headers:**
  - `Authorization`: Bearer Token
- **URL Parameters:**
  - `asset_id` (str, required): ID of the asset to be verified.
- **Responses:**
  - `200 OK`: Token and asset are valid.
  - `401 Unauthorized`: Token is missing, invalid, or expired.
  - `401 Unauthorized`: Asset ID is missing or not found for the user.

## User Routes

### Register User [POST]

- **URL:** `/register/`
- **Description:** Registers a new user.
- **Request Body:**
  ```json
  {
    "username": "string",
    "password": "string",
    "full_name": "string"
  }
  ```
- **Responses:**
  - `201 Created`: User registered successfully.
  - `400 Bad Request`: Invalid request body.
  - `401 Unauthorized`: Username already exists.
  - `500 Internal Server Error`: Error while creating user.

### Login User [POST]

- **URL:** `/login/`
- **Description:** Logs in a user.
- **Request Body:**
  ```json
  {
    "username": "string",
    "password": "string"
  }
  ```
- **Responses:**
  - `200 OK`: Login successful. Returns token and user ID.
  - `401 Unauthorized`: Incorrect password or user not found.
  - `500 Internal Server Error`: Error while authenticating user.

## Asset Routes

### Create Asset [POST]

- **URL:** `/asset/create/`
- **Description:** Creates a new asset.
- **Request Body:**
  ```json
  {
    "name": "string",
    "type": "string",
    "location": "string",
    "purchase_date": "string (dd/mm/yyyy)",
    "initial_cost": float,
    "operational_status": "string"
  }
  ```
- **Request Headers:**
  - `Authorization`: Bearer Token
- **Responses:**
  - `200 OK`: Asset created successfully.
  - `400 Bad Request`: Invalid request body.
  - `401 Unauthorized`: Token is missing, invalid, or expired.
  - `500 Internal Server Error`: Error while creating asset.

### Get Assets by User ID [GET]

- **URL:** `/asset/byuser/{user_id}`
- **Description:** Retrieves assets belonging to a user.
- **URL Parameters:**
  - `user_id` (str, required): ID of the user.
- **Request Headers:**
  - `Authorization`: Bearer Token
- **Responses:**
  - `200 OK`: Assets retrieved successfully.
  - `401 Unauthorized`: Token is missing, invalid, or expired.
  - `403 Forbidden`: Access forbidden.
  - `404 Not Found`: Assets not found.

### Get Assets by Name [GET]

- **URL:** `/asset/byname/{name}`
- **Description:** Retrieves assets by name.
- **URL Parameters:**
  - `name` (str, required): Name of the asset.
- **Request Headers:**
  - `Authorization`: Bearer Token
- **Responses:**
  - `200 OK`: Assets retrieved successfully.
  - `401 Unauthorized`: Token is missing, invalid, or expired.
  - `404 Not Found`: Assets not found.

### Get Assets by Type [GET]

- **URL:** `/asset/bytype/{type}`
- **Description:** Retrieves assets by type.
- **URL Parameters:**
  - `type` (str, required): Type of the asset.
- **Request Headers:**
  - `Authorization`: Bearer Token
- **Responses:**
  - `200 OK`: Assets retrieved successfully.
  - `401 Unauthorized`: Token is missing, invalid, or expired.
  - `404 Not Found`: Assets not found.

### Get Assets by Operational Status [GET]

- **URL:** `/asset/byoperational-status/{operational_status}`
- **Description:** Retrieves assets by operational status.
- **URL Parameters:**
  - `operational_status` (str, required): Operational status of the asset.
- **Request Headers:**
  - `Authorization`: Bearer Token
- **Responses:**
  - `200 OK`: Assets retrieved successfully.
  - `401 Unauthorized`: Token is missing, invalid, or expired.
  - `404 Not Found`: Assets not found.

### Get Assets by Location [GET]

- **URL:** `/asset/bylocation/{location}`
- **Description:** Retrieves assets by location.
- **URL Parameters:**
  - `location` (str, required): Location of the asset.
- **Request Headers:**
  - `Authorization`: Bearer Token
- **Responses:**
  - `200 OK`: Assets retrieved successfully.
  - `401 Unauthorized`: Token is missing, invalid, or expired.
  - `404 Not Found`: Assets not found.

### Get Assets by Purchase Date [POST]

- **URL:** `/asset/bydate/`
- **Description:** Retrieves assets by purchase date range.
- **Request Body:**
  ```json
  {
    "start_date": "string (dd/mm/yyyy)",
    "end_date": "string (dd/mm/yyyy)"
  }
  ```
- **Request Headers:**
  - `Authorization`: Bearer Token
- **Responses:**
  - `200 OK`: Assets retrieved successfully.
  - `401 Unauthorized`: Token is missing, invalid, or expired.
  - `404 Not Found`: Assets not found.

## Performance Metric Routes

### Create Performance Metric [POST]

- **URL:** `/performance_metric/create/`
- **Description:** Creates a new performance metric.
- **Request Body:**
  ```json
  {
    "asset_id": "string",
    "creation_date": "string (dd/mm/yyyy)",
    "uptime": float,
    "downtime": float,
    "maintenance_costs": float,
    "failure_rate": float,
    "efficiency": float
  }
  ```
- **Request Headers:**
  - `Authorization`: Bearer Token
- **Responses:**
  - `200 OK`: Performance metric created successfully.
  - `400 Bad Request`: Invalid request body.
  - `401 Unauthorized`: Token is missing, invalid, or expired.
  - `404 Not Found`: Performance metric already exists.
  - `500 Internal Server Error`: Error while creating performance metric.

### Get Performance Metrics by Date [POST]

- **URL:** `/performance_metric/bydate/`
- **Description:** Retrieves performance metrics by date range.
- **Request Body:**
  ```json
  {
    "asset_id": "string",
    "start_date": "string (dd/mm/yyyy