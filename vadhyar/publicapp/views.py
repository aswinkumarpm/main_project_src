from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.http import HttpResponseNotFound
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.shortcuts import render

from vadhyar import settings
from .EmailBackend import EmailBackEnd
from .forms import commontimetableForm
from .forms import coursesForm
from .forms import ExamForm
from .forms import feesForm
from .forms import InterviewAddForm
from .forms import LeavesForm
from .forms import LoginForm
from .forms import ResultForm
from .forms import salaryForm
from .forms import StudyMaterialForm
from .forms import subjectsForm
from .forms import teacherregForm
from .forms import TraineeRegForm
from .forms import trainerregForm
from .models import Complaint
from .models import courses
from .models import CustomUser
from .models import Exam
from .models import Feedback
from .models import fees
from .models import Hods
from .models import interplacement
from .models import Leaves
from .models import Result
from .models import salary
from .models import Students
from .models import StudyMaterial
from .models import subjects
from .models import Teacher
from .models import Trainees
from .models import Trainers
# Create your views here.
from .utils import generate_timetable


def test_test(request):
    name = request.POST.get('name', False)
    email = request.POST["email"]
    mobilenum = request.POST["mobilenum"]
    dob = request.POST["dob"]
    qualification = request.POST["qualification"]
    total = request.POST["total"]
    hodimag = request.FILES["hodimag"]

    # dep=request.POST["dep"]
    dep = request.POST.get('dep', False)
    house = request.POST["house"]
    place = request.POST["place"]
    post = request.POST["post"]
    password = request.POST["password"]

    stu = CustomUser.objects.create_user(username=name, password=password, email=email, user_type=1)

    stu.save()

    student = Hods.objects.get(hod__username=name)
    student.total_experience = total
    student.qualification = qualification
    student.mobile_number = mobilenum
    student.hodimage = hodimag
    student.department = dep
    student.housename = house
    student.dob = dob
    student.place = place
    student.post = post
    student.save()

    print("inside approve")

    subject = 'welcome to Vadhyar APP world'
    message = 'Hi thank you for registering in Vadhyar. Your password is' + password + ' .You Can Change Your Password in Profile Page'
    from django.conf import settings

    email_from = settings.EMAIL_HOST_USER
    # recipient_list = ["praveenmv93@gmail.com", ]
    context = {
        "d": "d",
    }
    from django.core.mail import send_mail

    send_mail(subject, message, email_from, [email, ])

    return render(request, 'adminapp/add_professor.html')


# def hod_details(request, id=None):
#     instance = get_object_or_404(Hods, id=id)
#     print(instance)
#
#     return render(request, 'adminapp/hod_salary.html', {"instance": instance})


def hod_salary(request, id=None):
    instance = get_object_or_404(Hods, hod_id=id)
    print(instance.hod.username)

    user_instance = CustomUser.objects.get(username=instance.hod.username)

    form = salaryForm(request.POST, id)
    print("called")
    if form.is_valid():
        print('called')
        month = request.POST["month"]
        salaryamount = request.POST["salaryamount"]
        paymentstatus = request.POST["paymentstatus"]
        pendingsalary = request.POST["pendingsalary"]

        alldata = salary(user_id=user_instance.id, month=month, salaryamount=salaryamount, paymentstatus=paymentstatus,
                         pendingsalary=pendingsalary)
        alldata.save()

        return redirect('admindex')

    #
    #     return render(request, 'adminapp/hod_salary.html', {"form": form, "instance": instance})
    # month = request.POST["month"]
    # salaryamount = request.POST["salaryamount"]
    # paymentstatus = request.POST["paymentstatus"]
    # pendingsalary = request.POST["pendingsalary"]
    #
    # alldata = salary(month=month, salaryamount=salaryamount, paymentstatus=paymentstatus, pendingsalary=pendingsalary)
    # alldata.save()

    print("aswin")
    salary_history = salary.objects.filter(user_id=user_instance.id)

    return render(request, 'adminapp/hod_salary.html',
                  {"form": form, "instance": instance, "salaryhistory": salary_history})


def hod_salarys(request, id=None):
    instance = get_object_or_404(Hods, hod_id=id)
    print(instance.hod.username)

    user_instance = CustomUser.objects.get(username=instance.hod.username)

    form = salaryForm(request.POST, id)
    print("called")
    if form.is_valid():
        print('called')
        month = request.POST["month"]
        salaryamount = request.POST["salaryamount"]
        paymentstatus = request.POST["paymentstatus"]
        pendingsalary = request.POST["pendingsalary"]

        alldata = salary(user_id=user_instance.id, month=month, salaryamount=salaryamount, paymentstatus=paymentstatus,
                         pendingsalary=pendingsalary)
        alldata.save()

        return redirect('admindex')

    #
    #     return render(request, 'adminapp/hod_salary.html', {"form": form, "instance": instance})
    # month = request.POST["month"]
    # salaryamount = request.POST["salaryamount"]
    # paymentstatus = request.POST["paymentstatus"]
    # pendingsalary = request.POST["pendingsalary"]
    #
    # alldata = salary(month=month, salaryamount=salaryamount, paymentstatus=paymentstatus, pendingsalary=pendingsalary)
    # alldata.save()

    print("aswin")
    salary_history = salary.objects.filter(user_id=user_instance.id)

    return render(request, 'hodapp/hod_salary.html',
                  {"form": form, "instance": instance, "salaryhistory": salary_history})


def teacher_salary(request, id=None):
    instance = get_object_or_404(Teacher, teacher_id=id)
    print(instance.teacher.username)

    user_instance = CustomUser.objects.get(username=instance.teacher.username)

    form = salaryForm(request.POST, id)
    print("called")
    if form.is_valid():
        print('called')
        month = request.POST["month"]
        salaryamount = request.POST["salaryamount"]
        paymentstatus = request.POST["paymentstatus"]
        pendingsalary = request.POST["pendingsalary"]

        alldata = salary(user_id=user_instance.id, month=month, salaryamount=salaryamount, paymentstatus=paymentstatus,
                         pendingsalary=pendingsalary)
        alldata.save()

        return redirect('admindex')

    salary_history = salary.objects.filter(user_id=user_instance.id)

    return render(request, 'adminapp/teacher_salary.html',
                  {"form": form, "instance": instance, "salaryhistory": salary_history})


