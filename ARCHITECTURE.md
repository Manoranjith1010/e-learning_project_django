# Project Architecture Overview

## System Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                      Client Layer                           │
│                  (Web/Mobile Frontend)                       │
└──────────────────────────┬──────────────────────────────────┘
                           │
┌──────────────────────────▼──────────────────────────────────┐
│                     API Gateway                             │
│  (Django REST Framework + CORS + Rate Limiting)             │
└──────────────────────────┬──────────────────────────────────┘
                           │
┌──────────────────────────▼──────────────────────────────────┐
│              Middleware Layer (common/)                     │
│  ┌─────────────────────────────────────────────────────┐   │
│  │ • RequestLoggingMiddleware - Track all requests     │   │
│  │ • ErrorHandlingMiddleware - Unified error responses │   │
│  │ • CORS - Cross-origin resource sharing             │   │
│  └─────────────────────────────────────────────────────┘   │
└──────────────────────────┬──────────────────────────────────┘
                           │
┌──────────────────────────▼──────────────────────────────────┐
│           Authentication & Authorization                    │
│  ┌─────────────────────────────────────────────────────┐   │
│  │ • JWT Authentication - Token-based auth            │   │
│  │ • Role-based Access Control - Student/Instructor   │   │
│  │ • Permission Classes - Fine-grained control        │   │
│  └─────────────────────────────────────────────────────┘   │
└──────────────────────────┬──────────────────────────────────┘
                           │
┌──────────────────────────▼──────────────────────────────────┐
│         View/Serializer Layer (apps/)                       │
│  ┌──────────────────────────────────────────────────────┐  │
│  │ LMS App       │ Users App     │ Analytics App        │  │
│  │ • Courses     │ • Auth        │ • Tracking           │  │
│  │ • Lessons     │ • Profiles    │ • Performance        │  │
│  │ • Progress    │ • Roles       │                      │  │
│  └──────────────────────────────────────────────────────┘  │
└──────────────────────────┬──────────────────────────────────┘
                           │
┌──────────────────────────▼──────────────────────────────────┐
│            Business Logic Layer (services/)                 │
│  ┌──────────────────────────────────────────────────────┐  │
│  │ • ProgressTracker - Track student progress          │  │
│  │ • CodeExecutor - Run code challenges                │  │
│  │ • LectureService - Manage lectures                  │  │
│  └──────────────────────────────────────────────────────┘  │
└──────────────────────────┬──────────────────────────────────┘
                           │
┌──────────────────────────▼──────────────────────────────────┐
│          Data Access Layer (models/)                        │
│  ┌──────────────────────────────────────────────────────┐  │
│  │ • User, Course, Lesson, Enrollment, Progress        │  │
│  │ • Quiz, Question, QuizAttempt                        │  │
│  │ • Payment, Document, etc.                           │  │
│  └──────────────────────────────────────────────────────┘  │
└──────────────────────────┬──────────────────────────────────┘
                           │
┌──────────────────────────▼──────────────────────────────────┐
│              Database Layer                                 │
│  ┌─────────────────────┬────────────────┬────────────────┐  │
│  │ PostgreSQL (Prod)   │ SQLite (Dev)   │ Redis (Cache)  │  │
│  │ Primary data store  │ Development DB │ Session/Cache  │  │
│  └─────────────────────┴────────────────┴────────────────┘  │
└──────────────────────────────────────────────────────────────┘
```

## Request Flow Diagram

```
HTTP Request
    │
    ▼
Middleware Layer
    │
    ├─► RequestLoggingMiddleware (log request)
    │
    ├─► ErrorHandlingMiddleware (error handling)
    │
    ▼
CORS Check
    │
    ▼
Authentication Check
    │
    ├─► JWT Token Validation
    │
    ├─► User Lookup
    │
    ▼
Authorization Check
    │
    ├─► Permission Classes (IsStudent, IsInstructor, etc.)
    │
    ├─► Role-based Access Control
    │
    ▼
