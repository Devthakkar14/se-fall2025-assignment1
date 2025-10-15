from django.core.management.base import BaseCommand
from django.utils import timezone
from polls.models import Question, Choice


class Command(BaseCommand):
    help = "Add a sample poll to the database"

    def add_arguments(self, parser):
        parser.add_argument(
            "--question",
            type=str,
            default="What's your favorite programming language?",
            help="The question text",
        )

    def handle(self, *args, **options):
        question_text = options["question"]

        # Create the question
        question = Question.objects.create(
            question_text=question_text,
            pub_date=timezone.now(),
        )

        # Create some default choices
        choices = ["Python", "JavaScript", "Java", "C++", "Other"]

        for choice_text in choices:
            Choice.objects.create(question=question, choice_text=choice_text, votes=0)

        self.stdout.write(
            self.style.SUCCESS(f'Successfully created poll: "{question_text}"')
        )
