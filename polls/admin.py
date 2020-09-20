from django.contrib import admin

from .models import Choice, Question, Comment

class ChoiceInline(admin.TabularInline):
    model = Choice 
    extra = 3

class CommentAdmin(admin.ModelAdmin):
    model = Comment 
    fieldsets = [
        (None,              {'fields': ['comment_text']}),
        (None,              {'fields': ['name']}),
        #('Date information', {'fields': ['publish_date'], 'classes': ['collapse']}),
    ]
    list_display = ('comment_text', 'name')


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']


admin.site.register(Question, QuestionAdmin)
admin.site.register(Comment, CommentAdmin)