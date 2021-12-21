from django.urls import path

from accounts_app.views import RegisterView, LoginAccountView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginAccountView.as_view(), name='login'),
]
