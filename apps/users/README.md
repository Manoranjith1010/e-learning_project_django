# Users App

User management, authentication, and profile management.

## Models

- **User** - Custom user model with roles
- **StudentProfile** - Extended student information
- **RecruiterProfile** - Extended recruiter information
- **AdminProfile** - Extended admin information

## User Roles

- `student` - Course learner
- `instructor` - Course creator
- `admin` - System administrator
- `recruiter` - Recruiter for placement

## API Endpoints

- `POST /api/users/register/` - User registration
- `POST /api/users/login/` - User login
- `GET /api/users/profile/` - Get user profile
- `PUT /api/users/profile/` - Update user profile
- `POST /api/users/logout/` - User logout
- `POST /api/users/verify-email/` - Verify email

## Features

- Email verification
- Phone verification
- Profile picture upload
- Role-based access control
- Password reset via email

## Usage

```python
from django.contrib.auth import get_user_model

User = get_user_model()

# Create user
user = User.objects.create_user(
    username="john",
    email="john@example.com",
    password="secure123",
    role="student"
)

# Check role
if user.role == "instructor":
    # Instructor-specific code
    pass
```
