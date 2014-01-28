from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

urlpatterns = patterns('uploader.views',
    #url(r'^home/$',TemplateView.as_view(template_name='uploader/../templates/home.html'),{'template':'home.html'}),
    url(r'^upload/$', 'upload', name='upload'),
    url(r'^query/$','query',name='query'),
    url(r'^results/$', 'results', name='results'),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
