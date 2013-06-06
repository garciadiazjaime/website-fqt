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
        url(r'^nosotros/(?P<category>[^/]+)$', 'app.front.views.nosotros', name='nosotros'),
    url(r'^programas$', 'app.front.views.programas', name='programas'),
        url(r'^programas/(?P<category>[^/]+)', 'app.front.views.programas', name='programas'),
        url(r'^inscripcion/(?P<form>[^/]+)$', 'app.front.views.inscripcion', name='inscripcion'),
    url(r'^ecotips$', 'app.front.views.ecotips', name='ecotips'),
        url(r'^ecotips/ecocapsulas/(?P<slug>[^/]+)$', 'app.front.views.ecotips', name='ecotips'),
        url(r'^ecotips/(?P<category>[^/]+)$', 'app.front.views.ecotips', name='ecotips'),


        url(r'^update_ecocapsulas$', 'app.youtube.views.update_ecocapsulas', name='test'),

    url(r'^transparencia$', 'app.front.views.transparencia', name='transparencia'),
        url(r'^transparencia/(?P<category>[^/]+)$', 'app.front.views.transparencia', name='transparencia'),
    url(r'^talleristas$', 'app.front.views.talleristas', name='talleristas'),
        url(r'^talleristas/(?P<category>[^/]+)$', 'app.front.views.talleristas', name='talleristas'),
    url(r'^campanas_donantes$', 'app.front.views.inversiones_sociales', name='campanas_donantes'),
        url(r'^campanas_donantes/(?P<category>[^/]+)$', 'app.front.views.inversiones_sociales', name='campanas_donantes'),
    url(r'^contacto$', 'app.front.views.contacto', name='contacto'),
        url(r'^contacto/(?P<category>[^/]+)$', 'app.front.views.contacto', name='contacto'),
    
    url(r'^test$', 'app.front.views.test', name='test'),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^tinymce/', include('tinymce.urls')),
)

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)