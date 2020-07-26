from rest_framework import serializers, viewsets
from rest_framework.permissions import IsAuthenticated

from api.models import AgilePrinciple
from api.permissions import IsAdminUserOrReadOnly


class AgilePrincipleSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgilePrinciple
        fields = "__all__"
        read_only_fields = ["created_by", "updated_by"]


class AgilePrincipleViewSet(viewsets.ModelViewSet):
    queryset = AgilePrinciple.objects.all()
    serializer_class = AgilePrincipleSerializer
    permission_classes = [IsAdminUserOrReadOnly]

    def perform_create(self, serializer):
        current_user = self.request.user.username
        return serializer.save(created_by=current_user)

    def perform_update(self, serializer):
        current_user = self.request.user.username
        return serializer.save(updated_by=current_user)
