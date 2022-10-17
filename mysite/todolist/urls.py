from . import views
from django.urls import path
app_name = 'task'
urlpatterns = [
    path('',views.IndexClassView.as_view(), name='index'),
    path('<int:pk>',views.TaskDetail.as_view(),name='details'),
    # add task
    path('add', views.add , name="add"),
    # edit task
    path('edit/<int:id>' , views.edit , name="edit") ,
    #delete task
    path('delete/<int:id>' , views.delete , name="delete") , 
    path('taskstatus/<int:id>' , views.taskstatus , name="taskstatus") , 
]
