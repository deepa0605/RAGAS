from django.db import models

class Raga(models.Model):

    name = models.CharField(max_length=100)
    week = models.IntegerField()
    date = models.DateField()
    arohanam = models.CharField(max_length=200, null=True, blank=True)
    avrohanam = models.CharField(max_length=200, null=True, blank=True)
    janyam = models.CharField(max_length=100, blank=True, null=True)
    arohanam_avrohanam = models.FileField(upload_to='audio/', null=True, blank=True)
    signature = models.FileField(upload_to='audio/', null=True, blank=True)
    carnatic = models.FileField(upload_to='audio/', null=True, blank=True)
    cine = models.FileField(upload_to='audio/', null=True, blank=True)

    
    
    def __str__(self):
        
        return self.name