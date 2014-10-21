"""
Definition of models.
"""

from django.db import models

# Create your models here.
def question (models.Model):
    qn_verbose = models.CharField(max_length=300)
    right_ans = models.ForeignKey('answers')


