from django.db import models
from django.urls import reverse  # Used to generate URLs by reversing the URL patterns
import uuid


class Author(models.Model):
    """
    Model representing an author.
    """
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    date_of_signup = models.DateField(auto_now_add=True)
    practices = models.ForeignKey('Practice', on_delete=models.CASCADE, blank=True, null=True, related_name='+')

    def __str__(self):
        """
        String for representing the Model object.
        """
        return '%s' % self.name


class Question(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200, default='')
    practice = models.ForeignKey('Practice', on_delete=models.CASCADE, blank=True, null=True, related_name='+')


class Practice(models.Model):
    """
    Model representing a programming file.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          help_text="Unique ID for this particular book across whole library")
    question = models.ForeignKey('Question', on_delete=models.SET_NULL, null=True, related_name='+')
    upload = models.FileField(upload_to='uploads/%Y/%m/%d/', default='')
    title = models.CharField(max_length=200)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    date_of_first_submit = models.DateField(auto_now_add=True)
    date_of_latest_submit = models.DateField(auto_now_add=True)
    code_language = models.ForeignKey('CodeLanguage', on_delete=models.DO_NOTHING, null=True)
    code_lines = models.PositiveSmallIntegerField()
    execute_result = models.CharField(max_length=20)
    execute_time = models.TimeField()

    def get_absolute_url(self):
        return reverse('practice-detail', args=[str(self.id)])

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.title


class CodeLanguage(models.Model):
    """
    Model representing a book genre (e.g. Science Fiction, Non Fiction).
    """
    name = models.CharField(max_length=100, help_text="Enter a programming language (e.g. python, C etc.)")

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name


