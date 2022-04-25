from django.urls import path
from .views import CustomUserViewSets
from rest_framework import routers
from django.conf.urls import include


#registering the Viewsets with the routers

router = routers.DefaultRouter()
router.register('', CustomUserViewSets)

urlpatterns = [
    path('', include(router.urls)),
    path(
        "verify-password",
        CustomUserViewSets.as_view({"post": "checkPassword"}),
    )

]