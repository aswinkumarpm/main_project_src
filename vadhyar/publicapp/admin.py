from django.contrib import admin
from publicapp.models import courses, Complaint
from publicapp.models import login
from publicapp.models import fees
from publicapp.models import salary
from publicapp.models import interplacement
from publicapp.models import subjects
from publicapp.models import hod
from publicapp.models import recordedvideos
from publicapp.models import teacherreg
from publicapp.models import Hods
from publicapp.models import Teacher
from publicapp.models import Students
from publicapp.models import Trainees
from publicapp.models import CustomUser
from publicapp.models import Trainers
from publicapp.models import StudyMaterial


# Register your models here.
admin.site.register(courses)
admin.site.register(login)
admin.site.register(fees)
admin.site.register(salary)
admin.site.register(interplacement)
admin.site.register(subjects)
admin.site.register(hod)
admin.site.register(recordedvideos)
admin.site.register(teacherreg)
admin.site.register(Hods)
admin.site.register(Teacher)
admin.site.register(Trainees)
admin.site.register(Students)
admin.site.register(Complaint)
admin.site.register(CustomUser)
admin.site.register(Trainers)
admin.site.register(StudyMaterial)

