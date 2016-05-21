from django.core.management.base import BaseCommand, CommandError
from donorData.models import Donor, PatronageCategory
import csv

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('filepath')

    def handle(self, *args, **options):

        with open(options['filepath'],'r') as tsvfile:
            reader = csv.DictReader(tsvfile, delimiter='\t')
            for line in reader:
                
                
                categories = line['Patronage Categories'].split(',')

                donor = Donor()
                donor.donor_ident = line['Donor ID'] 
                donor.first_name = line['First Name']
                donor.last_name = line['Last Name']
                donor.create_date = line['Timestamp']
                donor.job_title = line['Job Title']
                donor.employer_url = line['Employer URL']
                donor.employer_industry = line['Employer Industry']
                donor.patronage = line['Patronage (boards, etc.)']
                donor.save()

                print('cats',categories)

                if len (categories) != 0 and line['Patronage Categories'] != '':
                    print('here')
                    for cat in categories:
                        new = PatronageCategory()
                        new.donor = donor
                        new.category = cat
                        new.save()


                

                