def teacher_salarys(request, id=None):
    instance = get_object_or_404(Teacher, teacher_id=id)
    print(instance.teacher.username)

    user_instance = CustomUser.objects.get(username=instance.teacher.username)

    form = salaryForm(request.POST, id)
    print("called")
    if form.is_valid():
        print('called')
        month = request.POST["month"]
        salaryamount = request.POST["salaryamount"]
        paymentstatus = request.POST["paymentstatus"]
        pendingsalary = request.POST["pendingsalary"]

        alldata = salary(user_id=user_instance.id, month=month, salaryamount=salaryamount, paymentstatus=paymentstatus,
                         pendingsalary=pendingsalary)
        alldata.save()

        return redirect('admindex')

    salary_history = salary.objects.filter(user_id=user_instance.id)

    return render(request, 'teacherapp/salary.html',
                  {"form": form, "instance": instance, "salaryhistory": salary_history})


def trainer_salary(request, id=None):
    instance = get_object_or_404(Trainers, trainer_name_id=id)
    print(instance.trainer_name.username)

    user_instance = CustomUser.objects.get(username=instance.trainer_name.username)

    form = salaryForm(request.POST, id)
    print("called")
    if form.is_valid():
        print('called')
        month = request.POST["month"]
        salaryamount = request.POST["salaryamount"]
        paymentstatus = request.POST["paymentstatus"]
        pendingsalary = request.POST["pendingsalary"]

        alldata = salary(user_id=user_instance.id, month=month, salaryamount=salaryamount, paymentstatus=paymentstatus,
                         pendingsalary=pendingsalary)
        alldata.save()

        return redirect('admindex')

    salary_history = salary.objects.filter(user_id=user_instance.id)

    return render(request, 'adminapp/trainer_salary.html',
                  {"form": form, "instance": instance, "salaryhistory": salary_history})


def trainee_fee(request, id=None):
    instance = get_object_or_404(Trainees, trainee_id=id)
    print(instance.trainee.username)

    user_instance = CustomUser.objects.get(username=instance.trainee.username)

    form = feesForm(request.POST, id)
    print("called")
    if form.is_valid():
        print('called')
        feetype = request.POST["feetype"]
        feeamount = request.POST["feeamount"]
        paymentstatus = request.POST["paymentstatus"]
        due = request.POST["due"]

        alldata = fees(user_id=user_instance.id, feetype=feetype, feeamount=feeamount, paymentstatus=paymentstatus,
                       due=due)
        alldata.save()

        return redirect('admindex')

    fee_history = fees.objects.filter(user_id=user_instance.id)

    return render(request, 'adminapp/trainee_fee.html',
                  {"form": form, "instance": instance, "fee_history": fee_history})


def student_fee(request, id=None):
    instance = get_object_or_404(Students, student_name_id=id)
    print(instance.student_name.username)

    user_instance = CustomUser.objects.get(username=instance.student_name.username)

    form = feesForm(request.POST, id)
    print("called")
    if form.is_valid():
        print('called')
        feetype = request.POST["feetype"]
        feeamount = request.POST["feeamount"]
        paymentstatus = request.POST["paymentstatus"]
        due = request.POST["due"]

        alldata = fees(user_id=user_instance.id, feetype=feetype, feeamount=feeamount, paymentstatus=paymentstatus,
                       due=due)
        alldata.save()

        return redirect('admindex')
    fee_history = fees.objects.filter(user_id=user_instance.id)

    return render(request, 'adminapp/student_fee.html',
                  {"form": form, "instance": instance, "fee_history": fee_history})


# def hod_test_salary(request, id=None):
#     print("aswin")
#     print(id)
#     month = request.POST.get('month', None)
#     salaryamount = request.POST.get('salaryamount', None)
#     paymentstatus = request.POST.get("paymentstatus", None)
#     pendingsalary = request.POST.get("pendingsalary", None)
#     # alldata= salary(month=month,salaryamount=salaryamount,paymentstatus=paymentstatus,pendingsalary=pendingsalary,hod_id_id=id)
#     # alldata.save()
#     return render(request, 'test1.html', {"id": id})


def test_teacher(request):
    form = teacherregForm(request.POST)

    #
    # all = teacherreg(name=name, email=email, mobile_num=mobileno, dob=dob, qualification=qualification,
    #                  total_experience=total_experience, teacherimag=filenname, department=dep, housename=house,
    #                  place=place, pincode=post, subjects=subject, password=password)
    # all.save()
    return render(request, 'adminapp/add_teacher.html', {'form', form})


def hod_salary_details(request, hod_id=None):
    instance = get_object_or_404(salary, hod_id=hod_id)
    return render(request, 'adminapp/add_professor.html', {})


def view_hod(request):
    all_hods = Hods.objects.all()
    for i in all_hods:
        print(i.department, i.mobile_number)
    return render(request, 'adminapp/all_hod.html', {'head': all_hods})


def view_teachers(request):
    all_teachers = Teacher.objects.all()
    print(all_teachers)
    for i in all_teachers:
        print(i.department)
    return render(request, 'adminapp/all_teachers.html', {'teachers': all_teachers})


def view_students(request):
    all_teachers = Students.objects.all()
    print(all_teachers)
    for i in all_teachers:
        print(i.standard)
    return render(request, 'adminapp/all_students.html', {'teachers': all_teachers})


def index(request):
    return render(request, "publicapp/index.html", {})


def studentsave(request):
    if request.method == 'POST':
        uname = request.POST['user_name']
        print(uname)
        user_email = request.POST['user_email']
        print(user_email)
        user_mobile_number = request.POST['user_mobile_number']
        print(user_mobile_number)
        user_dob = request.POST['user_dob']
        print(user_dob)
        standard = request.POST['standard']
        print(standard)
        print(uname)

        stu = CustomUser.objects.create_user(username=uname, password='q1w2e3r4', email=user_email, user_type=3)

        stu.save()
        student = Students.objects.get(student_name__username=uname)
        student.standard = standard
        student.mobile_num = user_mobile_number
        student.dob = user_dob
        try:
            student.save()
        except Exception as e:
            print("EXCEPTION", e)
            messages.error(request, 'Please correct the error below. /n' + str(e))

        print("inside approve")

        subject = 'welcome to Vadhyar APP world'
        message = 'Hi thank you for registering in Vadhyar. Your password is q1w2e3r4 .You Can Change Your Password in Profile Page'
        from django.conf import settings

        email_from = settings.EMAIL_HOST_USER
        # recipient_list = ["praveenmv93@gmail.com", ]
        context = {
            "d": "d",
        }
        from django.core.mail import send_mail

        send_mail(subject, message, email_from, [user_email, ])
    return render(request, "publicapp/index.html", {})


