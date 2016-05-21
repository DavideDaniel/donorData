from .models import Donor, PatronageCategory
from django.forms import ModelForm, modelformset_factory, inlineformset_factory


donorFields = [
    'first_name', 'last_name', 'job_title',
    'employer_url', 'employer_industry'
]

DonorFormSet = inlineformset_factory(Donor, PatronageCategory, fields=['category'])

class DonorForm(ModelForm):
    class Meta:
        model = Donor
        fields = donorFields


PatronageCategoryFormSet = modelformset_factory(PatronageCategory, fields=['category'], extra=3)
