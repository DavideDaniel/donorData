from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^detail/(?P<pk>\d+)', views.detail, name='detail'),
    url(r'^new', views.new, name='new'),
    url(r'^api/donors', views.DonorAPIView.as_view(), name='donorapi'),
]
