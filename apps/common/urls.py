from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from apps.common.views import *
from apps.users.views import *

urlpatterns = [
    path('sign-up', SignupView.as_view()),
    path('verify/', VerifyView.as_view()),
    path('login/', SignInView.as_view()),
    path('needs_help', NeedHelpView.as_view()),
    path('create_petition', PetitionCreateView.as_view()),
    path('profile/<int:pk>', ProfileView.as_view()),
]