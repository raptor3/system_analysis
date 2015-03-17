from django.conf.urls import patterns, url
from apps.hadoopecosystem.views import HadoopEcosystemView

urlpatterns = patterns('hadoopecosystem.views',
    url(r'^&', HadoopEcosystemView.as_view(), name='hadoopecosystemtable'),
)
