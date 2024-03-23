from django.db import models


# Create your models here.

class Client(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self
        "{self.first_name} {self.last_name}"


class Lawyer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self
        "{self.first_name} {self.last_name}"


class Case(models.Model):
    STATUS_CHOICES = (
        ('PENDING', 'Pending'),
        ('OPEN', 'Open'),
        ('CLOSED', 'Closed')
    )
    title = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)

    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    lawyer = models.ForeignKey(Lawyer, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
