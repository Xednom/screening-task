from rest_framework import serializers, viewsets
from rest_framework.permissions import IsAuthenticated

from api.models import AgileValue
from api.permissions import IsAdminUserOrReadOnly


class AgileValuesSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgileValue
        fields = "__all__"


class AgileValueViewSet(viewsets.ModelViewSet):
    queryset = AgileValue.objects.all()
    serializer_class = AgileValuesSerializer
    permission_classes = [IsAdminUserOrReadOnly]
