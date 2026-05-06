from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from apis.models import Student
from apis.serializers import StudentListSerializer, StudentDetailSerializer
from apis.filters import StudentFilterSet


class StudentViewSet(viewsets.ModelViewSet):
    """ViewSet สำหรับ Student - สนับสนุน CRUD ทั้งหมด"""
    queryset = Student.objects.select_related('classroom', 'classroom__school').all()
    permission_classes = [AllowAny]
    filterset_class = StudentFilterSet
    
    def get_serializer_class(self):
        if self.action == 'retrieve':
            return StudentDetailSerializer
        return StudentListSerializer
