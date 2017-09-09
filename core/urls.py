from django.conf.urls import url
from .views import auth_user, add_pharmacie, list_pharmacie

urlpatterns = [
	url(r'^auth_user/', auth_user, name="authentification"),
	url(r'^add_pharmacie/', add_pharmacie, name="new_pharmacie"),
	url(r'^list_pharmacie/', list_pharmacie, name="list_pharmacie")
]