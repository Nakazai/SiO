from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

from SiO.admin import views as forening_auth_views
from SiO.core import views as core_views

# TODO: Herifra blir metodene fra hver app dirigert via URL
urlpatterns = [
    url(r'^$', core_views.home, name='home'),
    url(r'', include('SiO.core.urls')),
    url(r'^login', auth_views.login, {'template_name': 'core/cover.html'},
        name='login'),
    url(r'^logout', auth_views.logout, {'next_page': '/'}, name='logout'),
    url(r'^signup/$', forening_auth_views.signup, name='signup'),
    url(r'^(?P<username>[^/]+)/$', core_views.profile, name='profile'),
    url(r'^i18n/', include('django.conf.urls.i18n', namespace='i18n')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
