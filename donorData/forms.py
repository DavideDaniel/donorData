from .models import Donor, Patronage
from django.forms import ModelForm, modelformset_factory, inlineformset_factory


donorFields = [
    'first_name', 'last_name', 'job_title',
    'employer_url', 'employer_industry'
]

DonorFormSet = inlineformset_factory(Donor, Patronage, fields=['name'])

class DonorForm(ModelForm):
    class Meta:
        model = Donor
        fields = donorFields


PatronageFormSet = modelformset_factory(Patronage, fields=['name'], extra=3)
