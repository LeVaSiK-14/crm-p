from django.db import models
from django.contrib.auth.models import User
import datetime
from colorfield.fields import ColorField



class Status(models.Model):
    name_status = models.CharField(max_length=100)

    def __str__(self):
        return(self.name_status)

class Action(models.Model):
    name_action = models.CharField(max_length=100)

    def __str__(self):
        return(self.name_action)


class Space(models.Model):
    name = models.CharField('Название',max_length=100)
    photo = models.ImageField(upload_to='images/', blank=True)
    assign = models.ManyToManyField(User)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    add_date = models.DateField(auto_now_add=True)
    upd_date = models.DateField(auto_now_add=False, auto_now=True)
    created_by = models.CharField(max_length=150)
    color = ColorField(default='#FF0000')

    def __str__(self):
        return (self.name)



class CustomUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars/', blank=True)
    email = models.EmailField()
    action = models.ForeignKey(Action, on_delete=models.CASCADE, default='')


    def __str__(self):
        return self.user.username

    class Meta:
        ordering = ['user']
        verbose_name = 'user'
        verbose_name_plural = 'users'


class List(models.Model):
    space = models.ForeignKey(Space, on_delete=models.CASCADE, related_name='second')
    name_list = models.CharField(max_length=100)
    def __str__(self):
        return (self.name_list)


class Task(models.Model):
    lists = models.ForeignKey(List, on_delete=models.CASCADE, related_name='third')
    task_name = models.CharField(max_length=80, default='taskssssss', blank=True, null = True)
    assign = models.ManyToManyField(User, default=1, blank=True, null = True)
    dead_line = models.DateField(blank=True, null = True)
    attachments = models.FileField(upload_to='files/',blank=True, null = True)
    status = models.ForeignKey(Status, on_delete=models.CASCADE, default=2, blank=True, null = True)
    description = models.TextField(blank=True, null = True, default='descriptionssssssss')
    start_date = models.DateTimeField(auto_now_add=True, blank=True)
    end_date = models.DateTimeField(blank=True, null = True)
    created_by = models.CharField(max_length=150, blank=True, null = True, default='admin')

    def __str__(self):
        return(self.task_name)

class SubTask(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='four')
    task_name = models.CharField(max_length=80)
    assign = models.ManyToManyField(User)
    dead_line = models.DateField()
    attachments = models.FileField(upload_to='files/',blank=True)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    start_date = models.DateTimeField(auto_now_add=True, blank=True)

    end_date = models.DateTimeField(blank=True, null = True)
    created_by = models.CharField(max_length=150, null = True)


    def __str__(self):
        return(self.task_name)

class TaskComment(models.Model):
    task = models.ForeignKey(Task,on_delete=models.CASCADE, related_name = 'task_comment')
    name = models.CharField(max_length=100)
    comment  = models.TextField(blank=True)

    def __str__(self):
        return(self.comment)

class SubTaskComment(models.Model):
    subtask = models.ForeignKey(SubTask,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    comment  = models.TextField(blank=True)

    def __str__(self):
        return(self.comment)
