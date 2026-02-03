# E-Learning Platform - Django Project Structure Guide

## 📁 Project Structure Overview

```
e-learning_project_django/
├── apps/                           # Django applications
│   ├── analytics/                  # Analytics and tracking
│   ├── assessments/                # Quizzes and assessments
│   ├── coding/                     # Coding challenges
│   ├── documents/                  # Course documents
│   ├── finance/                    # Payment and invoicing
│   ├── lms/                        # Learning management system (core)
│   ├── sincerity/                  # Academic integrity checks
│   └── users/                      # User management
├── common/                         # Shared utilities
│   ├── utils/                      # Helper functions
│   ├── middleware/                 # Custom middleware
│   ├── exceptions/                 # Custom exceptions
│   ├── constants/                  # Application constants
│   ├── permissions/                # Custom permissions
│   ├── pagination/                 # Custom pagination
│   ├── validators/                 # Custom validators
│   └── config.py                   # Configuration
├── myproject/                      # Django project settings
├── templates/                      # HTML templates
├── static/                         # Static files (CSS, JS, images)
├── media/                          # User uploaded files
├── tests/                          # Test suite
├── scripts/                        # Management commands
├── manage.py                       # Django management
└── requirements.txt                # Python dependencies
```

## 🚀 Getting Started

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Environment Setup
```bash
cp .env.example .env
# Edit .env with your configuration
```

### 3. Database Setup
```bash
python manage.py migrate
python manage.py create_sample_data
```

### 4. Create Superuser
```bash
python manage.py createsuperuser
```

### 5. Run Development Server
```bash
python manage.py runserver
```

## 📚 Common Utilities

### Helpers (common/utils/helpers.py)
- `get_client_ip()` - Extract client IP from request
- `generate_token()` - Generate secure random token
- `send_email()` - Send emails with HTML support
- `format_error_response()` - Format error responses
- `format_success_response()` - Format success responses

### Decorators (common/utils/decorators.py)
- `@require_role()` - Check user role before accessing view
- `@handle_exceptions()` - Handle exceptions in views
- `@rate_limit()` - Rate limiting decorator
- `@cache_view()` - Cache view response

### Custom Exceptions (common/exceptions/custom_exceptions.py)
- `ValidationError` - Validation failed
- `NotFoundError` - Resource not found
- `PermissionDeniedError` - Insufficient permissions
- `ConflictError` - Resource conflict
- `RateLimitError` - Rate limit exceeded

### Custom Permissions (common/permissions/custom_permissions.py)
- `IsStudent` - Only student users
- `IsInstructor` - Only instructor users
- `IsAdminUser` - Only admin users
- `IsOwner` - Only object owner
- `IsStudentOrReadOnly` - Students read/write, others read only

## 🧪 Testing

### Run All Tests
```bash
pytest
```

### Run Specific Test
```bash
pytest tests/test_users.py::TestUserCreation
```

### Run with Coverage
```bash
pytest --cov=apps --cov=common
```

## 📋 Management Commands

### Create Sample Data
```bash
python manage.py create_sample_data
```

### List Users
```bash
python manage.py list_users
python manage.py list_users --role=instructor
```

## 🔧 API Usage

### Using Custom Responses
```python
from common.utils.helpers import format_success_response, format_error_response

# Success response
return Response(format_success_response(
    "User created successfully",
    data=serializer.data,
))

# Error response
return Response(format_error_response(
    "Invalid email",
    error_code="INVALID_EMAIL",
    details={"email": ["Invalid format"]}
), status=400)
```

### Using Decorators
```python
from common.utils.decorators import require_role, handle_exceptions

@require_role(['instructor', 'admin'])
@handle_exceptions
def create_course(request):
    # View code
    pass
```

### Using Exceptions
```python
from common.exceptions import ValidationError, NotFoundError

try:
    user = User.objects.get(id=user_id)
except User.DoesNotExist:
    raise NotFoundError("User not found")

if not validate_email(email):
    raise ValidationError("Invalid email format", error_code="INVALID_EMAIL")
```

## 🔐 Security Best Practices

1. **Environment Variables** - Use .env for sensitive data
2. **CORS** - Configure CORS_ALLOWED_ORIGINS in settings
3. **JWT** - Use JWT for API authentication
4. **Permissions** - Always check permissions in views
5. **Validation** - Validate all user input
6. **Rate Limiting** - Use @rate_limit decorator for sensitive operations
7. **Logging** - All important events are logged

## 📝 Logging

Logs are configured in `common/config.py`:
- **Console**: Real-time logs in terminal
- **File**: Rotating logs in `logs/app.log` (max 10MB, keeps 10 backups)

```python
import logging
logger = logging.getLogger(__name__)

logger.info("User login successful")
logger.warning("Suspicious activity detected")
logger.error("Database connection failed", exc_info=True)
```

## 🚦 API Pagination

All list endpoints use pagination:
```
GET /api/courses/?page=1&page_size=20
```

Default page size: 20
Maximum page size: 100

## 📦 Database Models

All models inherit from Django's base models:
- Use `auto_now_add=True` for creation timestamps
- Use `auto_now=True` for update timestamps
- Add `related_name` for reverse relations
- Use descriptive field names

## 🎯 Constants Usage

```python
from common.constants import USER_ROLES, COURSE_LEVELS, PAYMENT_STATUS

user.role = USER_ROLES['STUDENT']
course.level = COURSE_LEVELS['BEGINNER']
payment.status = PAYMENT_STATUS['COMPLETED']
```

## 📧 Email Templates

Email templates are in `templates/email/`:
- `base_email.html` - Base email template
- `verify_email.html` - Email verification
- Add more as needed

## 🗂️ Static Files

- CSS: `static/css/`
- JavaScript: `static/js/`
- Images: `static/images/`

Collect static files:
```bash
python manage.py collectstatic
```

## 📞 Support

For issues or questions, refer to the individual app documentation or open an issue on GitHub.
