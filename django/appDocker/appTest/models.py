from django.db import models
import django
# Create your models here.
class Test (models.Model):
    location = django.contrib.gis.db.models.PointField(null=True,blank=True)
    name =  models.CharField(max_length=255)
    
    def __self__(self):
        return self.location