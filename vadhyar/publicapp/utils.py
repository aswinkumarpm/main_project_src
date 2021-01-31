from publicapp.models import courses
from publicapp.models import CustomUser
from publicapp.models import subjects
from publicapp.models import Teacher
from publicapp.models import TimeTable


def generate_timetable():
    from datetime import datetime
    today = datetime.now().date()
    if not TimeTable.objects.filter(date=today).exists():
        teachers = CustomUser.objects.filter(user_type__in=[2, 4])
        for teacher in teachers:
            teacher_profile = Teacher.objects.get(teacher=teacher)
            session = TimeTable.objects.create(teacher=teacher, date=today, time=teacher_profile.available_time)
            if teacher.user_type == 1:
                course = subjects.objects.filter(teacher_id=teacher).first()
                session.subject = course
            else:
                course = courses.objects.filter(trainee_id=teacher).first()
                session.course = course
            session.save()

    return TimeTable.objects.filter(date=today)