def traineesave(request):
    if request.method == 'POST':
        uname = request.POST['name']
        print(uname)
        user_email = request.POST['email']
        print(user_email)
        user_mobile_number = request.POST['mobile_num']
        print(user_mobile_number)
        user_dob = request.POST['dob']
        print(user_dob)
        user_gender = request.POST['gender']
        print(user_gender)
        course = request.POST['course_name']
        print(course)
        print(uname)

        stu = CustomUser.objects.create_user(username=uname, password='q1w2e3r4', email=user_email, user_type=5)

        stu.save()
        student = Trainees.objects.get(trainee__username=uname)
        student.course = course
        student.mobile_num = user_mobile_number
        student.dob = user_dob
        student.gender = user_gender
        student.save()

        print("inside approve")

        subject = 'welcome to Vadhyar APP world'
        message = 'Hi thank you for registering in Vadhyar. Your password is q1w2e3r4 .You Can Change Your Password in Profile Page'
        from django.conf import settings

        email_from = settings.EMAIL_HOST_USER
        context = {
            "d": "d",
        }
        from django.core.mail import send_mail

        send_mail(subject, message, email_from, [user_email, ])
    return render(request, "publicapp/index.html", {})


def courseslist(request):
    return render(request, "publicapp/courses.html", {})


def contact(request):
    return render(request, "publicapp/contact.html", {})


def teachers(request):
    return render(request, "publicapp/teachers.html", {})


def tution(request):
    return render(request, "publicapp/tution.html", {})


def aboutus(request):
    return render(request, "publicapp/aboutus.html", {})


def civil(request):
    return render(request, "publicapp/civil.html", {})


def cs(request):
    return render(request, "publicapp/cs.html", {})


def mech(request):
    return render(request, "publicapp/mech.html", {})


def ec(request):
    return render(request, "publicapp/ec.html", {})


def studreg(request):
    return render(request, "publicapp/studreg.html", {})


def teacherregister(request):
    return render(request, "publicapp/teacherreg.html", {})


def us(request):
    return render(request, "publicapp/us.html", {})


def logintr(request):
    return render(request, "publicapp/logintr.html", {})


def loginh(request):
    return render(request, "publicapp/loginh.html", {})


def loginteach(request):
    return render(request, "publicapp/loginteach.html", {})


def logintrainer(request):
    return render(request, "publicapp/logintrainer.html", {})


def loginadmin(request):
    if request.method == 'POST':
        uname = request.POST['uname']
        passw = request.POST['passw']
        user = authenticate(request, username=uname, password=passw)
        if user is not None:
            login(request, user)
            return render(request, 'adminapp/admindex.html')

    return render(request, "publicapp/loginadmin.html", {})


def loginstud(request):
    return render(request, "publicapp/loginstud.html", {})


def re(request):
    if request.method == 'POST':
        uname = request.POST['user_name']
        print(uname)
        user_email = request.POST['user_email']
        print(user_email)
        user_mobile_number = request.POST['user_mobile_number']
        print(user_mobile_number)
        user_dob = request.POST['user_dob']
        print(user_dob)
        standard = request.POST['standard']
        print(standard)
        print(uname)
        try:
            stu = CustomUser.objects.create_user(username=uname, password='q1w2e3r4', email=user_email, user_type=3)

            stu.save()
            student = Students.objects.get(student_name__username=uname)
            student.standard = standard
            student.mobile_num = user_mobile_number
            student.dob = user_dob

            student.save()
            print("inside approve")

            subject = 'welcome to Vadhyar APP world'
            message = 'Hi thank you for registering in Vadhyar. Your password is q1w2e3r4 .You Can Change Your Password in Profile Page'
            from django.conf import settings

            email_from = settings.EMAIL_HOST_USER
            # recipient_list = ["praveenmv93@gmail.com", ]
            context = {
                "d": "d",
            }
            from django.core.mail import send_mail

            send_mail(subject, message, email_from, [user_email, ])
        except Exception as e:
            print("EXCEPTION", e)
            if str(e) == "UNIQUE constraint failed: publicapp_customuser.username":
                print("RRR")

                messages.error(request, 'Username must be a unique one, please try with another one')

            else:
                messages.error(request, str(e))

    return render(request, "publicapp/re.html", {})


def admindex(request):
    return render(request, "adminapp/admindex.html", {})


def add_professor(request):
    return render(request, "adminapp/add_professor.html", {})


def edit_professor(request):
    return render(request, "adminapp/edit_professor.html", {})


def professor_profile(request):
    return render(request, "adminapp/professor_profile.html", {})


def teacher_profile(request):
    return render(request, "adminapp/teacher_profile.html", {})


def trainer_profile(request):
    return render(request, "adminapp/trainer_profile.html", {})


def tution(request):
    return render(request, "publicapp/tution.html", {})


def autocad(request):
    return render(request, "publicapp/autocad.html", {})


def ds(request):
    return render(request, "publicapp/ds.html", {})


def revit(request):
    return render(request, "publicapp/revit.html", {})


def googles(request):
    return render(request, "publicapp/googles.html", {})


def stadd(request):
    return render(request, "publicapp/stadd.html", {})


def etab(request):
    return render(request, "publicapp/etab.html", {})


def vray(request):
    return render(request, "publicapp/vray.html", {})


def revitst(request):
    return render(request, "publicapp/revitst.html", {})


def navis(request):
    return render(request, "publicapp/navis.html", {})


def prim(request):
    return render(request, "publicapp/prim.html", {})


def autocadmech(request):
    return render(request, "publicapp/autocadmech.html", {})


def catia(request):
    return render(request, "publicapp/catia.html", {})


def solid(request):
    return render(request, "publicapp/solid.html", {})


def ansys(request):
    return render(request, "publicapp/ansys.html", {})


def nxcad(request):
    return render(request, "publicapp/nxcad.html", {})


def nxcam(request):
    return render(request, "publicapp/nxcam.html", {})


def nxnas(request):
    return render(request, "publicapp/nxnas.html", {})


def revitmep(request):
    return render(request, "publicapp/revitmep.html", {})


def prime(request):
    return render(request, "publicapp/prime.html", {})


def autocadec(request):
    return render(request, "publicapp/autocadec.html", {})


def ecrevit(request):
    return render(request, "publicapp/ecrevit.html", {})


