from django.conf import settings
from collegeManagementSystem import settings
from django.shortcuts import redirect ,render
from django.http import HttpResponseForbidden

# class LoginRequiredMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response

#     def __call__(self, request):
#         response = self.get_response(request)
#         if not request.user.is_authenticated and request.path not in settings.LOGIN_EXEMPT_URLS:
#             return redirect(settings.LOGIN_URL)
#         return response

# class TeacherRequiredMiddleware:
#     def __init__(self, get_response):
#         self.teacher_urls = ['/teacher/', '/teacher/<int:pk>', '/staffleave/<int:pk>','/subattendance/','/takeattendance/','/staffapplyleave/',   
#                              '/staffprofile/','/takeattendancestudent/','/','/logout/','/login/']
#         self.students_urls = ['/studentprofile/','/viewattendance/','/studentapplyleave/','/logout/','/','/login/']
#         self.hod_urls = ['/hodprofile/','/manageteacher/','/managestudent/','/managecourse/','/managesubject/','/managesession/','/staffleaverequests/','/logout/','/','/login/']
#         self.get_response = get_response


#     def __call__(self, request):
#         print("-*-------",request.path)
#         if request.user.is_authenticated and request.user.role == 'Teacher':
#             print("main if")
#             if request.user.role == 'Teacher' and request.path not in self.teacher_urls:
#                 print("inner if")
#                 return render(request,'login.html')
#             else:
#                 print("inner else")
#                 response = self.get_response(request)
#                 return response
#         elif request.user.is_authenticated and request.user.role == 'Student':
#             print("s main if")
#             if request.user.role == 'Student' and request.path not in self.students_urls:
#                 print("s inner if")
#                 return render(request,'login.html')
#             else:
#                 print("s inner else")   
#                 response = self.get_response(request)
#                 return response
#         elif request.user.is_authenticated and request.user.role == 'HOD':
#             print("main if",request.user.role == 'HOD' and request.path not in self.hod_urls)
#             if request.user.role == 'HOD' and request.path not in self.hod_urls:
#                 print("h inner if")
#                 return render(request,'login.html')
#             else:
#                 print("h inner else",request.user.role)
#                 response = self.get_response(request)
#                 return response
#         else:
#             response = self.get_response(request)
#             return response

