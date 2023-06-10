from django.core.mail import send_mail
from django.core.management.base import BaseCommand
from tasks.task.models import Task
from django.contrib.auth.models import User

class Command(BaseCommand):
    def handle(self, *args, **options):
        # get all users
        users = User.objects.all()
        # loop through each user
        for user in users:
            # get the tasks for the user
            tasks = Task.objects.filter(owner=user)
            # create a message with the task details
            message = f"Hello {user.username},\n\nHere are your tasks for today:\n\n"
            for task in tasks:
                message += f"- {task.title}: {task.detail} ({task.status})\n"
            message += "\nHave a nice day!"
            # send an email to the user
            send_mail(
                "Your daily tasks",
                message,
                "something@example.com",
                [user.email],
                fail_silently=False,
            )
            print(f"Successfully sent email to {user.email}")
