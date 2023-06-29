from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import *
from django.dispatch import receiver

role = (("HOD","HOD"),("Student","Student"),("Teacher","Teacher"))

class User(AbstractUser):
    email =  models.EmailField(max_length=255, unique=True )
    role = models.CharField(max_length=20,choices=role)
    profile_img = models.ImageField(upload_to="profileImages",null=True,blank=True)
    username = None 
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    

class SessionYear(models.Model):
    startYear = models.DateField()  
    endYear = models.DateField()
    
    def __str__(self):
        return f"{self.startYear}"

    
class Courses(models.Model):
    courseName = models.CharField(max_length=254)
    sessionYear = models.ForeignKey(SessionYear, null=True,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)    
    updated_at = models.DateTimeField(auto_now=True) 
    
    def __str__(self):
        return self.courseName
        
class Teachers(models.Model):
    user = models.OneToOneField(User,related_name="teacheruser" ,on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.user.first_name

class Students(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    course = models.ForeignKey(Courses, on_delete=models.CASCADE,null=True, related_name='students')
    sessionYear = models.ForeignKey(SessionYear, null=True,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

class HOD(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.user.first_name
     
class Subjects(models.Model):
    subName = models.CharField(max_length=254)
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teachers, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.subName

STATUS_CHOICES = (
    ("Reject","Reject"),
    ("Approve","Approve"),
    ("Requested","Requested")
    )
  
class StaffLeave(models.Model):
    status = models.CharField(max_length=254,choices=STATUS_CHOICES,null=True)
    teacher = models.ForeignKey(Teachers,on_delete=models.CASCADE,null=True)
    leaveDate = models.DateField()
    reason = models.CharField(max_length=254)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
     
class StudentLeave(models.Model):
    status = models.CharField(max_length=254,choices=STATUS_CHOICES)
    student = models.ForeignKey(Students,on_delete=models.CASCADE, related_name='students')
    leaveDate = models.DateField()
    reason = models.CharField(max_length=254)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
class Attendance(models.Model):
    student = models.ForeignKey(Students,on_delete=models.SET_NULL,null=True)
    subject = models.ForeignKey(Subjects, on_delete=models.SET_NULL, null=True)
    sessionYear = models.ForeignKey(SessionYear, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
class AttendanceNotification(models.Model):
    attendance = models.ForeignKey(Attendance,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        if instance.role == "HOD":
            HOD.objects.create(user=instance)
        if instance.role == "Teacher":
            Teachers.objects.create(user=instance)
        if instance.role == "Student":
            Students.objects.create(user=instance)

@receiver(post_save, sender=Attendance)
def create_attendance_notification(sender, instance,created, **kwargs):
    if created:
        AttendanceNotification.objects.create(attendance = instance)

@receiver(pre_delete, sender=Students)
def delete_leave_applications(sender, instance, **kwargs):
    leave_apps = StudentLeave.objects.filter(student=instance)
    leave_apps.delete()