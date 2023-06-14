from django.urls import path,include
from .import views
from student.api import *

urlpatterns = [
    
    # create  course api urls
    path('apishowcourse/',CourseViewSet.as_view()),
    path('apicourse/create',CreatecourseViewSet.as_view()),
    path('apicourse/update/<int:pk>',UpdatecourseViewSet.as_view()),
    path('apicourse/delete/<int:pk>',DeletecourseViewSet.as_view()),

    # create  addstudent api urls
    path('apistudent/show',ShowStudentViewSet.as_view()),
    path('apistudent/create',CreatestudentViewSet.as_view()),
    path('apistudent/update/<int:pk>',UpdatestudentiewSet.as_view()),
    path('apistudent/delete/<int:pk>',DeletestudentViewSet.as_view()),

    # project urls
    path('',views.index),
    path('courses/',views.courses),
    path('dashboard/',views.dashboard),
    path('employees/',views.employess),
    path('sign_up/',views.sign_up),
    path('tables/',views.tables),
    path('viewstudents/',views.viewstudents),
    path('addcourses/',views.addcourses),
    path('registration/',views.registration),
    path('addstudent/',views.addstudent),
    path('login/',views.login),
    path('search/',views.search),
    path('dltcourse/<pk>',views.dltcourse),
    path("update_course/<int:uid>/",views.update_course),
    path("updatecourse_data/",views.updatecourse_data),
]
