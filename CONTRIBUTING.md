# Contributing Guidelines

## Code Standards

### Python Style
- Follow PEP 8
- Use 4 spaces for indentation
- Max line length: 88 characters (Black formatter)
- Use meaningful variable names

### Django Best Practices
- Use class-based views when possible
- Always define `__str__()` in models
- Use `get_user_model()` for user references
- Add help_text to model fields
- Use related_name for reverse relations

### Naming Conventions
- Models: CamelCase (e.g., `CourseModule`)
- Functions: snake_case (e.g., `get_course_modules`)
- Constants: UPPER_SNAKE_CASE (e.g., `MAX_UPLOAD_SIZE`)
- Files: snake_case (e.g., `course_views.py`)

## Git Workflow

### Branch Naming
```
feature/description
bugfix/description
hotfix/description
refactor/description
```

### Commit Messages
```
[Type] Brief description

Detailed explanation if needed
- List any key changes
- Reference issues if applicable
```

Types: feat, fix, docs, style, refactor, test

### Pull Request Template
```
## Description
Brief description of changes

## Type of Change
- [ ] Feature
- [ ] Bug fix
- [ ] Documentation
- [ ] Refactoring

## Testing
- [ ] Unit tests added
- [ ] Integration tests added
- [ ] Manual testing completed

## Checklist
- [ ] Code follows style guidelines
- [ ] Documentation updated
- [ ] No breaking changes
```

## Code Review Checklist

- [ ] Code is readable and well-commented
- [ ] No duplicate code
- [ ] Proper error handling
- [ ] Tests are comprehensive
- [ ] Documentation is updated
- [ ] No sensitive data in code
- [ ] Performance implications considered

## Testing Requirements

- All new code must have tests
- Minimum 80% code coverage
- Run tests before committing: `pytest`
- Test both success and failure cases

### Test Structure
```python
class TestUserCreation:
    """Tests for user creation"""
    
    def test_valid_user_creation(self):
        """Test creating user with valid data"""
        pass
    
    def test_duplicate_email(self):
        """Test that duplicate emails are rejected"""
        pass
```

## Documentation Requirements

- Docstrings on all functions/classes
- README.md for each app
- Inline comments for complex logic
- Update API_DOCUMENTATION.md for endpoints

### Docstring Format
```python
def get_user_courses(user_id: int) -> list:
    """
    Get all courses for a specific user
    
    Args:
        user_id: The ID of the user
        
    Returns:
        List of Course objects
        
    Raises:
        NotFoundError: If user doesn't exist
    """
```

## Security Guidelines

- Never commit .env or secrets
- Use environment variables
- Validate all user input
- Use prepared statements for queries
- Add rate limiting to sensitive endpoints
- Hash passwords (Django handles this)
- Validate file uploads
- Use HTTPS in production

## Performance Guidelines

- Use select_related() for foreign keys
- Use prefetch_related() for reverse relations
- Add database indexes on frequently queried fields
- Cache expensive operations
- Use pagination for large datasets
- Profile before optimizing

## Release Process

1. Update version in `setup.py`
2. Update CHANGELOG.md
3. Create release branch: `release/v1.0.0`
4. Merge to main and tag: `v1.0.0`
5. Deploy to production

## Questions?

- Check existing code for patterns
- Read Django documentation
- Ask in team discussions
- Review similar implementations
