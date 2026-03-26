# Madiha's Portfolio Website

A cute and colorful portfolio website built with Flask and vanilla JavaScript.

## Features

- 🎨 Cartoon-style design with floating decorations
- 📱 Responsive mobile-friendly layout
- 👑 Admin panel for managing content
- 📊 Visitor counter
- 💌 Contact form with message management
- ⚡ Skills showcase with progress bars
- 🚀 Projects gallery

## Local Development

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

### Installation

1. **Install Python** (if not already installed):
   - Download from [python.org](https://www.python.org/downloads/)
   - Make sure to check "Add Python to PATH" during installation

2. **Clone or download the project**

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the server**:
   ```bash
   python server.py
   ```

5. **Open in browser**:
   - Portfolio: http://localhost:5001
   - Admin Panel: http://localhost:5001/admin

## Deployment on Render

1. **Push your code to GitHub**

2. **Create a new Web Service on Render**:
   - Connect your GitHub repository
   - Set the runtime to "Python"
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `python server.py`

3. **Environment Variables** (optional):
   - `PORT`: Automatically set by Render

## Project Structure

```
madiha_project/
├── server.py          # Flask backend server
├── database.py        # SQLite database operations
├── index.html         # Main portfolio page
├── admin.html         # Admin panel
├── style.css          # CSS styles
├── script.js          # Frontend JavaScript
├── requirements.txt   # Python dependencies
└── portfolio.db       # SQLite database (created automatically)
```

## API Endpoints

- `GET /api/profile` - Get profile information
- `GET /api/skills` - Get all skills
- `POST /api/skills` - Add new skill
- `GET /api/projects` - Get all projects
- `POST /api/projects` - Add new project
- `POST /api/contact` - Submit contact form
- `GET /api/messages` - Get all contact messages
- `GET /api/visitors` - Get visitor count
- `POST /api/visitors/increment` - Increment visitor count

## Technologies Used

- **Backend**: Flask, SQLite
- **Frontend**: HTML5, CSS3, JavaScript
- **Styling**: Custom CSS with Google Fonts
- **Icons**: Font Awesome

## Contributing

Feel free to submit issues and enhancement requests!

## License

This project is open source and available under the [MIT License](LICENSE).