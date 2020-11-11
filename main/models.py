from django.db import models

class Solution(models.Model):
    title = models.CharField(max_length=200, help_text='Enter a title of solution')
    description = models.TextField(max_length=1000, help_text='Enter a description of solution',)

    def __str__(self):
        return self.title
