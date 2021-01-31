from django.contrib.auth.models import AbstractUser
from django.db import models

from publicapp.models import phone_regex

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


class User(AbstractUser):
    USER_TYPE = ((1, "HOD"), (2, "Teacher"), (3, "Student"), (4, "Trainer"), (5, "Trainee"))
    user_type = models.IntegerField(choices=USER_TYPE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='profile-pic/')
    mobile_number = models.CharField(validators=[phone_regex], max_length=20, blank=True, null=True)
    date_of_birth = models.DateField()
    address = models.TextField()
    place = models.CharField(max_length=62)
    pin_code = models.IntegerField()
    department = models.CharField(max_length=12)
    gender = models.CharField(max_length=6)

    def __str__(self):
        return self.get_full_name() if self.get_full_name() else self.username


class Course(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Subject(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class HOD(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)
    qualification = models.CharField(max_length=128)
    experience = models.CharField(max_length=128)
    salary = models.IntegerField()

    def __str__(self):
        return f'{self.user} profile'


class Teacher(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)
    qualification = models.CharField(max_length=128)
    experience = models.CharField(max_length=128)
    available_time = models.CharField(max_length=32)
    subject = models.ForeignKey(to=Subject, on_delete=models.CASCADE)
    salary = models.IntegerField()

    def __str__(self):
        return f'{self.user} profile'


class Student(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)
    father_name = models.CharField(max_length=128)
    mother_name = models.CharField(max_length=128)
    guardian_number = models.CharField(validators=[phone_regex], max_length=20, blank=True, null=True)
    standard = models.CharField(max_length=20, blank=True, null=True)
    board = models.CharField(max_length=20, blank=True, null=True)
    school_name = models.CharField(max_length=256)
    fee = models.IntegerField()

    def __str__(self):
        return f'{self.user} profile'


class Trainers(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)
    qualification = models.CharField(max_length=128)
    experience = models.CharField(max_length=128)
    course = models.ForeignKey(to=Course, on_delete=models.CASCADE)
    salary = models.IntegerField()

    def __str__(self):
        return f'{self.user} profile'


class Trainee(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)
    father_name = models.CharField(max_length=128)
    mother_name = models.CharField(max_length=128)
    guardian_number = models.CharField(validators=[phone_regex], max_length=20, blank=True, null=True)
    course = models.ForeignKey(to=Course, on_delete=models.CASCADE)
    board = models.CharField(max_length=20, blank=True, null=True)
    school_name = models.CharField(max_length=256)
    fee = models.IntegerField()

    def __str__(self):
        return f'{self.user} profile'


class Leave(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    from_date = models.DateField()
    to_date = models.DateField()
    reason = models.DateField()
    status = models.CharField(max_length=16)

    def __str__(self):
        return f'Leave request of {self.user}'


class Feedback(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    feedback = models.TextField()

    def __str__(self):
        return f'Feedback from {self.user}'


class Complaint(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='from')
    to = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='to')
    complaint = models.TextField()

    def __str__(self):
        return f'complaint from {self.user}'


class fees(models.Model):
    # student, trainee
    feetype = models.CharField(max_length=35, choices=FEES_CHOICES)
    feeamount = models.IntegerField()
    paymentstatus = models.CharField(max_length=50)
    due = models.CharField(max_length=50)


class salary(models.Model):
    # hod, teacher, trainer
    month = models.CharField(max_length=35, choices=MONTH_CHOICES)
    salaryamount = models.IntegerField()
    paymentstatus = models.CharField(max_length=50)
    pendingsalary = models.IntegerField()


class interplacement(models.Model):
    # hod, trainer, trainee
    interplacement_id = models.AutoField(primary_key=True)
    companyname = models.CharField(max_length=10)
    date = models.DateField()
    time = models.TimeField(max_length=10)
    course_id = models.ForeignKey("publicapp.subjects", on_delete=models.CASCADE, blank=True, null=True)
    job_description = models.CharField(max_length=100)


class StudyMaterial(models.Model):
    material_type = models.CharField(choices=(('video', 'Video'), ('note', 'Note')), max_length=12)
    course = models.ForeignKey(to=Course, on_delete=models.CASCADE, blank=True, null=True)
    subject = models.ForeignKey(to=Subject, on_delete=models.CASCADE, blank=True, null=True)
    file = models.FileField(upload_to='study-material')
    uploaded_by = models.ForeignKey(to=User, on_delete=models.CASCADE, blank=True, null=True)
    uploaded_on = models.DateTimeField(auto_now_add=True)


class Exam(models.Model):
    course = models.ForeignKey(to=Course, on_delete=models.CASCADE, blank=True, null=True)
    subject = models.ForeignKey(to=Subject, on_delete=models.CASCADE, blank=True, null=True)
    conducted_by = models.ForeignKey(to=User, on_delete=models.CASCADE, blank=True, null=True)
    conducted_on = models.DateTimeField()
    # Time in minutes
    max_time = models.IntegerField()
    max_score = models.IntegerField()


class Result(models.Model):
    exam = models.ForeignKey(to=Exam, on_delete=models.CASCADE, blank=True, null=True)
    attended_by = models.ForeignKey(to=User, on_delete=models.CASCADE, blank=True, null=True)
    mark = models.IntegerField()


class ApplyExam(models.Model):
    exam = models.ForeignKey(to=Exam, on_delete=models.CASCADE, blank=True, null=True)
    trainee = models.ForeignKey(to=Trainee, on_delete=models.CASCADE, blank=True, null=True)


class TimeTable(models.Model):
    student = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='student')
    subject = models.ForeignKey(to=Subject, on_delete=models.CASCADE, blank=True, null=True)
    course = models.ForeignKey(to=Course, on_delete=models.CASCADE, blank=True, null=True)
    teacher = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='teacher')
    time = models.CharField(max_length=16)
    date = models.DateField()


class Attendance(models.Model):
    # subject wise
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='teacher')
    date = models.DateField()
    # subject = models.ForeignKey(to=Subject, on_delete=models.CASCADE, blank=True, null=True)
    status = models.CharField(max_length=6)

#
# class attendance(models.Model):
#     attendance_id = models.AutoField(primary_key=True)
#     subject_id = models.IntegerField()
#     attendance_date = models.DateField()
#     status = models.BooleanField(default=False)
#     hod_id = models.ForeignKey("publicapp.hod", on_delete=models.CASCADE, blank=True, null=True)
#     teacher_id = models.ForeignKey("publicapp.teacherreg", on_delete=models.CASCADE, blank=True, null=True)
#     # trainer_id=models.IntegerField()
#     student_id = models.ForeignKey("publicapp.student", on_delete=models.CASCADE, blank=True, null=True)
#     trainee_id = models.ForeignKey("publicapp.trainee", on_delete=models.CASCADE, blank=True, null=True)
#
#
# class attendancereport(models.Model):
#     # Individual Student Attendance
#     attendancereport_id = models.AutoField(primary_key=True)
#     student_id = models.ForeignKey(Student, on_delete=models.DO_NOTHING)
#     date = models.DateField(blank=True, null=True)
#     attendance_id = models.ForeignKey("publicapp.Attendance", on_delete=models.CASCADE, blank=True, null=True)
#     status = models.BooleanField(default=False)