def ecprim(request):
    return render(request, "publicapp/ecprim.html", {})


def java(request):
    return render(request, "publicapp/java.html", {})


def web(request):
    return render(request, "publicapp/web.html", {})


def python(request):
    return render(request, "publicapp/python.html", {})


def tu(request):
    return render(request, "publicapp/tu.html", {})


def viewteacher(request):
    return render(request, "publicapp/viewteacher.html", {})


def regteacher(request):
    return render(request, "publicapp/regteacher.html", {})


# def all_subjects(request):
#     sub = subjects.objects.all()
#     print(sub)
#
#     return render(request, "adminapp/all_subjects.html", {'sub' : sub})


# def subjectadd(request):
#     all_teachers = Teacher.objects.all()
#     form = subjectsForm(request.POST)
#     if form.is_valid():
#         subject_name = request.POST["subject_name"]
#         department = request.POST["department"]
#         stu = subjects.objects.create_user(subject_name=subject_name, department=department)
#
#         stu.save()
#         return redirect('admindex')
#     return render(request, "adminapp/subjectadd.html", {all_teachers: all_teachers, "form": form})


def add_teacher(request):
    form = teacherregForm(request.POST, request.FILES)

    if form.is_valid():
        name = request.POST["name"]
        email = request.POST["email"]
        mobile_num = request.POST["mobile_num"]
        dob = request.POST["dob"]
        qualification = request.POST["qualification"]
        total_experience = request.POST["total_experience"]
        teacherimag = request.FILES["teacherimag"]
        department = request.POST.get('department', None)
        house = request.POST["housename"]
        place = request.POST["place"]
        pincode = request.POST["pincode"]
        subjects = request.POST.get('subjects', None)
        available_time = request.POST.get('available_time', None)
        password = request.POST["password"]

        stu = CustomUser.objects.create_user(username=name, password=password, email=email, user_type=2)

        stu.save()

        student = Teacher.objects.get(teacher__username=name)
        student.total_experience = total_experience
        student.qualification = qualification
        student.mobile_number = mobile_num
        student.teacherimag = teacherimag
        student.department = department
        student.subjects__subject_name = subjects
        student.available_time = available_time
        student.housename = house
        student.dob = dob
        student.place = place
        student.post = pincode
        student.save()

        print("inside approve")

        subject = 'welcome to Vadhyar APP world'
        message = 'Hi thank you for registering in Vadhyar. Your password is' + password + ' .You Can Change Your Password in Profile Page'
        from django.conf import settings

        email_from = settings.EMAIL_HOST_USER
        # recipient_list = ["praveenmv93@gmail.com", ]
        context = {
            "d": "d",
        }
        from django.core.mail import send_mail

        send_mail(subject, message, email_from, [email, ])

    # name = request.POST["name"]
    # email = request.POST["email"]
    # mobileno = request.POST["mobileno"]
    # dob = request.POST["dob"]
    # qualification = request.POST["qualification"]
    # total_experience = request.POST["total_experience"]
    # filenname = request.FILES["filename"]
    # print(filenname)
    # dep = request.POST.get('dep', None)
    # house = request.POST["house"]
    # place = request.POST["place"]
    # post = request.POST["post"]
    # subject = request.POST.get('subject', None)
    # password = request.POST["password"]
    #
    # all = teacherreg(name=name, email=email, mobile_num=mobileno, dob=dob, qualification=qualification,
    #                  total_experience=total_experience, teacherimag=filenname, department=dep, housename=house,
    #                  place=place, pincode=post, subjects=subject, password=password)
    # all.save()
    return render(request, 'adminapp/add_teacher.html', {"form": form})


def add_trainer(request):
    form = trainerregForm(request.POST, request.FILES)

    if form.is_valid():
        name = request.POST["name"]
        email = request.POST["email"]
        mobile_num = request.POST["mobile_num"]
        dob = request.POST["dob"]
        qualification = request.POST["qualification"]
        total_experience = request.POST["total_experience"]
        trainerimage = request.FILES["trainerimage"]
        department = request.POST.get('department', None)
        house = request.POST["housename"]
        place = request.POST["place"]
        pincode = request.POST["pincode"]
        course = request.POST.get('course', None)
        available_time = request.POST.get('available_time', None)
        password = request.POST["password"]

        stu = CustomUser.objects.create_user(username=name, password=password, email=email, user_type=4)

        stu.save()

        student = Trainers.objects.get(trainer_name__username=name)
        student.total_experience = total_experience
        student.qualification = qualification
        student.mobile_number = mobile_num
        student.trainerimag = trainerimage
        student.department = department
        student.courses__course_name = course
        student.available_time = available_time
        student.housename = house
        student.dob = dob
        student.place = place
        student.post = pincode
        student.save()

        print("inside approve")

        subject = 'welcome to Vadhyar APP world'
        message = 'Hi thank you for registering in Vadhyar. Your password is' + password + ' .You Can Change Your Password in Profile Page'
        from django.conf import settings

        email_from = settings.EMAIL_HOST_USER
        # recipient_list = ["praveenmv93@gmail.com", ]
        context = {
            "d": "d",
        }
        from django.core.mail import send_mail
        send_mail(subject, message, email_from, [email, ])

    return render(request, "adminapp/add_trainer.html", {"form": form})


def trainersave(request):
    form = trainerregForm(request.POST, request.FILES)

    if form.is_valid():
        name = request.POST["name"]
        email = request.POST["email"]
        mobile_num = request.POST["mobile_num"]
        dob = request.POST["dob"]
        qualification = request.POST["qualification"]
        total_experience = request.POST["total_experience"]
        trainerimag = request.FILES["teacherimag"]
        department = request.POST.get('department', None)
        house = request.POST["housename"]
        place = request.POST["place"]
        pincode = request.POST["pincode"]
        course = request.POST.get('course', None)
        available_time = request.POST.get('available_time', None)
        password = request.POST["password"]

        stu = CustomUser.objects.create_user(username=name, password=password, email=email, user_type=4)

        stu.save()

        student = Trainers.objects.get(teacher__username=name)
        student.total_experience = total_experience
        student.qualification = qualification
        student.mobile_number = mobile_num
        student.trainerimag = trainerimag
        student.department = department
        student.course_id = course
        student.available_time = available_time
        student.housename = house
        student.dob = dob
        student.place = place
        student.post = pincode
        student.save()

        print("inside approve")

        subject = 'welcome to Vadhyar APP world'
        message = 'Hi thank you for registering in Vadhyar. Your password is' + password + ' .You Can Change Your Password in Profile Page'
        from django.conf import settings

        email_from = settings.EMAIL_HOST_USER
        # recipient_list = ["praveenmv93@gmail.com", ]
        context = {
            "d": "d",
        }
        from django.core.mail import send_mail
        send_mail(subject, message, email_from, [email, ])

    return render(request, "adminapp/add_trainer.html", {"form": form})


