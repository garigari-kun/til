from rest_framework import serializers

from .models import JobList

class JobListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = JobList
        fields = ('id', 'jobtitle', 'jobdescription', 'postdate')
