from django.contrib import admin
from .models import CurrentCourse,CourseStudentMap,CourseFacultyMap

# Register your models here.
admin.site.register(CurrentCourse)
admin.site.register(CourseStudentMap)
admin.site.register(CourseFacultyMap)