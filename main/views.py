from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from .forms import *
from django.views.generic import View
from django.urls import reverse
from django.http import HttpResponseRedirect

def main(request):
	space = Space.objects.filter(assign=request.user.id)
	if request.method == "POST":
		form_list = ListForm(request.POST)
		if form_list.is_valid():
			post = form_list.save()
			post.save()
			return redirect ('/')
	else:
		form_list = ListForm()

	if request.method == "POST":
		form_space = SpaceForm(request.POST)
		if form_space.is_valid():
			post = form_space.save()
			post.save()
			return redirect ('/')
	else:
		form_space = SpaceForm()
	return render(request, 'main/index.html', context = {'space':space, 'form_list': form_list, 'form_space': form_space})

def status(request, task_id):
	lists = List.objects.all()
	space = Space.objects.filter(assign=request.user.id)
	bbs = Task.objects.filter(status=task_id, assign=request.user.id)
	form_list = ListForm()
	form_space = SpaceForm()
	status = Status.objects.all()
	current_status = Status.objects.get(id = task_id)
	context = {
		'status': status,
		'bbs':bbs,
		'current_status':current_status,
		'space':space, 
		'lists': lists, 
		'form_list': form_list,
		'form_space': form_space,
	}
	return render(request, 'main/status.html', context)

def task(request, list_id):
	space = Space.objects.filter(assign=request.user.id)
	lists = get_object_or_404(List, id=list_id)
	form_list = ListForm()
	form_space = SpaceForm()
	status = Status.objects.all()

	if request.method == "POST":
		task_form = TaskForm(request.POST or None)
		if task_form.is_valid():
			task = task_form.save()
			task.save()
			return redirect(reverse('task_url', args = (lists.id,)))
	else:
		task_form = TaskForm(initial = {'lists': lists})
	return render(request, 'main/task.html', context = {'status':status,'lists':lists, 'space':space, 'form_list': form_list, 'form_space': form_space, 'task_form': task_form})

# def subtask(request, task_id):
# 	space = Space.objects.filter(assign=request.user.id)
# 	task = get_object_or_404(Task, id=task_id)
# 	form_list = ListForm()
# 	form_space = SpaceForm()

# 	if request.method == "POST":
# 		subtask_form = SubTaskForm(request.POST)
# 		if subtask_form.is_valid():
# 			post = subtask_form.save()
# 			post.save()
# 			return redirect(reverse('subtask_url', args = (task.id,)))
# 	else:
# 		subtask_form = SubTaskForm(initial = {'task': task})
# 	context = {
# 		'task':task,
# 		'subtask_form': subtask_form,
# 		'space':space, 
# 		'form_list': form_list, 
# 		'form_space': form_space,
# 		}
# 	return render(request, 'main/subtask.html', context = context)

def TaskDetail(request, task_id, list_id):
	task = get_object_or_404(Task, id=task_id)
	lists = get_object_or_404(List, id=list_id)
	form_upd = TaskForm(instance = task, initial = {'lists' : lists}) 
	latest_comments_list = task.task_comment.order_by('-id')[:10]
	task_comment_form = TaskCommentForm(request.POST)
	if task_comment_form.is_valid():
		task_comment_save = task_comment_form.save()
		return HttpResponseRedirect(reverse('task_detail_url', args = (lists.id,task.id)))
	forms = TaskForm(request.POST, instance = task)
	if forms.is_valid():
		upd_task = forms.save()
		return redirect(reverse('task_detail_url', args = (lists.id,task.id)))

	
	form_task_comment = TaskCommentForm(initial = {'task': task})

	if request.method == "POST":
		subtask_form = SubTaskForm(request.POST)
		if subtask_form.is_valid():
			post = subtask_form.save()
			post.save()
			return redirect(reverse('task_detail_url', args = (lists.id,task.id)))
	else:
		subtask_form = SubTaskForm(initial = {'task': task})
	if request.method == 'POST':
		task.delete()
		return redirect(reverse('task_url', args = (lists.id,)))
	context = {
	'form_task_comment': form_task_comment,
	"task_detail": task, 
	'form_upd': form_upd, 
	'lists': lists,  
	'latest_comments_list': latest_comments_list,
	'subtask_form': subtask_form
	}
	return render(request, 'main/task_detail.html', context = context)

def SpaceDetail(request, space_id):
	space = get_object_or_404(Space, id=space_id)
	form_list = ListForm()
	form_space = SpaceForm()
	if request.method == 'POST':
		space.delete()
		return redirect(reverse('main'))
	return render(request, 'main/space_detail.html', context = {'space': space, 'form_list': form_list, 'form_space': form_space})

if __name__ == '__main__':
    	DEBAG = True