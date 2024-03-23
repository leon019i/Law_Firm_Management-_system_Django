import os
import django
from faker import Faker
import random

# Replace 'myproject.settings' with the path to your settings module,
# typically '<your_project_name>.settings'
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoProject.settings')
django.setup()

# Now you can import your models
from cases.models import Client, Lawyer, Case

fake = Faker()


# Function to create fake clients
def create_clients(n):
    for _ in range(n):
        phone_number = ''.join(filter(str.isdigit, fake.phone_number()))[:15]  # Keep only digits and limit to 15
        Client.objects.create(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            email=fake.email(),
            phone=phone_number,
        )


# Function to create fake lawyers
def create_lawyers(n):
    for _ in range(n):
        phone_number = ''.join(filter(str.isdigit, fake.phone_number()))[:15]  # Keep only digits and limit to 15
        Lawyer.objects.create(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            email=fake.email(),
            phone=phone_number,
        )


# Function to create fake cases
def create_cases(n):
    clients = list(Client.objects.all())
    lawyers = list(Lawyer.objects.all())
    status_choices = [choice[0] for choice in Case.STATUS_CHOICES]

    for _ in range(n):
        Case.objects.create(
            title=fake.sentence(nb_words=5),
            description=fake.text(max_nb_chars=200),
            status=random.choice(status_choices),
            client=random.choice(clients),
            lawyer=random.choice(lawyers),
        )


# Creating fake data
create_clients(10)  # Create 10 fake clients
create_lawyers(9)  # Create 5 fake lawyers
create_cases(20)  # Create 20 fake cases



