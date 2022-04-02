from django.db import models
from django.core.validators import MinValueValidator


# Create your models here.
class Questions(models.Model):
    question = models.TextField(max_length=500,
                                verbose_name="Question",
                                help_text="Input question",
                                null=False)

    answer = models.CharField(max_length=100,
                              verbose_name="Answer",
                              help_text="Input correct answer")

    image = models.ImageField(verbose_name="Image",
                              help_text="Image for question",
                              null=True,
                              blank=True,
                              default=None)

    DJANGO = "Django"
    DB = "Databases"

    THEMES = [
        (DJANGO, "Django"),
        (DB, "Databases"),
    ]

    theme = models.CharField(max_length=20,
                             verbose_name="Theme",
                             help_text="Input question theme",
                             default=DJANGO,
                             choices=THEMES)

    def __str__(self):
        return f"{self.question} ({self.answer})"


class Answer(models.Model):
    answer = models.CharField(max_length=100,
                              verbose_name="Answer",
                              help_text="Input answer",
                              null=False)

    question = models.ForeignKey(Questions,
                                 on_delete=models.CASCADE,
                                 null=True,
                                 related_name="answers",
                                 verbose_name="Question",
                                 help_text="Input question")

    def __str__(self):
        return f"{self.answer}"


class Result(models.Model):
    date = models.DateTimeField(verbose_name="Date",
                                help_text="Date of testing",
                                null=False,
                                auto_now_add=True)

    user = models.CharField(max_length=100,
                            verbose_name="User",
                            help_text="User",
                            null=False)

    total_questions = models.IntegerField(verbose_name="Total questions",
                                          help_text="Number of total questions",
                                          null=False,
                                          validators=[MinValueValidator(0.0)])

    correct_answers = models.IntegerField(verbose_name="Correct answers",
                                          help_text="Number of correct answers",
                                          null=False,
                                          validators=[MinValueValidator(0.0)])

    result = models.DecimalField(verbose_name="Result, %",
                                 help_text="Test result, %",
                                 null=False,
                                 max_digits=5,
                                 decimal_places=2)
