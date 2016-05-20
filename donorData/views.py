from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.views import generic
from .forms import DonorForm, DonorFormSet, PatronageFormSet
from .models import Donor


class IndexView(generic.ListView):
    model = Donor
    template_name = 'donorData/index.html'


def new(request):

    #LineItemFormSet = inlineformset_factory(Invoice, LineItem, form=LineItemForm, extra=5)
    if request.method == 'POST':
        # invoice_form = InvoiceForm(request.POST, prefix='invoice')
        # lineitem_formset = LineItemFormSet(request.POST, request.FILES, prefix='line')
        # if invoice_form.is_valid() and lineitem_formset.is_valid():
        #     invoice = invoice_form.save()
        #     # I recreate my lineitem_formset bound to the new invoice instance
        #     lineitem_formset = LineItemFormSet(request.POST, request.FILES, prefix='line', instance=invoice)
        #     # I have to validate (again - so I'm confident) to access clean data
        #     lineitem_formset.is_valid()
        #     lineitem_formset.save()
        #     if 'submit_more' in request.POST:
        #         return HttpResponseRedirect(reverse('invoices:add_invoice'))
        #     else:
        #         return HttpResponseRedirect(reverse('invoices:get_invoices'))
        # else:
        #     return render(request, 'invoices/invoice_add.html', {
        #         'message'           : "Check your form",
        #         'invoice_form'      : invoice_form,
        #         'lineitem_formset'  : lineitem_formset,
        #     })
        pass
    else:
        donor_form = DonorForm(prefix='donor')
        patronage_formset = PatronageFormSet(prefix='patronage')
        print('donorForm')
        print(donor_form)
        print('patronage')
        print(patronage_formset)
        return render(request, 'donorData/donorDetail.html', {
            'donor_form': donor_form,
            'patronage_formset': patronage_formset,
        })

def detail(request, pk):    
    if request.method == 'POST':
        try: 
            donorInstance = Donor.objects.get(pk=pk)
        except:
            return Http404('Donor does not exist')
        else:
            form = DonorFormSet(request.POST, instance=donorInstance)
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
        
