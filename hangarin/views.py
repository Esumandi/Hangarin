from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Category, Priority, Task, SubTask, Note

# Create your views here.

#class HomePageView(ListView):
 #  model = Task
#   context_object_name = 'home'
#   template_name = "home.html"

def home(request):

   return render(request, 'home.html')


# Category Views
class CategoryListView(ListView):
    model = Category
    context_object_name = 'categories'
    template_name = 'hangarin/category_list.html'
    ordering = ['name']
    paginate_by = 5


class CategoryCreateView(CreateView):
    model = Category
    fields = ['name']
    template_name = 'hangarin/category_form.html'
    success_url = reverse_lazy('category-list')
    paginate_by = 5


class CategoryUpdateView(UpdateView):
    model = Category
    fields = ['name']
    template_name = 'hangarin/category_form.html'
    success_url = reverse_lazy('category-list')
    paginate_by = 5


class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'hangarin/category_confirm_delete.html'
    success_url = reverse_lazy('category-list')
    paginate_by = 5


# Priority Views
class PriorityListView(ListView):
    model = Priority
    context_object_name = 'priorities'
    template_name = 'hangarin/priority_list.html'
    ordering = ['name']
    paginate_by = 5


class PriorityCreateView(CreateView):
    model = Priority
    fields = ['name']
    template_name = 'hangarin/priority_form.html'
    success_url = reverse_lazy('priority-list')
    paginate_by = 5


class PriorityUpdateView(UpdateView):
    model = Priority
    fields = ['name']
    template_name = 'hangarin/priority_form.html'
    success_url = reverse_lazy('priority-list')
    paginate_by = 5


class PriorityDeleteView(DeleteView):
    model = Priority
    template_name = 'hangarin/priority_confirm_delete.html'
    success_url = reverse_lazy('priority-list')
    paginate_by = 5


# Task Views
class TaskListView(ListView):
    model = Task
    context_object_name = 'tasks'
    template_name = 'hangarin/task_list.html'
    ordering = ['-created_at']
    paginate_by = 5


class TaskCreateView(CreateView):
    model = Task
    fields = ['title', 'description', 'status', 'deadline', 'priority', 'category']
    template_name = 'hangarin/task_form.html'
    success_url = reverse_lazy('task-list')
    paginate_by = 5


class TaskUpdateView(UpdateView):
    model = Task
    fields = ['title', 'description', 'status', 'deadline', 'priority', 'category']
    template_name = 'hangarin/task_form.html'
    success_url = reverse_lazy('task-list')
    paginate_by = 5


class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'hangarin/task_confirm_delete.html'
    success_url = reverse_lazy('task-list')
    paginate_by = 5


# SubTask Views
class SubTaskListView(ListView):
    model = SubTask
    context_object_name = 'subtasks'
    template_name = 'hangarin/subtask_list.html'
    ordering = ['-created_at']
    paginate_by = 5


class SubTaskCreateView(CreateView):
    model = SubTask
    fields = ['task', 'title', 'status']
    template_name = 'hangarin/subtask_form.html'
    success_url = reverse_lazy('subtask-list')
    paginate_by = 5


class SubTaskUpdateView(UpdateView):
    model = SubTask
    fields = ['task', 'title', 'status']
    template_name = 'hangarin/subtask_form.html'
    success_url = reverse_lazy('subtask-list')
    paginate_by = 5


class SubTaskDeleteView(DeleteView):
    model = SubTask
    template_name = 'hangarin/subtask_confirm_delete.html'
    success_url = reverse_lazy('subtask-list')
    paginate_by = 5


# Note Views
class NoteListView(ListView):
    model = Note
    context_object_name = 'notes'
    template_name = 'hangarin/note_list.html'
    ordering = ['-created_at']
    paginate_by = 5


class NoteCreateView(CreateView):
    model = Note
    fields = ['task', 'content']
    template_name = 'hangarin/note_form.html'
    success_url = reverse_lazy('note-list')
    paginate_by = 5

class NoteUpdateView(UpdateView):
    model = Note
    fields = ['task', 'content']
    template_name = 'hangarin/note_form.html'
    success_url = reverse_lazy('note-list')
    paginate_by = 5

class NoteDeleteView(DeleteView):
    model = Note
    template_name = 'hangarin/note_confirm_delete.html'
    success_url = reverse_lazy('note-list')
    paginate_by = 5
