from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.contrib.postgres.fields import ArrayField


class Formation(models.Model):

    class Sections(models.TextChoices):
        GENERAL_CONCEPTS = "GENERAL_CONCEPTS", "Concept Généraux"
        ANALYSIS = 'ANALYSIS', "Analyses"
        PRETREATMENT = 'PRETREATMENT', "Prétraitement"
        CHEMICAL_TREATMENT = 'CHEMICAL_TREATMENT', "Traitement Chimique"
        CONTROL = 'CONTROL', "Controle"
        WATER_TOWER = 'WATER_TOWER', 'Tours d\'eau'
        BOILER = 'BOILER', 'Chaudière'
        MICROBIOLOGY = 'MICROBIOLOGY', 'Microbiologie'
        CLOSED_NETWORK = 'CLOSED_NETWORK', 'Réseaux fermés'

    title = models.CharField(max_length=100)
    description = models.TextField()
    section = models.CharField('Section', max_length=255, choices=Sections.choices, default=Sections.ANALYSIS, null=True)
    date_posted = models.DateTimeField(default=timezone.now)
    video = models.FilePathField(path="/media/video_formations", recursive=True)


    def __str__(self):
        return self.title
