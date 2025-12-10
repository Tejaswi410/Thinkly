# 💭 Thinkly

> A modern social platform for sharing thoughts, built with Django

[![Django](https://img.shields.io/badge/Django-5.0-green.svg)](https://www.djangoproject.com/)
[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

Thinkly is a minimalist social media platform that lets users share their thoughts, upload photos, interact through likes and comments. Built with Django and featuring a sleek, modern UI with glassmorphism effects.

## ✨ Features

- 🔐 **User Authentication** - Secure registration, login, and logout
- 💬 **Share Thoughts** - Post text updates with optional photo uploads
- ❤️ **Like System** - Like thoughts from other users (prevents duplicate likes)
- 💭 **Comments** - Engage in conversations through comments
- ✏️ **Edit & Delete** - Full control over your own thoughts
- 🎨 **Modern UI** - Beautiful gradient design with glassmorphism effects
- 📱 **Responsive** - Works seamlessly on desktop, tablet, and mobile
- ⚡ **Performance Optimized** - Efficient database queries with annotations

## 🚀 Quick Start

### Prerequisites

- Python 3.10 or higher
- pip (Python package manager)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/thinkly.git
   cd thinkly
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   
   # On Windows:
   venv\Scripts\activate
   
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up the database**
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser (optional)**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**
   ```bash
   python manage.py runserver
   ```

7. **Open your browser**
   ```
   http://127.0.0.1:8000/feed/
   ```

## 📁 Project Structure

```
thinkly/
├── app/                      # Main application
│   ├── migrations/           # Database migrations
│   ├── templates/            # HTML templates
│   ├── admin.py              # Admin configuration
│   ├── forms.py              # Form definitions
│   ├── models.py             # Database models
│   ├── urls.py               # URL routing
│   └── views.py              # View logic
├── Thinkly/                  # Project settings
│   ├── settings.py           # Configuration
│   ├── urls.py               # Root URL config
│   └── wsgi.py               # WSGI config
├── templates/                # Base templates
│   ├── layout.html           # Base layout
│   ├── modern_thought_feed.html
│   └── registration/         # Auth templates
├── media/                    # Uploaded files
├── staticfiles/              # Collected static files
├── manage.py                 # Django management script
├── requirements.txt          # Python dependencies
└── README.md                 # This file
```

## 🛠️ Technologies Used

- **Backend**: Django 5.0
- **Database**: SQLite (development) / PostgreSQL (production ready)
- **Styling**: Custom CSS with modern gradients and glassmorphism
- **File Uploads**: Pillow for image processing
- **Static Files**: WhiteNoise for production static file serving
- **Deployment**: Gunicorn WSGI server

## 🎨 Features in Detail

### Authentication System
- Custom styled login and registration forms
- Secure password validation
- Session-based authentication
- User-specific content access

### Thought Management
- Create thoughts with optional photo uploads
- Edit your own thoughts
- Delete your own thoughts
- View all thoughts in a chronological feed

### Social Interactions
- **Like System**: 
  - One like per user per thought
  - Real-time like count updates
  - Visual feedback for already-liked thoughts
- **Comments**: 
  - Add comments to any thought
  - View all comments in thread
  - Timestamped interactions

### UI/UX
- Modern dark theme with cyan/purple accents
- Gradient backgrounds and glassmorphism effects
- Responsive grid layout (1-4 columns based on screen size)
- Smooth animations and hover effects
- Custom SVG logo with thought bubble design

## ⚙️ Configuration

### Environment Variables

Create a `.env` file in the project root:

```env
DJANGO_SECRET_KEY=your-secret-key-here
DJANGO_DEBUG=true
DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1
```

### Generate a Secret Key

```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

## 🚢 Deployment

### Deploy to Render

1. Push your code to GitHub
2. Connect your repository to Render
3. Set environment variables in Render dashboard:
   - `DJANGO_SECRET_KEY`
   - `DJANGO_DEBUG=false`
   - `DJANGO_ALLOWED_HOSTS=your-domain.onrender.com`
4. Render will automatically deploy using `render.yaml`

### Production Checklist

- [ ] Set `DEBUG=False` in production
- [ ] Configure `ALLOWED_HOSTS` with your domain
- [ ] Use a strong, random `SECRET_KEY`
- [ ] Set up a production database (PostgreSQL recommended)
- [ ] Configure static file serving
- [ ] Set up media file storage (S3 recommended)
- [ ] Enable HTTPS
- [ ] Set up error monitoring

## 🧪 Testing

Run the test suite:

```bash
python manage.py test
```

## 📸 Screenshots

### Feed View
The main feed displays all thoughts in a beautiful masonry grid layout with like and comment counts.

### Thought Creation
Users can share thoughts with optional photo uploads through an intuitive form.

### Authentication
Clean, modern login and registration pages with proper validation.

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Development Guidelines

- Follow PEP 8 style guidelines
- Write tests for new features
- Update documentation as needed
- Use type hints where appropriate

## 🐛 Known Issues & Solutions

### IDE Warning: "Cannot access attribute 'comments'"
This is a linting warning and doesn't affect functionality. Django automatically creates reverse relations. To fix:

```python
# Add to models.py
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from django.db.models import QuerySet
    
class Thought(models.Model):
    # ... existing fields ...
    if TYPE_CHECKING:
        comments: QuerySet['Comment']
```

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Django documentation and community
- Modern UI design inspiration from contemporary social platforms
- Inter font family by Rasmus Andersson

## 📧 Contact

Your Name - [@yourusername](https://twitter.com/yourusername)

Project Link: [https://github.com/yourusername/thinkly](https://github.com/yourusername/thinkly)

---

<div align="center">
  <strong>Built with ❤️ using Django</strong>
</div>