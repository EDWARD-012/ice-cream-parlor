# Ice Cream Parlor - Django Project

A responsive and user-friendly website for an ice cream parlor built with Django.

## Features

- User-friendly interface
- Responsive design
- Product pages for ice cream flavors
- Dynamic content management using Django admin

## Setup Instructions

### Requirements

- Python 3.x
- Django (see `requirements.txt` for details)

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/EDWARD-012/ice-cream-parlor.git
    ```
    
2. Navigate to the project directory:
    ```bash
    cd ice-cream-parlor
    ```

3. Create and activate a virtual environment:
    ```bash
    python3 -m venv venv
    source venv/bin/activate    # For Windows, use `venv\Scripts\activate`
    ```

4. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

5. Apply the migrations:
    ```bash
    python manage.py migrate
    ```

6. Run the server:
    ```bash
    python manage.py runserver
    ```

7. Access the website by opening your browser and navigating to:
    ```
    http://127.0.0.1:8000
    ```

## License

This project is licensed under the MIT License.
