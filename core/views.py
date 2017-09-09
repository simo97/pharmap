from cmath import phase

from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Pharmacie, Pharmacien
from django.core import serializers
# Create your views here.

"""
	Faudra les routes pour :
	* La liste des pharmacie
	* Ajouter une pharmacie
	* authentifier un user
	* inscrire un user
	* modifier un user
	* effacer une pharmacie
	* modifier une pharmacie
	* avoir les details d'une pharmacie
"""

def list_pharmacie(request):
	dict_pharmacie = {}
	dict_json_data = {}
	#for pharmacie in Pharmacie.objects.filter(valide=True):
	data = serializers.serialize("json", Pharmacie.objects.filter(valide=True))
	return HttpResponse(data, content_type='application/json')

def add_pharmacie(request):
	""" Pour ajouter une pharmacie """
	#i#f  request.user.is_authenticated :
	#logout(request)
	#return HttpResponse(request.user.pharmacien.nom)
	pharmacie = Pharmacie()
	pharmacie.nom = request.POST['nom']
	pharmacie.photo = request.POST['photo']
	pharmacie.longitude = request.POST['long']
	pharmacie.latitude = request.POST['latitude']
	pharmacie.telephone = request.POST['telephone']
	pharmacie.heure_ouverture = request.POST['heur_ouvert']
	pharmacie.heure_fermeture = request.POST['heur_fermeture']
	pharmacie.email = request.POST['email']
	pharmacie.info_supp = request.POST['info_supp']
	u = request.user
	pharmacie.pharmacien = u.pharmacien
	pharmacie.save()
	return HttpResponse("{'response':'ok'}")

def logout_user(request):
	logout(request)
	return HttpResponse("{'auth':'ok'}")

def auth_user(request):
	"""pour authentifier un utilisateur """
	username = request.POST['uname']
	password = request.POST['password']
	user = authenticate(username=username, password=password)
	if user is not None :
		login(request,user)# le login ici
		return HttpResponse("{'login':'ok'}") ## je retourne le json de l'onjet user
	else:
		return HttpResponse("{'auth':'no'}")

def registration(request):
	pharmacien = Pharmacien()
	user = User()

	user.username = request.POST['uname']
	user.password = request.POST['password']
	user.email = request.POST['mail']
	user.first_name = request.POST['nom']
	user.last_name = request.POST['prenom']

	pharmacien.telephone = request.POST['telephone']
	pharmacien.info_supp = request.POST['detail']
	pharmacien.user = user # je les connecte ici

	user.save()
	pharmacien.save()
	return HttpResponse("{'response':'ok'}")

def edit_user(request):
	""" Va permettre d'enregistrer les modifications faites sur un user"""
	pass

def delete_pharmacie(request, phar_id):
	"""Pour supprimer une pharmacie """
	pharmaci = Pharmacie.objects.filter(id=id)
	if pharmaci.delete() :
		return HttpResponse("{'response':'ok'}")
	else:
		return HttpResponse("{'response':'no'}")

def edit_pharmacie(request):
	""" Pour editer une pharmacie"""
	pharmacie = Pharmacie.objects.filter(id= request.POST['id'])
	pharmacie.nom = request.POST['nom']
	pharmacie.photo = request.POST['photo']
	pharmacie.longitude = request.POST['long']
	pharmacie.latitude = request.POST['latitude']
	pharmacie.telephone = request.POST['telephone']
	pharmacie.heure_ouverture = request.POST['heur_ouvert']
	pharmacie.heure_fermeture = request.POST['heur_fermeture']
	pharmacie.email = request.POST['email']
	pharmacie.info_supp = request.POST['info_supp']
	if pharmacie.save() :
		return HttpResponse("{'response':'ok'}")
	else:
		return HttpResponse("{'response':'no'}")

def detail_pharmacie(request):
	""" Les details d'une pharmacie"""
	pass
