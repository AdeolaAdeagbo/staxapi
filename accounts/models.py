# accounts/models.py

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator

class User(AbstractUser):
    """Custom User model for Stax platform"""
    
    ROLE_CHOICES = [
        ('student', 'Student'),
        ('contributor', 'Contributor'),
        ('admin', 'Admin'),
    ]
    
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=255)
    university = models.CharField(max_length=255, blank=True, null=True)
    course_of_study = models.CharField(max_length=255, blank=True, null=True)
    profile_image = models.ImageField(upload_to='profiles/', blank=True, null=True)
    points = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    is_verified = models.BooleanField(default=False)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='student')
    bio = models.TextField(blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # Override username requirement - use email as primary identifier
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'full_name']
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = 'User'
        verbose_name_plural = 'Users'
    
    def __str__(self):
        return self.email
    
    def add_points(self, points):
        """Add points to user account"""
        self.points += points
        self.save()
        
    def deduct_points(self, points):
        """Deduct points from user account"""
        if self.points >= points:
            self.points -= points
            self.save()
            return True
        return False