View Execution
    │
    ├─► Serializer Validation
    │
    ├─► Business Logic (Services)
    │
    ├─► Database Queries
    │
    ▼
Response Formatting
    │
    ├─► Pagination (if applicable)
    │
    ├─► Error/Success Response
    │
    ▼
HTTP Response
    │
    ▼
Client
```

## File Organization by Layer

```
Common (Shared Utilities)
├── utils/
│   ├── helpers.py (functions)
│   └── decorators.py (function wrappers)
├── middleware/
│   ├── request_logging.py
│   └── error_handling.py
├── exceptions/
│   └── custom_exceptions.py
├── permissions/
│   └── custom_permissions.py
├── pagination/
│   └── custom_pagination.py
└── validators/
    └── custom_validators.py

Apps (Business Logic)
├── lms/
│   ├── models/
│   ├── serializers/
│   ├── views/
│   └── services/
├── users/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   └── permissions.py
└── [other apps]

Configuration
├── myproject/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── common/
│   └── config.py
└── .env

Frontend
├── templates/
│   ├── base/
│   └── email/
└── static/
    ├── css/
    └── js/

Testing
├── tests/
│   ├── conftest.py (fixtures)
│   ├── factories/ (test data)
│   └── fixtures/ (test fixtures)
└── pytest.ini

Infrastructure
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── .gitignore
```

## Data Model Relationships

```
User (AbstractUser)
├── one-to-one → StudentProfile
├── one-to-one → RecruiterProfile
├── one-to-one → AdminProfile
├── one-to-many → Course (as instructor)
├── one-to-many → Enrollment
├── many-to-many → Course (enrolled)
└── many-to-many → Group, Permission

Course
├── many-to-one → User (instructor)
├── one-to-many → Module
├── one-to-many → Lesson
├── one-to-many → Enrollment
└── one-to-many → CourseAnalytics

Module
├── many-to-one → Course
└── one-to-many → Lesson

Lesson
├── many-to-one → Module
├── one-to-many → LessonProgress
└── one-to-many → Document

Enrollment
├── many-to-one → User
├── many-to-one → Course
└── one-to-many → LessonProgress

LessonProgress
├── many-to-one → User
├── many-to-one → Lesson
└── many-to-one → Enrollment
```

## API Endpoint Structure

```
/api/
├── auth/
│   ├── register/ (POST)
│   ├── login/ (POST)
│   ├── token/ (POST)
│   └── refresh/ (POST)
├── users/
│   ├── profile/ (GET, PUT)
│   └── {id}/ (GET, PUT, DELETE)
├── courses/
│   ├── (GET, POST)
│   ├── {id}/ (GET, PUT, DELETE)
│   └── {id}/lessons/ (GET)
├── lessons/
│   ├── (GET)
│   ├── {id}/ (GET, PUT)
│   └── {id}/progress/ (GET, PUT)
├── enrollments/
│   ├── (GET, POST)
│   └── {id}/ (GET, DELETE)
├── quizzes/
│   ├── (GET)
│   ├── {id}/ (GET)
│   └── {id}/attempts/ (POST)
└── analytics/
    ├── dashboard/ (GET)
    └── courses/{id}/ (GET)
```

## Technology Stack

```
Backend Framework
  └── Django 4.2 (Web Framework)
      ├── Django REST Framework (API)
      ├── Django CORS Headers (Cross-origin)
      ├── Django Filter (Filtering)
      └── Celery (Task Queue)

Authentication
  └── djangorestframework-simplejwt (JWT)

Database
  ├── PostgreSQL (Production)
  ├── SQLite (Development)
  └── Redis (Caching)

Testing
  ├── Pytest
  ├── Pytest-Django
  ├── Factory-Boy
  └── Pytest-Cov

Code Quality
  ├── Black (Formatting)
  ├── Flake8 (Linting)
  └── isort (Import Sorting)

File Storage
  └── Pillow (Image Processing)

Deployment
  ├── Docker
  ├── Docker Compose
  └── Gunicorn/WSGI
```

---

**This comprehensive structure is production-ready and scalable!**
