from django.contrib import admin
from.models import Students,Course

class AdminStudents (admin.ModelAdmin):
    list_display = ['sname','email','loc']


class AdminCourse(admin.ModelAdmin):
    list_display = ['cname', 'fee', 'iname']


admin.site.register(Students,AdminStudents)
admin.site.register(Course,AdminCourse)