def all_course(request):
    queryset = courses.objects.all()
    print(queryset)
    return render(request, "adminapp/all_course.html", {'queryset': queryset})


def courseadd(request):
    form = coursesForm(request.POST)
    if form.is_valid():
        course_name = request.POST["course_name"]
        course_duration = request.POST["course_duration"]
        course_department = request.POST.get("course_department", None)
        course_fee = request.POST["course_fee"]
        if courses.objects.filter(course_name=course_name).count() > 0:
            print("Ffff")
            messages.error(request, "Course name must be unique")
        else:
            stu = courses(course_name=course_name, course_duration=course_duration, course_department=course_department,
                          course_fee=course_fee)

            stu.save()
            return redirect('admindex')
    return render(request, "adminapp/courseadd.html", {'form': form})


def all_subjects(request):
    sub = subjects.objects.all()
    print(sub)

    return render(request, "adminapp/all_subjects.html", {'sub': sub})


def subjectadd(request):
    all_teachers = Teacher.objects.all()
    form = subjectsForm(request.POST)
    if form.is_valid():
        subject_name = request.POST["subject_name"]
        department = request.POST["department"]
        stu = subjects(subject_name=subject_name, department=department)

        stu.save()
        return redirect('admindex')
    return render(request, "adminapp/subjectadd.html", {all_teachers: all_teachers, "form": form})


def timetableadd(request):
    print("gagagga")
    form = commontimetableForm(request.POST)
    print("called")
    if form.is_valid():
        instance = form.save()
        print(instance)
        form.save()
    return render(request, "adminapp/timetableadd.html", {"form": form})


def select_teacher_timetable(request):
    return render(request, "adminapp/subjectadd.html", {all_teachers: all_teachers, "form": form})


def interplacementadd(request):
    form = InterviewAddForm(request.POST)
    print("called")
    if form.is_valid():
        companyname = request.POST["companyname"]
        description = request.POST["description"]
        date = request.POST["date"]
        time = request.POST["time"]
        course_name = request.POST["course_name"]
        print(course_name)
        print(companyname)

        alldata = interplacement()
        alldata.companyname = companyname

        alldata.job_description = description
        alldata.date = date
        alldata.time = time
        alldata.course_id = course_name
        alldata.save()

        return redirect('admindex')

    return render(request, "adminapp/interplacement.html", {'form': form})


def all_interview(request):
    interviews = interplacement.objects.all()

    return render(request, "adminapp/all_interview.html", {'interviews': interviews})


def all_videos(request):
    queryset = StudyMaterial.objects.filter(material_type='video')
    return render(request, "adminapp/all_videos.html", {'queryset': queryset})


def all_notes(request):
    queryset = StudyMaterial.objects.filter(material_type='note')
    return render(request, "adminapp/all_notes.html", {'queryset': queryset})


def recordvideos(request):
    form = StudyMaterialForm(request.POST, request.FILES)
    if form.is_valid():
        instance = form.save()
        print(instance)
        print('video saved')
        print('video saved')

    return render(request, "adminapp/recordvideos.html", {'form': form})


def all_students(request):
    return render(request, "adminapp/all_students.html")


def studentfee(request):
    return render(request, "adminapp/studentfee.html")


def complaints(request):
    return render(request, "adminapp/complaints.html")


def all_teachers(request):
    return render(request, "adminapp/all_teachers.html")


def all_hod(request):
    return render(request, "adminapp/all_hod.html")


def all_trainers(request):
    all_trainers = Trainers.objects.all()
    print(all_trainers)
    return render(request, "adminapp/all_trainers.html", {'trainers': all_trainers})


def all_trainee(request):
    all_trainees = Trainees.objects.all()
    print(all_trainees)
    for i in all_trainees:
        print(i)
    return render(request, "adminapp/all_trainee.html", {'trainees': all_trainees})


def hodindex(request):
    return render(request, "hodapp/hodindex.html")


def retrainer(request):
    form = TraineeRegForm()
    if request.method == 'POST':
        uname = request.POST['name']
        print(uname)
        user_email = request.POST['email']
        print(user_email)
        user_mobile_number = request.POST['mobile_num']
        print(user_mobile_number)
        user_dob = request.POST['dob']
        print(user_dob)
        user_gender = request.POST['gender']
        print(user_gender)
        course = request.POST['course_name']
        print(course)
        print(uname)

        try:
            stu = CustomUser.objects.create_user(username=uname, password='q1w2e3r4', email=user_email, user_type=5)

            stu.save()
            student = Trainees.objects.get(trainee__username=uname)
            student.course = courses.objects.get(course_name=course)
            student.mobile_num = user_mobile_number
            student.dob = user_dob
            student.gender = user_gender
            student.save()

            print("inside approve")

            subject = 'welcome to Vadhyar APP world'
            message = 'Hi thank you for registering in Vadhyar. Your password is q1w2e3r4 .You Can Change Your Password in Profile Page'
            from django.conf import settings

            email_from = settings.EMAIL_HOST_USER
            context = {
                "d": "d",
            }
            from django.core.mail import send_mail

            send_mail(subject, message, email_from, [user_email, ])
            return redirect("/")
        except Exception as e:
            print("ESCEPTION", e)

            if str(e) == "UNIQUE constraint failed: publicapp_customuser.username":
                messages.error(request, "Username must be unique please try with another. ")
            else:
                messages.error(request, str(e))
    return render(request, "publicapp/retrainer.html", {'form': form})


def hodteacher(request):
    return render(request, "hodapp/hodteacher.html")


def hodtrainer(request):
    return render(request, "hodapp/hodtrainer.html")


def hodstudent(request):
    return render(request, "hodapp/hodstudent.html")


def hodtrainee(request):
    hos = Hods.objects.get(hod=request.user)
    dep = hos.department
    print(dep)
    trainers = Trainers.objects.filter(department=dep).values_list('course__course_name').distinct()
    query = Trainees.objects.filter(course__course_name__in=trainers)
    print(query)
    return render(request, "hodapp/hodtrainee.html",{"query":query})


