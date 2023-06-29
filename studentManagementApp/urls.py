from django.contrib import admin
from django.urls import path
from studentManagementApp.views import * 
from django.conf.urls.static import static

urlpatterns = [
    path('', LoginView.as_view(), name='login'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', logoutview, name='logout'),
    path('registration/',StaffHodRegisterView.as_view(),name="createstudent"),
    path('course/', CourseView.as_view(), name='newcourse'),
    path('course/<int:pk>', CourseView.as_view(), name='newcourse'),
    path('session/', SessionYearView.as_view(), name='newsession'),
    path('session/<int:pk>', SessionYearView.as_view(), name='editsession'),
    path('subject/', SubjectView.as_view(), name='addsubject'),
    path('subject/<int:pk>', SubjectView.as_view(), name='editsubject'),
    path('teacher/', TeachersView.as_view(), name='teacher'),
    path('teacher/<int:pk>', TeachersView.as_view(), name='editteacher'),
    path('student/', StudentView.as_view(), name='student'),
    path('student/<int:pk>', StudentView.as_view(), name='editstudent'),
    path('staffleave/', StaffLeaveView.as_view(), name='studentleave'),
    path('staffleave/<int:pk>', StaffLeaveView.as_view(), name='editstudentleave'),
    path('studentleave/', StudentLeaveView.as_view(), name='staffleave'),
    path('studentleave/<int:pk>', StudentLeaveView.as_view(), name='editstaffleave'),
    path('teachers/', TeachersDashBoard, name='teachers'),
    path('takeattendancestudent/', takeattendance, name='takeattendancestudent'),
    path('subattendance/', Subattendance.as_view(), name='subattendance'),
    path('takeattendance/', TakeAttendance.as_view(), name='takeattendance'),
    path('studentnotification/', StudentNotifications.as_view(), name='studentnotification'),

    path('manageteacher/', TeacherListView.as_view(), name='manageteacher'),
    path('managestudent/', StudentListView.as_view(), name='managestudent'),
    path('managecourse/', CourseListView.as_view(), name='managecourse'),
    path('managesubject/', SubjectListView.as_view(), name='managesubject'),
    path('managesession/', SessionListView.as_view(), name='managesession'),
    path('staffleaverequests/', StaffLeaveListView.as_view(), name='staffleaverequests'),
    path('studentsleaverequests/', StudentsLeaveRequestsListView.as_view(), name='studentsleaverequests'),
    
    path('staffapplyleave/', StaffApplyLeaveView.as_view(), name='staffapplyleave'), 
    path('studentapplyleave/', StudentApplyLeaveView.as_view(), name='studentapplyleave'),
    path('myattendance/', MyattendanceView.as_view(), name='myattendance'),
    path('viewattendance/', ViewAttendanceView.as_view(), name='viewattendance'),
    path('studentprofile/', StudentProfileView.as_view(), name='studentprofile'),
    path('staffprofile/', StaffProfileView.as_view(), name='staffprofile'),
    path('hodprofile/', HodProfileView.as_view(), name='hodprofile'),
    path('editprofile/', MyProfileView.as_view(), name='editprofile'),
    
    path('register/',Register.as_view(),name="register"),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

