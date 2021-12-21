from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from accounts_app.views import HomepageView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts_app.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('request/', include('requests_app.urls')),
    path('request/', include('chat_app.urls')),
    path('', HomepageView.as_view(), name='home'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
