#!/bin/bash

# Test script for CI/CD setup
echo "Testing CI/CD setup locally..."

# Activate virtual environment if it exists
if [ -d "venv" ]; then
    echo "Activating virtual environment..."
    source venv/bin/activate
fi

# Check if requirements are installed
echo "Checking if requirements are installed..."
pip list | grep -E "(black|flake8|coverage|coveralls)" || {
    echo "Installing requirements..."
    pip install -r requirements.txt
}

# Test black formatting
echo "Testing black formatting..."
black --check . && echo "✅ Black formatting check passed" || {
    echo "❌ Black formatting check failed. Run 'black .' to fix."
    exit 1
}

# Test flake8 linting
echo "Testing flake8 linting..."
flake8 . && echo "✅ Flake8 linting passed" || {
    echo "❌ Flake8 linting failed. Fix the issues above."
    exit 1
}

# Test Django tests
echo "Testing Django tests..."
python manage.py test && echo "✅ Django tests passed" || {
    echo "❌ Django tests failed. Fix the test issues."
    exit 1
}

# Test coverage
echo "Testing coverage..."
coverage run --source='.' manage.py test
coverage report
echo "✅ Coverage test completed"

echo "🎉 All CI/CD tests passed locally!"
echo "You can now push to GitHub and set up Travis CI."
