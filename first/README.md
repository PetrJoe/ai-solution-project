# Solutions Django Project

## Overview
Solutions is a Django web application project. This project includes a core app and follows standard Django project structure.

## Project Structure
- `solutions/` - Main project directory containing settings and configuration
- `core/` - Django application within the project

## Requirements
- Python 3.x
- Django 5.1.x

## Setup Instructions

### 1. Clone the repository
```bash
git clone <repository-url>
cd solutions
```

### 2. Create and activate a virtual environment (recommended)
```bash
python -m venv venv
```

On Windows:
```bash
venv\Scripts\activate
```

On macOS/Linux:
```bash
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run migrations && makemigrations
```bash
python manage.py migrate
```
```bash
python manage.py makemigrations
```

### 5. Create a superuser (optional)
```bash
python manage.py createsuperuser
```

### 6. Run the development server
```bash
python manage.py runserver
```

The application will be available at http://127.0.0.1:8000/

## Configuration
The main configuration for this project is in `solutions/settings.py`. Key settings include:

- DEBUG mode is currently set to `True` (development mode)
- The project uses Django's built-in template system
- Template directories are configured to include a "templates" folder at the project root

## Deployment
For production deployment, make sure to:
1. Set `DEBUG = False` in settings.py
2. Configure a proper `SECRET_KEY`
3. Update `ALLOWED_HOSTS` with your domain
4. Follow Django's deployment checklist: https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

## License
[Specify your license here]

## Contact
[Your contact information]
