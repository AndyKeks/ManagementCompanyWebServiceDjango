from django.urls import path

from requests_app.views import CreateRequestView, ListRequestsView

urlpatterns = [
    path('new/', CreateRequestView.as_view(), name='create_request'),
    path('list/', ListRequestsView.as_view(), name='list_requests'),
]