def addleave(request):
    return render(request, "hodapp/addleave.html")


def allleave(request):
    return render(request, "hodapp/allleave.html")


def teacherindex(request):
    if request.method == 'POST':
        uname = request.POST['email']
        passw = request.POST['pass']
        print(uname, passw)

    return render(request, "teacherapp/teacherindex.html")


def studentindex(request):
    if request.method == 'POST':
        email = request.POST['email']
        passw = request.POST.get('passw', None)

        print(email, passw)

    return render(request, "studentapp/studentindex.html")


def traineeindex(request):
    return render(request, "traineeapp/traineeindex.html")


def studleave(request):
    return render(request, "studentapp/studleave.html")


def feedback(request):
    return render(request, "studentapp/feedback.html")


#
#
def studcomplaints(request):
    return render(request, "studentapp/studcomplaints.html")


#

def all_complaints(request):
    return render(request, "studentapp/all_complaints.html")


def all_leaves(request):
    return render(request, "studentapp/all_leaves.html")


def studvideo(request):
    return render(request, "studentapp/studvideo.html")


def studprofile(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            print("values updated")
            return redirect('studentindex')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, "studentapp/studprofile.html", {"form": form})


def studexam(request):
    return render(request, "studentapp/studexam.html")


def studnotes(request):
    return render(request, "studentapp/studnotes.html")


def studprogressre(request):
    return render(request, "studentapp/studprogressre.html")


def viewtrainers(request):
    return render(request, "traineeapp/viewtrainers.html")


def all_traineeleave(request):
    return render(request, "traineeapp/all_traineeleave.html")


def traineeleave(request):
    return render(request, "traineeapp/traineeleave.html")


def traineefeedback(request):
    return render(request, "traineeapp/traineefeedback.html")


def traineevideo(request):
    return render(request, "traineeapp/traineevideo.html")


def all_traineecomplaints(request):
    return render(request, "traineeapp/all_traineecomplaints.html")


def traineecomplaints(request):
    return render(request, "traineeapp/traineecomplaints.html")


def viewinterview(request):
    return render(request, "traineeapp/viewinterview.html")


def traineeprofile(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            print("values updated")
            return redirect('studentindex')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, "traineeapp/traineeprofile.html", {'form': form})


def trainee_exam(request):
    return render(request, "traineeapp/trainee_exam.html")


def trainee_notes(request):
    return render(request, "traineeapp/trainee_notes.html")


def trainee_report(request):
    return render(request, "traineeapp/trainee_report.html")


def allteacher_complaints(request):
    query = Complaint.objects.filter(user=request.user)
    print(query)
    return render(request, "teacherapp/allteacher_complaints.html", {"query": query})


def complaint_view(request):
    # form = ComplaintForm()
    return render(request, "teacherapp/teacher_complaints.html")


def teacherleave(request):
    title = 'Request Leave'
    data = Leaves.objects.filter(taken_by=request.user)
    if request.method == 'POST':
        form = LeavesForm(request.POST)
        if form.is_valid():
            leave = form.save(commit=False)
            leave.taken_by = request.user
            leave.save()
            messages.success(request, 'Success')
            return redirect('request-leave')
    else:
        form = LeavesForm()

    return render(request, "teacherapp/teacherleave.html", {'form': form, 'title': title, 'list_data': data})


def allteacher_leave(request):
    return render(request, "teacherapp/allteacher_leave.html")


def teachernotes(request):
    return render(request, "teacherapp/teachernotes.html")


def allteacher_notes(request):
    return render(request, "teacherapp/allteacher_notes.html")


def teacherprofile(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            print("values updated")
            return redirect('studentindex')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, "teacherapp/teacherprofile.html", {'form': form})


def studfeedbacks(request):
    return render(request, "teacherapp/studfeedback.html")


def studleave(request):
    return render(request, "teacherapp/studleave.html")


def teachervideo(request):
    return render(request, "teacherapp/teachervideo.html")


def teacherstudent(request):
    query = ""
    try:
        sub = Teacher.objects.get(teacher=request.user)
        query = Students.objects.filter(standard=sub.subjects.subject_name)
        print("dd", sub)
        print("ee", query)
    except Exception as e:
        print("Exception", e)
    return render(request, "teacherapp/teacherstudent.html", {"query": query})


def teacherleavereq(request):
    return render(request, "hodapp/teacherleavereq.html")


def trainerleavereq(request):
    return render(request, "hodapp/trainerleavereq.html")


def traineeleavereq(request):
    return render(request, "hodapp/traineeleavereq.html")


def studentleavereq(request):
    return render(request, "hodapp/studentleavereq.html")


def studentcomp(request):
    return render(request, "hodapp/studentcomp.html")


def trainercomp(request):
    return render(request, "hodapp/trainercomp.html")


def traineecomp(request):
    return render(request, "hodapp/traineecomp.html")


def hodprofile(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            print("values updated")
            return redirect('studentindex')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, "hodapp/hodprofile.html", {'form': form})


def hodinterview(request):
    return render(request, "hodapp/hodinterview.html")


def viewexam(request):
    return render(request, "hodapp/viewexam.html")


def viewnotes(request):
    return render(request, "hodapp/viewnotes.html")


def viewstureport(request):
    return render(request, "hodapp/viewstureport.html")


def hodvideo(request):
    return render(request, "hodapp/.html")


def studentscomp(request):
    return render(request, "adminapp/studentscomp.html")


def traineescomp(request):
    return render(request, "adminapp/traineescomp.html")


def teacherscomp(request):
    return render(request, "adminapp/teacherscomp.html")


def trianerscomp(request):
    return render(request, "adminapp/trianerscomp.html")


def trainerindex(request):
    return render(request, "trainerapp/trainerindex.html")


def alltrainer_complaints(request):
    return render(request, "trainerapp/alltrainer_complaints.html")


def trainer_complaints(request):
    return render(request, "trainerapp/trainer_complaints.html")


def trainerleave(request):
    return render(request, "trainerapp/trainerleave.html")


def alltrainer_leave(request):
    return render(request, "trainerapp/alltrainer_leave.html")


def alltrainer_exam(request):
    return render(request, "trainerapp/alltrainer_exam.html")


def trainerexam(request):
    return render(request, "trainerapp/trainerexam.html")


def trainernotes(request):
    return render(request, "trainerapp/trainernotes.html")


def alltrainer_notes(request):
    return render(request, "trainerapp/alltrainer_notes.html")


