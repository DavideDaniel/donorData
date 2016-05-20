from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.views import generic
from .forms import DonorForm
from .models import Donor


class IndexView(generic.ListView):
    model = Donor
    template_name = 'donorData/index.html'


def new(request):
    if request.method == 'POST':
        form = DonorForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/')
    else:
        form = DonorForm()
        return render(request, 'donorData/donorDetail.html', {'form': form})


def detail(request, pk):    
    if request.method == 'POST':
        try: 
            donorInstance = Donor.objects.get(pk=pk)
        except:
            return Http404('Donor does not exist')
        else:
            form = DonorForm(request.POST, instance=donorInstance)
            if form.is_valid():
                form.save()
            return HttpResponseRedirect('/')
    else:
        try: 
            donorInstance = Donor.objects.get(pk=pk)
        except:
            return Http404('Donor does not exist')
        else:
            form = DonorForm(instance=donorInstance)
            return render(request,'donorData/donorDetail.html',{'form': form})
        
