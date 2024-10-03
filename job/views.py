from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator
from .models import job
from .form import Applyform ,JobForm


# Create your views here.
def job_list(request):
    job_list=job.objects.all()
    paginator=Paginator(job_list,3)
    page_number=request.GET.get('page')
    page_obj= paginator.get_page(page_number)
    cotext={'jobs':page_obj}
    return render(request,"job/job_list.html",cotext)

def job_detail(request, slug):
    job_detail=job.objects.get(slug=slug)
    if request.method=='POST':
        form=Applyform(request.POST,request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.job=job_detail
            myform.save()
    else:
        form = Applyform()


    cotext={'job':job_detail,'form': form}
    return render(request,"job/job_details.html",cotext)

def jop_add(request):

    if request.method=='POST':
        form=JobForm(request.POST,request.FILES)
        if form.is_valid():
            myform=form.save(commit=False)
            myform.owner=request.user
            myform.save()
            return redirect(reverse('jobs:job_list'))
        
    else:
        form=JobForm()
    
    

    return render(request,"job/add_job.html",{'form':form})