def alltrainer_report(request):
    return render(request, "trainerapp/alltrainer_report.html")


def traineereport(request):
    return render(request, "trainerapp/traineereport.html")


def trainerprofile(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            print("values updated")
            return redirect('studentindex')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, "trainerapp/trainerprofile.html", {'form': form})


def traineefeedback(request):
    return render(request, "trainerapp/traineefeedback.html")


def trainee_leave(request):
    return render(request, "trainerapp/trainee_leave.html")


def trainervideo(request):
    return render(request, "trainerapp/trainervideo.html")


def trainerstudent(request):
    query = ''
    try:
        train = Trainers.objects.get(trainer_name=request.user)
        train_course = train.course.course_name
        query = Trainees.objects.filter(course__course_name=train_course)
    except Exception as e:
        print("Exception", e)

    return render(request, "trainerapp/trainerstudent.html", {"query": query})


def hod_salary_details(request):
    return render(request, "adminapp/hod_salary_details.html")


def email_logins(request):
    print("inside email login")
    if request.method != "POST":
        form = LoginForm()
        print("no post")
        return render(request, 'publicapp/login.html', {"form": form})
    else:
        print("post")
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            print("email,pass", email, password)
            user = EmailBackEnd.authenticate(request, username=request.POST.get('email'),
                                             password=request.POST.get('password'))
            print("user", user)
            if user != None:
                login(request, user)
                user_type = user.user_type
                print(user_type)
                if request.user.is_superuser:
                    return redirect('admindex')
                if user_type == '1':
                    return redirect('hodindex')
                elif user_type == '2':
                    return redirect('teacherindex')

                elif user_type == '3':
                    return redirect('studentindex')
                elif user_type == '4':
                    return redirect('traineeindex')
                elif user_type == '5':
                    return redirect('traineeindex')
                else:
                    messages.error(request, "Invalid Login!")
                    return redirect('login')
            else:
                messages.error(request, "Invalid Login Credentials!")
                print("invalid credentials")
                return redirect('email_login')
        else:
            print("not valid")
            messages.error(request, "Invalid Login Credentials!")

    return render(request, 'publicapp/login.html', {"form": form})


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            print("values updated")
            return redirect('studentindex')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'accounts/change_password.html', {
        'form': form
    })


#
# def complaint_view(request):
#     form = ComplaintForm()
#     return render(request, "teacherapp/teacher_complaints.html",{"form":form})

def teacher_complaints(request):
    if request.method == "POST":
        try:
            complaint = request.POST.get('admin_hod')
            complaints_description = request.POST.get('complaints_description')
            # ((1, "HOD"), (2, "TEACHER"), (3, "STUDENT"), (4, "TRAINER"), (5, "TRAINEE"))
            department = None
            if request.user.user_type_data == 2:
                dep = Teacher.objects.get(teacher=request.user)
                department = dep.department
            elif request.user.user_type_data == 3:
                dep = Students.objects.get(student_name=request.user)
                department = dep.standard
            elif request.user.user_type_data == 4:
                dep = Trainers.objects.get(trainer_name=request.user)
                department = dep.department
            # elif request.user.is_superuser:
            #     department="ADMIN"
            # else:
            #     dep = Trainees.objects.get(trainee=request.user)
            #     department = dep.department

            obj = Complaint()
            obj.user = request.user
            obj.to = complaint
            obj.complaint = complaints_description
            obj.department = department
            obj.save()
            return redirect("allteacher_complaints")
        except:
            pass


    else:
        print("else")
    return render(request, "teacherapp/teacher_complaints.html")


def teachercomp(request):
    if request.user.is_superuser:
        query = Complaint.objects.filter(to="ADMIN")
        # ((1, "HOD"), (2, "TEACHER"), (3, "STUDENT"), (4, "TRAINER"), (5, "TRAINEE"))
    else:
        hod = Hods.objects.get(hod=request.user)
        department = hod.department

        query = Complaint.objects.filter(to="HOD", department=department).order_by('-id')

    return render(request, "hodapp/teachercomp.html", {"query": query})


def add_reply(request, id):
    print("id", id)
    dep = Hods.objects.get(hod=request.user)
    department = dep.department
    if request.method == "POST":
        reply = request.POST.get('complaints_description')
        print("re", reply)
        obj = Complaint.objects.get(id=id)
        obj.response = reply
        obj.save()

        return redirect('teachercomp')
    else:
        pass
    return render(request, "hodapp/add_replies.html")


def teacherexam(request):
    form = ExamForm(request.POST)
    if form.is_valid():
        exam_name = request.POST["exam_name"]
        conducted_on = request.POST["conducted_on"]
        max_time = request.POST["max_time"]
        time = request.POST["time"]
        max_score = request.POST["max_score"]
        subject = request.POST["subject"]
        course = request.POST["course"]
        print(course)
        print(subject)

        stu = Exam(exam_name=exam_name, conducted_on=conducted_on, conducted_by=request.user, time=time,
                   max_time=max_time, max_score=max_score, subject_id=subject, course_id=course)

        stu.save()
        return redirect('teacherindex')
    return render(request, "teacherapp/teacherexam.html", {'form': form})


def allteacher_exam(request):
    query_set = Exam.objects.all()
    return render(request, "teacherapp/allteacher_exam.html", {'query_set': query_set})


def teacherexamsave(request):
    return render(request, "teacherapp/teacherexam.html")


def allteacher_report(request):
    query_set = Result.objects.all()
    return render(request, "teacherapp/allteacher_report.html", {'queryset': query_set})


def studreport(request):
    form = ResultForm(request.POST)
    if form.is_valid():
        exam = request.POST["exam"]
        attended_by = request.POST["attended_by"]
        mark = request.POST["mark"]
        date = request.POST["date"]
        grade = request.POST["grade"]
        status = request.POST["status"]

        stu = Result(exam_id=exam, attended_by_id=attended_by, mark=mark, date=date,
                     grade=grade, status=status)

        stu.save()
        return redirect('teacherindex')
    return render(request, "teacherapp/studreport.html", {'form': form})


def time_table_view(request, teacher_type):
    time_table = generate_timetable(request.user)
    print(time_table, '*' * 100)
    if teacher_type == 'teacher':
        title = "Teacher's Time Table"
        time_table = time_table.filter(teacher__user_type__in=[2, 'TEACHER'])
    elif teacher_type == 'trainer':
        title = "Trainer's Time Table"
        time_table = time_table.filter(teacher__user_type=['TRAINER', 4])
    else:
        title = "Time Table"
        time_table = time_table.filter(teacher__user_type__in=['TEACHER', 'TRAINER', 2, 4])

    return render(request, 'hodapp/time-table.html', {'time_table': time_table, 'title': title})


