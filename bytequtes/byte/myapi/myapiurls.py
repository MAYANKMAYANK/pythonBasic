from django.conf.urls import url
from . import views
# from .views import add_data

#url code
from myapi.views import Curd
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r'api', Curd, basename='user')


urlpatterns=[
    url(r'^all_data',views.all_data,name='all_data'),
    url(r'^add_data',views.add_data,name='add_data'),
    url(r'^delete_data/(?P<uid>\d+)/$',views.delete_data,name='delete_data'),
    url(r'^upd_data/(?P<uid>\d+)/$',views.upd_data,name='upd_data')
]

urlpatterns += router.urls
