from django import forms
from django.core.validators import RegexValidator
from django.shortcuts import render
from publicapp.models import login
from publicapp.models import student
from publicapp.models import teacherreg
from publicapp.models import trainee
from publicapp.models import trainerreg
from publicapp.models import fees
from publicapp.models import salary
from publicapp.models import interplacement
from publicapp.models import attendance
from publicapp.models import attendancereport
from publicapp.models import courses
from publicapp.models import feedbackstudent
from publicapp.models import examination
from publicapp.models import studentresult
from publicapp.models import subjects
from publicapp.models import hod
from publicapp.models import leavereport
from publicapp.models import complaints
from publicapp.models import recordedvideos
from publicapp.models import applyforexam
# from publicapp.models import courestimetable
from publicapp.models import commontimetable
from publicapp.models import notes

# from vadhyar.institute.models import Course
phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                             message=
                             "Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(max_length=120, widget=forms.PasswordInput())


class loginForm(forms.ModelForm):
    username = forms.CharField(label="username", max_length=50)
    password = forms.EmailField(label="password", max_length=50)


class studentForm(forms.Form):
    name = forms.CharField(label="name", max_length=30)
    email = forms.EmailField(label="email", max_length=50)
    mobile_num = forms.IntegerField(label="mobile_num")
    gender = forms.CharField(label="gender", max_length=10)
    dob = forms.DateField(label="dob")
    fathername = forms.CharField(label="fathername", max_length=30)
    mothername = forms.CharField(label="mothername", max_length=30)
    housename = forms.CharField(label="housename", max_length=50)
    place = forms.CharField(label="place", max_length=50)
    pincode = forms.IntegerField(label="pincode")
    guardnumber = forms.IntegerField(label="guardnumber")
    standard = forms.CharField(label="standard", max_length=20)
    board = forms.CharField(label="board", max_length=20)
    studtype = forms.CharField(label="studtype", max_length=10)
    schoolname = forms.CharField(label="schoolname", max_length=50)
    splace = forms.CharField(label="splace", max_length=50)
    spincode = forms.IntegerField(label="spincode")
    studentimag = forms.FileField()


class teacherregForm(forms.ModelForm):
    DEPARTMENT_CHOICES = (('1-4', '1-4'),
                          ('5-7', '5-7'),
                          ('8-10', '8-10'),
                          ('+1 Science', '+1 Science'),
                          ('+2 science', '+2 science'),
                          ('+1 Commerce', '+1 Commerce'),
                          ('+2 Commerce', '+2 Commerce'),
                          ('+2 Commerce', '+2 Commerce'),
                          ('B.com/ M.com', 'B.com/ M.com'),
                          ('Civil Engineering', 'Civil Engineering'),
                          ('Mechanical Engineering', 'Mechanical Engineering'),
                          ('Electrical&Electronics Engineering', 'Electrical&Electronics Engineering'),
                          ('Computer Science Engineering', 'Computer Science Engineering'),

                          )

    AVAILABLETIME_CHOICES = (('4-5', '4-5'),
                             ('5-6', '5-6'),
                             ('6-7', '6-7'),
                             ('7-8', '7-8'),
                             ('8-9', '8-9'),
                             ('9-10', '9-10'),
                             )

    department = forms.ChoiceField(required=True)
    available_time = forms.ChoiceField(required=True)

    def __init__(self, *args, **kwargs):
        super(teacherregForm, self).__init__(*args, **kwargs)

        self.fields["subjects"].queryset = subjects.objects.all()
        self.fields['department'].choices = self.DEPARTMENT_CHOICES
        self.fields['available_time'].choices = self.AVAILABLETIME_CHOICES

    class Meta:
        model = teacherreg
        fields = ['name', 'email', 'mobile_num', 'department', 'teacherimag', 'dob', 'qualification',
                  'total_experience', 'subjects', 'housename',
                  'place', 'pincode', 'password', 'available_time']
    # name = forms.CharField(label="name", max_length=30)
    # email = forms.EmailField(label="email", max_length=50)
    # mobile_num = forms.IntegerField(label="mobile_num")
    # dob = forms.DateField(label="dob")
    # qualification = forms.CharField(label="qualification", max_length=20)
    # total_experience = forms.CharField(label="total_experience", max_length=5)
    # subjects = forms.CharField(max_length=20)
    # subjects = forms.CharField(max_length=20)
    # occupation = forms.CharField(label="occupation", max_length=20)
    # teacherimag = forms.FileField()
    # housename = forms.CharField(label="housename", max_length=50)
    # place = forms.CharField(label="place", max_length=50)
    # pincode = forms.IntegerField(label="pincode")


