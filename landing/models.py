from django.db import models

class Information(models.Model):
    firstName = models.CharField(max_length=75)
    lastName = models.CharField(max_length=75)
    email = models.EmailField()
    questions = models.TextField(max_length=450, blank=True)

    def __str__(self):
        return f'{self.email}'
