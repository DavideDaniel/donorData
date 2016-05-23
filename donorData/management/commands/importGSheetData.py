from django.core.management.base import BaseCommand, CommandError
from donorData.models import Donor, PatronageCategory
from django.core.exceptions import ValidationError

import datetime
import csv


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('filepath')

    def handle(self, *args, **options):

        with open(options['filepath'], 'r') as tsvfile:
            reader = csv.DictReader(tsvfile, delimiter='\t')
            for line in reader:

                categories = line['Patronage Categories'].split(',')
                donorName = line['First Name'] + " " + line['Last Name']

                donor = Donor()
                donor.donor_ident = line['Donor ID']
                donor.name = donorName
                donor.job_title = line['Job Title']
                donor.employer_url = line['Employer URL']
                donor.employer_industry = line['Employer Industry']
                donor.patronage = line['Patronage (boards, etc.)']
                try:
                    donor.full_clean()
                except ValidationError as e:
                    print(donorName)
                    print(e)
                else:
                    donor.save()
                if line['Patronage Categories'] != '':
                    for cat in categories:
                        cat = cat.strip()
                        if cat in self.catMap.keys():
                            new = PatronageCategory(donor=donor, category=cat)
                            try:
                                new.full_clean()
                            except ValidationError as e:
                                print(cat)
                                print(e)
                            else:
                                new.save()
                        else:
                            print('Skipping category "{}" for donor {}'.format(cat, donorName))

    goodCatList = [
        'Science & Technology',
        'Education',
        'Arts & Culture',
        'Environment',
        'Social Justice',
        'Civic',
        'Health',
        'Democratic & Liberal',
        'Republican & Conservative',
        #'Child Welfare',
        #'Industry',
        'Business',
        'Animal Rights',
        'Independent Party',
    ]

    catMap = {
        'Science & Technology': 'Science & Technology',
        'Education': 'Education',
        'Arts & Culture': 'Arts & Culture',
        'Environment': 'Environment',
        'Social Justice': 'Social Justice',
        'Civic': 'Civic',
        'Health': 'Health',
        'Democratic & Liberal': 'Democratic & Liberal',
        'Republican & Conservative': 'Republican & Conservative',
        #'Child Welfare': 'Child Welfare',
        #'Industry': 'Industry',
        'Business': 'Business',
        'Animal Rights': 'Animal Rights',
        'Independent Party': 'Independent Party',

        'Libertarian': 'Republican & Conservative',
        'Energy': 'Business',
        'Sports': 'Business',
        'Taco Bell Heir': 'Business',
        'Lumber': 'Business',
        'Venture Capitalism': 'Business',
        'Animals': 'Animal Rights',
        'Local City Officials in charge of Willamette River Superfund cleanup': 'Business',
        'Independent Party of Oregon': 'Independent Party',
        'Big Sisters': 'Social Justice',
        'College Sports': 'Business',
        'Big Brothers': 'Social Justice',
        'Economics': 'Business',
        'Children': 'Social Justice',
        'Financial Services': 'Business',
        'Business': 'Business',
        'Attorney': 'Business',
        'Progressive Party': 'Democratic & Liberal',
        'Finance': 'Business',
        'Light Rail Construction': 'Business',
        'Big Sisters': 'Social Justice',
        'Entrepreneurship in Emerging Markets': 'Business',
        'Animal Advocady': 'Animal Rights',
        'Animal advocacy': 'Animal Rights',
        'Oregon Progressive Party': 'Democratic & Liberal',
        'Transportation': 'Business',
    }