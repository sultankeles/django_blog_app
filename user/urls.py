from django.urls import path, include

from .views import RegisterView

from rest_framework.authtoken import views

urlpatterns = [
    path('auth/', include('dj_rest_auth.urls')),
    path('register/', RegisterView.as_view()),
    path('login/', views.obtain_auth_token),
]
