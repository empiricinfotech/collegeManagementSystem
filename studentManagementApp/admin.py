from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(User)
admin.site.register(SessionYear)
admin.site.register(Courses)
admin.site.register(Subjects)
admin.site.register(Teachers)
admin.site.register(HOD)
admin.site.register(StaffLeave)
admin.site.register(StudentLeave)

@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('id','student','subject','sessionYear','status','created_at','updated_at')
    
@admin.register(Students)
class StudentsAdmin(admin.ModelAdmin):
    list_display = ('user','course','sessionYear','created_at','updated_at')
    
@admin.register(AttendanceNotification)
class AttendanceNotificationAdmin(admin.ModelAdmin):
    list_display = ('attendance','created_at')