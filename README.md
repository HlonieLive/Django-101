# Django Project

#### This is a beginner-to-intermediate Django web application built while learning Python and web development through **SimpliLearn's Django course**. The project demonstrates a wide range of Django concepts including models, views, URL routing, templates, forms, user authentication, and database migrations.

#### It is designed to help me practice full-stack development skills using Django’s powerful built-in tools and prepare for real-world deployment.


- Project and app structure
- Models and database migrations
- Admin interface
- URL routing
- Views
- Working with data in the Django shell

## 🧰 Features

- **Genre Collection Management**: Organize creative collections (e.g., Fiction, Poetry) with names, descriptions, and cover images.
- **Models**: `Collection` and `Piece` models with full database integration.
- **Admin Panel**: Full CRUD operations via Django’s built-in admin interface.
- **HTML Templates**: Dynamic pages rendered using Django’s template engine.
- **User Authentication**: Sign up, log in, and log out functionality for secure access.
- **Forms & User Input**: Custom forms for creating and editing collections and pieces, with validation and POST handling.
- **Database**: Uses SQLite for development (default Django database).

## 🛠️ Setup Instructions

1. **Clone the repository**
     git clone https://github.com/your-username/your-django-project.git
     cd your-django-project

2. **Create and activate a virtual environment**
     python -m venv venv
     # On Windows:
     venv\Scripts\activate
     # On macOS/Linux:
     source venv/bin/activate

3. **Install Django**
     pip install django

4. **Apply database migrations**
     python manage.py makemigrations
     python manage.py migrate

5. **Create a superuser (for admin access)**
     python manage.py createsuperuser

6. **Run the development server**
     python manage.py runserver
