from publicapp.models import courses
from publicapp.models import CustomUser
from publicapp.models import subjects
from publicapp.models import Teacher
from publicapp.models import TimeTable
from publicapp.models import Trainers


def generate_timetable():
    from datetime import datetime
    today = datetime.now().date()
    if not TimeTable.objects.filter(date=today).exists():
        print('date not exist')
        teachers = CustomUser.objects.filter(user_type__in=[2, 4])
        print(f'{teachers.count()} teachers found')
        for teacher in teachers:
            if teacher.user_type == 2:
                print('is a teacher')
                teacher_profile = Teacher.objects.get(teacher=teacher)
                session = TimeTable.objects.create(teacher=teacher, date=today, time=teacher_profile.available_time)
                course = subjects.objects.filter(teacher_id=teacher).first()
                session.subject = course
                session.save()

            elif teacher.user_type == 4:
                print('is a trainer')
                teacher_profile = Trainers.objects.get(trainer_name=teacher)
                session = TimeTable.objects.create(teacher=teacher, date=today, time=teacher_profile.available_time)
                course = courses.objects.filter(trainee_id=teacher).first()
                session.course = course
                session.save()

            else:
                pass

    return TimeTable.objects.filter(date=today)
