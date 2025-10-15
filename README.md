# Django Polls Application

A Django web application for creating and managing polls, built as part of Software Engineering coursework.

## Features

- Create and manage polls
- Vote on polls
- View poll results
- Admin interface for poll management

## Build Status

[![Build Status](https://travis-ci.com/Devthakkar14/se-fall2025-assignment1.svg?branch=main)](https://travis-ci.com/Devthakkar14/se-fall2025-assignment1)
[![Coverage Status](https://coveralls.io/repos/github/Devthakkar14/se-fall2025-assignment1/badge.svg?branch=main)](https://coveralls.io/github/Devthakkar14/se-fall2025-assignment1)

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/Devthakkar14/se-fall2025-assignment1.git
   cd se-fall2025-assignment1
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run migrations:
   ```bash
   python manage.py migrate
   ```

5. Create a superuser:
   ```bash
   python manage.py createsuperuser
   ```

6. Run the development server:
   ```bash
   python manage.py runserver
   ```

## Testing

Run the test suite:
```bash
python manage.py test
```

Run with coverage:
```bash
coverage run --source='.' manage.py test
coverage report
```

## Code Quality

This project uses:
- **Black** for code formatting
- **Flake8** for linting
- **Coverage.py** for test coverage
- **Travis CI** for continuous integration

## Deployment

The application is automatically deployed to AWS Elastic Beanstalk when tests pass on the main branch.

## Live Application

[Deployed Application URL](https://django-polls-prod.eba-g4a3cury.us-east-1.elasticbeanstalk.com)

## License

This project is for educational purposes.

## Test Update

This is a test update to verify CI/CD pipeline is working correctly.
