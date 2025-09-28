#!/usr/bin/env python
"""
Script to create sample data for the polls application.
This script is run after migrations to populate the database with initial data.
"""

import os
import sys
import django
from django.utils import timezone

# Add the project directory to the Python path
sys.path.append('/var/app/current')

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myAPP_SEfall2025.settings')
django.setup()

from polls.models import Question, Choice

def create_sample_data():
    """Create sample questions and choices if they don't exist."""
    print("Checking for existing data...")
    
    if Question.objects.exists():
        print("Sample data already exists.")
        return
    
    print("Creating sample data...")
    
    # Create sample questions
    questions_data = [
        {
            'question_text': "What is your favorite programming language?",
            'choices': [
                ("Python", 0),
                ("JavaScript", 0),
                ("Java", 0),
                ("C++", 0),
                ("Go", 0)
            ]
        },
        {
            'question_text': "What is your preferred development environment?",
            'choices': [
                ("VS Code", 0),
                ("PyCharm", 0),
                ("Vim/Neovim", 0),
                ("Sublime Text", 0),
                ("IntelliJ IDEA", 0)
            ]
        },
        {
            'question_text': "Which database do you prefer for web applications?",
            'choices': [
                ("PostgreSQL", 0),
                ("MySQL", 0),
                ("SQLite", 0),
                ("MongoDB", 0),
                ("Redis", 0)
            ]
        }
    ]
    
    for q_data in questions_data:
        question = Question.objects.create(
            question_text=q_data['question_text'],
            pub_date=timezone.now()
        )
        
        for choice_text, votes in q_data['choices']:
            Choice.objects.create(
                question=question,
                choice_text=choice_text,
                votes=votes
            )
    
    print("Successfully created sample data!")

if __name__ == '__main__':
    try:
        create_sample_data()
        print("Sample data creation completed successfully!")
    except Exception as e:
        print(f"Error creating sample data: {e}")
        sys.exit(1)