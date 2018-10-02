from django.contrib import admin
from django.urls import path

from MyApp.views import LoginView, AddUserView, LogoutView, CategoriesView, TasksView, MessageView
from MyApp.views import DeleteCategoriesView, EditCategoriesView, DetailCategoriesView, ArchivesView, DeleteTaskView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view(), name='login-view'),
    path('adduser/', AddUserView.as_view(), name='adduser-view'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('categories/', CategoriesView.as_view(), name='categories-view'),
    path('editcategories/<int:category_id>', EditCategoriesView.as_view(), name='edit-categories-view'),
    path('deletecategories/<int:category_id>', DeleteCategoriesView.as_view(), name='delete-categories-view'),
    path('detailcategories/<int:category_id>', DetailCategoriesView.as_view(), name='detail-categories-view'),
    path('tasks/', TasksView.as_view(), name='tasks-view'),
    path('deletetask/<int:task_id>', DeleteTaskView.as_view(), name='delete-task-view'),
    path('message/', MessageView.as_view(), name='message-view'),
    path('archives/', ArchivesView.as_view(), name='archives-view'),

]
