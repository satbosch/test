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
###########################################################
# Object_Unit_Download
###########################################################
class Object_Unit_Download(models.Model):
    component               = models.CharField(         db_column='Component',            max_length=200,     blank=True,                  unique=True )
    version                 = models.CharField(         db_column='Version',              max_length=200,     blank=True,                  null=True   )

    def __str__(self):
            return self.name

###########################################################
# Object_Unit_Create
###########################################################
class Object_Unit_Create(models.Model):
    # Black Duck Component fields
    name = models.CharField(db_column='Name', max_length=30, blank=True, null=False)
    version = models.CharField(db_column='Version', max_length=30, blank=True, null=True)
    homepage = models.CharField(db_column='Homepage', max_length=200, blank=True, null=True)  # Changed from URLField to CharField
    
    # MITRE/NVD Section fields
    mitre_name = models.CharField(db_column='MITRE_Name', max_length=30, blank=True, null=True)
    mitre_version = models.CharField(db_column='MITRE_Version', max_length=30, blank=True, null=True)
    vendor = models.CharField(db_column='Vendor', max_length=100, blank=True, null=True)
    cpe = models.CharField(db_column='CPE', max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name