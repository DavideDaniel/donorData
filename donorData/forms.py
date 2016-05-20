from .models import Donor
from django.forms import ModelForm


class DonorForm(ModelForm):
    class Meta:
        model = Donor
        fields = [
            'first_name', 'last_name', 'job_title',
            'employer_url', 'employer_industry'
        ]
