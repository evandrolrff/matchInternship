from rest_framework import serializers
from .models import *

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ['name', 'date', 'email', 'communication', 'proactivity', 'organized', 'planner', 'meticulous', 'responsible']

class ProfessorSerializer(PersonSerializer):
    class Meta:
        model = Professor
        fields = ['person', 'occupation', 'discipline', 'registration']

class StudentSerializer(PersonSerializer):
    class Meta:
        model = Student
        fields = ['person', 'field', 'registration', 'semester']

class PartnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partner
        fields = ['name', 'local']

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobOpportunity
        fields = ['number', 'description', 'workload', 'partner']

