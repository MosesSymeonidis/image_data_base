from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import TemplateView

urlpatterns = patterns('',
       # (r'^$', include('uploader.urls')),
    url(r'^$/', RedirectView.as_view(url='home/')), # Just for ease of use.
    url(r'^home/$',TemplateView.as_view(template_name='home.html'),{'template':'home.html'}),

)+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
