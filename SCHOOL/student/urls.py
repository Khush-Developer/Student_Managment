from django.urls import path
from .import views

urlpatterns = [
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
