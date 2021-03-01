from django.contrib import admin
from django.urls import path, include
from racho.views import index
from racho.views import contact
from racho.views import top
from racho.views import about
from racho.views import ustav
from racho.views import contests
from django.conf import settings

from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name = "index"),
    path('contact/', contact, name = "contact"),
    path('top/', top, name = "top"),
    path('about/', about, name="about"),
    path('ustav/', ustav, name = "ustav"),
    path('contests/', contests, name = "contests"),
    path('feedback/', include('racho.urls')),
    path('news/', include('cores.urls')),
    path('topback/', include('game.urls')),
    path('i18n/', include('django.conf.urls.i18n')),

]

urlpatterns += i18n_patterns(
    path('pages/', include('django.contrib.flatpages.urls')),
    path('top/', top, name="top"),
    path('', index),
    path('contact/', contact, name = "contact"),
    path('about/', about, name="about"),
    path('ustav/', ustav, name = "ustav"),
    path('contests/', contests, name = "contests"),
)



if settings.DEBUG:
    if settings.MEDIA_ROOT:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
