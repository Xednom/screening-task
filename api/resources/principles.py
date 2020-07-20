from rest_framework import serializers, viewsets
from rest_framework.permissions import IsAuthenticated

from api.models import AgilePrinciple
from api.permissions import IsAdminUserOrReadOnly


class AgilePrincipleSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgilePrinciple
        fields = "__all__"


class AgilePrincipleViewSet(viewsets.ModelViewSet):
    queryset = AgilePrinciple.objects.all()
    serializer_class = AgilePrincipleSerializer
    permission_classes = [IsAdminUserOrReadOnly]
