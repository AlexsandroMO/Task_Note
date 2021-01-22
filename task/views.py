from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Task
#from apps.funcionarios.models import 


@login_required
def index(request):

    tasks = Task.objects.all().order_by('doc')

    return render(request,'task/index.html',{'tasks': tasks})

    