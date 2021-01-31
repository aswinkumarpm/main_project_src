from django import forms
from django.core.validators import RegexValidator
from django.forms import PasswordInput
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
from publicapp.models import notes, Hods

# from vadhyar.institute.models import Course
from .models import Complaint, Exam, Students, CustomUser
from publicapp.models import StudyMaterial

phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                             message=
                             "Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
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


class DateInput(forms.DateInput):
    input_type = 'date'

class TimeInput(forms.TimeInput):
    input_type = 'time'


class trainerregForm(forms.Form):
    # DEPARTMENT_CHOICES = (('1-4', '1-4'),
    #                       ('5-7', '5-7'),
    #                       ('8-10', '8-10'),
    #                       ('+1 Science', '+1 Science'),
    #                       ('+2 science', '+2 science'),
    #                       ('+1 Commerce', '+1 Commerce'),
    #                       ('+2 Commerce', '+2 Commerce'),
    #                       ('+2 Commerce', '+2 Commerce'),
    #                       ('B.com/ M.com', 'B.com/ M.com'),
    #                       ('Civil Engineering', 'Civil Engineering'),
    #                       ('Mechanical Engineering', 'Mechanical Engineering'),
    #                       ('Electrical&Electronics Engineering', 'Electrical&Electronics Engineering'),
    #                       ('Computer Science Engineering', 'Computer Science Engineering'),
    #                       )

    AVAILABLETIME_CHOICES = (('4-5', '4-5'),
                             ('5-6', '5-6'),
                             ('6-7', '6-7'),
                             ('7-8', '7-8'),
                             ('8-9', '8-9'),
                             ('9-10', '9-10'),
                             )

    def __init__(self, *args, **kwargs):
        super(trainerregForm, self).__init__(*args, **kwargs)
        self.fields['course'] = forms.ChoiceField(
            choices=[(o.courses_id, str(o.course_name)) for o in courses.objects.all()]
        )
        # self.fields['department'].choices = self.DEPARTMENT_CHOICES
        self.fields['available_time'].choices = self.AVAILABLETIME_CHOICES

    name = forms.CharField(label="name", max_length=30)
    email = forms.EmailField(label="email", max_length=50)
    mobile_num = forms.CharField(validators=[phone_regex], label="mobile_num")
    # department = forms.ChoiceField(required=True)
    available_time = forms.ChoiceField(required=True)

    dob = forms.DateField(label="dob", widget=DateInput)
    qualification = forms.CharField(label="qualification", max_length=20)
    total_experience = forms.CharField(label="total_experience", max_length=5)
    course = forms.ChoiceField(label="Please Enter Course Name")
    trainerimage = forms.FileField()
    housename = forms.CharField(label="housename", max_length=50)
    place = forms.CharField(label="place", max_length=50)
    pincode = forms.IntegerField(label="pincode")
    password = forms.CharField(widget=PasswordInput)


class teacherregForm(forms.Form):
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
                          ('Computer Science Engineering', 'Computer Science Engineering'),)


    AVAILABLETIME_CHOICES = (('4-5', '4-5'),
                             ('5-6', '5-6'),
                             ('6-7', '6-7'),
                             ('7-8', '7-8'),
                             ('8-9', '8-9'),
                             ('9-10', '9-10'),
                             )



    def __init__(self, *args, **kwargs):
        super(teacherregForm, self).__init__(*args, **kwargs)
        self.fields['subjects'] = forms.ChoiceField(
            choices=[(o.subject_name, str(o.subject_name)) for o in subjects.objects.all()]
        )
        self.fields['department'].choices = self.DEPARTMENT_CHOICES
        self.fields['available_time'].choices = self.AVAILABLETIME_CHOICES

    name = forms.CharField(label="name", max_length=30)
    email = forms.EmailField(label="email", max_length=50)
    mobile_num = forms.CharField(validators=[phone_regex], label="mobile_num")
    department = forms.ChoiceField(required=True)
    available_time = forms.ChoiceField(required=True)

    dob = forms.DateField(label="dob", widget=DateInput)
    qualification = forms.CharField(label="qualification", max_length=20)
    total_experience = forms.CharField(label="total_experience", max_length=5)
    subjects = forms.ChoiceField(label="Please Enter Subject Name")
    teacherimag = forms.FileField()
    housename = forms.CharField(label="housename", max_length=50)
    place = forms.CharField(label="place", max_length=50)
    pincode = forms.IntegerField(label="pincode")
    password = forms.CharField(widget=PasswordInput)


# class Meta:
#     model = teacherreg
#     fields = ['name', 'email', 'mobile_num', 'department', 'teacherimag', 'dob', 'qualification',
#               'total_experience', 'subjects', 'housename',
#               'place', 'pincode', 'password', 'available_time']


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


# class trainerregForm(forms.Form):
#     name = forms.CharField(label="name", max_length=30)
#     email = forms.EmailField(label="email", max_length=50)
#     mobile_num = forms.IntegerField(label="mobile_num")
#     gender = forms.CharField(label="gender", max_length=10)
#     dob = forms.DateField(label="dob")
#     qualification = forms.CharField(label="qualification", max_length=20)
#     total_experience = forms.CharField(label="total_experience", max_length=5)
#     subjects = forms.CharField(max_length=20)
#     occupation = forms.CharField(label="occupation", max_length=20)
#     trainerimag = forms.FileField()
#     housename = forms.CharField(label="housename", max_length=50)
#     place = forms.CharField(label="place", max_length=50)
#     pincode = forms.IntegerField(label="pincode")


