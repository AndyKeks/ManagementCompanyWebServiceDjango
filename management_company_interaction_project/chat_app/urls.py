from django.urls import path

from chat_app.views import ChatRequestView, SetWorkStatusView, SetCloseStatusView

urlpatterns = [
    path('<int:pk>/', ChatRequestView.as_view(), name='chat_request'),
    path('<int:pk>/set_work', SetWorkStatusView.as_view(), name='set_status_work'),
    path('<int:pk>/set_close', SetCloseStatusView.as_view(), name='set_status_close'),
]
