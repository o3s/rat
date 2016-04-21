from django.conf.urls import url
from .views import (
    activ_list,
    activ_details,
    activ_add,
    activ_edit,
    activ_del,
    )


app_name = 'activ'
urlpatterns = [
    url(r'^$', activ_list, name='activ'),
    url(r'^add/$', activ_add, {}, name='activ_add'),
    url(r'^edit/(?P<activ_id>\d+)/$', activ_edit, {}, 'activ_edit'),
    url(r'^del/(?P<activ_id>\d+)/$', activ_del, {}, 'activ_del'),
    url(r'^(?P<activ_id>[0-9]+)$', activ_details, name='activ_details'),
    ]