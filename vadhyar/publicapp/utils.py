from publicapp.models import CustomUser
from publicapp.models import TimeTable


def generate_timetable():
    from datetime import datetime
    today = datetime.now().date()
    if not TimeTable.objects.filter(date=today).exists():
        teachers = CustomUser.objects.filter(user_type__in=[2, 3])
        for teacher in teachers:
            TimeTable.objects.create(teacher=teacher, date=today, )  # todo: add time