class traineeForm(forms.Form):
    name = forms.CharField(label="name", max_length=30)
    email = forms.EmailField(label="email", max_length=50)
    mobile_num = forms.IntegerField(label="mobile_num")
    gender = forms.CharField(label="gender", max_length=10)
    dob = forms.DateField(label="dob")
    traineeimag = forms.FileField()
    fathername = forms.CharField(label="fathername", max_length=30)
    mothername = forms.CharField(label="mothername", max_length=30)
    housename = forms.CharField(label="housename", max_length=50)
    place = forms.CharField(label="place", max_length=50)
    pincode = forms.IntegerField(label="pincode")
    guardnumber = forms.IntegerField(label="guardnumber")
    qualification = forms.CharField(label="qualification", max_length=20)


class trainerregForm(forms.Form):
    name = forms.CharField(label="name", max_length=30)
    email = forms.EmailField(label="email", max_length=50)
    mobile_num = forms.IntegerField(label="mobile_num")
    gender = forms.CharField(label="gender", max_length=10)
    dob = forms.DateField(label="dob")
    qualification = forms.CharField(label="qualification", max_length=20)
    total_experience = forms.CharField(label="total_experience", max_length=5)
    subjects = forms.CharField(max_length=20)
    occupation = forms.CharField(label="occupation", max_length=20)
    trainerimag = forms.FileField()
    housename = forms.CharField(label="housename", max_length=50)
    place = forms.CharField(label="place", max_length=50)
    pincode = forms.IntegerField(label="pincode")


class feesForm(forms.Form):
    #  
    feetype = forms.CharField(label="feetype", max_length=35)
    feeamount = forms.IntegerField(label="feeamount")
    paymentstatus = forms.CharField(label="paymentstatus", max_length=50)
    due = forms.CharField(max_length=50, label="due")


class salaryForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(salaryForm, self).__init__(*args, **kwargs)
        print(*args[1])

    class Meta:
        model = salary
        fields = ['month', 'salaryamount', 'paymentstatus', 'pendingsalary']
    # id=    (primary_key=True)
    # month=forms.CharField(label="month",max_length=10)
    # salaryamount=forms.IntegerField(label="salaryamount")
    # paymentstatus=forms.CharField(label="paymentstatus",max_length=50)
    # pendingsalary=forms.IntegerField(label="pendingsalary")
    # hod_id=forms.IntegerField()
    # trainer_id=forms.IntegerField()
    # teacher_id=forms.IntegerField()


class interplacementForm(forms.Form):
    companyname = forms.CharField(label="companyname", max_length=10)
    date = forms.DateField(label="date")
    time = forms.TimeField(label="time")
    description = forms.CharField(label="description", max_length=100)


class attendanceForm(forms.Form):
    subject_id = forms.IntegerField()
    attendance_date = forms.DateField(label="attendancedate")
    status = forms.BooleanField(label="status")


class attendancereportForm(forms.Form):
    # Individual Student Attendance

    student_id = forms.IntegerField()
    attendance_id = forms.IntegerField()
    status = forms.BooleanField()


class coursesForm(forms.Form):
    course_name = forms.CharField(label="coursename", max_length=50)

    course_duration = forms.CharField(label="duration", max_length=50)
    course_description = forms.CharField(label="description", max_length=50)
    course_department = forms.CharField(label="department", max_length=15)
    course_trainer = forms.CharField(label="trainer", max_length=15)
    course_fee = forms.IntegerField()


