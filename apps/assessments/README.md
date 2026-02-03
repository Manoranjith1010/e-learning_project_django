# Assessments App

Quiz and assessment management.

## Models

- **Quiz** - Quiz metadata
- **Question** - Quiz questions
- **QuizAttempt** - Student quiz attempts

## API Endpoints

- `GET /api/quizzes/` - List quizzes
- `POST /api/quizzes/{id}/attempts/` - Start quiz attempt
- `POST /api/quiz-attempts/{id}/submit/` - Submit answers

## Features

- Multiple question types (MCQ, short answer)
- Auto-grading for MCQs
- Attempt tracking
- Score analytics
