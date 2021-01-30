from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash

from .EmailBackend import EmailBackEnd
from .forms import subjectsForm, commontimetableForm, salaryForm, teacherregForm, LoginForm, TraineeRegForm, \
    trainerregForm
from .models import hod, salary, teacherreg, student, CustomUser, Students, Trainees, Hods, Teacher, Trainers


# Create your views here.


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


def test_salary(request, id=None):
    print(id)

    form = salaryForm(request.POST,id)
    print("called")
    if form.is_valid():
        instance = form.save()
        print(instance)
        form.save()

        return render(request, 'adminapp/hod_salary.html', {"form": form})
    # month = request.POST["month"]
    # salaryamount = request.POST["salaryamount"]
    # paymentstatus = request.POST["paymentstatus"]
    # pendingsalary = request.POST["pendingsalary"]
    #
    # alldata = salary(month=month, salaryamount=salaryamount, paymentstatus=paymentstatus, pendingsalary=pendingsalary)
    # alldata.save()

    print("aswin")
    i = salary.objects.all()
    for q in i:
        print(q)
    return render(request, 'adminapp/hod_salary.html', {"form": form})


def hod_test_salary(request, id=None):
    print("aswin")
    print(id)
    month = request.POST.get('month', None)
    salaryamount = request.POST.get('salaryamount', None)
    paymentstatus = request.POST.get("paymentstatus", None)
    pendingsalary = request.POST.get("pendingsalary", None)
    # alldata= salary(month=month,salaryamount=salaryamount,paymentstatus=paymentstatus,pendingsalary=pendingsalary,hod_id_id=id)
    # alldata.save()
    return render(request, 'test1.html', {"id": id})


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
        student.standard = course
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






def courses(request):
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


def courseadd(request):
    return render(request, "adminapp/courseadd.html")


def all_course(request):
    return render(request, "adminapp/all_course.html")


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
        # send_mail(subject, message, email_from, [email, ])


    return render(request, "adminapp/add_trainer.html", {"form": form})




def all_subjects(request):
    return render(request, "adminapp/all_subjects.html")


def subjectadd(request):
    all_teachers = teacherreg.objects.all()
    form = subjectsForm(request.POST)
    if form.is_valid():
        instance = form.save()
        print(instance)
        form.save()
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


def interplacement(request):
    return render(request, "adminapp/interplacement.html")


def all_interview(request):
    return render(request, "adminapp/all_interview.html")


def all_videos(request):
    return render(request, "adminapp/all_videos.html")


def recordvideos(request):
    return render(request, "adminapp/recordvideos.html")


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

    return render(request, "publicapp/retrainer.html", {'form': form})


def hodteacher(request):
    return render(request, "hodapp/hodteacher.html")


def hodtrainer(request):
    return render(request, "hodapp/hodtrainer.html")


def hodstudent(request):
    return render(request, "hodapp/hodstudent.html")


def hodtrainee(request):
    return render(request, "hodapp/hodtrainee.html")


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


def studcomplaints(request):
    return render(request, "studentapp/studcomplaints.html")


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
    return render(request, "teacherapp/allteacher_complaints.html")


def teacher_complaints(request):
    return render(request, "teacherapp/teacher_complaints.html")


def teacherleave(request):
    return render(request, "teacherapp/teacherleave.html")


def allteacher_leave(request):
    return render(request, "teacherapp/allteacher_leave.html")


def allteacher_exam(request):
    return render(request, "teacherapp/allteacher_exam.html")


def teacherexam(request):
    return render(request, "teacherapp/teacherexam.html")


def teachernotes(request):
    return render(request, "teacherapp/teachernotes.html")


def allteacher_notes(request):
    return render(request, "teacherapp/allteacher_notes.html")


def allteacher_report(request):
    return render(request, "teacherapp/allteacher_report.html")


def studreport(request):
    return render(request, "teacherapp/studreport.html")


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


def studfeedback(request):
    return render(request, "teacherapp/studfeedback.html")


def studleave(request):
    return render(request, "teacherapp/studleave.html")


def teachervideo(request):
    return render(request, "teacherapp/teachervideo.html")


def teacherstudent(request):
    return render(request, "teacherapp/teacherstudent.html")


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


def teachercomp(request):
    return render(request, "hodapp/teachercomp.html")


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
    return render(request, "trainerapp/trainerstudent.html")


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
            print("email,pass",email,password)
            user = EmailBackEnd.authenticate(request, username=request.POST.get('email'),
                                             password=request.POST.get('password'))
            print("user",user)
            if user != None:
                login(request, user)
                user_type = user.user_type
                print(user_type)
                if request.user.is_superuser:
                    return redirect('admindex')
                if user_type == '1':
                    return redirect('hodindex')
                elif user_type == '2':
                    return redirect('teacher_home')

                elif user_type == '3':
                    return redirect('studentindex')
                elif user_type == '4':
                    return redirect('trainer_home')
                elif user_type == '5':
                    return redirect('trainee_home')
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

    return render(request,'publicapp/login.html',{"form":form})


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
