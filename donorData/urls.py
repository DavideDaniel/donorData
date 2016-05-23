from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^detail/(?P<pk>\d+)', views.detail, name='detail'),
    url(r'^new', views.new, name='new'),
    url(r'^api/donors', views.AllDonorsAPIView.as_view(), name='allDonorsAPI'),
    url(r'^api/donor/(?P<pk>\d+)', views.DonorByIdAPIView.as_view(), name='donorAPI'),
    url(r'^api/donor/(?P<name>\D+\s?\D*)/?$', views.DonorByNameAPIView.as_view(), name='donorAPI'),
]
