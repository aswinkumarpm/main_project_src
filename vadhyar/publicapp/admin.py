from django.contrib import admin
from publicapp.models import courses
from publicapp.models import login
from publicapp.models import fees
from publicapp.models import salary
from publicapp.models import interplacement
from publicapp.models import subjects
from publicapp.models import hod
from publicapp.models import recordedvideos
from publicapp.models import teacherreg


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

