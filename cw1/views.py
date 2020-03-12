from django.shortcuts import render
from django.shortcuts import HttpResponse, redirect, render
from .models import User, Rate, Module
import json
from django.db.models import Avg,Sum
# Create your views here.
def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user_exist = User.objects.filter(name=username).first()
        if user_exist:
            # return render(request, 'index.html')
            status = -1
            # return HttpResponse('The user name already exists, please go to the login page!')
        else:
            email = request.POST.get('email')
            user = User()
            user.name = username
            user.password = password
            user.email = email
            user.save()
            status = 0
        data = {
            "status": status
        }
        data = json.dumps(data)
        return HttpResponse(data)
        # return HttpResponse(username + ' is register successfully')
            # return render(request, 'home.html')
    else:
        return render(request, 'register.html')


def home(request):
    pass
    return render(request, 'home.html')


def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        # return redirect('/index/')
        user_exist = User.objects.filter(name=username)
        if user_exist:
            user = user_exist.first()
            true_password = user.password
            if password == true_password:
                status = 0
            else:
                status = -1
        else:
            status = -2
        data = {
            "status":status
        }
        data = json.dumps(data)
        return HttpResponse(data)
        #return render(request, 'home.html')
    #return render(request, 'login.html')


# def logout(request):
# pass
# return redirect('/index/')
def index(request):
    pass
    return render(request, 'index.html')


def rate(request):
    if request.method == 'POST':
        student_name =request.POST.get('student_name')
        code = request.POST.get('code')
        name = request.POST.get('name')
        year = request.POST.get('year')
        semester = request.POST.get('semester')
        teacher = request.POST.get('teacher')
        score = request.POST.get('score')

        rate = Rate()
        rate.code = code
        rate.name = name
        rate.year = year
        rate.semester = semester
        rate.teacher = teacher
        rate.score = score
        try:
            rate.save()
            status = 0
        except:
            status = -1
        data = {
            "status":status
        }
        data= json.dumps(data)
        return HttpResponse(data)


def list_(request):
    if request.method == 'GET':
        code_get = request.GET.get('code')
        year_get = request.GET.get('year')
        semester_get = request.GET.get('semester')
        modules = Module.objects.all()
        dict = {}
        for module in modules:
            key = module.code + '_' + module.year + '_' + module.semester + '_' + module.name
            if key in dict:
                value = dict[key] + ',' + module.teacher
                dict[key] = value
            else:
                # key = module.code + '_' + module.year + '_' + module.semester + '_' + module.name
                dict[key] = module.teacher
        result = []
        for key,value in dict.items():
            key_list = key.split('_')
            code = key_list[0]
            year = key_list[1]
            semester = key_list[2]
            name = key_list[3]
            teachers = value
            if code_get != '' and code_get !=code:
                continue
            if year_get != '' and year_get != year:
                continue
            if semester_get != '' and semester_get != semester:
                continue
            message = {
                'Code':code,
                'Name': name,
                'Year':year,
                'Semester':semester,

                'Taught_by':teachers
            }
            result.append(message)
        data = {
            'result':result,
            'state':1,
        }
        all = json.dumps(data)
        print(dict, dict.values())
        return HttpResponse(all)


def view(request):
    teacher_get = request.GET.get("teacher_id")
    teacher_score = Rate.objects.all().values("teacher").annotate(averageScore=Avg("score"))
    print(teacher_score)
    data = []
    for each_teacher in teacher_score:
        print (each_teacher)
        print(each_teacher['teacher'], each_teacher['averageScore'])
        dict_ = {}
        teacher_id = each_teacher['teacher']
        if teacher_get != '' and teacher_id != teacher_get:
            continue
        averageScore = each_teacher['averageScore']
        averageScore = round(averageScore+0.0000000000001)
        dict_['teacher_id'] = teacher_id
        dict_['averageScore'] = averageScore
        data.append(dict_)
    result = {
        'data': data,
        'state': 1,
    }
    all = json.dumps(result)
    return HttpResponse(all)


def average(request):
    if request.method == 'GET':
        teacher_get = request.GET.get('teacher_id')
        code_get = request.GET.get('code')
        average_score = Rate.objects.all().values("teacher","code").annotate(averageScore=Avg("score"))
        print(average_score)
        data = []
        for each_teacher in average_score:
            print(each_teacher)
            print(each_teacher['teacher'], each_teacher['averageScore'])
            dict_ = {}
            teacher_id = each_teacher['teacher']
            code = each_teacher['code']
            if teacher_get != '' and teacher_get !=teacher_id:
                continue
            if code_get != '' and code != code_get:
                continue
            averageScore = each_teacher['averageScore']
            averageScore = round(averageScore + 0.0000000000001)
            dict_['teacher_id'] = teacher_id
            dict_['code'] = code
            dict_['averageScore'] = averageScore
            data.append(dict_)
        result = {
            'data': data,
            'state': 1,
        }
        all = json.dumps(result)
        return HttpResponse(all)

def re_password(request):
    if request.method == "POST":
        username = request.POST.get('username')
        old_password = request.POST.get('old_password')
        new_password = request.POST.get('new_password')
        re_new_password = request.POST.get('re_new_password')
        # return redirect('/index/')
        user_exist = User.objects.filter(name=username)
        if user_exist:
            user = user_exist.first()
            true_password = user.password
            if old_password == true_password:
                if new_password == re_new_password:
                    user.password = new_password
                    user.save()
                    status = 0
                else:
                    status = -2
            else:
                status = -1
        else:
            status = -3
        data = {
            "status": status
        }
        data = json.dumps(data)
        return HttpResponse(data)
