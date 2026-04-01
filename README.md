Educational News Website
Description

An educational project built with Django, PostgreSQL, and Tailwind CSS.
Demonstrates basic CRUD operations using Django ORM and minimal frontend design.

This project is for learning purposes only, so:

No user registration or authentication
No roles
Minimal functionality

Pages:

Home — displays a list of news
News — shows all news items
Add News — form for creating news items
Technologies
Python / Django
PostgreSQL
Node.js + Tailwind CSS
Installation
Clone the repository:
git clone <repository_url>
cd <project_name>
Create a virtual environment:
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
Install Python dependencies:
pip install -r requirements.txt
Create a .env file in the project root and add your database credentials:
DB_NAME=<your_db_name>
DB_USER=<your_db_user>
DB_PASSWORD=<your_db_password>
DB_HOST=<your_db_host>
DB_PORT=<your_db_port>
Apply migrations:
python manage.py migrate
Install Node.js dependencies and build Tailwind CSS:
npm install
npm run build  # or npm run dev for development
Run the server:
python manage.py runserver
Usage
Open http://127.0.0.1:8000/
Browse news items
Add new news via the form