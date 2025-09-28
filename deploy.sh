#!/bin/bash

# Django Polls App Deployment Script
# This script prepares and deploys the Django application to AWS Elastic Beanstalk

echo "=== Django Polls App Deployment Script ==="

# Check if we're in the right directory
if [ ! -f "manage.py" ]; then
    echo "Error: manage.py not found. Please run this script from the project root directory."
    exit 1
fi

# Clean up unnecessary files
echo "Cleaning up unnecessary files..."
rm -rf venv/ __pycache__/ .git/
find . -name "*.pyc" -delete
find . -name "__pycache__" -type d -exec rm -rf {} + 2>/dev/null || true

# Remove documentation files from deployment
rm -f *.md

echo "Files cleaned up successfully."

# Create deployment package
echo "Creating deployment package..."
zip -r django-polls-deployment.zip . -x "venv/*" ".git/*" "*.pyc" "__pycache__/*" "*.md" "deploy.sh"

echo "Deployment package created: django-polls-deployment.zip"

# Check if EB CLI is available
if command -v eb &> /dev/null; then
    echo "EB CLI found. Deploying to Elastic Beanstalk..."
    eb deploy
else
    echo "EB CLI not found. Please upload django-polls-deployment.zip manually to AWS Elastic Beanstalk."
    echo "Or install EB CLI: pip install awsebcli"
fi

echo "=== Deployment script completed ==="
