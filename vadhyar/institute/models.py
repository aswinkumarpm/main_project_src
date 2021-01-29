from django.contrib.auth.models import AbstractUser
from django.db import models

from publicapp.models import phone_regex


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
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='teacher')
    date = models.DateField()
    status = models.CharField(max_length=6)
