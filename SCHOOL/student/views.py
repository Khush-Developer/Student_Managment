from django.shortcuts import render,redirect
from . models import *
from django.contrib import messages
from django.contrib.auth.hashers import make_password,check_password
from django.db.models import Q
 
def index(request):
    return render(request,'index.html')

def courses(request):
    course = Addcourse.objects.filter(is_active=True).order_by('id')
    return render(request,'courses.html',{'request':request,'course':course})

def dashboard(request):
    return render(request,'dashboard.html')

def employess(request):
    return render(request,'employess.html')

def hostel_details(request):
    return render(request,'hostel_details.html')

def notification(request):
    return render(request,'notification.html')

def pd_dashboard(request):
    return render(request,'pd_dashboard.html')

def profile(request):
    return render(request,'profile.html')

def sign_up(request):
    return render(request,'sign_up.html')

def tables(request):
    return render(request,'tables.html')

def tenants(request):
    return render(request,'tenants.html')

def viewstudents(request):
    student=Addstudent.objects.all()
    addcourses = Addcourse.objects.all()
    return render(request,'viewstudents.html',{'student':student,'addcourses':addcourses})

def addcourses(request):
    if request.method == 'POST':
        c_name=request.POST['CourseName']
        c_fees=request.POST['CourseFees']
        c_duration=request.POST['Duration']
        c_desc=request.POST['CourseDesc']
        messages.success(request,'Course Added Successfully')
        Addcourse.objects.create(course = c_name, fees = c_fees, duration = c_duration, desc =c_desc)
        return redirect('/courses/')
    
def dltcourse(request,pk):
    Addcourse.objects.filter(id = pk).delete()
    return redirect('/courses/')

def update_course(request,uid):
    update=Addcourse.objects.get(id=uid)
    return render(request,'update_course.html',context={'student':update,})

def updatecourse_data(request):
    if request.method == "POST":
        uid = request.POST["uid"]
        c_name=request.POST['CourseName']
        c_fees=request.POST['CourseFees']
        c_duration=request.POST['Duration']
        c_desc=request.POST['CourseDesc']
        Addcourse.objects.filter(id=uid).update(course=c_name, fees=c_fees,
                                                 duration=c_duration,
                                                 desc=c_desc)
        return redirect("/courses/")

def login(request):
    if request.method =='POST':
        username = request.POST['email']
        user_password = request.POST['password']
        if Registration.objects.filter(email = username).exists():
            obj = Registration.objects.get(email = username)
            password = obj.password
            if check_password(user_password,password):
                return redirect('/dashboard/')
            else:
                messages.error(request,'password is incorrect')
                return redirect('/')
        else:
            messages.error(request,'email is not registered')
            return redirect('/')
        

def registration(request):
    if request.method == 'POST':
        name=request.POST['name']
        email=request.POST['email']
        password=make_password(request.POST['password'])
        if Registration.objects.filter(email = email).exists():
             messages.error(request,'email already exist.')
             return redirect('/sign_up/')
        else:
            Registration.objects.create(name = name,email = email, password = password)
            messages.success(request,'registration successful')
            return redirect('/')
        
def addstudent(request):
    if request.method=='POST': 
        s_name=request.POST.get('name')
        s_email=request.POST.get('email')
        s_mobile=request.POST.get('mobile')
        s_college=request.POST.get('college')
        s_degree=request.POST.get('degree')
        s_addcourse_id = request.POST.get('course')
        s_course=Addcourse.objects.get(id=s_addcourse_id)
        if Addstudent.objects.filter(semail=s_email).exists():
            messages.error(request,'email already exists')
            return redirect('/addstudents/')
        elif Addstudent.objects.filter(smobile = s_mobile).exists():
            messages.error(request,'mobile no is already exists')
            return redirect('/addstudents/')
        else:
            Addstudent.objects.create(sname=s_name,
                                      semail=s_email,
                                      smobile=s_mobile,
                                      scollege=s_college,
                                      sdegree=s_degree,
                                      scourses = s_course,
                                     )
            messages.success(request,'student added successfully')
            student = Addstudent.objects.all()
            addcourses = Addcourse.objects.all()
            return render(request, 'viewstudents.html', {'student': student, 'addcourses': addcourses,})
    else:
        student = Addstudent.objects.all()
        addcourses = Addcourse.objects.all()
        return render(request,'viewstudents.html',{'student': student, 'addcourses': addcourses}) 


def search(request):
    if 'q' in request.GET:
        q = request.GET['q']
        multiple_q = Q(Q(sname__icontains = q) | Q(semail__icontains = q)) |Q(smobile__icontains = q)
        student = Addstudent.objects.filter(multiple_q)
    else:
        student = Addstudent.objects.all()
    context = {'student':student}
    return render(request,'viewstudents.html',context)
