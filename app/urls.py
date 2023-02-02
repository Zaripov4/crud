from django.urls import path, include
from .views import UserViewSet
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('', UserViewSet)


urlpatterns = [
    path('', include(router.urls)),
]

# CRUD

# Create   # POST
# Read     # GET
# Update   # PUT/PATCH
# Delete   # DELETE



