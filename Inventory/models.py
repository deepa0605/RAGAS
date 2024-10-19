from django.db import models

class Raga(models.Model):
    
    raga_id = models.CharField(max_length=50, primary_key=True, blank=True)
    name = models.CharField(max_length=100)
    key = models.CharField(max_length=100, blank=True, null=True)
    updated_week = models.IntegerField(null=True, blank=True)
    updated_date = models.DateField(null=True, blank=True)
    posted_week = models.IntegerField(null=True)
    posted_date = models.DateField(null=True)
    melaraga_text = models.CharField(max_length=100, blank=True, null=True)
    melaraga_key = models.CharField(max_length=100, blank=True, null=True)
    aliases = models.CharField(max_length=200, blank=True, null=True)
    scale_aro = models.CharField(max_length=200, null=True, blank=True)
    scale_avro = models.CharField(max_length=200, null=True, blank=True)
    aro_clip_file = models.FileField(upload_to='static/carnatic_music', blank=True, null=True)
    aro_clip_name = models.CharField(max_length=200, blank=True, null=True)
    sig_clip_file = models.FileField(upload_to='static/carnatic_music', blank=True, null=True)
    sig_clip_name = models.CharField(max_length=200, blank=True, null=True)
    car_clip_file = models.FileField(upload_to='static/carnatic_music', blank=True, null=True)
    car_clip_name = models.CharField(max_length=200, blank=True, null=True)
    cin_clip_file = models.FileField(upload_to='static/carnatic_music', blank=True, null=True)
    cin_clip_name = models.CharField(max_length=200, blank=True, null=True)
    related_songs = models.ManyToManyField('Song', related_name='ragas', blank=True)

    def __str__(self):
        return self.name


class Song(models.Model):
    song_id = models.CharField(max_length=50, primary_key=True, blank=True)
    name = models.CharField(max_length=100)
    posted_week = models.IntegerField(null=True)
    posted_date = models.DateField(null=True)
    tala = models.CharField(max_length=200, null=True, blank=True)
    composer = models.CharField(max_length=200, null=True, blank=True)
    related_ragas = models.ManyToManyField('Raga', related_name='songs', blank=True)
    related_songs = models.ManyToManyField('self', symmetrical=True, blank=True)
    song_clip_file = models.FileField(upload_to='static/carnatic_music', blank=True, null=True)
    

    def __str__(self):
        return self.name
    

class Varnam(models.Model):
    varnam_id = models.CharField(max_length=50, primary_key=True, blank=True)
    name = models.CharField(max_length=100)
    posted_week = models.IntegerField(null=True)
    posted_date = models.DateField(null=True)
    updated_week = models.IntegerField(null=True)
    updated_date = models.DateField(null=True)
    tala = models.CharField(max_length=200, null=True, blank=True)
    composer = models.CharField(max_length=200, null=True, blank=True)
    related_ragas = models.ManyToManyField('Raga', related_name='varnams', blank=True)
    related_songs = models.ManyToManyField('Song', related_name='varnams', blank=True)
    varna_clip_file = models.FileField(upload_to='static/carnatic_music', blank=True, null=True)

    def __str__(self):
        return self.name
    

class Comparisons(models.Model):
    comparison_id = models.CharField(max_length=50, primary_key=True, blank=True)
    name = models.CharField(max_length=100)
    posted_week = models.IntegerField(null=True)
    posted_date = models.DateField(null=True)
    updated_week = models.IntegerField(null=True)
    updated_date = models.DateField(null=True)

    class Meta:
        verbose_name = "Comparisons"
        verbose_name_plural = "Comparisons"    

    def __str__(self):
        return self.name    
    
class DoItYourself(models.Model):
    diy_id = models.CharField(max_length=50, primary_key=True, blank=True)
    name = models.CharField(max_length=100)
    posted_week = models.IntegerField(null=True)
    posted_date = models.DateField(null=True)
    question1_answer = models.CharField(max_length=200, null=True, blank=True)
    question2_answer = models.CharField(max_length=200, null=True, blank=True)
    question3_answer = models.CharField(max_length=200, null=True, blank=True)  

    class Meta:
        verbose_name = "Do it yourself"
        verbose_name_plural = "Do it yourself"

    def __str__(self):
        return self.name  