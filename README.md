```markdown
<div align="center">

#  MacKart

### MacBook E-Commerce Web Application

A modern Flask-based e-commerce web application built specifically for browsing and managing MacBook products.

<br>

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)

</div>

---

## About MacKart

MacKart is a Flask-based e-commerce web application designed specifically for MacBook products. The application provides a modern shopping-style interface where users can browse MacBook products and view their details, while administrators can access a dedicated dashboard to manage product information.

The project demonstrates practical implementation of Python web development, Flask backend development, frontend design, authentication, product management, JSON-based data storage, and responsive user interfaces.

---

## Features

### Customer Experience

- Browse MacBook products
- View product information
- View product prices and descriptions
- Clean and responsive shopping interface
- Product-focused e-commerce experience
- Modern web interface

### Admin Features

- Admin authentication
- Dedicated admin dashboard
- Manage MacBook products
- Update product prices
- Update product descriptions
- Manage product information

### Application Features

- Flask-powered backend
- Dynamic HTML rendering
- JSON-based data management
- Responsive web design
- Organized static assets
- Simple and maintainable project structure

---

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Backend programming |
| Flask | Web application framework |
| HTML5 | Page structure |
| CSS3 | Styling and responsive design |
| JavaScript | Client-side functionality |
| JSON | Product and user data storage |
| Git | Version control |
| GitHub | Source code hosting |

---

## Application Architecture

```text
                    ┌──────────────────────┐
                    │        User          │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │    MacKart Frontend  │
                    │   HTML / CSS / JS    │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │    Flask Backend     │
                    │       app.py         │
                    └──────────┬───────────┘
                               │
                    ┌──────────┴──────────┐
                    │                     │
                    ▼                     ▼
             ┌─────────────┐       ┌─────────────┐
             │  data.json  │       │ users.json  │
             │  Products   │       │    Users    │
             └─────────────┘       └─────────────┘
```

---

## Project Structure

```text
mackart/
│
├── app.py
├── data.json
├── users.json
├── requirements.txt
├── README.md
│
├── templates/
│   ├── ...
│   └── ...
│
└── static/
    ├── css/
    │   └── ...
    │
    └── images/
        ├── m1.jpg
        ├── m2.jpg
        ├── m3.jpg
        ├── m4.jpg
        └── m5.jpg
```

---

## Installation

### Prerequisites

Make sure the following are installed:

- Python 3.x
- pip
- Git
- Visual Studio Code

### 1. Clone the Repository

```bash
git clone https://github.com/sachinrv30/mackart.git
```

### 2. Navigate to the Project

```bash
cd mackart
```

### 3. Create a Virtual Environment

For macOS and Linux:

```bash
python3 -m venv venv
```

Activate the environment:

```bash
source venv/bin/activate
```

For Windows:

```bash
python -m venv venv
```

```bash
venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Add Product Images

Make sure the required product images are available inside:

```text
static/images/
```

Required images:

```text
m1.jpg
m2.jpg
m3.jpg
m4.jpg
m5.jpg
```

### 6. Run the Application

```bash
python app.py
```

The application will run at:

```text
http://127.0.0.1:5000
```

Open the URL in your browser to access MacKart.

---

## Admin Access

MacKart includes an administrator login and dashboard for managing product information.

For local development:

```text
Username: admin
Password: admin
```

> **Security Notice:** These credentials are intended only for local development and demonstration purposes. Production applications should use secure credentials, password hashing, and environment variables for sensitive configuration.

---

## Product Management

The admin dashboard allows authorized administrators to manage MacBook product information.

Current management capabilities include:

```text
Product
   │
   ├── Name
   ├── Price
   └── Description
```

Administrators can update product prices and descriptions through the management interface.

---

## Data Management

MacKart currently uses JSON files for lightweight data storage.

### Product Data

```text
data.json
```

Stores information related to MacBook products.

### User Data

```text
users.json
```

Stores application user information used by the current authentication system.

The JSON-based approach keeps the project lightweight and easy to understand while demonstrating basic data persistence.

---

## Running the Project Locally

After installation, use:

```bash
cd mackart
source venv/bin/activate
pip install -r requirements.txt
python app.py
```

Then open:

```text
http://127.0.0.1:5000
```

To stop the Flask development server:

```text
Ctrl + C
```

---

## Development Workflow

```text
Clone Repository
       │
       ▼
Create Virtual Environment
       │
       ▼
Install Dependencies
       │
       ▼
Run Flask Application
       │
       ▼
Open Local Website
       │
       ▼
Test Features
       │
       ▼
Make Changes
       │
       ▼
Commit Changes
       │
       ▼
Push to GitHub
```

---

## Future Enhancements

The project can be expanded with advanced e-commerce functionality such as:

- Shopping cart
- Wishlist
- Product search
- Product filtering and sorting
- Product categories
- User profiles
- Order management
- Checkout system
- Payment gateway integration
- Product reviews and ratings
- Email notifications
- Secure password hashing
- MySQL or PostgreSQL database
- REST API
- Cloud deployment
- Progressive Web App support

---

## Production Improvements

For a production-ready version, the current JSON-based storage can be replaced with a proper relational or NoSQL database.

Potential improvements include:

- MySQL or PostgreSQL
- SQLAlchemy
- Flask-Login
- Secure password hashing
- Environment variables
- REST APIs
- Cloud storage
- Production WSGI server
- Cloud deployment

Possible production architecture:

```text
                  ┌──────────────────┐
                  │      Client      │
                  │   Web / Mobile   │
                  └────────┬─────────┘
                           │
                           ▼
                  ┌──────────────────┐
                  │  Flask Backend   │
                  │   Application    │
                  └────────┬─────────┘
                           │
              ┌────────────┼────────────┐
              ▼            ▼            ▼
        ┌──────────┐ ┌──────────┐ ┌──────────┐
        │ Database │ │ Storage  │ │ Payment  │
        │ MySQL    │ │  Cloud   │ │ Gateway  │
        └──────────┘ └──────────┘ └──────────┘
```

---

## Learning Outcomes

This project provides practical experience with:

- Python web development
- Flask application architecture
- Routing and request handling
- Dynamic HTML templates
- Frontend and backend integration
- Authentication concepts
- Product management
- JSON data handling
- Responsive web design
- Virtual environments
- Dependency management
- Git and GitHub workflow

---

## Project Status

```text
Project        : MacKart
Project Type   : E-Commerce Web Application
Backend        : Flask
Frontend       : HTML / CSS / JavaScript
Data Storage   : JSON
Repository     : GitHub
Status         : Active Development
```

---

## Author

### Sachin R V

**MCA Student | Aspiring Software Developer**

Interested in:

- Software Development
- Python
- Web Development
- Artificial Intelligence
- Machine Learning
- Full-Stack Development

---

## Repository

GitHub:  
https://github.com/sachinrv30/mackart

---

<div align="center">

###  MacKart

**A MacBook-focused e-commerce web application built with Flask**

Built with Python • Flask • HTML • CSS • JavaScript

**Developed by Sachin R V**

</div>
```