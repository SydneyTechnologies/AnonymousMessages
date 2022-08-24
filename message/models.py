from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Message(models.Model):
    target = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, blank=True, null=True)
    message = models.TextField()
    @property
    def get_title(self):
        return self.message[0:10]
    
    def __str__(self) -> str:
        return self.get_title
