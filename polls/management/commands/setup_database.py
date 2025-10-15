from django.core.management.base import BaseCommand
from django.core.management import call_command
from django.utils import timezone
from polls.models import Question, Choice


class Command(BaseCommand):
    help = "Setup database with migrations and sample data"

    def handle(self, *args, **options):
        self.stdout.write("Running migrations...")
        call_command("migrate", verbosity=0)

        self.stdout.write("Checking for existing data...")
        if not Question.objects.exists():
            self.stdout.write("Creating sample data...")

            # Create a sample question
            question = Question.objects.create(
                question_text="What is your favorite programming language?",
                pub_date=timezone.now(),
            )

            # Create choices
            Choice.objects.create(question=question, choice_text="Python", votes=0)

            Choice.objects.create(question=question, choice_text="JavaScript", votes=0)

            Choice.objects.create(question=question, choice_text="Java", votes=0)

            Choice.objects.create(question=question, choice_text="C++", votes=0)

            self.stdout.write(self.style.SUCCESS("Successfully created sample data!"))
        else:
            self.stdout.write("Sample data already exists.")

        self.stdout.write(self.style.SUCCESS("Database setup completed successfully!"))
