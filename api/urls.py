from django.urls import include, path

from rest_framework.routers import DefaultRouter

from api.resources.principles import AgilePrincipleViewSet
from api.resources.values import AgileValueViewSet


router = DefaultRouter()

router.register("agile-values", AgileValueViewSet)
router.register("agile-principles", AgilePrincipleViewSet)

urlpatterns = [path("", include(router.urls))]
