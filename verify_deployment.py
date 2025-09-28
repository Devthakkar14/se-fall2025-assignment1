#!/usr/bin/env python
"""
Deployment verification script for Django polls application.
This script checks if the database is properly set up and accessible.
"""

import os
import sys
import django

# Add the project directory to the Python path
sys.path.append('/var/app/current')

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myAPP_SEfall2025.settings')
django.setup()

from django.db import connection
from polls.models import Question, Choice

def verify_deployment():
    """Verify that the deployment is working correctly."""
    print("=== Deployment Verification ===")
    
    try:
        # Test database connection
        with connection.cursor() as cursor:
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
            tables = cursor.fetchall()
            print(f"✓ Database connection successful")
            print(f"✓ Found {len(tables)} tables: {[table[0] for table in tables]}")
        
        # Check if polls_question table exists
        if any('polls_question' in table for table in tables):
            print("✓ polls_question table exists")
        else:
            print("✗ polls_question table missing!")
            return False
        
        # Check if polls_choice table exists
        if any('polls_choice' in table for table in tables):
            print("✓ polls_choice table exists")
        else:
            print("✗ polls_choice table missing!")
            return False
        
        # Test model access
        question_count = Question.objects.count()
        choice_count = Choice.objects.count()
        print(f"✓ Found {question_count} questions and {choice_count} choices")
        
        if question_count == 0:
            print("⚠ No questions found - sample data may not have been created")
        else:
            print("✓ Sample data is present")
        
        print("=== Deployment verification completed successfully! ===")
        return True
        
    except Exception as e:
        print(f"✗ Deployment verification failed: {e}")
        return False

if __name__ == '__main__':
    success = verify_deployment()
    sys.exit(0 if success else 1)
