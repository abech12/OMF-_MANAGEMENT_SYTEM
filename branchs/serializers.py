from rest_framework import serializers
from .models import OCSSC_branch_office

class BranchOfficeSerializer(serializers.ModelSerializer):
    class Meta:
        model = OCSSC_branch_office
        fields = '__all__'