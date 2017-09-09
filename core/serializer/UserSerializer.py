from rest_framework import Serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		field = 'id','username'