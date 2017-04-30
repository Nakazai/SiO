from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.contrib import admin

from SiO.CoAdmin import views as admin_auth_views
from SiO.member import views as member_views
from SiO.core import views as core_views
from SiO.calapp import views as events_views
from SiO.chart import views as chart_views

# from dedal.site import site as dedal_site

# TODO: Herifra blir metodene fra hver app dirigert via URL
# TODO: URL: rekkefølgen på SiO må være øverst slik at de vises i nettleser
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', core_views.home, name='home'),
    url(r'', include('SiO.core.urls')),
    url(r'', include('SiO.member.urls')),
    url(r'', include('SiO.CoAdmin.urls')),
    url(r'', include('SiO.calapp.urls')),
    url(r'', include('SiO.chart.urls')),
    url(r'^login', auth_views.login, {'template_name': 'core/cover.html'},
        name='login'),
    url(r'^logout', auth_views.logout, {'next_page': '/'}, name='logout'),
    # url(r'^signup/$', admin_auth_views.signup, name='signup'),
    url(r'session_security/', include('session_security.urls')),
    # url(r'^membersignup/$', member_views.membersignup, name='membersignup'),
    url(r'^(?P<username>[^/]+)/$', core_views.profile, name='profile'),
    # url(r'', include('SiO.calapp.urls')),
    url(r'^i18n/', include('django.conf.urls.i18n', namespace='i18n')),
    # url(r'^', include(dedal_site.urls)),
    # url(r'^calapp/$', events_views.calapp, name='calapp'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

admin.site.site_header = 'SiO administration'

