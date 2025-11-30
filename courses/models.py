# courses/models.py

from django.db import models
from django.utils.text import slugify
from django.core.validators import MinValueValidator, MaxValueValidator
from accounts.models import User

class Category(models.Model):
    """Course categories like Agriculture, Law, Sciences, etc."""
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    description = models.TextField(blank=True, null=True)
    icon_url = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Course(models.Model):
    """Online courses offered on Stax"""
    
    LEVEL_CHOICES = [
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
    ]
    
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='courses')
    instructor_name = models.CharField(max_length=255)
    instructor_image = models.ImageField(upload_to='instructors/', blank=True, null=True)
    instructor_bio = models.TextField(blank=True, null=True)
    
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    duration = models.CharField(max_length=100, help_text="e.g., '4 weeks', '20 hours'")
    level = models.CharField(max_length=20, choices=LEVEL_CHOICES, default='beginner')
    thumbnail_image = models.ImageField(upload_to='courses/', blank=True, null=True)
    
    is_published = models.BooleanField(default=False)
    enrolled_count = models.IntegerField(default=0)
    rating = models.DecimalField(
        max_digits=3, 
        decimal_places=2, 
        default=0.00,
        validators=[MinValueValidator(0.00), MaxValueValidator(5.00)]
    )
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class Lesson(models.Model):
    """Individual lessons within a course"""
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='lessons')
    title = models.CharField(max_length=255)
    description = models.TextField()
    video_url = models.URLField(blank=True, null=True)
    content = models.TextField(blank=True, null=True, help_text="Text content/notes")
    duration = models.CharField(max_length=50, help_text="e.g., '15 mins'")
    order = models.IntegerField(default=0)
    is_free_preview = models.BooleanField(default=False)
    
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['order']
    
    def __str__(self):
        return f"{self.course.title} - {self.title}"


class Enrollment(models.Model):
    """Track student enrollments in courses"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='enrollments')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='enrollments')
    enrolled_at = models.DateTimeField(auto_now_add=True)
    progress_percentage = models.IntegerField(
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(100)]
    )
    completed_at = models.DateTimeField(blank=True, null=True)
    certificate_issued = models.BooleanField(default=False)
    
    class Meta:
        unique_together = ('user', 'course')
        ordering = ['-enrolled_at']
    
    def __str__(self):
        return f"{self.user.email} - {self.course.title}"


class Review(models.Model):
    """Course reviews and ratings"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='reviews')
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        unique_together = ('user', 'course')
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.user.full_name} - {self.course.title} ({self.rating}★)"


class Certificate(models.Model):
    """Certificates issued upon course completion"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='certificates')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='certificates')
    certificate_id = models.CharField(max_length=100, unique=True)
    issued_at = models.DateTimeField(auto_now_add=True)
    certificate_url = models.URLField(blank=True, null=True)
    
    class Meta:
        unique_together = ('user', 'course')
        ordering = ['-issued_at']
    
    def __str__(self):
        return f"Certificate {self.certificate_id} - {self.user.full_name}"
    
    def save(self, *args, **kwargs):
        if not self.certificate_id:
            import uuid
            self.certificate_id = f"STAX-{uuid.uuid4().hex[:8].upper()}"
        super().save(*args, **kwargs)