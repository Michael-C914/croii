# Django
from django.urls import path, include
# DRF
from rest_framework.routers import DefaultRouter

# Views
from user.views.session_manager import BlacklistTokenUpdateView, MyTokenObtainPairView
from user.views.user_juridic_view import UserJuridicViewSet

router = DefaultRouter()
router.register(r'user_juridic', UserJuridicViewSet, basename='user_juridic')

urlpatterns = [
    path('signout/blacklist/', BlacklistTokenUpdateView.as_view(),
         name='blacklist'),
    path('api/token/', MyTokenObtainPairView.as_view(),
         name='token_obtain_pair'),  # Get Token - SignIn
    path('', include(router.urls))
]
