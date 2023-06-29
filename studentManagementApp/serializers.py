from rest_framework import serializers
from .models import *
from django.contrib.auth import authenticate

class UserRegistrationSerializer(serializers.Serializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)

    def validate(self, data):
        password = data.get('password')
        confirm_password = data.get('confirm_password')

        if password and password != confirm_password:
            raise serializers.ValidationError("Passwords do not match.")

        return data

    def create(self, validated_data):
        validated_data.pop('confirm_password')
        user = User.objects.create_user(**validated_data)
        return user

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)
    
    class Meta:
        model = User
        fields = ['first_name','last_name','email','password','confirm_password']
    def create(self, validated_data):
        password = validated_data.pop('password')
        confirm_password = validated_data.pop('confirm_password')
        if password != confirm_password:
            raise serializers.ValidationError("Passwords do not match")
        
        user = User.objects.create(first_name=validated_data['first_name'],last_name=validated_data['last_name'],email=validated_data['email'],role='HOD',is_staff=True,is_superuser = True)

        user.set_password(password)
        user.save()
        return user
        
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, attrs):
        user = authenticate(
            username=attrs['username'], password=attrs['password']
        )
        if not user:
            raise serializers.ValidationError('Invalid username or password')

        attrs['user'] = user
        return attrs
    
class SessionSerializer(serializers.ModelSerializer):
    startYear = serializers.DateField(format="%Y-%m-%d")
    endYear = serializers.DateField(format="%Y-%m-%d")
    
    class Meta:
        model = SessionYear
        fields = ['id','startYear','endYear']
    
class CourseSerializer(serializers.ModelSerializer):
    class Meta:
            model = Courses
            fields = ['id','courseName','sessionYear']

class NewCourseSerializer(serializers.ModelSerializer):
    sessionYear = SessionSerializer()
    class Meta:
        model = Courses
        fields = ['id','courseName','sessionYear']
    
    
    def update(self, instance, validated_data):
        session_year_data = validated_data.pop('sessionYear', None)
        if session_year_data is not None:
            session_year_serializer = SessionSerializer(instance.sessionYear.id, data=session_year_data)
        session = SessionYear.objects.get(pk=id)
        instance.courseName = validated_data.get('courseName', instance.courseName)
        instance.sessionYear = session
        instance.save()

        return instance

class TeacherSerializer(serializers.ModelSerializer):    
    class Meta:
        model = User
        fields = ['first_name','last_name','email']     
        
class AddSubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subjects
        fields = '__all__'      

class StudentUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name','last_name','email','password']
        
    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User.objects.create(**validated_data)
        user.role = "Student"
        user.set_password(password)
        user.save()
        return user
      
class StudentSerializer(serializers.ModelSerializer):
    user = StudentUserSerializer()
    class Meta:
        model = Students
        fields = ['user','course','sessionYear']
        
    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = StudentUserSerializer.create(StudentUserSerializer(), validated_data=user_data)
        student = Students.objects.create(user=user, **validated_data)
        return student
    

class StaffLeaveSerializer(serializers.ModelSerializer):
    class Meta:
        model = StaffLeave
        fields = "__all__"
        
class StudentLeaveSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentLeave
        fields = ['leaveDate','reason']
        
class MyAttendanceSerializer(serializers.Serializer):
    subjects = serializers.ChoiceField(choices=Subjects.objects.all())
    start_date = serializers.DateField()
    end_date = serializers.DateField()

  