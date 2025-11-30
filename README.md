# Ìæì STAX - Nigerian EdTech Platform Backend

![Python](https://img.shields.io/badge/python-3.11+-blue.svg)
![Django](https://img.shields.io/badge/django-5.0+-green.svg)
![DRF](https://img.shields.io/badge/DRF-3.14+-orange.svg)
![PostgreSQL](https://img.shields.io/badge/postgresql-15+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

> A comprehensive backend API for an educational technology platform that provides online courses and past examination questions for Nigerian university students.

**Live API:** [https://api.stax.ng](https://api.stax.ng) *(Replace with your deployed URL)*  
**Frontend:** [https://stax.ng](https://stax.ng)  
**API Documentation:** [https://api.stax.ng/docs](https://api.stax.ng/docs) *(Add when ready)*

---

## Ì≥ã Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Configuration](#configuration)
- [Database Setup](#database-setup)
- [Running the Application](#running-the-application)
- [API Endpoints](#api-endpoints)
- [Testing](#testing)
- [Deployment](#deployment)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

---

## Ìºü Overview

**Stax** is a Nigerian EdTech platform designed to solve educational resource accessibility challenges faced by university students. The platform combines two core functionalities:

1. **Online Courses** - Structured learning paths with video lessons, progress tracking, and certificates
2. **Past Questions Bank** - Crowdsourced repository of past examination questions from Nigerian universities with a gamified contribution system

This repository contains the **backend API** built with Django REST Framework, providing robust authentication, course management, file uploads, and a points-based gamification system.

---

## ‚ú® Features

### Ì¥ê User Management
- JWT-based authentication (access & refresh tokens)
- User registration with email validation
- Role-based access control (Student, Contributor, Admin)
- Profile management with image uploads
- Password change and reset functionality

### Ì≥ö Course System
- Browse courses by category (Computer Science, Law, Medicine, etc.)
- Course enrollment and progress tracking
- Video lessons with ordered sequencing
- Course reviews and ratings
- Certificate generation upon completion
- Search and filter functionality

### Ì≥ù Past Questions Repository
- Upload past examination questions (PDF, images)
- Search by university, course code, year, semester
- Admin approval workflow for quality control
- Download tracking and analytics
- View counter for popular content

### ÌæÆ Gamification
- Points-based contributor system
- Earn points for uploading approved questions
- Leaderboard showing top contributors
- Future: Redeem points for premium access

### Ìª°Ô∏è Admin Features
- Django admin panel for content management
- Approve/reject uploaded questions
- Award points to contributors
- User management and moderation
- Platform analytics and reporting

---

## Ìª†Ô∏è Tech Stack

### Backend Framework
- **Django 5.0+** - High-level Python web framework
- **Django REST Framework 3.14+** - Powerful toolkit for building Web APIs
- **Django REST Framework SimpleJWT** - JWT authentication

### Database
- **PostgreSQL 15+** (Production)
- **SQLite** (Development)

### File Storage
- **Cloudinary** / **AWS S3** - Cloud storage for images and PDFs

### Authentication
- **JWT Tokens** - Stateless authentication with token refresh

### Additional Libraries
- **Pillow** - Image processing
- **python-decouple** - Environment variables management
- **psycopg2-binary** - PostgreSQL adapter
- **django-cors-headers** - CORS handling for frontend integration

---

## Ì≥Å Project Structure

```
stax-backend/
‚îú‚îÄ‚îÄ accounts/                   # User authentication & profiles
‚îÇ   ‚îú‚îÄ‚îÄ migrations/
‚îÇ   ‚îú‚îÄ‚îÄ __init__.py
‚îÇ   ‚îú‚îÄ‚îÄ admin.py               # Admin configuration for users
‚îÇ   ‚îú‚îÄ‚îÄ models.py              # User model
‚îÇ   ‚îú‚îÄ‚îÄ serializers.py         # User serializers
‚îÇ   ‚îú‚îÄ‚îÄ urls.py                # Auth endpoints
‚îÇ   ‚îî‚îÄ‚îÄ views.py               # Auth views
‚îÇ
‚îú‚îÄ‚îÄ courses/                    # Course management system
‚îÇ   ‚îú‚îÄ‚îÄ migrations/
‚îÇ   ‚îú‚îÄ‚îÄ __init__.py
‚îÇ   ‚îú‚îÄ‚îÄ admin.py               # Admin for courses, lessons, enrollments
‚îÇ   ‚îú‚îÄ‚îÄ models.py              # Course, Lesson, Enrollment, Review, Certificate models
‚îÇ   ‚îú‚îÄ‚îÄ serializers.py         # Course serializers
‚îÇ   ‚îú‚îÄ‚îÄ urls.py                # Course endpoints
‚îÇ   ‚îî‚îÄ‚îÄ views.py               # Course views
‚îÇ
‚îú‚îÄ‚îÄ questions/                  # Past questions system
‚îÇ   ‚îú‚îÄ‚îÄ migrations/
‚îÇ   ‚îú‚îÄ‚îÄ __init__.py
‚îÇ   ‚îú‚îÄ‚îÄ admin.py               # Admin for past questions
‚îÇ   ‚îú‚îÄ‚îÄ models.py              # PastQuestion, Contribution, QuestionDownload models
‚îÇ   ‚îú‚îÄ‚îÄ serializers.py         # Question serializers
‚îÇ   ‚îú‚îÄ‚îÄ urls.py                # Question endpoints
‚îÇ   ‚îî‚îÄ‚îÄ views.py               # Question views
‚îÇ
‚îú‚îÄ‚îÄ stax_api/                   # Main project settings
‚îÇ   ‚îú‚îÄ‚îÄ __init__.py
‚îÇ   ‚îú‚îÄ‚îÄ asgi.py
‚îÇ   ‚îú‚îÄ‚îÄ settings.py            # Django settings
‚îÇ   ‚îú‚îÄ‚îÄ urls.py                # Root URL configuration
‚îÇ   ‚îî‚îÄ‚îÄ wsgi.py
‚îÇ
‚îú‚îÄ‚îÄ media/                      # User-uploaded files (development)
‚îú‚îÄ‚îÄ static/                     # Static files
‚îú‚îÄ‚îÄ .env.example               # Environment variables template
‚îú‚îÄ‚îÄ .gitignore                 # Git ignore file
‚îú‚îÄ‚îÄ manage.py                  # Django management script
‚îú‚îÄ‚îÄ requirements.txt           # Python dependencies
‚îî‚îÄ‚îÄ README.md                  # This file
```

---

## Ì∫Ä Installation

### Prerequisites

- Python 3.11 or higher
- PostgreSQL 15+ (for production)
- pip (Python package manager)
- virtualenv (recommended)

### Step 1: Clone the Repository

```bash
git clone https://github.com/yourusername/stax-backend.git
cd stax-backend
```

### Step 2: Create Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ‚öôÔ∏è Configuration

### Environment Variables

Create a `.env` file in the project root (copy from `.env.example`):

```bash
cp .env.example .env
```

Edit `.env` with your configuration:

```env
# Django Settings
SECRET_KEY=your-secret-key-here-generate-a-strong-one
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# Database Configuration (Production)
DATABASE_URL=postgresql://user:password@localhost:5432/stax_db

# Or separate PostgreSQL settings
DB_NAME=stax_db
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=localhost
DB_PORT=5432

# Email Configuration
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-specific-password

# File Storage (Cloudinary)
CLOUDINARY_CLOUD_NAME=your_cloud_name
CLOUDINARY_API_KEY=your_api_key
CLOUDINARY_API_SECRET=your_api_secret

# Or AWS S3
AWS_ACCESS_KEY_ID=your_access_key
AWS_SECRET_ACCESS_KEY=your_secret_key
AWS_STORAGE_BUCKET_NAME=your_bucket_name
AWS_S3_REGION_NAME=us-east-1

# CORS Settings
CORS_ALLOWED_ORIGINS=http://localhost:3000,https://stax.ng

# JWT Settings (optional - defaults are fine)
JWT_ACCESS_TOKEN_LIFETIME=1440  # minutes (24 hours)
JWT_REFRESH_TOKEN_LIFETIME=10080  # minutes (7 days)
```

### Generate Secret Key

```python
# In Python shell
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())
```

---

## Ì≤æ Database Setup

### Option 1: SQLite (Development - Default)

No setup needed! Django will create `db.sqlite3` automatically.

### Option 2: PostgreSQL (Production)

**Install PostgreSQL:**

```bash
# Ubuntu/Debian
sudo apt-get install postgresql postgresql-contrib

# macOS (Homebrew)
brew install postgresql
```

**Create Database:**

```bash
# Access PostgreSQL
sudo -u postgres psql

# Create database and user
CREATE DATABASE stax_db;
CREATE USER stax_user WITH PASSWORD 'your_password';
ALTER ROLE stax_user SET client_encoding TO 'utf8';
ALTER ROLE stax_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE stax_user SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE stax_db TO stax_user;
\q
```

**Update settings.py:**

Uncomment PostgreSQL database settings in `stax_api/settings.py` and comment out SQLite.

---

## ÌøÉ Running the Application

### 1. Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 2. Create Superuser (Admin Account)

```bash
python manage.py createsuperuser
```

Follow prompts to create admin credentials.

### 3. Collect Static Files (Production)

```bash
python manage.py collectstatic
```

### 4. Run Development Server

```bash
python manage.py runserver
```

The API will be available at: **http://127.0.0.1:8000/api/**

### 5. Access Admin Panel

Visit: **http://127.0.0.1:8000/admin/**

Login with your superuser credentials.

---

## Ì≥° API Endpoints

### Authentication

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| POST | `/api/auth/register/` | User registration | No |
| POST | `/api/auth/login/` | User login | No |
| POST | `/api/auth/logout/` | User logout | Yes |
| POST | `/api/auth/token/refresh/` | Refresh access token | No |
| GET | `/api/auth/profile/` | Get user profile | Yes |
| PUT | `/api/auth/profile/` | Update profile | Yes |
| POST | `/api/auth/change-password/` | Change password | Yes |
| GET | `/api/auth/users/{id}/` | Public user profile | No |

### Courses

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| GET | `/api/courses/` | List courses | No |
| GET | `/api/courses/{id}/` | Course details | No |
| GET | `/api/courses/category/{slug}/` | Courses by category | No |
| POST | `/api/courses/{id}/enroll/` | Enroll in course | Yes |
| GET | `/api/courses/my-courses/` | User's courses | Yes |
| GET | `/api/courses/{id}/lessons/` | Course lessons | Yes (enrolled) |
| POST | `/api/courses/{id}/review/` | Add review | Yes |

### Categories

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| GET | `/api/categories/` | List categories | No |
| GET | `/api/categories/{slug}/` | Category details | No |

### Past Questions

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| GET | `/api/questions/` | List approved questions | No |
| GET | `/api/questions/{id}/` | Question details | No |
| POST | `/api/questions/upload/` | Upload question | Yes |
| GET | `/api/questions/my-uploads/` | User's uploads | Yes |
| GET | `/api/questions/search/` | Search questions | No |
| POST | `/api/questions/{id}/download/` | Download question | Yes |
| GET | `/api/questions/pending/` | Pending approval | Admin |
| POST | `/api/questions/{id}/approve/` | Approve question | Admin |
| POST | `/api/questions/{id}/reject/` | Reject question | Admin |

### Contributions

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| GET | `/api/contributions/leaderboard/` | Top contributors | No |
| GET | `/api/contributions/my-points/` | User's points | Yes |

**Full API documentation:** Visit `/api/docs/` (when Swagger is set up)

---

## Ì∑™ Testing

### Run All Tests

```bash
python manage.py test
```

### Run Specific App Tests

```bash
python manage.py test accounts
python manage.py test courses
python manage.py test questions
```

### Run with Coverage

```bash
pip install coverage
coverage run --source='.' manage.py test
coverage report
coverage html  # Generate HTML report
```

### Test with Postman

1. Import the Postman collection: `stax-api.postman_collection.json` *(create this)*
2. Set up environment variables (base_url, access_token)
3. Run the collection

---

## Ì∫¢ Deployment

### Deploy to Render

1. **Create Account:** Sign up at [render.com](https://render.com)

2. **Create Web Service:**
   - Connect GitHub repository
   - Build command: `pip install -r requirements.txt && python manage.py collectstatic --noinput && python manage.py migrate`
   - Start command: `gunicorn stax_api.wsgi:application`

3. **Add Environment Variables:**
   - Add all variables from `.env`
   - Set `DEBUG=False`
   - Set `ALLOWED_HOSTS` to your Render URL

4. **Create PostgreSQL Database:**
   - Add PostgreSQL service in Render
   - Copy `DATABASE_URL` to your web service environment

5. **Deploy!**

### Deploy to Railway

1. **Create Account:** Sign up at [railway.app](https://railway.app)

2. **Create New Project:**
   - Deploy from GitHub
   - Add PostgreSQL plugin
   - Set environment variables

3. **Configure:**
   - Railway auto-detects Django
   - Ensure `Procfile` exists:
     ```
     web: gunicorn stax_api.wsgi
     release: python manage.py migrate
     ```

4. **Deploy!**

### Production Checklist

- [ ] Set `DEBUG=False`
- [ ] Configure `ALLOWED_HOSTS`
- [ ] Set up PostgreSQL database
- [ ] Configure file storage (S3/Cloudinary)
- [ ] Set up email service
- [ ] Enable HTTPS
- [ ] Set secure `SECRET_KEY`
- [ ] Configure CORS properly
- [ ] Run migrations
- [ ] Collect static files
- [ ] Create superuser
- [ ] Test all endpoints
- [ ] Monitor logs

---

## Ì≥ä Database Schema

See [ERD Diagram](docs/erd-diagram.png) for complete database structure.

**Core Entities:**
- Users (authentication & profiles)
- Categories (subject classifications)
- Courses (online courses)
- Lessons (course content)
- Enrollments (student-course relationship)
- Reviews (course ratings)
- Certificates (completion certificates)
- PastQuestions (exam questions)
- Contributions (contributor tracking)
- QuestionDownloads (download tracking)

---

## Ì¥í Security

- Passwords hashed with Django's default hasher (PBKDF2)
- JWT tokens for stateless authentication
- CORS configured for frontend domain only
- File upload validation (type, size)
- Rate limiting on sensitive endpoints (recommended)
- SQL injection protection (Django ORM)
- XSS protection enabled
- CSRF protection for non-API requests

---

## Ì¥ù Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create feature branch: `git checkout -b feature/AmazingFeature`
3. Commit changes: `git commit -m 'Add AmazingFeature'`
4. Push to branch: `git push origin feature/AmazingFeature`
5. Open Pull Request

### Coding Standards

- Follow PEP 8 style guide
- Write docstrings for all functions/classes
- Add tests for new features
- Update documentation

---

## Ì≥ù License

This project is licensed under the MIT License - see [LICENSE](LICENSE) file for details.

---

## Ì±®‚ÄçÌ≤ª Author

**[Your Name]**

- GitHub: [@yourusername](https://github.com/yourusername)
- LinkedIn: [Your LinkedIn](https://linkedin.com/in/yourprofile)
- Email: your.email@example.com
- Portfolio: [yourportfolio.com](https://yourportfolio.com)

---

## Ìπè Acknowledgments

- ALX Africa Software Engineering Program
- Django Documentation
- Django REST Framework
- Nigerian EdTech Community
- All contributors and testers

---

## Ì≥û Support

For support, email your.email@example.com or create an issue in the GitHub repository.

---

## Ì∑∫Ô∏è Roadmap

### Phase 1 (Completed) ‚úÖ
- User authentication system
- Course management
- Past questions repository
- Points system

### Phase 2 (In Progress) Ì∫ß
- Frontend integration
- Email notifications
- Certificate PDF generation
- Search optimization

### Phase 3 (Planned) Ì≥ã
- Payment integration (Paystack)
- Live classes
- Discussion forums
- Mobile app API
- AI-powered recommendations

---

## Ì≥à Project Statistics

![Lines of Code](https://img.shields.io/badge/Lines%20of%20Code-10K+-blue)
![API Endpoints](https://img.shields.io/badge/API%20Endpoints-50+-green)
![Database Tables](https://img.shields.io/badge/Database%20Tables-10-orange)

**Built with ‚ù§Ô∏è for Nigerian Students**

---

## Ì¥ó Links

- **Frontend Repository:** [github.com/username/stax-frontend](https://github.com/username/stax-frontend)
- **API Documentation:** [api.stax.ng/docs](https://api.stax.ng/docs)
- **Live Demo:** [stax.ng](https://stax.ng)
- **Project Board:** [Project Management](https://github.com/users/yourusername/projects/1)

---

*Last Updated: December 2024*

^X

