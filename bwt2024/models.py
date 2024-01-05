from django.db import models


###########################################################
# Object_Unit
###########################################################
class Object_Unit(models.Model):
    name                   = models.CharField(         db_column='Name',            max_length=30,     blank=True,                  unique=True )
    description            = models.CharField(         db_column='Description',     max_length=200,    blank=True,     null=True                )

    def __str__(self):
            return self.name


###########################################################
# BOM_Dictionary
###########################################################
class BOM_Dictionary(models.Model):
    bom_component               = models.CharField(             db_column='BOMComponent',                      max_length=200,  null= True               )
    bom_component_version       = models.CharField(             db_column='BOMComponentVersion',               max_length=200,  null= True               )
    bom_homepage                = models.CharField(             db_column='BOMHomepage',                       max_length=200,  null= True               )
    component                   = models.CharField(             db_column='Component',                         max_length=200,  null= True               )
    version                     = models.CharField(             db_column='Version',                           max_length=200,  null= True               )
    vendor                      = models.CharField(             db_column='Vendor',                            max_length=200,  null= True               )
    cpe                         = models.CharField(             db_column='CPE',                               max_length=200,  null= True               )

    def __str__(self):
            return self.cpe