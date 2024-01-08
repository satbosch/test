# -*- encoding: utf-8 -*-
"""
Copyright (c) 2024 - XC/EVI
"""

from django.db      import models

###########################################################
# Object_Unit
###########################################################
class Object_Unit(models.Model):
    name                   = models.CharField(         db_column='Name',            max_length=30,     blank=True,                  unique=True )
    description            = models.CharField(         db_column='Description',     max_length=200,    blank=True,     null=True                )

    def __str__(self):
            return self.name
