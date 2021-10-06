from django.db import models

# Model for a contact message
class Contact(models.Model):
    email=models.EmailField()
    subject=models.CharField(max_length=255)
    message=models.TextField()

    def __str__(self):
        return self.email

    