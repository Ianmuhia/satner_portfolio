from django.db import models


# Create your models here.
class cv(models.Model):
    # file = models.FileField(upload_to='cv/')
    cv = models.TextField()

    def __str__(self):
        return self.cv
