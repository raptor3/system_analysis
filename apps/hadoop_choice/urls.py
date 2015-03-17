from django.conf.urls import patterns, url

from hadoop_choice.views import *

urlpatterns = patterns('hadoopecosystem.views',
    url(r'^$', main_input_view,  name='hadoo_choice_main'),
    url(r'^results/', main_input_view,  name='hadoo_choice_main'),

    url(r'^storagepart_and_processingpart/', all_component,  name='storagepart_and_processingpart'),

    url(r'^create_distributed_filesystem/', create_distributed_filesystem, name='create_distributed_filesystem'),
    url(r'^create_distributed_programming/', create_distributed_programming, name='create_distributed_programming'),
    url(r'^create_machine_learning/', create_machine_learning, name='create_machine_learning'),
    url(r'^create_sql_on_hadoop/', create_sql_on_hadoop, name='create_sql_on_hadoop'),
    url(r'^delete_all_model/', delete_all_model, name='delete_all_model'),

)
