from django.db import models

class Solution(models.Model):
    title = models.CharField(max_length=200, help_text='Enter a title of solution')
    description = models.TextField(max_length=1000, help_text='Enter a description of solution')

    def __str__(self):
        return self.title

class Job(models.Model):
    title = models.CharField(max_length=200, help_text='Enter a title of job')
    short_description = models.TextField(max_length=1000, help_text='Enter a short description of job')
    description = models.TextField(max_length=2000, blank=True, null=True, help_text='Enter a full description of job')
    tag = models.CharField(max_length=200, help_text='Enter a tag of job', blank=True, null=True)
    responsibility_1 = models.CharField(max_length=300, blank=True, null=True, help_text='Enter a responsibility of vacancy')
    responsibility_2 = models.CharField(max_length=300, blank=True, null=True, help_text='Enter a responsibility of vacancy')
    responsibility_3 = models.CharField(max_length=300, blank=True, null=True, help_text='Enter a responsibility of vacancy')
    responsibility_4 = models.CharField(max_length=300, blank=True, null=True, help_text='Enter a responsibility of vacancy')
    responsibility_5 = models.CharField(max_length=300, blank=True, null=True, help_text='Enter a responsibility of vacancy')
    requirement_1 = models.CharField(max_length=300, blank=True, null=True, help_text='Enter a requirement of vacancy')
    requirement_2 = models.CharField(max_length=300, blank=True, null=True, help_text='Enter a requirement of vacancy')
    requirement_3 = models.CharField(max_length=300, blank=True, null=True, help_text='Enter a requirement of vacancy')
    requirement_4 = models.CharField(max_length=300, blank=True, null=True, help_text='Enter a requirement of vacancy')
    requirement_5 = models.CharField(max_length=300, blank=True, null=True, help_text='Enter a requirement of vacancy')
    requirement_6 = models.CharField(max_length=300, blank=True, null=True, help_text='Enter a requirement of vacancy')
    requirement_7 = models.CharField(max_length=300, blank=True, null=True, help_text='Enter a requirement of vacancy')
    requirement_8 = models.CharField(max_length=300, blank=True, null=True, help_text='Enter a requirement of vacancy')
    requirement_9 = models.CharField(max_length=300, blank=True, null=True, help_text='Enter a requirement of vacancy')
    nice_to_have_1 = models.CharField(max_length=300, blank=True, null=True, help_text='Enter a nice to have of vacancy')
    nice_to_have_2 = models.CharField(max_length=300, blank=True, null=True, help_text='Enter a nice to have of vacancy')


    def __str__(self):
        return self.title
