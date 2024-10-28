# Base Project with FastAPI

This is a base project for building systems in Python using FastAPI. It includes configurations for Docker, linting, automated testing, SQLAlchemy for database integration, and a `BaseRepository` class with generic CRUD methods.

## Technologies

- **Python** (version 3.9+)
- **FastAPI** - Web framework for building APIs
- **Docker** - For containerization and easy deployment
- **SQLAlchemy** - ORM for database integration
- **Alembic** - For database migrations
- **Pytest** - For automated testing
- **Flake8** and **Black** - Tools for linting and code formatting

## Project Structure

```plaintext
├── app
│   ├── __init__.py
│   ├── main.py              # API configuration
│   ├── core
│   │   ├── config.py        # Application settings
│   │   └── database.py      # Database configuration with SQLAlchemy
│   ├── models
│   │   └── user.py          # Example User model
│   ├── repositories
│   │   └── base.py          # BaseRepository class with generic CRUD methods
│   └── tests                # Automated tests with Pytest
│       └── test_user.py
├── alembic                  # Directory for migrations
│   └── versions             # Generated Alembic migrations
├── Dockerfile               # Dockerfile for containerization
├── docker-compose.yml       # Docker Compose configuration
├── requirements.txt         # Application dependencies
└── README.md                # Project documentation
```

## Para rodar o Projeto:

### 1. Crie e configura o .env.

``` json
    touch .env   
```

### 2. Builder no docker.

``` json
    docker-compose build   
```

### 3. Suba o container

``` json
    docker-compose up   
```

This README provides a structured and detailed overview for running and contributing to the FastAPI project.





