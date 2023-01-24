from django.urls import include, path
from rest_framework import routers

from .views import UserListView


router = routers.DefaultRouter(trailing_slash=False)
# router = routers.DefaultRouter()

router.register('', viewset=UserListView)

urlpatterns = [
    path('/', UserListView.as_view()),
    path('/auth/', include('dj_rest_auth.urls')),
    # path('auth/register/', include('dj_rest_auth.registration.urls'))
]