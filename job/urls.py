from django.urls import path,include
from . import views
from . import api

app_name='job'

urlpatterns = [
    path('',views.job_list,name='job_list'),
    path('add',views.jop_add,name='add_job'),
    path('<str:slug>',views.job_detail,name='job_details'),

    # api
    path('api/jobs',api.joblistapi,name='job_list_api'),
    path('api/jobs/<int:id>',api.job_detail_api,name='job_detail_api'),

    #CBV
    path('api/v2/jobs',api.JobListApi.as_view(),name='Job_List_Api'),
    path('api/v2/jobs/<int:id>',api.JobDetail.as_view(),name='Job_Detail'),

]