from django.db import models
from django.core.validators import MinValueValidator

class UserModel(models.Model):
    GENDER = (
        ('MALE', 'Male'),
        ('FEMALE', 'Female'),
        ('OTHER', 'Prefer not to say')
    )
    user_name = models.CharField(max_length=100)
    email = models.EmailField(blank=False, null=False)
    age = models.DecimalField(max_digits=2, decimal_places=0, validators=[MinValueValidator(0)])
    gender = models.CharField( max_length=6, choices=GENDER)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user_name

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        ordering = ['created']