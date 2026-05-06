from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from apis.models import Teacher
from apis.serializers import TeacherListSerializer, TeacherDetailSerializer
from apis.filters import TeacherFilterSet


class TeacherViewSet(viewsets.ModelViewSet):
    """ViewSet สำหรับ Teacher - สนับสนุน CRUD ทั้งหมด"""
    queryset = Teacher.objects.prefetch_related('classrooms').all()
    permission_classes = [AllowAny]
    filterset_class = TeacherFilterSet
    
    def get_serializer_class(self):
        if self.action == 'retrieve':
            return TeacherDetailSerializer
        return TeacherListSerializer
