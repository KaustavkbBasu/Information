from django.conf.urls import url
from new import views

urlpatterns = [
    url(r'^$',views.InfoListView.as_view(),name='info_list'),
    url(r'^edit/$', views.CreateInfoView.as_view(), name='edit'),
    # url(r'^user/(?P<pk>\d+)$',views.InfoDetailView.as_view(), name='info_detail'),
    url(r'^user/(?P<pk>\d+)/remove/$', views.InfoDeleteView.as_view(), name='user_remove'),
    ]
