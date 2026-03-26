# Portfolio Website

This is a Flask-based portfolio website project that connects to a SQLite database to serve and display portfolio items.

## Project Structure

```
portfolio-website
├── src
│   ├── app.py                # Entry point of the Flask application
│   ├── config.py             # Configuration settings for the application
│   ├── models
│   │   └── __init__.py       # Database models for portfolio items
│   ├── routes
│   │   └── __init__.py       # Application routes
│   ├── templates
│   │   ├── base.html         # Base HTML template
│   │   ├── index.html        # Homepage template
│   │   └── portfolio.html     # Portfolio items template
│   └── static
│       ├── css
│       │   └── style.css     # CSS styles for the website
│       └── js
│           └── script.js     # JavaScript for client-side interactivity
├── requirements.txt           # Project dependencies
└── README.md                  # Project documentation
```

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd portfolio-website
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   ```

3. Activate the virtual environment:
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```
     source venv/bin/activate
     ```

4. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

5. Run the application:
   ```
   python src/app.py
   ```

6. Open your web browser and navigate to `http://127.0.0.1:5000` to view the portfolio website.

## Usage

- The homepage displays an overview of the portfolio.
- The portfolio page showcases individual portfolio items fetched from the database.

## License

This project is licensed under the MIT License.