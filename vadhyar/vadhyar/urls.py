from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path

from publicapp.views import *

if settings.DEBUG:
    urlpatterns = [
        path('admin/', admin.site.urls),
        url(r'^$', index, name='index'),
        url(r'^courseslist$', courseslist, name='courseslist'),
        url(r'^contact$', contact, name='contact'),
        url(r'^teachers$', teachers, name='teachers'),
        url(r'^tution$', tution, name='tution'),
        url(r'^aboutus$', aboutus, name='aboutus'),
        url(r'^civil$', civil, name='civil'),
        url(r'^cs$', cs, name='cs'),
        url(r'^mech$', mech, name='mech'),
        url(r'^ec$', ec, name='ec'),
        url(r'^studreg$', studreg, name='studreg'),
        url(r'^studentsave$', studentsave, name='studentsave'),
        url(r'^teacherregister$', teacherregister, name='teacherregister'),
        url(r'^us$', us, name='us'),
        url(r'^logintr$', logintr, name='logintr'),
        url(r'^loginh$', loginh, name='loginh'),
        url(r'^loginteach$', loginteach, name='loginteach'),
        url(r'^logintrainer$', logintrainer, name='logintrainer'),
        url(r'^loginadmin$', loginadmin, name='loginadmin'),
        url(r'^loginstud$', loginstud, name='loginstud'),
        url(r'^re$', re, name='re'),
        url(r'^admindex$', admindex, name='admindex'),
        url(r'^add_professor$', add_professor, name='add_professor'),
        url(r'^edit_professor$', edit_professor, name='edit_professor'),
        url(r'^professor_profile$', professor_profile, name='professor_profile'),
        url(r'^teacher_profile$', teacher_profile, name='teacher_profile'),
        url(r'^trainer_profile$', trainer_profile, name='trainer_profile'),
        url(r'^tution$', tution, name='tution'),
        url(r'^autocad$', autocad, name='autocad'),
        url(r'^ds$', ds, name='ds'),
        url(r'^revit$', revit, name='revit'),
        url(r'^googles$', googles, name='googles'),
        url(r'^stadd$', stadd, name='stadd'),
        url(r'^etab$', etab, name='etab'),
        url(r'^vray$', vray, name='vray'),
        url(r'^revitst$', revitst, name='revitst'),
        url(r'^navis$', navis, name='navis'),
        url(r'^prim$', prim, name='prim'),
        url(r'^autocadmech$', autocadmech, name='autocadmech'),
        url(r'^catia$', catia, name='catia'),
        url(r'^solid$', solid, name='solid'),
        url(r'^ansys$', ansys, name='ansys'),
        url(r'^nxcad$', nxcad, name='nxcad'),
        url(r'^nxcam$', nxcam, name='nxcam'),
        url(r'^nxnas$', nxnas, name='nxnas'),
        url(r'^revitmep$', revitmep, name='revitmep'),
        url(r'^prime$', prime, name='prime'),
        url(r'^autocadec$', autocadec, name='autocadec'),
        url(r'^ecrevit$', ecrevit, name='ecrevit'),
        url(r'^ecprim$', ecprim, name='ecprim'),
        url(r'^java$', java, name='java'),
        url(r'^web$', web, name='web'),
        url(r'^python$', python, name='python'),
        url(r'^tu$', tu, name='tu'),
        url(r'^viewteacher$', viewteacher, name='viewteacher'),
        url(r'^regteacher$', regteacher, name='regteacher'),
        url(r'^courseadd$', courseadd, name='courseadd'),
        url(r'^all_course$', all_course, name='all_course'),
        url(r'^add_teacher$', add_teacher, name='add_teacher'),
        url(r'^add_trainer$', add_trainer, name='add_trainer'),
        url(r'^all_subjects$', all_subjects, name='all_subjects'),
        url(r'^subjectadd$', subjectadd, name='subjectadd'),
        url(r'^interplacementadd$', interplacementadd, name='interplacementadd'),
        url(r'^all_interview$', all_interview, name='all_interview'),
        url(r'^all_videos$', all_videos, name='all_videos'),
        url(r'^recordvideos$', recordvideos, name='recordvideos'),
        url(r'^all_students$', all_students, name='all_students'),
        url(r'^studentfee$', studentfee, name='studentfee'),
        # url(r'^complaintss$', complaintss, name='complaintss'),
        url(r'^all_teachers$', all_teachers, name='all_teachers'),
        url(r'^all_hod$', all_hod, name='all_hod'),
        url(r'^all_trainers$', all_trainers, name='all_trainers'),
        url(r'^all_trainee$', all_trainee, name='all_trainee'),
        url(r'^hodindex$', hodindex, name='hodindex'),
        url(r'^retrainer$', retrainer, name='retrainer'),
        url(r'^hodteacher$', hodteacher, name='hodteacher'),
        url(r'^hodstudent$', hodstudent, name='hodstudent'),
        url(r'^hodtrainee$', hodtrainee, name='hodtrainee'),
        url(r'^hodtrainer$', hodtrainer, name='hodtrainer'),
        url(r'^allleave$', allleave, name='allleave'),
        url(r'^addleave$', addleave, name='addleave'),
        url(r'^teacherindex$', teacherindex, name='teacherindex'),
        url(r'^traineesave$', traineesave, name='traineesave'),
        url(r'^studentindex$', studentindex, name='studentindex'),
        url(r'^studleave$', studleave, name='studleave'),
        url(r'^feedback$', feedback, name='feedback'),
        url(r'^studcomplaints$', studcomplaints, name='studcomplaints'),
        url(r'^all_complaints$', all_complaints, name='all_complaints'),
        url(r'^all_leaves$', all_leaves, name='all_leaves'),
        url(r'^studvideo$', studvideo, name='studvideo'),
        url(r'^studprofile$', studprofile, name='studprofile'),
        url(r'^studexam$', studexam, name='studexam'),
        url(r'^studnotes$', studnotes, name='studnotes'),
        url(r'^studprogressre$', studprogressre, name='studprogressre'),
        url(r'^viewtrainers$', viewtrainers, name='viewtrainers'),
        url(r'^all_traineeleave$', all_traineeleave, name='all_traineeleave'),
        url(r'^traineeleave$', traineeleave, name='traineeleave'),
        url(r'^traineefeedback$', traineefeedback, name='traineefeedback'),
        url(r'^traineevideo$', traineevideo, name='traineevideo'),
        url(r'^all_traineecomplaints$', all_traineecomplaints, name='all_traineecomplaints'),
        url(r'^traineecomplaints$', traineecomplaints, name='traineecomplaints'),
        url(r'^viewinterview$', viewinterview, name='viewinterview'),
        url(r'^traineeprofile$', traineeprofile, name='traineeprofile'),
        url(r'^trainee_exam$', trainee_exam, name='trainee_exam'),
        url(r'^trainee_notes$', trainee_notes, name='trainee_notes'),
        url(r'^trainee_report$', trainee_report, name='trainee_report'),
        url(r'^allteacher_complaints$', allteacher_complaints, name='allteacher_complaints'),
        url(r'^teacher_complaints$', teacher_complaints, name='teacher_complaints'),
        url(r'^allteacher_leave$', allteacher_leave, name='allteacher_leave'),
        url(r'^teacherleave$', teacherleave, name='teacherleave'),
        url(r'^teacherexam$', teacherexam, name='teacherexam'),
        url(r'^allteacher_exam$', allteacher_exam, name='allteacher_exam'),
        url(r'^teachernotes$', teachernotes, name='teachernotes'),
        url(r'^allteacher_notes$', allteacher_notes, name='allteacher_notes'),
        url(r'^allteacher_report$', allteacher_report, name='allteacher_report'),
        url(r'^studreport$', studreport, name='studreport'),
        url(r'^teacherprofile$', teacherprofile, name='teacherprofile'),
        url(r'^studfeedback$', studfeedback, name='studfeedback'),
        url(r'^studfeedbacks$', studfeedbacks, name='studfeedbacks'),
        url(r'^studleave$', studleave, name='studleave'),
        url(r'^teachervideo$', teachervideo, name='teachervideo'),
        url(r'^teacherstudent$', teacherstudent, name='teacherstudent'),
        url(r'^teacherleavereq$', teacherleavereq, name='teacherleavereq'),
        url(r'^trainerleavereq$', trainerleavereq, name='trainerleavereq'),
        url(r'^traineeleavereq$', traineeleavereq, name='traineeleavereq'),
        url(r'^studentleavereq$', studentleavereq, name='studentleavereq'),
        url(r'^studentcomp$', studentcomp, name='studentcomp'),
        url(r'^traineecomp$', traineecomp, name='traineecomp'),
        url(r'^teachercomp$', teachercomp, name='teachercomp'),
        url(r'^trainercomp$', trainercomp, name='trainercomp'),
        url(r'^hodprofile$', hodprofile, name='hodprofile'),
        url(r'^hodinterview$', hodinterview, name='hodinterview'),
        url(r'^viewexam$', viewexam, name='viewexam'),
        url(r'^viewnotes$', viewnotes, name='viewnotes'),
        url(r'^viewstureport$', viewstureport, name='viewstureport'),
        url(r'^hodvideo$', hodvideo, name='hodvideo'),
        url(r'^studentscomp$', studentscomp, name='studentscomp'),
        url(r'^traineescomp$', traineescomp, name='traineescomp'),
        url(r'^teacherscomp$', teacherscomp, name='teacherscomp'),
        url(r'^trianerscomp$', trianerscomp, name='trianerscomp'),
        url(r'^alltrainer_complaints$', alltrainer_complaints, name='alltrainer_complaints'),
        url(r'^trainer_complaints$', trainer_complaints, name='trainer_complaints'),
        url(r'^alltrainer_leave$', alltrainer_leave, name='alltrainer_leave'),
        url(r'^trainerleave$', trainerleave, name='trainerleave'),
        url(r'^trainerexam$', trainerexam, name='trainerexam'),
        url(r'^alltrainer_exam$', alltrainer_exam, name='alltrainer_exam'),
        url(r'^trainernotes$', trainernotes, name='trainernotes'),
        url(r'^alltrainer_notes$', alltrainer_notes, name='alltrainer_notes'),
        url(r'^alltrainer_report$', alltrainer_report, name='alltrainer_report'),
        url(r'^traineereport$', traineereport, name='traineereport'),
        url(r'^trainerprofile$', trainerprofile, name='trainerprofile'),
        url(r'^traineefeedback$', traineefeedback, name='traineefeedback'),
        url(r'^trainee_leave$', trainee_leave, name='trainee_leave'),
        url(r'^trainervideo$', trainervideo, name='trainervideo'),
        url(r'^trainerstudent$', trainerstudent, name='trainerstudent'),
        url(r'^trainerindex$', trainerindex, name='trainerindex'),

        url(r'^hod_salary_details$', hod_salary_details, name='hod_salary_details'),

        url(r'^test_test$', test_test, name='test_test'),
        url(r'^hod_salary/(?P<id>\d+)/$', hod_salary, name='hod_salary'),
        url(r'^hod_salarys/(?P<id>\d+)/$', hod_salarys, name='hod_salarys'),
        url(r'^teacher_salary/(?P<id>\d+)/$', teacher_salary, name='teacher_salary'),
        url(r'^teacher_salarys/(?P<id>\d+)/$', teacher_salarys, name='teacher_salarys'),
        url(r'^trainer_salary/(?P<id>\d+)/$', trainer_salary, name='trainer_salary'),
        url(r'^trainee_fee/(?P<id>\d+)/$', trainee_fee, name='trainee_fee'),
        url(r'^student_fee/(?P<id>\d+)/$', student_fee, name='student_fee'),
        url(r'^view_hod$', view_hod, name='view_hod'),
        url(r'^view_teachers$', view_teachers, name='view_teachers'),
        url(r'^view_students$', view_students, name='view_students'),
        url(r'^test_teacher$', test_teacher, name='test_teacher'),
        url(r'^timetableadd$', timetableadd, name='timetableadd'),
        url(r'^traineeindex', traineeindex, name='traineeindex'),
        # url(r'^hod_test_salary/(?P<id>\d+)/$', hod_test_salary, name='hod_test_salary'),
        # url(r'^hod_details/(?P<id>\d+)/$', hod_details, name='hod_details'),
        url(r'^email_login$', email_logins, name='email_login'),
        url(r'^password/$', change_password, name='change_password'),
        path('logout/', auth_views.LogoutView.as_view()),
        path('complaints/', complaint_view, name="complaint_view"),
        path('all_notes/', all_notes, name="all_notes"),
        path('teacherexamsave/', teacherexamsave, name="teacherexamsave"),
        url(r'^request_leave', request_leave, name='request_leave'),
        url(r'^leavereq', leavereq, name='leavereq'),

        path('teacher_leave_request_list/', teacher_leave_request_list, name='teacher_leave_request_list'),
        path('student_leave_request_list/', student_leave_request_list, name='student_leave_request_list'),
        path('trainee_leave_request_list/', trainee_leave_request_list, name='trainee_leave_request_list'),
        path('trainer_leave_request_list/', trainer_leave_request_list, name='trainer_leave_request_list'),
        path('leave-request/<int:obj_id>/approve/', approve_leave_request, name='staff-leave-request-approve'),
        path('leave-request/<int:obj_id>/reject/', reject_leave_request, name='staff-leave-request-reject'),
        path('add_reply/<int:id>/', add_reply, name='add_reply'),
        path('time-table-view/<str:teacher_type>/', time_table_view, name="time-table-view"),

    ]
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
