# LMS (Learning Management System) App

Core app for course management and learning.

## Models

- **Course** - Course information and metadata
- **Module** - Course modules/units
- **Lesson** - Individual lessons within modules
- **Enrollment** - Student enrollment in courses
- **LessonProgress** - Student progress on lessons

## Views

- `CourseViewSet` - CRUD operations for courses
- `LessonViewSet` - CRUD operations for lessons
- `EnrollmentViewSet` - Manage enrollments
- `ProgressViewSet` - Track learning progress

## API Endpoints

- `GET /api/courses/` - List all courses
- `POST /api/courses/` - Create new course
- `GET /api/courses/{id}/` - Get course details
- `PUT /api/courses/{id}/` - Update course
- `DELETE /api/courses/{id}/` - Delete course

## Permissions

- Students can only access enrolled courses
- Instructors can manage their own courses
- Admins have full access

## Services

### ProgressTracker
Tracks student progress through courses

```python
from apps.lms.services import ProgressTracker

tracker = ProgressTracker(user, course)
completion_percentage = tracker.get_progress()
tracker.mark_lesson_complete(lesson_id)
```
