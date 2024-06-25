# Project Title

This project includes two possible tasks for a Python Developer test:

1. **Google and Facebook Authentication**: Implement user authentication through Google and Facebook APIs using Django and Django Allauth.
2. **CRUD REST API for Teams and People**: Create a REST API with CRUD endpoints for managing teams and people within those teams using Django and Django REST Framework.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Testing](#testing)
- [Contributing](#contributing)

## Installation

### Prerequisites
- Python 3.11+
- Django 5.0+
- Django REST Framework
- Django Allauth (for Task 1)

### Setup
1. Clone the repository:
    ```sh
    git clone https://github.com/zozulia-developer/crud_test.git
    cd crud_test
    ```

2. Create and activate a virtual environment:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

4. Create `.env` file from `.env.example`.

5. Apply migrations:
    ```sh
    python manage.py migrate
    ```

6. Create a superuser:
    ```sh
    python manage.py createsuperuser
    ```

7. Run the server:
    ```sh
    python manage.py runserver
    ```

## Usage

### Google and Facebook Authentication (Task 1)
- Configure your Google and Facebook credentials in the `.env` file.
- Access the authentication endpoints at `/accounts/google/login/` and `/accounts/facebook/login/`.

### CRUD REST API for Teams and People (Task 2)
- Use the provided API endpoints to manage teams and people.
- http://127.0.0.1:8000/swagger/

## API Endpoints

### Teams
- **Create Team**: `POST /api/teams/`
- **List Teams**: `GET /api/teams/`
- **Retrieve Team**: `GET /api/teams/{id}/`
- **Update Team**: `PUT /api/teams/{id}/`
- **Delete Team**: `DELETE /api/teams/{id}/`

### People
- **Create Person**: `POST /api/people/`
- **List People**: `GET /api/people/`
- **Retrieve Person**: `GET /api/people/{id}/`
- **Update Person**: `PUT /api/people/{id}/`
- **Delete Person**: `DELETE /api/people/{id}/`

## Testing
To run tests, use the following command:
```sh
python manage.py test
```
