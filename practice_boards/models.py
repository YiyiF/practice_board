from django.db import models
from django.urls import reverse  # Used to generate URLs by reversing the URL patterns
import uuid


class Author(models.Model):
    """
    Model representing an author.
    """
    name = models.CharField(max_length=100, primary_key=True)
    department = models.CharField(max_length=100)
    date_of_signup = models.DateField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('author-detail', args=[str(self.name)])

    def calculate_personal_practices(self):
        return Practice.objects.filter(author=self).count()

    def generate_personal_practices(self):
        return Practice.objects.filter(author=self)

    def __str__(self):
        """
        String for representing the Model object.
        """
        return '%s' % self.name


class Question(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200, default='')

    def generate_done_practices(self):
        return Practice.objects.filter(question_id=self)

    def generate_undo_authors(self):
        done_authors = self.generate_done_practices().values('author')
        undo_authors = Author.objects.values('name').exclude(name__in=done_authors.all())
        return undo_authors



    def __str__(self):
        """
        String for representing the Model object.
        """
        return '%s' % self.title


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


class Practice(models.Model):
    """
    Model representing a programming file.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          help_text="Unique ID for this particular book across whole library")
    question = models.ForeignKey(Question, to_field='id', on_delete=models.CASCADE, blank=True, null=True)
    upload = models.FileField(upload_to='uploads/%Y/%m/%d/', null=True, default='')
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, to_field='name', on_delete=models.CASCADE, blank=True, null=True)
    date_of_first_submit = models.DateField(auto_now_add=True)
    date_of_latest_submit = models.DateField(auto_now_add=True)
    code_language = models.ForeignKey(CodeLanguage, on_delete=models.DO_NOTHING, null=True)
    code_lines = models.PositiveSmallIntegerField(blank=True, null=True)
    execute_result = models.CharField(max_length=20, blank=True, null=True)
    execute_time = models.TimeField(blank=True, null=True)

    def get_absolute_url(self):
        return reverse('practice-detail', args=[str(self.id)])


    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.title





