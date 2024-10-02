from django.shortcuts import render
from django.core.paginator import Paginator
from .models import job


# Create your views here.
def job_list(request):
    job_list=job.objects.all()
    paginator=Paginator(job_list,1)
    page_number=request.GET.get('page')
    page_obj= paginator.get_page(page_number)
    cotext={'jobs':page_obj}
    return render(request,"job/job_list.html",cotext)

def job_detail(request, slug):
    job_detail=job.objects.get(slug=slug)
    cotext={'job':job_detail}
    return render(request,"job/job_details.html",cotext)