from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Pharmacien(models.Model):
	telephone = models.BigIntegerField()
	info_supp = models.TextField(verbose_name="Information supplementaire", null=True)

	user = models.OneToOneField(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.nom

class Pharmacie(models.Model):
	nom = models.CharField(max_length=100)
	photo = models.CharField(max_length=100, blank=True)
	longitude = models.FloatField()
	latitude = models.FloatField()
	telephone = models.BigIntegerField()
	heure_ouverture = models.TimeField(verbose_name="Heure d'ouverture ")#
	heure_fermeture = models.TimeField(verbose_name="Heure de fermeture")
	email = models.EmailField()
	info_supp = models.TextField(verbose_name="Information supplementaire")
	pharmacien = models.ForeignKey(Pharmacien, on_delete=models.CASCADE)
	valide = models.BooleanField(verbose_name="Activer", default=False)

	def __str__(self):
		return self.nom