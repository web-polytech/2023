from rest_framework.viewsets import ModelViewSet
from admission.models import Admission
from admission.serializers import AdmissionSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action


class AdmissionViewset(ModelViewSet):
    queryset = Admission.objects.all()
    serializer_class = AdmissionSerializer

    @action(methods=['POST'],
            detail=False,
            permission_classes=[IsAuthenticated],
            url_path="new_post")
    def create_post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'message': 'Post created successfully'})
