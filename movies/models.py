from django.db import models
from users.models import UserModel

class MovieModel(models.Model):
    usuario = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    review = models.TextField()
    created = models.DateTimeField(auto_now_add=True),
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.usuario
    
    class Meta:
        verbose_name = 'Movie'
        verbose_name_plural = 'Movies'
        ordering = ['-updated']
