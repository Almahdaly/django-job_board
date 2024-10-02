from django.shortcuts import render
from .models import job


# Create your views here.
def job_list(request):
    job_list=job.objects.all()
    cotext={'jobs':job_list}
    return render(request,"job/job_list.html",cotext)

def job_detail(request, id):
    job_detail=job.objects.get(id=id)
    cotext={'job':job_detail}
    return render(request,"job/job_details.html",cotext)