class subjectsForm(forms.ModelForm):
    class Meta:
        model = subjects
        fields = ['subject_name', 'department', 'teacher_id']

    # id =    (primary_key=True)
    # subject_name = forms.CharField(label="subjectname",max_length=50)
    # department = forms.CharField(label="department",max_length=15)
    # teacher_id= forms.CharField(label="teacher",max_length=20)


class feedbackstudentForm(forms.Form):
    feedback = forms.CharField(label="feedback")


class examinationForm(forms.Form):
    student_id = forms.IntegerField()
    examdetails = forms.CharField(label="message", max_length=20)
    date = forms.DateField(label="date")
    time = forms.TimeField(label="time")


class studentresultForm(forms.Form):
    student_id = forms.IntegerField()
    subject_id = forms.IntegerField()
    subject_exam_marks = forms.FloatField()
    grade = forms.CharField(label="grade", max_length=5)
    status = forms.CharField(label="status", max_length=15)
    date = forms.DateField(label="date")


class hodForm(forms.Form):
    name = forms.CharField(label="name", max_length=30)
    email = forms.EmailField(label="email", max_length=50)
    mobile_num = forms.IntegerField(label="mobile_num")
    gender = forms.CharField(label="gender", max_length=10)
    dob = forms.DateField(label="dob")
    qualification = forms.CharField(label="qualification", max_length=20)
    total_experience = forms.CharField(label="total_experience", max_length=5)
    subjects = forms.CharField(max_length=20)
    occupation = forms.CharField(label="occupation", max_length=20)
    hodimag = forms.FileField()
    housename = forms.CharField(label="housename", max_length=50)
    place = forms.CharField(label="place", max_length=50)
    pincode = forms.IntegerField(label="pincode")


class leavereportForm(forms.Form):
    leave_date = forms.CharField(label="leave_date", max_length=255)
    leave_message = forms.CharField(label="leave_msg")
    leave_status = forms.IntegerField()


class complaints(forms.Form):
    complaints_description = forms.CharField()


class recordedvideosForm(forms.Form):
    # recordedvideos_id=    (primary_key=True)
    date = forms.DateField(label="date")
    subjects_id = forms.IntegerField()
    teacher_id = forms.IntegerField()
    trainer_id = forms.IntegerField()
    video = forms.CharField(label="video", max_length=100)


class applyforexamForm(forms.Form):
    courses_id = forms.IntegerField()
    certificate = forms.CharField(label="certificate", max_length=50)


class courestimetableForm(forms.Form):
    course_id = forms.IntegerField()
    day = forms.CharField(label="days", max_length=15)
    time = forms.TimeField()
    trainer_id = forms.IntegerField()


class commontimetableForm(forms.ModelForm):
    class Meta:
        model = commontimetable
        fields = ['subjects_id', 'day', 'time', 'teacher_id']

    # classes=forms.CharField(max_length=10)
    # subjects_id = forms.IntegerField()
    # day = forms.CharField(max_length=15)
    # time = forms.TimeField()
    # teacher_id = forms.IntegerField()


class notesForm(forms.Form):
    teacher_id = forms.IntegerField()
    subject_id = forms.IntegerField()
    notes_pdf = forms.CharField(label="notespdf", max_length=50)
    questionpaper_pdf = forms.CharField(label="question", max_length=50)


class DateInput(forms.DateInput):
    input_type = 'date'


class TraineeRegForm(forms.Form):
    CHOICES = [('Male', 'Male'),
               ('Female', 'Female')]
    name = forms.CharField(label="Name", max_length=30)
    email = forms.EmailField(label="Email", max_length=50)
    mobile_num = forms.CharField(label='Mobile Number', validators=[phone_regex], max_length=20)
    gender = forms.ChoiceField(label='Gender', choices=CHOICES, widget=forms.RadioSelect)
    dob = forms.DateField(label="Date of birth", widget=DateInput())

    def __init__(self, *args, **kwargs):
        super(TraineeRegForm, self).__init__(*args, **kwargs)
        self.fields['course_name'] = forms.ChoiceField(
            choices=[(o.course_name, str(o.course_name)) for o in courses.objects.all()]
        )

    course_name = forms.ChoiceField(label="Please Enter Course Name")
