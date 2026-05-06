from django.db import models


class School(models.Model):
    """โรงเรียน"""
    name = models.CharField(max_length=255)
    abbreviation = models.CharField(max_length=50)
    address = models.TextField()
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']


class Classroom(models.Model):
    """ห้องเรียน"""
    LEVEL_CHOICES = [
        (1, 'ชั้น 1'),
        (2, 'ชั้น 2'),
        (3, 'ชั้น 3'),
        (4, 'ชั้น 4'),
        (5, 'ชั้น 5'),
        (6, 'ชั้น 6'),
    ]
    SEMESTER_CHOICES = [
        (1, 'ภาคเรียนที่ 1'),
        (2, 'ภาคเรียนที่ 2'),
    ]
    
    level = models.IntegerField(choices=LEVEL_CHOICES)
    semester = models.IntegerField(choices=SEMESTER_CHOICES)
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='classrooms')
    
    def __str__(self):
        return f'{self.school.abbreviation} ชั้น {self.level} ภาค {self.semester}'
    
    class Meta:
        ordering = ['school', 'level', 'semester']
        unique_together = ['school', 'level', 'semester']


class Teacher(models.Model):
    """ครู"""
    GENDER_CHOICES = [
        ('M', 'ชาย'),
        ('F', 'หญิง'),
    ]
    
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    classrooms = models.ManyToManyField(Classroom, related_name='teachers', blank=True)
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
    class Meta:
        ordering = ['first_name', 'last_name']


class Student(models.Model):
    """นักเรียน"""
    GENDER_CHOICES = [
        ('M', 'ชาย'),
        ('F', 'หญิง'),
    ]
    
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE, related_name='students')
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
    class Meta:
        ordering = ['first_name', 'last_name']
