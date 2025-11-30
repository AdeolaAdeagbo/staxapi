from django.contrib import admin
from .models import Category, Course, Lesson, Enrollment, Review, Certificate

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'created_at']
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name']

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'instructor_name', 'price', 'level', 'is_published', 'enrolled_count', 'rating', 'created_at']
    list_filter = ['category', 'level', 'is_published']
    search_fields = ['title', 'instructor_name']
    prepopulated_fields = {'slug': ('title',)}
    ordering = ['-created_at']

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ['title', 'course', 'order', 'duration', 'is_free_preview', 'created_at']
    list_filter = ['course', 'is_free_preview']
    search_fields = ['title', 'course__title']
    ordering = ['course', 'order']

@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ['user', 'course', 'progress_percentage', 'enrolled_at', 'completed_at', 'certificate_issued']
    list_filter = ['certificate_issued', 'course']
    search_fields = ['user__email', 'course__title']
    ordering = ['-enrolled_at']

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['user', 'course', 'rating', 'created_at']
    list_filter = ['rating', 'course']
    search_fields = ['user__email', 'course__title', 'comment']
    ordering = ['-created_at']

@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ['certificate_id', 'user', 'course', 'issued_at']
    search_fields = ['certificate_id', 'user__email', 'course__title']
    ordering = ['-issued_at']
