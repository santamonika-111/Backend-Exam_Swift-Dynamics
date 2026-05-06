from rest_framework import serializers
from .models import School, Classroom, Teacher, Student


class SchoolListSerializer(serializers.ModelSerializer):
    """Serializer สำหรับการแสดงรายชื่อโรงเรียน"""
    class Meta:
        model = School
        fields = ['id', 'name', 'abbreviation', 'address']


class SchoolDetailSerializer(serializers.ModelSerializer):
    """Serializer สำหรับการแสดงรายละเอียดโรงเรียน"""
    classroom_count = serializers.SerializerMethodField()
    teacher_count = serializers.SerializerMethodField()
    student_count = serializers.SerializerMethodField()
    
    def get_classroom_count(self, obj):
        return obj.classrooms.count()
    
    def get_teacher_count(self, obj):
        # ดึงครูจากทุกห้องเรียนของโรงเรียนนี้
        return Teacher.objects.filter(classrooms__school=obj).distinct().count()
    
    def get_student_count(self, obj):
        # ดึงนักเรียนจากทุกห้องเรียนของโรงเรียนนี้
        return Student.objects.filter(classroom__school=obj).count()
    
    class Meta:
        model = School
        fields = ['id', 'name', 'abbreviation', 'address', 'classroom_count', 'teacher_count', 'student_count']


class TeacherMinimalSerializer(serializers.ModelSerializer):
    """Serializer ขั้นต่ำของครูสำหรับการแสดงใน Classroom"""
    class Meta:
        model = Teacher
        fields = ['id', 'first_name', 'last_name', 'gender']


class StudentMinimalSerializer(serializers.ModelSerializer):
    """Serializer ขั้นต่ำของนักเรียนสำหรับการแสดงใน Classroom"""
    class Meta:
        model = Student
        fields = ['id', 'first_name', 'last_name', 'gender']


class ClassroomDetailSerializer(serializers.ModelSerializer):
    """Serializer สำหรับการแสดงรายละเอียดห้องเรียน"""
    teachers = TeacherMinimalSerializer(many=True, read_only=True)
    students = StudentMinimalSerializer(many=True, read_only=True)
    school_name = serializers.CharField(source='school.name', read_only=True)
    
    class Meta:
        model = Classroom
        fields = ['id', 'level', 'semester', 'school', 'school_name', 'teachers', 'students']


class ClassroomListSerializer(serializers.ModelSerializer):
    """Serializer สำหรับการแสดงรายชื่อห้องเรียน"""
    school_name = serializers.CharField(source='school.name', read_only=True)
    
    class Meta:
        model = Classroom
        fields = ['id', 'level', 'semester', 'school', 'school_name']


class TeacherListSerializer(serializers.ModelSerializer):
    """Serializer สำหรับการแสดงรายชื่อครู"""
    class Meta:
        model = Teacher
        fields = ['id', 'first_name', 'last_name', 'gender']


class TeacherDetailSerializer(serializers.ModelSerializer):
    """Serializer สำหรับการแสดงรายละเอียดครู"""
    classrooms = ClassroomListSerializer(many=True, read_only=True)
    
    class Meta:
        model = Teacher
        fields = ['id', 'first_name', 'last_name', 'gender', 'classrooms']


class ClassroomForTeacherSerializer(serializers.ModelSerializer):
    """Serializer สำหรับการแสดงห้องเรียนที่ครูสอน"""
    school_name = serializers.CharField(source='school.name', read_only=True)
    
    class Meta:
        model = Classroom
        fields = ['id', 'level', 'semester', 'school_name']


class StudentListSerializer(serializers.ModelSerializer):
    """Serializer สำหรับการแสดงรายชื่อนักเรียน"""
    class Meta:
        model = Student
        fields = ['id', 'first_name', 'last_name', 'gender']


class StudentDetailSerializer(serializers.ModelSerializer):
    """Serializer สำหรับการแสดงรายละเอียดนักเรียน"""
    classroom_info = serializers.SerializerMethodField()
    
    def get_classroom_info(self, obj):
        if obj.classroom:
            return {
                'id': obj.classroom.id,
                'level': obj.classroom.get_level_display(),
                'semester': obj.classroom.get_semester_display(),
                'school': obj.classroom.school.name
            }
        return None
    
    class Meta:
        model = Student
        fields = ['id', 'first_name', 'last_name', 'gender', 'classroom', 'classroom_info']
