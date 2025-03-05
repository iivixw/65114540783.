from django.db import models

class Course(models.Model):
    course_code = models.CharField(max_length=100, unique=True)  # รหัสวิชา
    course_name = models.CharField(max_length=255)  # ชื่อวิชา

    def __str__(self):
        return f"{self.course_code} - {self.course_name}"