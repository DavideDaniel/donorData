from rest_framework import serializers
from rest_framework.relations import StringRelatedField
from .models import Donor, PatronageCategory


# class PatronageCategorySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = PatronageCategory
#         fields = ['category']


class DonorSerializer(serializers.ModelSerializer):
    categories = StringRelatedField(many=True)

    class Meta:
        model = Donor
        fields = [
            'id',
            'donor_ident',
            'first_name',
            'last_name',
            'create_date',
            'update_date',
            'job_title',
            'employer_url',
            'employer_industry',
            'patronage',
            'categories',
        ]


