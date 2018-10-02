from datetime import date, datetime, timedelta, timezone

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User

from .forms import MessageForm
from .models import Task, Categories, PRIORITY, MyMessage


class LoginView(View):

    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        loginuser = request.POST['login']
        passworduser = request.POST['password']
        last_log = User.objects.filter(username=request.user)
        tasks = Task.objects.filter(create_user=request.user.id).order_by('deadline')


        if loginuser and passworduser:
            user = authenticate(username=loginuser, password=passworduser)

            if user is not None:
                login(request, user)
                last_loggin = request.user.accessdata.last_access
                print(last_loggin)
                my_time = datetime.now()
                print(my_time)
                check = request.user.last_login
                print(check)
                check = check.strftime("%Y, %B, %D, %H, %M, %S")
                print(check)

                return render(request, 'main.html', {'last_log': last_log,
                                                     'tasks': tasks})
            else:
                return HttpResponse('bad pass or login')
        else:
            return redirect('login-view')


class LastAccessMixin(object):
    def dispatch(self, request):
        if request.user.is_authenticated():
            request.user.accessdata.last_access = timezone.now()
            request.user.accessdata.save(update_fields=['last_access'])
        return super(LastAccessMixin, self).dispatch(request)

class LogoutView(LastAccessMixin, View):
    def get(self, request):
        logout(request)
        return redirect('login-view')


class AddUserView(View):

    def get(self, request):
        return render(request, 'sign.html')

    def post(self, request):
        loginuser = request.POST['login']
        passworduser = request.POST['password']
        emailuser = request.POST['email']
        if loginuser and passworduser and emailuser:
            User.objects.create_user(username=loginuser, password=passworduser, email=emailuser)

            return redirect('login-view')
        else:
            return redirect('adduser-view')


class CategoriesView(View):

    def get(self, request):
        user = request.user
        compare_date = date.today()
        if user.is_authenticated:

            categories = Categories.objects.filter(owner=user)
            tasks = Task.objects.filter(create_user=request.user.id).order_by('deadline').filter(deadline__range=[compare_date,
                                                                                                          '2020-01-01'])

            return render(request, 'categories.html', {
                'categories': categories,
                'tasks': tasks
            })

    def post(self, request):
        name = request.POST['name']
        owner = request.user
        categories = Categories.objects.all()
        if name:
            Categories.objects.create(name=name, owner=owner)
        return redirect('categories-view')


class EditCategoriesView(View):

    def get(self, request, category_id):
        category = Categories.objects.get(id=category_id)
        return render(request, 'editcategories.html', {'category': category})


    def post(self, request, category_id):
        category = Categories.objects.get(id=category_id)
        name = request.POST['name']
        category.name = name
        category.save()
        return redirect('categories-view')

class DeleteCategoriesView(View):
    def get(self, request, category_id):
            category = Categories.objects.get(id=category_id)
            category.delete()
            return redirect('categories-view')


class DetailCategoriesView(View):
    def get(self, request, category_id):
        compare_date = date.today()
        tasks = Task.objects.filter(categorie__owner=request.user).filter(categorie__id=category_id).order_by('deadline').filter(deadline__range=[compare_date,
                                                                                                          '2020-01-01'])
        return render(request, 'detailscategories.html', {'tasks': tasks})


class TasksView(View):

    def get(self, request):
        user = request.user
        if user.is_authenticated:
            categories = Categories.objects.filter(owner=request.user.id)
            compare_date = date.today()
            tasks = Task.objects.filter(create_user=user.id).order_by('deadline').filter(deadline__range=[compare_date,
                                                                                                          '2020-01-01'])
            for t in tasks:
                print(date.today())
                print('zmiana')
                print(t.deadline)

                if t.deadline < date.today():
                    print('ok')
                    out = 0

            return render(request, 'tasks.html', {
                'categories': categories,
                'tasks': tasks,
                'PRIORITY': PRIORITY,

            })


    def post(self, request):
        name = request.POST['name']
        priority = request.POST.get('priority')
        categorie = request.POST.get('cat')
        deadline = request.POST['deadline']
        Task.objects.create(name=name, priority=priority, categorie_id=categorie,  deadline=deadline, create_user=request.user)
        return redirect('tasks-view')


class MessageView(View):

    def get(self, request):
        compare_date = date.today()

        messages = MyMessage.objects.filter(towho=request.user)
        tasks = Task.objects.filter(create_user=request.user.id).order_by('deadline').filter(deadline__range=[compare_date,
                                                                                                          '2020-01-01'])

        form = MessageForm()
        return render(request, 'messages.html', {'messages': messages,
                                                 'form': form,
                                                 'tasks': tasks })

    def post(self, request):
        messages = MyMessage.objects.filter(towho=request.user)
        form = MessageForm(request.POST)
        if form.is_valid():
            MyMessage.objects.create(fromwho=request.user,
                                     towho=form.cleaned_data['towho'],
                                     description=form.cleaned_data['description'])
            return redirect('message-view')


class ArchivesView(View):

    def get(self, request):
        user = request.user
        if user.is_authenticated:
            compare_date = date.today()
            categories = Categories.objects.filter(owner=request.user.id)
            tasks = Task.objects.filter(create_user=request.user).filter(deadline__range=['1990-01-01',compare_date])
            return render(request, 'archives.html', {
                'categories': categories,
                'tasks': tasks,
                'PRIORITY': PRIORITY,

            })


class DeleteTaskView(View):
    def get(self, request, task_id):
            task = Task.objects.get(id=task_id)
            task.delete()
            return redirect('tasks-view')


