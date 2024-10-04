from django.urls import path,include
from . import views
from . import api

app_name='job'

urlpatterns = [
    path('',views.job_list,name='job_list'),
    path('add',views.jop_add,name='add_job'),
    path('<str:slug>',views.job_detail,name='job_details'),

    # api
    path('api/list',api.joblistapi,name='job_list_api'),
]