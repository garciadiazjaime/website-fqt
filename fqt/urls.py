from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',    
    url(r'^$', include('app.front.urls')),
    url(r'^$', 'app.front.views.home', name='inicio'),
    url(r'^inicio$', 'app.front.views.home', name='inicio'),
    url(r'^nosotros$', 'app.front.views.nosotros', name='nosotros'),
    url(r'^programas$', 'app.front.views.programas', name='programas'),
        url(r'^programas/(?P<category>[^/]+)/$', 'app.front.views.programas', name='programas'),
    url(r'^ecotips$', 'app.front.views.ecotips', name='ecotips'),
    url(r'^transparencia$', 'app.front.views.transparencia', name='transparencia'),
    url(r'^talleristas$', 'app.front.views.talleristas', name='talleristas'),
    url(r'^inversiones_sociales$', 'app.front.views.inversiones_sociales', name='inversiones_sociales'),
    url(r'^contacto$', 'app.front.views.contacto', name='contacto'),
    
    url(r'^admin/', include(admin.site.urls)),
    url(r'^tinymce/', include('tinymce.urls')),
)

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)