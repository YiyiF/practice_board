from django.contrib import admin
from .models import Author, Practice, CodeLanguage, Question


# admin.site.register(Author)
# Define the admin class


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'department')


admin.site.register(Author, AuthorAdmin)


class PracticeAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date_of_latest_submit')
    list_filter = ('author', 'title')


admin.site.register(Practice, PracticeAdmin)


@admin.register(CodeLanguage)
class CodeLanguageAdmin(admin.ModelAdmin):
    list_display = ('name',)


# @admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')


admin.site.register(Question, QuestionAdmin)

