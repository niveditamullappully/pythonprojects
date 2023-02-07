from django.urls import path
from. import views


urlpatterns=[
    path('',views.index,name='index'),
    path('delete/<int:taskid>/',views.delete,name='delete'),
    path('update/<int:taskid>/',views.update,name='update'),
    path ('cbvindex/',views.Tasklistview.as_view(),name='Tasklistview'),
    path('cbvdetails/<int:pk>/',views.Taskdetailview.as_view(),name='Taskdetailview'),
    path('cbvupdate/<int:pk>/', views.Taskupdateview.as_view(), name='Taskupdateview'),
    path('cbvdelete/<int:pk>/', views.Taskdeleteview.as_view(), name='Taskdeleteview')



]