from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import OCSSC_branch_office
from .serializers import BranchOfficeSerializer


class BranchOfficeViewSet(viewsets.ModelViewSet):
    queryset = OCSSC_branch_office.objects.all()
    serializer_class = BranchOfficeSerializer
    permission_classes = [IsAuthenticated]