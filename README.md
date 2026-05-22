# MacBook Store

A simple Flask web application for displaying and managing MacBook products.

## Features

- Public product catalog
- Admin login and dashboard
- Update product prices and descriptions
- Responsive design

## Setup

1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Add product images to `static/images/`:
   - m1.jpg
   - m2.jpg
   - m3.jpg
   - m4.jpg
   - m5.jpg

3. Run the application:
   ```
   python app.py
   ```

4. Open http://127.0.0.1:5000 in your browser.

## Admin Access

- Username: admin
- Password: admin

## Project Structure

- `app.py`: Main Flask application
- `data.json`: Product data
- `templates/`: HTML templates
- `static/`: CSS and images