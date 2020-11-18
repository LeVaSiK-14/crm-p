from django.urls import path
from . import views

urlpatterns = [
	path('', views.main, name = 'main'),
	path('space/<int:space_id>/', views.SpaceDetail, name = 'space_detail_url'),
	path('task/<int:list_id>/', views.task, name = 'task_url'),
	# path('subtask/<int:task_id>/', views.subtask, name = 'subtask_url'),
	path('task_detail/<int:list_id>/<int:task_id>/', views.TaskDetail, name = 'task_detail_url'),

	path('status/<int:task_id>/', views.status, name = 'status_url')
] 