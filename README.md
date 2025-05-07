## Features

- **Article Management**: Create new articles using a form rendered with `crispy-forms`.
- **Template Inheritance**: Uses `base.html` as the base template for consistent design.
- **CSRF Protection**: Secures forms with Django's CSRF token.


## Prerequisites

To run this project, ensure you have the following installed:
- Python 3.8+
- Django 5.2+
- `django-crispy-forms` library


## Installation

Follow these steps to set up the project:

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd news

2. Create a Virtual Environment:
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install Dependencies:
pip install -r requirements.txt

4. Apply Migrations:
python manage.py migrate

5. Run the Development Server:
python manage.py runserver

6. Access the Application: Open your browser and navigate to http://127.0.0.1:8000/.

Usage

- Navigate to the "New Article" page to create a new article.
- The form is styled using crispy-forms.

Configuration

- Templates: Located in the news/templates/ directory.
- Static Files: Place CSS and JavaScript files in the static/ directory.

License

This project is licensed under the MIT License. See the LICENSE file for details.

