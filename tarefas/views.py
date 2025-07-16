from django.shortcuts import render
from.models import Tarefa

# Create your views here.
def listaTarefa(request):
    Tarefas_list = Tarefa.objects.all().order_by('-created_at')
    return render(request, 'tarefas/list.html',{'tarefas': Tarefas_list})