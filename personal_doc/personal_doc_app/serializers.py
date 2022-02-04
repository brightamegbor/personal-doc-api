from dataclasses import field
from rest_framework import serializers
from personal_doc_app.models import Users

class UsersSerializers(serializers.ModelSerializer):

  class Meta:
    model = Users
    fields = ('id', 
              'username', 
              'password')