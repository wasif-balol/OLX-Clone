# 🛍️ OLX Clone

> A Django-powered online marketplace clone inspired by OLX, built with Python and a customizable e-commerce template.

---

## 🚀 Features

- ✅ Built using **Django** (Python web framework)
- 🎨 Clean and responsive **e-commerce template** UI
- 🏷️ Full CRUD: list, view, create, update, delete product ads
- 🔐 User authentication (sign up, log in, log out)
- 🖼️ Image uploads for each listing
- 📍 Categorized listings for better filtering
- 🔧 Easily customizable for extensions like messaging, payments, etc.

---

## 🧰 Prerequisites

- Python version: `3.6`, `3.7`, or `3.8`
- Django (as specified in `requirements.txt`)
- `pip`, and preferably a **Python virtual environment**

---

## 🔧 Installation & Setup

```bash
# 1. Clone the repo
git clone https://github.com/wasif-balol/OLX-Clone.git

# 2. Navigate to the project directory
cd OLX-Clone

# 3. Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate  # 📌 on Windows: venv\Scripts\activate

# 4. Install dependencies
pip install -r requirements.txt

# 5. Apply database migrations
python manage.py migrate

# 6. Create a superuser for admin access
python manage.py createsuperuser

# 7. Start the development server
python manage.py runserver
