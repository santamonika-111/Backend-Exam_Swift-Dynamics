from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from apis.models import School
from apis.serializers import SchoolListSerializer, SchoolDetailSerializer
from apis.filters import SchoolFilterSet


class SchoolViewSet(viewsets.ModelViewSet):
    """ViewSet สำหรับ School - สนับสนุน CRUD ทั้งหมด"""
    queryset = School.objects.all()
    permission_classes = [AllowAny]
    filterset_class = SchoolFilterSet
    
    def get_serializer_class(self):
        if self.action == 'retrieve':
            return SchoolDetailSerializer
        return SchoolListSerializer