class feesForm(forms.Form):
    FEES_CHOICES = (
        ("june-september", "june-september"),
        ("october-december", "october-december"),
        ("january-march", "january-march")
    )

    feetype = forms.ChoiceField(label="feetype", choices=FEES_CHOICES)
    feeamount = forms.IntegerField(label="feeamount")
    paymentstatus = forms.CharField(label="paymentstatus", max_length=50)
    due = forms.CharField(max_length=50, label="due")


class salaryForm(forms.Form):

    def __init__(self, *args, **kwargs):
        super(salaryForm, self).__init__(*args, **kwargs)
        print(*args[1])
        # instance = Hods.objects.get(id=*args[1])
        # print(instance.hod.username)

    # class Meta:
    #     model = salary
    #     fields = ['month', 'salaryamount', 'paymentstatus', 'pendingsalary']
    # id=    (primary_key=True)
    MONTH_CHOICES = (
        ("january", "january"),
        ("february", "february"),
        ("march", "march"),
        ("april", "april"),
        ("may", "may"),
        ("june", "june"),
        ("july", "july"),
        ("august", "august"),
        ("september", "september"),
        ("october", "october"),
        ("november", "november"),
        ("december", "december")
    )
    month=forms.ChoiceField(label="month", choices=MONTH_CHOICES)
    salaryamount=forms.IntegerField(label="salaryamount")
    paymentstatus=forms.CharField(label="paymentstatus",max_length=50)
    pendingsalary=forms.IntegerField(label="pendingsalary")
    # hod_id=forms.IntegerField()
    # trainer_id=forms.IntegerField()
    # teacher_id=forms.IntegerField()


class interplacementForm(forms.Form):
    companyname = forms.CharField(label="companyname", max_length=10)
    date = forms.DateField(label="date")
    time = forms.TimeField(label="time")
    description = forms.CharField(label="description", max_length=100)


class InterviewAddForm(forms.Form):
    companyname = forms.CharField(label="companyname", max_length=10)
    description = forms.CharField(label="description", max_length=100)
    date = forms.DateField(label="Date", widget=DateInput())
    time = forms.TimeField(label="time", widget=TimeInput())

    def __init__(self, *args, **kwargs):
        super(InterviewAddForm, self).__init__(*args, **kwargs)
        self.fields['course_name'] = forms.ChoiceField(
            choices=[(o.courses_id, str(o.course_name)) for o in courses.objects.all()]
        )

    course_name = forms.ChoiceField(label="Please Enter Course Name")


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
    # course_description = forms.CharField(label="description", max_length=50)
    course_department = forms.CharField(label="department", max_length=15, required=False)
    # course_trainer = forms.CharField(label="trainer", max_length=15)
    course_fee = forms.IntegerField()


class subjectsForm(forms.Form):

    # class Meta:
    #     model = subjects
    #     fields = ['subject_name', 'department']

    # id =    (primary_key=True)
    # subject_name = forms.CharField(label="subjectname",max_length=50)
    subject_name= forms.CharField(label="Subject Name",max_length=50)

    department= forms.ChoiceField(label="Department", choices=DEPARTMENT_CHOICES)

class StudyMaterialForm(forms.ModelForm):
    class Meta:
        model = StudyMaterial
        fields = ['material_type', 'course', 'subject', 'file']


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


class ComplaintForm(forms.ModelForm):
    class Meta:
        model = Complaint
        fields = ['complaint','to']


class ExamForm(forms.Form):
    exam_name = forms.CharField(label="Exam Name", required=False)
    conducted_on = forms.DateField(label="Conducted ON", widget=DateInput())

    time = forms.TimeField(label="Time", widget=TimeInput())
    max_time = forms.IntegerField(label="max_time")
    max_score = forms.IntegerField(label="max_score")
    subject = forms.ModelChoiceField(queryset=subjects.objects.all(), required=False)
    course = forms.ModelChoiceField(queryset=courses.objects.all(), required=False)

    def __init__(self, *args, **kwargs):
        super(ExamForm, self).__init__(*args, **kwargs)
        self.fields['course'] = forms.ChoiceField(
            choices=[(o.courses_id, str(o.course_name)) for o in courses.objects.all()]
        )
        self.fields['subject'] = forms.ChoiceField(
            choices=[(o.subjects_id, str(o.subject_name)) for o in subjects.objects.all()]
        )


class ResultForm(forms.Form):
    exam = forms.ModelChoiceField(queryset=Exam.objects.all(), required=False)
    attended_by = forms.ModelChoiceField(queryset=CustomUser.objects.filter(user_type__in=[3, 5]), required=False)
    mark = forms.IntegerField(label='Mark')
    date = forms.DateField(label="Conducted ON", widget=DateInput())
    grade = forms.CharField(max_length=50, required=False)
    status = forms.CharField(max_length=50, required=False)


