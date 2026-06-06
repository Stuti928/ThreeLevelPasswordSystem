from django.db import models

class UserData(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)

    rgb_password = models.CharField(max_length=100)

    image_password = models.ImageField(upload_to='password_images/')

    def __str__(self):
        return self.username