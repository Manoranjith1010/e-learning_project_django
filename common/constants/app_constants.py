"""
Application-wide constants
"""

# User Roles
USER_ROLES = {
    "STUDENT": "student",
    "INSTRUCTOR": "instructor",
    "ADMIN": "admin",
    "RECRUITER": "recruiter",
}

USER_ROLE_CHOICES = [
    ("student", "Student"),
    ("instructor", "Instructor"),
    ("admin", "Admin"),
    ("recruiter", "Recruiter"),
]

# Course Levels
COURSE_LEVELS = {
    "BEGINNER": "beginner",
    "INTERMEDIATE": "intermediate",
    "ADVANCED": "advanced",
}

COURSE_LEVEL_CHOICES = [
    ("beginner", "Beginner"),
    ("intermediate", "Intermediate"),
    ("advanced", "Advanced"),
]

# Course Status
COURSE_STATUS = {
    "DRAFT": "draft",
    "PUBLISHED": "published",
    "ARCHIVED": "archived",
}

COURSE_STATUS_CHOICES = [
    ("draft", "Draft"),
    ("published", "Published"),
    ("archived", "Archived"),
]

# Enrollment Status
ENROLLMENT_STATUS = {
    "ACTIVE": "active",
    "COMPLETED": "completed",
    "DROPPED": "dropped",
    "PENDING": "pending",
}

ENROLLMENT_STATUS_CHOICES = [
    ("active", "Active"),
    ("completed", "Completed"),
    ("dropped", "Dropped"),
    ("pending", "Pending"),
]

# Lesson Status
LESSON_STATUS = {
    "NOT_STARTED": "not_started",
    "IN_PROGRESS": "in_progress",
    "COMPLETED": "completed",
}

LESSON_STATUS_CHOICES = [
    ("not_started", "Not Started"),
    ("in_progress", "In Progress"),
    ("completed", "Completed"),
]

# Payment Status
PAYMENT_STATUS = {
    "PENDING": "pending",
    "COMPLETED": "completed",
    "FAILED": "failed",
    "REFUNDED": "refunded",
}

PAYMENT_STATUS_CHOICES = [
    ("pending", "Pending"),
    ("completed", "Completed"),
    ("failed", "Failed"),
    ("refunded", "Refunded"),
]

# Pagination
DEFAULT_PAGE_SIZE = 20
MAX_PAGE_SIZE = 100

# API Settings
API_TIMEOUT = 30  # seconds
MAX_UPLOAD_SIZE = 10 * 1024 * 1024  # 10 MB

# Cache Timeouts
CACHE_TIMEOUT_SHORT = 300  # 5 minutes
CACHE_TIMEOUT_MEDIUM = 3600  # 1 hour
CACHE_TIMEOUT_LONG = 86400  # 24 hours
