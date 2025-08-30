# 🌟 Thinkly

**Thinkly** is a modern web application built with **Django** that allows users to share their **thoughts, feelings, and ideas** in a clean and organized way.  
Users can **create, edit, and delete** their thoughts, and even **attach images** to them.  
The application features a clean, **responsive UI built with Bootstrap 5**, ensuring a seamless experience on all devices.

<div align="center">
  <img src="media/photos/demo.png" alt="Thinkly Demo" width="70%">
  <br>
  <em>✨ A place to share your thoughts, beautifully.</em>
</div>

---

## 📑 Table of Contents
- [✨ Features](#-features)
- [⚡ Getting Started](#-getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [🚀 Deployment](#-deployment)
- [🛠️ Built With](#%EF%B8%8F-built-with)
- [🤝 Contributing](#-contributing)
- [📜 License](#-license)

---

## ✨ Features

✅ User authentication (**login, registration, logout**)  
✅ Full CRUD operations for thoughts  
✅ Attach photos to each thought  
✅ Clean, **responsive Bootstrap 5 UI**  
✅ User-specific thought management  

---

## ⚡ Getting Started

Follow these steps to set up **Thinkly** locally on your machine.  

### 🔧 Prerequisites
Make sure you have installed:

- [Python 3.10+](https://www.python.org/downloads/)
- [pip](https://pip.pypa.io/en/stable/installation/)
- [git](https://git-scm.com/)

---

### 🖥️ Installation (Single Command Sequence)

```bash
# Clone the repository
git clone https://github.com/Tejaswi410/Thinkly.git
cd Thinkly

# Create and activate a virtual environment
# On macOS/Linux
python3 -m venv venv && source venv/bin/activate
# On Windows (use this instead)
# python -m venv venv && venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run database migrations
python manage.py migrate

# (Optional) Create a superuser for admin access
python manage.py createsuperuser

# Start the development server
python manage.py runserver

# Now open your browser at http://127.0.0.1:8000
```
---
## 📜 License

This project is licensed under the MIT License – see the LICENSE.md
 file for details.

<div align="center"> Made by <a href="https://github.com/Tejaswi410">Tejaswi</a> </div>

---
