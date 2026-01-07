from django.db import models

class Task(models.Model):
    # Fields Indentify
    title = models.CharField(max_length=200)  # VARCHAR(200)
    completed = models.BooleanField(default=False) # BOOLEAN (0/1)
    created_at = models.DateTimeField(auto_now_add=True) # TIMESTAMP

    def __str__(self):
        return self.title