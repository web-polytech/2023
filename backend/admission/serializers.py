from rest_framework import serializers
from admission.models import Admission


class AdmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model= Admission
        fields ='__all__'
