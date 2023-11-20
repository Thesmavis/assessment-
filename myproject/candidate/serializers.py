from rest_framework import serializers
from . models import *

class candidate_ser(serializers.ModelSerializer) :
    class Meta :
        model = Candidatedirectory
        fields='__all__'
