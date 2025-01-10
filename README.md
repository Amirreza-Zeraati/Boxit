# Steam-like Platform with FastAPI

This project is a platform inspired by Steam, built using FastAPI, SQLAlchemy, and PostgreSQL. It includes features for managing users and games with a CRUD API. Docker is used for containerization, making deployment and setup simple.

---

## Project Structure

```plaintext
steam-fastapi
├── .env                      # Environment variables
├── docker-compose.app.yml    # Docker Compose file for the application
├── docker-compose.db.yml     # Docker Compose file for the database
├── Dockerfile                # Dockerfile for building the application container
├── main.py                   # Main FastAPI application
├── requirements.txt          # Python dependencies
```

---

## Features

### User Management
- Create, read, update, and delete user profiles.
- Includes additional fields like wallet balance, profile picture, and account creation date.

### Game Management
- Manage a catalog of games with CRUD functionality.
- Includes game metadata such as title, description, price, release date, developer, publisher, genre, rating, and cover image.

---

## Prerequisites

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)
- Python 3.12

---

## Setup and Installation

### 1. Clone the Repository
```bash
git clone https://github.com/Amirreza-Zeraati/steam-fastapi.git
cd steam-fastapi
```

### 2. Configure Environment Variables
Create a `.env` file in the root directory with the following content:

```env
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_DB=steam
DATABASE_HOST=db
DATABASE_PORT=5432
```


### 3. Build and Run the Application with Docker

#### Step 1: Start the Database
```bash
docker-compose -f docker-compose.db.yml up -d
```

#### Step 2: Start the Application
```bash
docker-compose -f docker-compose.app.yml up --build
```

---

## API Endpoints

### User Endpoints
- `POST /users/` - Create a new user
- `GET /users/` - List all users
- `GET /users/{user_id}` - Retrieve a specific user by ID
- `PUT /users/{user_id}` - Update a user by ID
- `DELETE /users/{user_id}` - Delete a user by ID

### Game Endpoints
- `POST /games/` - Create a new game
- `GET /games/` - List all games
- `GET /games/{game_id}` - Retrieve a specific game by ID
- `PUT /games/{game_id}` - Update a game by ID
- `DELETE /games/{game_id}` - Delete a game by ID

---

## Example Requests

### Create a User
**Request:**
```json
{
  "name": "John Doe",
  "email": "john.doe@example.com",
  "password": "securepassword123",
  "is_active": true
}
```

**Response:**
```json
{
  "id": 1,
  "name": "John Doe",
  "email": "john.doe@example.com",
  "is_active": true,
  "wallet_balance": 0,
  "profile_picture": null,
  "created_at": "2025-01-10T14:30:00"
}
```

### Create a Game
**Request:**
```json
{
  "title": "Epic Adventure",
  "description": "A thrilling open-world adventure game.",
  "price": 60,
  "release_date": "2025-03-01",
  "developer": "GameStudioX",
  "publisher": "Epic Games",
  "genre": "Adventure",
  "rating": 5,
  "cover_image": "https://example.com/images/epic_adventure.png"
}
```

**Response:**
```json
{
  "id": 1,
  "title": "Epic Adventure",
  "description": "A thrilling open-world adventure game.",
  "price": 60,
  "release_date": "2025-03-01",
  "developer": "GameStudioX",
  "publisher": "Epic Games",
  "genre": "Adventure",
  "rating": 5,
  "cover_image": "https://example.com/images/epic_adventure.png"
}
```

---

## Testing
You can test the API using tools like [Postman](https://www.postman.com/)

---

## Contributing
Feel free to fork the repository and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

---
