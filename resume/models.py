from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from . import fields


class Resume(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    picture = models.ImageField()
    birth_date = models.DateField()
    phone_number = PhoneNumberField()
    about = models.TextField(max_length=400, null=True, blank=True)
    LANGUAGES = (
        ('en', 'English'),
        ('fa', 'فارسی'),
    )
    resume_language = models.CharField(choices=LANGUAGES, max_length=30)

    def get_full_name(self):
        return '{first_name} {last_name}'.format(first_name=self.first_name, last_name=self.last_name)

    def __str__(self):
        return '{name}-{lang}'.format(name=self.get_full_name(), lang=self.resume_language)


class Skill(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    proficiency = fields.IntegerRangeField(min_value=0, max_value=100)
    description = models.TextField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.title


class Certificate(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    organization = models.CharField(max_length=50)
    issue_date = models.DateField()

    def __str__(self):
        return '{organization} - {title}'.format(organization=self.organization, title=self.title)


class Project(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    organization = models.CharField(max_length=50)
    description = models.TextField(max_length=300, blank=True, null=True)
    date_completed = models.DateField()
    demo_link = models.CharField(max_length=150)
    skills_used = models.ManyToManyField(Skill)

    def __str__(self):
        return self.title


class Language(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    reading_proficiency = fields.IntegerRangeField(min_value=0, max_value=100)
    writing_proficiency = fields.IntegerRangeField(min_value=0, max_value=100)
    speaking_proficiency = fields.IntegerRangeField(min_value=0, max_value=100)
    listening_proficiency = fields.IntegerRangeField(min_value=0, max_value=100)

    def __str__(self):
        return self.title


class SocialMedia(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
    linked_in = models.CharField(help_text='https://www.linkedin.com/in/[User_ID]',
                                 max_length=100, blank=True, null=True)
    telegram = models.CharField(help_text='https://t.me/[User_ID]',
                                max_length=100, blank=True, null=True)
    stack_overflow = models.CharField(help_text='https://stackoverflow.com/users/[User_ID]',
                                      max_length=100, blank=True, null=True)
    github = models.CharField(help_text='https://github.com/[User_ID]',
                              max_length=100, blank=True, null=True)

    def __str__(self):
        return self.resume.get_full_name()

