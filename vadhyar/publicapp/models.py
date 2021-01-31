from __future__ import unicode_literals

from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

FEES_CHOICES = (
    ("june-september", "june-september"),
    ("october-december", "october-december"),
    ("january-march", "january-march")
)

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
phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                             message=
                             "Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")


class CustomUser(AbstractUser):
    user_type_data = ((1, "HOD"), (2, "TEACHER"), (3, "STUDENT"), (4, "TRAINER"), (5, "TRAINEE"))
    user_type = models.CharField(default=1, choices=user_type_data, max_length=10)


class student(models.Model):
    student_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    mobile_num = models.IntegerField()
    dob = models.DateField()
    fathername = models.CharField(max_length=30, blank=True, null=True)
    mothername = models.CharField(max_length=30, blank=True, null=True)
    housename = models.CharField(max_length=50, blank=True, null=True)
    place = models.CharField(max_length=50, blank=True, null=True)
    pincode = models.IntegerField(blank=True, null=True)
    guardnumber = models.IntegerField(blank=True, null=True)
    standard = models.CharField(max_length=20)
    board = models.CharField(max_length=20, blank=True, null=True)
    studtype = models.CharField(max_length=10, blank=True, null=True)
    schoolname = models.CharField(max_length=50, blank=True, null=True)
    splace = models.CharField(max_length=50, blank=True, null=True)
    spincode = models.IntegerField(blank=True, null=True)
    studentimag = models.FileField(upload_to="Student")
    password = models.CharField(max_length=50)


class login(models.Model):
    admin_id = models.AutoField(primary_key=True)
    username = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)


class teacherreg(models.Model):
    # teacher_id=models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    mobile_num = models.IntegerField()
    dob = models.DateField()
    qualification = models.CharField(max_length=20)
    total_experience = models.CharField(max_length=5)
    subjects = models.ForeignKey("publicapp.subjects", on_delete=models.CASCADE, blank=True, null=True)
    department = models.CharField(max_length=20)
    available_time = models.CharField(max_length=50)
    teacherimag = models.FileField(upload_to="teacher")
    housename = models.CharField(max_length=50, blank=True, null=True)
    place = models.CharField(max_length=50, blank=True, null=True)
    pincode = models.IntegerField(blank=True, null=True)
    password = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.name


class trainee(models.Model):
    trainee_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    mobile_num = models.IntegerField()
    dob = models.DateField()
    traineeimag = models.FileField(upload_to="trainee")
    fathername = models.CharField(max_length=30, blank=True, null=True)
    mothername = models.CharField(max_length=30, blank=True, null=True)
    housename = models.CharField(max_length=50, blank=True, null=True)
    place = models.CharField(max_length=50, blank=True, null=True)
    pincode = models.IntegerField(blank=True, null=True)
    guardnumber = models.IntegerField(blank=True, null=True)
    course = models.CharField(max_length=20, blank=True, null=True)
    password = models.CharField(max_length=20, blank=True, null=True)


class trainerreg(models.Model):
    trainer_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    mobile_num = models.IntegerField()
    dob = models.DateField()
    qualification = models.CharField(max_length=20)
    total_experience = models.CharField(max_length=5)
    subjects = models.CharField(max_length=20)
    available_time = models.CharField(max_length=50)
    occupation = models.CharField(max_length=20)
    trainerimag = models.FileField()
    housename = models.CharField(max_length=50)
    place = models.CharField(max_length=50)
    pincode = models.IntegerField()


