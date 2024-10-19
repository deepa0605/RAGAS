from django.contrib import admin
from .models import Raga, Song, Varnam, Comparisons, DoItYourself

@admin.register(Raga)
class RagaAdmin(admin.ModelAdmin):
    list_display = ('name',)
    filter_horizontal = ('related_songs',) 

@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ('name',)
    filter_horizontal = ('related_ragas', 'related_songs') 

@admin.register(Varnam)
class VarnamAdmin(admin.ModelAdmin):
    list_display = ('name',)
    filter_horizontal = ('related_ragas', 'related_songs')

@admin.register(Comparisons)
class ComparisonsAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(DoItYourself)
class DiyAdmin(admin.ModelAdmin):
    list_display = ('name',)