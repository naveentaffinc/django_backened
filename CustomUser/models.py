from django.db import models



class CustomUserModel(models.Model):

    #defining the fields of the model below.

    email = models.EmailField(max_length = 100)
    username = models.CharField(unique=True, max_length=50)
    password = models.CharField(max_length = 100)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username