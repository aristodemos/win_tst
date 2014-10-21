"""
Definition of models.
"""

from django.db import models

# Create your models here.
class question (models.Model):
    qn_verb     = models.CharField(max_length=300)
    right_ans   = models.ForeignKey('answer')

class answer (models.Model):
    ans_verb    = models.CharField(max_length=300)
    qn          = models.ForeignKey(question)
