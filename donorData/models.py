from django.db import models

# Create your models here.


class Donor(models.Model):
    donor_ident = models.CharField(max_length=10)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255, blank=True)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    job_title = models.CharField(max_length=255, blank=True)
    employer_url = models.CharField(max_length=255, blank=True)
    employer_industry = models.CharField(max_length=255, blank=True)
    patronage = models.TextField(blank=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class PatronageCategory(models.Model):
    donor = models.ForeignKey(Donor, related_name='categories')
    category = models.CharField(max_length=255)

    def __str__(self):
        return self.category

    class Meta:
        verbose_name_plural = 'Patronage Categories'
