from django.contrib import admin
from .models import PastQuestion, Contribution, QuestionDownload

@admin.register(PastQuestion)
class PastQuestionAdmin(admin.ModelAdmin):
    list_display = ['course_code', 'course_name', 'university', 'year', 'semester', 'uploaded_by', 'status', 'views_count', 'downloads_count', 'created_at']
    list_filter = ['status', 'university', 'year', 'semester', 'category']
    search_fields = ['course_code', 'course_name', 'university', 'uploaded_by__email']
    ordering = ['-created_at']
    
    actions = ['approve_questions', 'reject_questions']
    
    def approve_questions(self, request, queryset):
        for question in queryset:
            if question.status == 'pending':
                question.status = 'approved'
                question.reviewed_by = request.user
                question.save()
                # Award points to contributor
                question.uploaded_by.add_points(question.points_earned)
        self.message_user(request, f'{queryset.count()} questions approved')
    approve_questions.short_description = 'Approve selected questions'
    
    def reject_questions(self, request, queryset):
        queryset.update(status='rejected', reviewed_by=request.user)
        self.message_user(request, f'{queryset.count()} questions rejected')
    reject_questions.short_description = 'Reject selected questions'

@admin.register(Contribution)
class ContributionAdmin(admin.ModelAdmin):
    list_display = ['user', 'past_question', 'points_awarded', 'status', 'created_at']
    list_filter = ['status']
    search_fields = ['user__email', 'past_question__course_code']
    ordering = ['-created_at']

@admin.register(QuestionDownload)
class QuestionDownloadAdmin(admin.ModelAdmin):
    list_display = ['user', 'past_question', 'downloaded_at']
    search_fields = ['user__email', 'past_question__course_code']
    ordering = ['-downloaded_at']
