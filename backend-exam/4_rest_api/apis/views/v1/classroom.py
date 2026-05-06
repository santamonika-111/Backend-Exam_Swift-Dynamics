from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from apis.models import Classroom
from apis.serializers import ClassroomListSerializer, ClassroomDetailSerializer
from apis.filters import ClassroomFilterSet


class ClassroomViewSet(viewsets.ModelViewSet):
    """ViewSet สำหรับ Classroom - สนับสนุน CRUD ทั้งหมด"""
    queryset = Classroom.objects.select_related('school').prefetch_related('teachers', 'students').all()
    permission_classes = [AllowAny]
    filterset_class = ClassroomFilterSet
    
    def get_serializer_class(self):
        if self.action == 'retrieve':
            return ClassroomDetailSerializer
        return ClassroomListSerializer