def studfeedback(request):
    if request.method == "POST":
        try:
            feedback_to = request.POST.get('email')
            feedback_description = request.POST.get('feedback')
            # ((1, "HOD"), (2, "TEACHER"), (3, "STUDENT"), (4, "TRAINER"), (5, "TRAINEE"))
            # department = None
            # if request.user.user_type_data == 2:
            #     dep = Teacher.objects.get(teacher=request.user)
            #     department = dep.department
            # elif request.user.user_type_data == 3:
            #     dep = Students.objects.get(student_name=request.user)
            #     department = dep.standard
            # elif request.user.user_type_data == 4:
            #     dep = Trainers.objects.get(trainer_name=request.user)
            #     department = dep.department
            if Teacher.objects.filter(teacher__email=feedback_to).count() > 0:
                print("d")

                print("ggg", feedback_to)
                print("dddd", feedback_description)
                obj = Feedback()
                obj.user = request.user
                obj.email = feedback_to
                obj.feedback = feedback_description
                obj.save()
                try:
                    student = Students.objects.get(student_name=request.user)
                    contacts = student.mobile_num
                    from django.core.mail import send_mail
                    subject = "Feedback From Student"
                    message = feedback_description + " by " + " \n" + request.user.username + ", \n" + contacts
                    email_from = settings.EMAIL_HOST_USER
                    send_mail(subject, message, email_from, [feedback_to, ])
                except:
                    print("mail send error")
                    pass
                return redirect("studentindex")
            else:
                print("ddddd")
                messages.error(request, 'Please Enter a valid teacher Email.')
                return render(request, "studentapp/feedback.html")
        except:
            pass


    else:
        print("else")
    return render(request, "studentapp/feedback.html")


def request_leave(request):
    title = 'Request Leave'
    data = Leaves.objects.filter(taken_by=request.user)
    if request.method == 'POST':
        form = LeavesForm(request.POST)
        if form.is_valid():
            leave = form.save(commit=False)
            leave.taken_by = request.user
            leave.save()
            messages.success(request, 'Success')
            return redirect('request_leave')
    else:
        form = LeavesForm()
    return render(request, 'adminapp/addleave.html', {'form': form, 'title': title, 'list_data': data})


def hod_leave_request_list(request):
    title = 'Hod Leave Requests'
    list_data = Leaves.objects.filter(taken_by__user_type=1, status='pending')
    approved = Leaves.objects.filter(taken_by__user_type=1, status='approved')
    rejected = Leaves.objects.filter(taken_by__user_type=1, status='rejected')
    context = {'title': title, 'list_data': list_data, 'approved': approved, 'rejected': rejected}
    return render(request, 'adminapp/leave_list.html', context)


def leavereq(request):
    if request.user.is_superuser:
        return redirect('hod_leave_request_list')


def teacher_leave_request_list(request):
    title = 'Teacher Leave Requests'
    list_data = Leaves.objects.filter(taken_by__user_type=2, status='pending')
    approved = Leaves.objects.filter(taken_by__user_type=2, status='approved')
    rejected = Leaves.objects.filter(taken_by__user_type=2, status='rejected')
    context = {'title': title, 'list_data': list_data, 'approved': approved, 'rejected': rejected}
    return render(request, 'adminapp/leave_list.html', context)


def student_leave_request_list(request):
    title = 'Student Leave Requests'
    list_data = Leaves.objects.filter(taken_by__user_type=3, status='pending')
    approved = Leaves.objects.filter(taken_by__user_type=3, status='approved')
    rejected = Leaves.objects.filter(taken_by__user_type=3, status='rejected')
    return render(request, 'adminapp/leave_list.html',
                  {'title': title, 'list_data': list_data, 'approved': approved, 'rejected': rejected})


def trainee_leave_request_list(request):
    title = 'Trainee Leave Requests'
    list_data = Leaves.objects.filter(taken_by__user_type=5, status='pending')
    approved = Leaves.objects.filter(taken_by__user_type=5, status='approved')
    rejected = Leaves.objects.filter(taken_by__user_type=5, status='rejected')
    return render(request, 'adminapp/leave_list.html',
                  {'title': title, 'list_data': list_data, 'approved': approved, 'rejected': rejected})


def trainer_leave_request_list(request):
    title = 'Trainer Leave Requests'
    list_data = Leaves.objects.filter(taken_by__user_type=4, status='pending')
    approved = Leaves.objects.filter(taken_by__user_type=4, status='approved')
    rejected = Leaves.objects.filter(taken_by__user_type=4, status='rejected')
    return render(request, 'adminapp/leave_list.html',
                  {'title': title, 'list_data': list_data, 'approved': approved, 'rejected': rejected})


@login_required

def approve_leave_request(request, obj_id):
    try:
        leave = Leaves.objects.get(id=obj_id)
    except Leaves.DoesNotExist:
        return HttpResponseNotFound('Not Found')
    else:
        leave.status = 'approved'
        leave.save()
        messages.success(request, 'Leave Approved')
        if leave.taken_by.user_type == 1:
            url = redirect('hod_leave_request_list')
        elif leave.taken_by.user_type == 2:
            url = redirect('teacher_leave_request_list')
        elif leave.taken_by.user_type == 3:
            url = redirect('student_leave_request_list')
        elif leave.taken_by.user_type == 4:
            url = redirect('trainer_leave_request_list')
        else:
            url = redirect('trainee_leave_request_list')
        return url


@login_required
def reject_leave_request(request, obj_id):
    try:
        leave = Leaves.objects.get(id=obj_id)
    except Leaves.DoesNotExist:
        return HttpResponseNotFound('Not Found')
    else:
        leave.status = 'rejected'
        leave.save()
        messages.error(request, 'Leave Rejected')
        if leave.taken_by.user_type == 1:
            url = redirect('hod_leave_request_list')
        elif leave.taken_by.user_type == 2:
            url = redirect('teacher_leave_request_list')
        elif leave.taken_by.user_type == 3:
            url = redirect('student_leave_request_list')
        elif leave.taken_by.user_type == 4:
            url = redirect('trainer_leave_request_list')
        else:
            url = redirect('trainee_leave_request_list')
        return url
