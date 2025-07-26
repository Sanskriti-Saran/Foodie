<<<<<<< HEAD
# Foodie
A django web-app based on popular food joints in Lucknow
=======
# Flavors of Lucknow (Foodie)

A Django web application to explore and filter food spots in Lucknow, categorized by vegetarian, non-vegetarian, meals, and desserts. Includes advanced search and filtering features.

## Features
- Browse food spots by category (Veg, Non-Veg, Meals, Desserts)
- Advanced filtering by name, location, and price
- Responsive, modern UI with Tailwind CSS
- Navigation between all main pages
- Static assets and templates organized for easy customization

## Setup Instructions

### 1. Clone the Repository
```
git clone <your-repo-url>
cd <repo-folder>
```

### 2. Create and Activate Virtual Environment
```
python -m venv .venv
# On Windows:
.\.venv\Scripts\activate
```

### 3. Install Dependencies
```
pip install django
```

### 4. Apply Migrations
```
python manage.py makemigrations
python manage.py migrate
```

### 5. Run the Development Server
```
python manage.py runserver
```

### 6. Access the App
Open your browser and go to: [http://localhost:8000/](http://localhost:8000/)

## Project Structure
```
Django/
├── config/                # Django project settings
├── Foodie/                # Main app with models, views, templates, static
│   ├── migrations/
│   ├── static/
│   │   └── foodie-filters.js
│   ├── templates/
│   │   ├── home.html
│   │   ├── veg.html
│   │   ├── nonveg.html
│   │   ├── meals.html
│   │   ├── desserts.html
│   │   └── about.html
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── ...
├── manage.py
└── ...
```

## Customization
- Add or edit food spots in the Django admin or via fixtures.
- Update templates in `Foodie/templates/` for UI changes.
- Add static files (JS, CSS, images) in `Foodie/static/`.

## License
MIT License

---
For any issues or feature requests, please open an issue or contact the maintainer.
>>>>>>> 5fc532f (Initial commit)
