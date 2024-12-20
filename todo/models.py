from django.db import models


class Todo(models.Model):
    event = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.event[:50]

    class Meta:
        ordering = ['-created_at']
