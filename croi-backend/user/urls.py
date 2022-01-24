from django.urls import path, re_path

from user.views import BlacklistTokenUpdateView, MyTokenObtainPairView


urlpatterns = [
    path('signout/blacklist/', BlacklistTokenUpdateView.as_view(),
         name='blacklist'),
    path('api/token/', MyTokenObtainPairView.as_view(),
         name='token_obtain_pair'),  # Get Token - SignIn
]
