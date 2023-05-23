from rest_framework import serializers
from authentication.models import User
from admission.models import Admission
from achievements.models import Achievement



class AdmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admission
        fields = ['status']


class AchievementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Achievement
        fields = ['id', 'user_id', 'level', 'title', 'years']



class UserSerializer(serializers.ModelSerializer):
    achievements = AchievementSerializer(many=True, read_only=True)
    status = AdmissionSerializer(read_only=True)

    class Meta:
        model = User
        fields = ['id', 'name', 'users_image', 'start_education', 'end_education',
                  'mentor', 'score', 'specialization', 'status', 'is_active',
                   'achievements']




    def create(self, validated_data):
        password=validated_data.pop('password',None)
        instance = self.Meta.model(**validated_data)
        instance.is_active=True


        if password is not None:
            instance.set_password(password)
        instance.save()

        return instance
