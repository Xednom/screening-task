from django.urls import include, path

from rest_framework.routers import DefaultRouter

from api.resources.principles import AgilePrincipleViewSet
from api.resources.values import AgileValueViewSet


router = DefaultRouter()

router.register("agile-values", AgileValueViewSet, basename="agile-list")
router.register("agile-principles", AgilePrincipleViewSet, basename="agile-principles")

urlpatterns = [path("", include(router.urls))]
