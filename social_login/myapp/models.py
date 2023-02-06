from django.db import models

class User(models.Model):
    email = models.EmailField(unique=True,blank=False)
    password = models.CharField(max_length=20)
    otp =models.IntegerField(default=459)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True,blank=False)
    updated_at = models.DateTimeField(auto_now=True,blank=False)

    def __str__(self):
        return self.email+ "- "+self.email