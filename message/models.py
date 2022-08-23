from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Message(models.model):
    target = models.ForeignKey(get_user_model())
    message = models.TextField()
    @property
    def get_title(self):
        return self.message[0:10]
    
    def __str__(self) -> str:
        return self.get_title
