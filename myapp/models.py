from django.db import models

class URL(models.Model):
    url = models.CharField(max_length=200)
    update_at = models.DateTimeField(auto_now_add=True)
    is_available = models.BooleanField(default=False)
    
    def __str__(self):
        return self.url