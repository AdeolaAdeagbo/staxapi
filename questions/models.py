# questions/models.py

from django.db import models
from django.core.validators import MinValueValidator
from accounts.models import User
from courses.models import Category

class PastQuestion(models.Model):
    """Past examination questions uploaded by contributors"""
    
    STATUS_CHOICES = [
        ('pending', 'Pending Review'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]
    
    SEMESTER_CHOICES = [
        ('first', 'First Semester'),
        ('second', 'Second Semester'),
        ('both', 'Both Semesters'),
    ]
    
    title = models.CharField(max_length=255)
    university = models.CharField(max_length=255)
    course_code = models.CharField(max_length=50)
    course_name = models.CharField(max_length=255)
    year = models.IntegerField(validators=[MinValueValidator(2000)])
    semester = models.CharField(max_length=20, choices=SEMESTER_CHOICES)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='past_questions')
    
    # File upload
    file = models.FileField(upload_to='past_questions/')
    file_type = models.CharField(max_length=10, blank=True)  # pdf, jpg, png
    
    # Contributor info
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='uploaded_questions')
    points_earned = models.IntegerField(default=10)  # Points given to contributor
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    
    # Engagement metrics
    views_count = models.IntegerField(default=0)
    downloads_count = models.IntegerField(default=0)
    
    # Admin review
    reviewed_by = models.ForeignKey(
        User, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True,
        related_name='reviewed_questions'
    )
    review_notes = models.TextField(blank=True, null=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Past Question'
        verbose_name_plural = 'Past Questions'
    
    def __str__(self):
        return f"{self.course_code} - {self.university} ({self.year})"
    
    def save(self, *args, **kwargs):
        # Set file type based on uploaded file
        if self.file:
            extension = self.file.name.split('.')[-1].lower()
            self.file_type = extension
        super().save(*args, **kwargs)
    
    def increment_views(self):
        """Increment view count"""
        self.views_count += 1
        self.save(update_fields=['views_count'])
    
    def increment_downloads(self):
        """Increment download count"""
        self.downloads_count += 1
        self.save(update_fields=['downloads_count'])


class Contribution(models.Model):
    """Track user contributions and points earned"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='contributions')
    past_question = models.ForeignKey(
        PastQuestion, 
        on_delete=models.CASCADE, 
        related_name='contributions'
    )
    points_awarded = models.IntegerField(default=0)
    status = models.CharField(
        max_length=20,
        choices=PastQuestion.STATUS_CHOICES,
        default='pending'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.user.full_name} - {self.points_awarded} points"


class QuestionDownload(models.Model):
    """Track who downloaded what questions"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='downloads')
    past_question = models.ForeignKey(
        PastQuestion,
        on_delete=models.CASCADE,
        related_name='download_records'
    )
    downloaded_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-downloaded_at']
        unique_together = ('user', 'past_question')
    
    def __str__(self):
        return f"{self.user.email} - {self.past_question.course_code}"