# Django Polls Application

A Django web application for creating and managing polls, built as part of Software Engineering coursework.

## Features

- Create and manage polls
- Vote on polls
- View poll results
- Admin interface for poll management

## Build Status

[![Build Status](https://travis-ci.com/YOUR_GITHUB_USERNAME/YOUR_REPO_NAME.svg?branch=main)](https://travis-ci.com/YOUR_GITHUB_USERNAME/YOUR_REPO_NAME)
[![Coverage Status](https://coveralls.io/repos/github/YOUR_GITHUB_USERNAME/YOUR_REPO_NAME/badge.svg?branch=main)](https://coveralls.io/github/YOUR_GITHUB_USERNAME/YOUR_REPO_NAME)

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/YOUR_GITHUB_USERNAME/YOUR_REPO_NAME.git
   cd YOUR_REPO_NAME
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

[Deployed Application URL](https://your-app-name.elasticbeanstalk.com)

## License

This project is for educational purposes.
