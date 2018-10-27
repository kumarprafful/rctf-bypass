from django.db import models

# Create your models here.
class GeneratedString(models.Model):
    string = models.CharField(max_length=20)

    def __str__(self):
        return self.string
