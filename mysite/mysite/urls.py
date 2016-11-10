
from django.conf.urls import url,include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

app_name= 'events'

urlpatterns = [
    url(r'^events/',include('events.urls')),
    url(r'^admin/', admin.site.urls),
	url(r'^accounts/', include('allauth.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
