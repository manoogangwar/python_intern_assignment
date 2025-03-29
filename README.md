Django App API

This is a Django-based API for managing app details using Django REST Framework (DRF) and SQLite.

Setup Instructions

1. Clone the Repository

git clone <repository_link>
cd <project_directory>

2. Create a Virtual Environment

python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

3. Install Dependencies

pip install -r requirements.txt

4. Apply Migrations

python manage.py makemigrations
python manage.py migrate

5. Run the Development Server

python manage.py runserver

The API will be available at http://127.0.0.1:8000/

API Endpoints

Method

Endpoint

Description

GET

/apps/

Retrieve all apps

POST

/apps/

Add a new app

GET

/apps/{id}/

Get app by ID

PUT

/apps/{id}/

Update an app

DELETE

/apps/{id}/

Delete an app

Example Requests

Add an App (POST)

{
    "app_name": "Test App",
    "version": "1.0",
    "description": "This is a sample app."
}

Get App (GET)

curl http://127.0.0.1:8000/apps/1/

Delete App (DELETE)

curl -X DELETE http://127.0.0.1:8000/apps/1/

License

This project is for educational purposes.