class fees(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    feetype = models.CharField(max_length=35, choices=FEES_CHOICES)
    feeamount = models.IntegerField()
    paymentstatus = models.CharField(max_length=50)
    due = models.CharField(max_length=50)
    trainee_id = models.ForeignKey("publicapp.Trainees", on_delete=models.CASCADE, blank=True, null=True)
    student_id = models.ForeignKey("publicapp.Students", on_delete=models.CASCADE, blank=True, null=True)


class salary(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    month = models.CharField(max_length=35, choices=MONTH_CHOICES)
    salaryamount = models.IntegerField()
    paymentstatus = models.CharField(max_length=50)
    pendingsalary = models.IntegerField()
    hod_id = models.ForeignKey("publicapp.Hods", on_delete=models.CASCADE, blank=True, null=True)
    # trainer_id=models.IntegerField()
    teacher_id = models.ForeignKey("publicapp.Teacher", on_delete=models.CASCADE, blank=True, null=True)
    trainer_id = models.ForeignKey("publicapp.Trainers", on_delete=models.CASCADE, blank=True, null=True)


class StudyMaterial(models.Model):
    material_type = models.CharField(choices=(('video', 'Video'), ('note', 'Note')), max_length=12)
    course = models.ForeignKey(to="publicapp.courses", on_delete=models.CASCADE, blank=True, null=True)
    subject = models.ForeignKey(to="publicapp.subjects", on_delete=models.CASCADE, blank=True, null=True)
    file = models.FileField(upload_to='study-material')
    uploaded_by = models.ForeignKey(to=CustomUser, on_delete=models.CASCADE, blank=True, null=True)
    uploaded_on = models.DateTimeField(auto_now_add=True)

    # hod_id = models.ForeignKey("publicapp.hod", on_delete=models.CASCADE, blank=True, null=True)
    # # trainer_id=models.IntegerField()
    # trainee_id = models.ForeignKey("publicapp.trainee", on_delete=models.CASCADE, blank=True, null=True)


class attendance(models.Model):
    attendance_id = models.AutoField(primary_key=True)
    subject_id = models.IntegerField()
    attendance_date = models.DateField()
    status = models.BooleanField(default=False)
    hod_id = models.ForeignKey("publicapp.hod", on_delete=models.CASCADE, blank=True, null=True)
    teacher_id = models.ForeignKey("publicapp.teacherreg", on_delete=models.CASCADE, blank=True, null=True)
    # trainer_id=models.IntegerField()
    student_id = models.ForeignKey("publicapp.student", on_delete=models.CASCADE, blank=True, null=True)
    trainee_id = models.ForeignKey("publicapp.trainee", on_delete=models.CASCADE, blank=True, null=True)


class attendancereport(models.Model):
    # Individual Student Attendance
    attendancereport_id = models.AutoField(primary_key=True)
    student_id = models.IntegerField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    attendance_id = models.ForeignKey("publicapp.attendance", on_delete=models.CASCADE, blank=True, null=True)
    status = models.BooleanField(default=False)


class courses(models.Model):
    courses_id = models.AutoField(primary_key=True)
    course_name = models.CharField(max_length=50)
    course_pic = models.FileField(upload_to='uploads', blank=True, null=True)
    course_duration = models.CharField(max_length=20)
    course_department = models.CharField(max_length=15, blank=True, null=True)
    course_description = models.CharField(max_length=15, blank=True, null=True)
    course_trainer = models.CharField(max_length=15, blank=True, null=True)
    course_fee = models.IntegerField()
    hod_id = models.ForeignKey("publicapp.hod", on_delete=models.CASCADE, blank=True, null=True)
    trainee_id = models.ForeignKey("publicapp.trainee", on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.course_name


class interplacement(models.Model):
    companyname = models.CharField(max_length=10)
    date = models.DateField()
    time = models.TimeField(max_length=10)
    course = models.ForeignKey(courses, on_delete=models.CASCADE, blank=True, null=True)
    job_description = models.CharField(max_length=100)


class subjects(models.Model):
    subjects_id = models.AutoField(primary_key=True)
    subject_name = models.CharField(max_length=50)
    department = models.CharField(max_length=15)
    teacher = models.CharField(max_length=20, null=True, blank=True)
    hod_id = models.ForeignKey("publicapp.hod", on_delete=models.CASCADE, blank=True, null=True,
                               related_name="subject_hod")
    teacher_id = models.ForeignKey("publicapp.Teacher", on_delete=models.CASCADE, blank=True, null=True,
                                   related_name="subject_teacher")

    def __str__(self):
        return self.subject_name


class feedbackstudent(models.Model):
    feedback_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    date = models.DateField()
    feedback = models.TextField()
    teacheremail = models.CharField(max_length=20)
    teacher_id = models.ForeignKey("publicapp.teacherreg", on_delete=models.CASCADE, blank=True, null=True)
    student_id = models.ForeignKey("publicapp.student", on_delete=models.CASCADE, blank=True, null=True)
    # trainer_id= models.ForeignKey("publicapp.trainerreg", on_delete=models.CASCADE, blank=True, null=True)


class examination(models.Model):
    examination_id = models.AutoField(primary_key=True)
    teacher_id = models.ForeignKey("publicapp.teacherreg", on_delete=models.CASCADE, blank=True, null=True)
    student_id = models.ForeignKey("publicapp.student", on_delete=models.CASCADE, blank=True, null=True)
    hod_id = models.ForeignKey("publicapp.hod", on_delete=models.CASCADE, blank=True, null=True)
    trainee_id = models.ForeignKey("publicapp.trainee", on_delete=models.CASCADE, blank=True, null=True)
    examdetails = models.TextField(max_length=20)
    date = models.DateField()
    time = models.TimeField(max_length=10)


class studentresult(models.Model):
    studentresult_id = models.AutoField(primary_key=True)
    student_id = models.ForeignKey("publicapp.student", on_delete=models.CASCADE, blank=True, null=True)
    subject_id = models.ForeignKey("publicapp.subjects", on_delete=models.CASCADE, blank=True, null=True)
    trainee_id = models.ForeignKey("publicapp.trainee", on_delete=models.CASCADE, blank=True, null=True)
    teacher_id = models.ForeignKey("publicapp.teacherreg", on_delete=models.CASCADE, blank=True, null=True)
    subject_exam_marks = models.FloatField(default=0)
    grade = models.CharField(max_length=5)
    status = models.CharField(max_length=20)
    date = models.DateField()


class hod(models.Model):
    hod_id = models.AutoField(primary_key=True)
    # admi_id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    mobile_num = models.IntegerField()
    # gender= models.IntegerField()
    dob = models.DateField()
    qualification = models.CharField(max_length=20)
    total_experience = models.IntegerField()
    # subjects=models.CharField(max_length=20)
    hodimag = models.FileField()
    housename = models.CharField(max_length=50, blank=True, null=True)
    place = models.CharField(max_length=50, blank=True, null=True)
    pincode = models.IntegerField(blank=True, null=True)
    password = models.CharField(max_length=20)
    department = models.IntegerField()


class complaints(models.Model):
    complaints_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    admin_hod = models.IntegerField()
    complaints_description = models.TextField()
    hod_id = models.ForeignKey("publicapp.hod", on_delete=models.CASCADE, blank=True, null=True)
    teacher_id = models.ForeignKey("publicapp.teacherreg", on_delete=models.CASCADE, blank=True, null=True)
    # trainer_id=models.IntegerField()
    student_id = models.ForeignKey("publicapp.student", on_delete=models.CASCADE, blank=True, null=True)
    trainee_id = models.ForeignKey("publicapp.trainee", on_delete=models.CASCADE, blank=True, null=True)


# class Complaint(models.Model):
#     user = models.ForeignKey(to=CustomUser, on_delete=models.CASCADE, related_name='user')
#     to_who = (("HOD", "HOD"), ("ADMIN", "ADMIN"))
#     to = models.CharField(max_length=50,choices=to_who)
#     complaint = models.TextField()
#     response = models.TextField(blank=True, null=True)
#     created = models.DateTimeField(auto_now_add=True,blank=True,null=True)
#     department = models.CharField(max_length=120,blank=True, null=True)
#
#     def _str_(self):
#         return f'complaint from {self.user}'

class recordedvideos(models.Model):
    recordedvideos_id = models.AutoField(primary_key=True)
    date = models.DateField()
    time = models.TimeField()
    subjects_id = models.IntegerField()
    teacher_id = models.ForeignKey("publicapp.teacherreg", on_delete=models.CASCADE, blank=True, null=True)
    # trainer_id=models.IntegerField()
    video = models.FileField(upload_to="publicapp")
    hod_id = models.ForeignKey("publicapp.hod", on_delete=models.CASCADE, blank=True, null=True)
    hod = models.CharField(max_length=35)
    subject = models.CharField(max_length=35, blank=True, null=True)


class applyforexam(models.Model):
    applyforexam_id = models.AutoField(primary_key=True)
    courses_id = models.IntegerField()
    certificate = models.CharField(max_length=50)


# class courestimetable(models.Model):
#      courestimetable_id=models.AutoField(primary_key=True)
#      course_id=models.IntegerField()
#      day=models.CharField(max_length=15)
#      time=models.TimeField()
#      trainer_id=models.IntegerField()


class commontimetable(models.Model):
    commontimetable_id = models.AutoField(primary_key=True)
    # classes=models.CharField(max_length=10)
    subjects_id = models.ForeignKey("publicapp.subjects", on_delete=models.CASCADE, blank=True, null=True)
    day = models.CharField(max_length=15)
    time = models.TimeField()
    teacher_id = models.ForeignKey("publicapp.teacherreg", on_delete=models.CASCADE, blank=True, null=True)
    available_time = models.CharField(max_length=50)
    standard = models.CharField(max_length=20)
    student_id = models.ForeignKey("publicapp.student", on_delete=models.CASCADE, blank=True, null=True)


class notes(models.Model):
    notes_id = models.AutoField(primary_key=True)
    teacher_id = models.ForeignKey("publicapp.teacherreg", on_delete=models.CASCADE, blank=True, null=True)
    # trainer_id=models.IntegerField()
    student_id = models.ForeignKey("publicapp.student", on_delete=models.CASCADE, blank=True, null=True)
    trainee_id = models.ForeignKey("publicapp.trainee", on_delete=models.CASCADE, blank=True, null=True)
    subject = models.CharField(max_length=35, blank=True, null=True)
    date = models.DateField()
    time = models.TimeField()
    notes_pdf = models.FileField(upload_to="Notes")


class Hods(models.Model):
    hod = models.OneToOneField(CustomUser, on_delete=models.CASCADE, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    dob = models.DateField(blank=True, null=True)
    qualification = models.CharField(max_length=20, blank=True, null=True)
    total_experience = models.IntegerField(blank=True, null=True)
    mobile_number = models.CharField(validators=[phone_regex], max_length=20, blank=True, null=True)
    hodimage = models.FileField(blank=True, null=True)
    housename = models.CharField(max_length=50, blank=True, null=True)
    place = models.CharField(max_length=50, blank=True, null=True)
    pincode = models.IntegerField(blank=True, null=True)
    department = models.CharField(max_length=120, blank=True, null=True)


class Teacher(models.Model):
    teacher = models.OneToOneField(CustomUser, on_delete=models.CASCADE, blank=True, null=True,
                                   related_name="teachers_for_students")
    address = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    mobile_num = models.CharField(validators=[phone_regex], max_length=20, blank=True, null=True)
    dob = models.DateField(blank=True, null=True)
    qualification = models.CharField(max_length=20, blank=True, null=True)
    total_experience = models.CharField(max_length=5, blank=True, null=True)
    subjects = models.ForeignKey("publicapp.subjects", on_delete=models.CASCADE, blank=True, null=True,
                                 related_name="subject_for_student")
    department = models.CharField(max_length=20, blank=True, null=True)
    available_time = models.CharField(max_length=50, blank=True, null=True)
    teacherimage = models.FileField(upload_to="teacher", blank=True, null=True)
    housename = models.CharField(max_length=50, blank=True, null=True)
    place = models.CharField(max_length=50, blank=True, null=True)
    pincode = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.teacher.username


class Students(models.Model):
    student_name = models.OneToOneField(CustomUser, on_delete=models.CASCADE, blank=True, null=True)
    gender = models.CharField(max_length=50, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    mobile_num = models.CharField(validators=[phone_regex], max_length=20, blank=True, null=True)
    dob = models.DateField(blank=True, null=True)
    fathername = models.CharField(max_length=30, blank=True, null=True)
    mothername = models.CharField(max_length=30, blank=True, null=True)
    housename = models.CharField(max_length=50, blank=True, null=True)
    place = models.CharField(max_length=50, blank=True, null=True)
    pincode = models.IntegerField(blank=True, null=True)
    guardnumber = models.IntegerField(blank=True, null=True)
    standard = models.CharField(max_length=20, blank=True, null=True)
    board = models.CharField(max_length=20, blank=True, null=True)
    studtype = models.CharField(max_length=10, blank=True, null=True)
    schoolname = models.CharField(max_length=50, blank=True, null=True)
    studentimage = models.FileField(upload_to="Student", blank=True, null=True)


class Trainers(models.Model):
    trainer_name = models.OneToOneField(CustomUser, on_delete=models.CASCADE, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    mobile_num = models.CharField(validators=[phone_regex], max_length=20, blank=True, null=True)
    dob = models.DateField(blank=True, null=True)
    qualification = models.CharField(max_length=20, blank=True, null=True)
    total_experience = models.CharField(max_length=5, blank=True, null=True)
    subjects = models.ForeignKey("publicapp.subjects", on_delete=models.CASCADE, blank=True, null=True,
                                 related_name="students_name")
    course = models.ForeignKey(courses, on_delete=models.CASCADE, blank=True, null=True)

    department = models.CharField(max_length=20, blank=True, null=True)
    available_time = models.CharField(max_length=50, blank=True, null=True)
    trainerimage = models.FileField(upload_to="trainer", blank=True, null=True)
    housename = models.CharField(max_length=50, blank=True, null=True)
    place = models.CharField(max_length=50, blank=True, null=True)
    pincode = models.IntegerField(blank=True, null=True)


class Trainees(models.Model):
    trainee = models.OneToOneField(CustomUser, on_delete=models.CASCADE, blank=True, null=True)
    gender = models.CharField(max_length=50, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    mobile_num = models.CharField(validators=[phone_regex], max_length=20, blank=True, null=True)
    dob = models.DateField(blank=True, null=True)
    fathername = models.CharField(max_length=30, blank=True, null=True)
    mothername = models.CharField(max_length=30, blank=True, null=True)
    housename = models.CharField(max_length=50, blank=True, null=True)
    place = models.CharField(max_length=50, blank=True, null=True)
    pincode = models.IntegerField(blank=True, null=True)
    guardnumber = models.IntegerField(blank=True, null=True)
    course = models.ForeignKey(courses, on_delete=models.CASCADE, blank=True, null=True)
    board = models.CharField(max_length=20, blank=True, null=True)
    traineetype = models.CharField(max_length=10, blank=True, null=True)
    schoolname = models.CharField(max_length=50, blank=True, null=True)
    traineetimage = models.FileField(upload_to="Trainee", blank=True, null=True)


class leavereport(models.Model):
    leavereport_id = models.AutoField(primary_key=True)
    student_id = models.ForeignKey("publicapp.student", on_delete=models.CASCADE, blank=True, null=True)
    teacher_id = models.ForeignKey("publicapp.teacherreg", on_delete=models.CASCADE, blank=True, null=True)
    trainee_id = models.ForeignKey("publicapp.trainee", on_delete=models.CASCADE, blank=True, null=True)
    hod_id = models.ForeignKey("publicapp.hod", on_delete=models.CASCADE, blank=True, null=True)

    from_date = models.DateField(blank=True, null=True)
    to_date = models.DateField(blank=True, null=True)
    teacheremail = models.CharField(max_length=20)
    leave_message = models.TextField()
    leave_status = models.IntegerField(default=0)


class LeaveReportStudent(models.Model):
    id = models.AutoField(primary_key=True)
    student_id = models.ForeignKey(Students, on_delete=models.CASCADE)
    leave_date = models.CharField(max_length=255)
    leave_message = models.TextField()
    leave_status = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()


class LeaveReportStaff(models.Model):
    id = models.AutoField(primary_key=True)
    staff_id = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    leave_date = models.CharField(max_length=255)
    leave_message = models.TextField()
    leave_status = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()


@receiver(post_save, sender=CustomUser)
# Now Creating a Function which will automatically insert data in HOD, Staff or Student
def create_user_profile(sender, instance, created, **kwargs):
    # if Created is true (Means Data Inserted)
    if created:
        # Check the user_type and insert the data in respective tables
        if instance.user_type == 1:
            Hods.objects.create(hod=instance)
        if instance.user_type == 2:
            Teacher.objects.create(teacher=instance)
        if instance.user_type == 3:
            Students.objects.create(student_name=instance)
        if instance.user_type == 4:
            Trainers.objects.create(trainer_name=instance)
        if instance.user_type == 5:
            Trainees.objects.create(trainee=instance)


@receiver(post_save, sender=CustomUser)
def save_user_profile(sender, instance, **kwargs):
    if instance.user_type == 1:
        instance.hods.save()
    if instance.user_type == 2:
        instance.teachers_for_students.save()
    if instance.user_type == 3:
        instance.students.save()
    if instance.user_type == 4:
        instance.trainers.save()
    if instance.user_type == 5:
        instance.trainees.save()


class Complaint(models.Model):
    user = models.ForeignKey(to=CustomUser, on_delete=models.CASCADE, related_name='user')
    to_who = (("HOD", "HOD"), ("ADMIN", "ADMIN"))
    to = models.CharField(max_length=50, choices=to_who)
    complaint = models.TextField()
    response = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    department = models.CharField(max_length=120, blank=True, null=True)

    def __str__(self):
        return f'complaint from {self.user}'


class TimeTable(models.Model):
    subject = models.ForeignKey(to=subjects, on_delete=models.CASCADE, blank=True, null=True)
    course = models.ForeignKey(to=courses, on_delete=models.CASCADE, blank=True, null=True)
    teacher = models.ForeignKey(to=CustomUser, on_delete=models.CASCADE, related_name='teacher')
    time = models.CharField(max_length=16)
    date = models.DateField()


class StudentsAttending(models.Model):
    time_table = models.ForeignKey(to=TimeTable, on_delete=models.CASCADE)
    student = models.ForeignKey(to=CustomUser, on_delete=models.CASCADE, related_name='teacher')
