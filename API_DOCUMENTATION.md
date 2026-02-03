# API Documentation

## Authentication

All API endpoints require JWT authentication except public endpoints.

### Get Access Token
```
POST /api/token/
Content-Type: application/json

{
    "username": "user@example.com",
    "password": "password123"
}
```

Response:
```json
{
    "access": "eyJ0eXAiOiJKV1QiLCJhbGc...",
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGc..."
}
```

### Using Access Token
```
GET /api/courses/
Authorization: Bearer <access_token>
```

## User Management

### Create User
```
POST /api/users/register/
Content-Type: application/json

{
    "username": "newuser",
    "email": "user@example.com",
    "password": "securepassword123",
    "first_name": "John",
    "last_name": "Doe",
    "role": "student"
}
```

### Get User Profile
```
GET /api/users/profile/
Authorization: Bearer <access_token>
```

### Update User Profile
```
PUT /api/users/profile/
Authorization: Bearer <access_token>
Content-Type: application/json

{
    "first_name": "Jane",
    "bio": "Student of web development"
}
```

## Courses

### List Courses
```
GET /api/courses/?page=1&page_size=20
```

Query Parameters:
- `page` - Page number (default: 1)
- `page_size` - Results per page (default: 20, max: 100)
- `search` - Search in title/description
- `level` - Filter by level (beginner, intermediate, advanced)
- `status` - Filter by status (draft, published, archived)

### Get Course Details
```
GET /api/courses/{id}/
```

### Create Course
```
POST /api/courses/
Authorization: Bearer <access_token>
Content-Type: application/json

{
    "title": "Django Basics",
    "slug": "django-basics",
    "description": "Learn Django fundamentals",
    "category": "Web Development",
    "level": "beginner",
    "duration_weeks": 4
}
```

### Update Course
```
PUT /api/courses/{id}/
Authorization: Bearer <access_token>
Content-Type: application/json
```

### Delete Course
```
DELETE /api/courses/{id}/
Authorization: Bearer <access_token>
```

## Enrollments

### Enroll in Course
```
POST /api/enrollments/
Authorization: Bearer <access_token>
Content-Type: application/json

{
    "course_id": 1
}
```

### Get User Enrollments
```
GET /api/enrollments/
Authorization: Bearer <access_token>
```

## Progress Tracking

### Get Course Progress
```
GET /api/progress/?course_id={course_id}
Authorization: Bearer <access_token>
```

### Update Lesson Progress
```
PUT /api/progress/{id}/
Authorization: Bearer <access_token>
Content-Type: application/json

{
    "status": "completed",
    "notes": "Completed all exercises"
}
```

## Error Responses

All error responses follow this format:

```json
{
    "success": false,
    "message": "Error description",
    "error_code": "ERROR_CODE",
    "details": {}
}
```

HTTP Status Codes:
- `200` - Success
- `201` - Created
- `400` - Bad Request
- `401` - Unauthorized
- `403` - Forbidden
- `404` - Not Found
- `409` - Conflict
- `429` - Too Many Requests
- `500` - Server Error

## Rate Limiting

API rate limits:
- 1000 requests per hour per IP
- 100 requests per minute for authenticated users

Response headers:
- `X-RateLimit-Limit` - Total limit
- `X-RateLimit-Remaining` - Requests remaining
- `X-RateLimit-Reset` - Reset timestamp

## Pagination

Standard pagination response:

```json
{
    "count": 42,
    "next": "http://api.example.com/courses/?page=2",
    "previous": null,
    "results": [...]
}
```

## Examples

### Complete User Registration Flow
```bash
# 1. Register
curl -X POST http://localhost:8000/api/users/register/ \
  -H "Content-Type: application/json" \
  -d '{
    "username": "john_doe",
    "email": "john@example.com",
    "password": "securepass123",
    "first_name": "John",
    "last_name": "Doe",
    "role": "student"
  }'

# 2. Login
curl -X POST http://localhost:8000/api/token/ \
  -H "Content-Type: application/json" \
  -d '{
    "username": "john_doe",
    "password": "securepass123"
  }'

# 3. Get profile
curl -X GET http://localhost:8000/api/users/profile/ \
  -H "Authorization: Bearer <access_token>"
```

## Webhooks (Future Implementation)

Webhooks will be available for events like:
- `user.created` - New user registration
- `enrollment.created` - New course enrollment
- `course.published` - Course published
- `payment.completed` - Payment completed
