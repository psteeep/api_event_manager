# Django Event Management REST API

This is a Django REST API for managing events such as conferences, meetups, etc. The application allows users to create, view, update, and delete events. It also handles user registration and event registration.

## Features

- **Event Management**: Create, read, update, and delete events.
- **User Management**: Basic user registration and authentication.
- **Event Registration**: Users can register for events.
- **API Documentation**: Automatically generated using Swagger UI.
- **Docker**: Containerized application for easy deployment.

## Getting Started

### Prerequisites

- Python 3.x
- Django
- Django REST framework
- Docker (for containerization)


### Installation

1. **Clone the repository**:

    ```bash
    git clone https://github.com/psteeep/api_event_manager.git
    cd api_event_manager
    ```

2. **Create a `.env` file**:

    Create a `.env` file in the root directory of your project with the following content:

    ```plaintext
    SECRET_KEY=your-secret-key

    # Postgres
    DB_HOST=db
    DB_USER=user
    DB_PASSWORD=password
    DB_NAME=event_manager
    DB_PORT=5432
    ```

    Replace the placeholder values with your actual settings.

3. **Create and activate a virtual environment**:

    ```bash
    python -m venv .venv
    source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
    ```

4. **Install dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

5. **Apply migrations**:

    ```bash
    python manage.py migrate
    ```

6. **Create a superuser (optional, for admin access)**:

    ```bash
    python manage.py createsuperuser
    ```

7. **Run the development server**:

    ```bash
    python manage.py runserver
    ```

### Docker Compose

To manage your application with Docker Compose:

- **Start the application**:

    ```bash
    docker-compose up --build
    ```

- **Stop the application**:

    ```bash
    docker-compose down
    ```

- **View logs**:

    ```bash
    docker-compose logs -f
    ```


### API Endpoints

- **User Registration**: `POST /api/register/`
- **Obtain Token**: `POST /api/token/`
- **Refresh Token**: `POST /api/token/refresh/`
- **List Events**: `GET /api/events/`
- **Create Event**: `POST /api/events/`
- **Retrieve Event**: `GET /api/events/{id}/`
- **Update Event**: `PATCH /api/events/{id}/`
- **Delete Event**: `DELETE /api/events/{id}/`
- **List My Event Registrations**: `GET /api/registrations/my/`
Description: Retrieve a list of events that the authenticated user has registered for.
- **Register for an Event**: `POST /api/registrations/`Description: Register the authenticated user for a specific event.

### Advanced Features

- **Search and Filter Events**:
  - **Search by Title**: `GET /api/events/?title=<search_term>`
  - **Filter by Location**: `GET /api/events/?location=<location>`
  - **Filter by Date**: `GET /api/events/?date=<date>`
  - **Combine Filters**: `GET /api/events/?title=<search_term>&location=<location>&date=<date>`

### Documentation

API documentation is available at `/swagger/` or `/redoc/` after starting the development server.
