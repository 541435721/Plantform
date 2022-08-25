from django.shortcuts import render
from django.http import HttpResponse
import django.contrib.auth as auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
import MicroApp.models as models
import Utils.file_op as file_op


# Create your views here.
def index(request):
    return user_login(request)
    # return render(request, 'index.html')


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        psd = request.POST.get('password')
        user = auth.authenticate(username=username, password=psd)
        if user is not None:
            auth.login(request, user)
            current_user = models.UserInfo.objects.get(User=user)
            current_user.UserLoginNum += 1
            current_user.save()
            return manager(request)
    return render(request, 'login_page.html')


def user_register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        psd = request.POST.get('password')
        confirm_psd = request.POST.get('confirm_password')
        if psd == confirm_psd:
            # todo 重名检查
            User.objects.create_user(username=username, password=psd)
            user = auth.authenticate(username=username, password=psd)
            new_user = models.UserInfo(User=user, UserName=user.username, UserType=1, UserLoginNum=0)
            new_user.save()
            if user is not None:
                auth.login(request, user)
                return manager(request)
    return render(request, 'reg_page.html')


@login_required
def logout(request):
    auth.logout(request)
    return render(request, 'login_page.html')


@login_required
def manager(request):
    user = request.user
    return render(request, 'manager_page/index.html', {'user': user})


@login_required
def detail(request):
    projects = models.Project.objects.all()
    return render(request, 'manager_page/index_v1.html', {'projects': projects})


@login_required
def create_proj(request):
    if request.method == 'POST':
        proj_name = request.POST.get('uid')
        proj_desc = request.POST.get('about')
        print(request.FILES['uploadfile'])
        user = models.UserInfo.objects.get(UserName='bbb')
        dst_path = file_op.organize_path(user.UserName, proj_name)
        file_op.handle_uploaded_file(request.FILES['uploadfile'], dst_path)

        # todo 写入数据库
        new_proj = models.Project.objects.create(ProjectName=proj_name, ProjectDesc=proj_desc, ProjectCreator=user,
                                                 ProjectStatus=0)
        new_proj.save()
        return detail(request)
    return render(request, 'manager_page/create_proj.html')


def chart(request):
    return render(request, 'manager_page/chart.html')


def testDB(request):
    # Create a new user
    username = 'test3'
    User.objects.create_user(username=username, password='aaa')  # 系统中创建用户
    user = auth.authenticate(username=username, password='aaa')
    print(user)
    # user_info = models.UserInfo(user=user)  # 创建用户表
    # user_info.save()
    return HttpResponse("Create User.")
