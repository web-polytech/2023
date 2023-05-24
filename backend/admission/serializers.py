from rest_framework import serializers
from admission.models import Admission


class AdmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admission
        ref_name = "Admission"
        fields = "__all__"
