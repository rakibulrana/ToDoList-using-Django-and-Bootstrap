from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Todo,Todoform
def HomePage(request):

    tododatas = Todo.objects.all().order_by('-id')
    content = {
        'todo': tododatas,
        'form': Todoform
    }

    if request.method == 'POST':
        data = request.POST
        form = Todoform(data)
        if form.is_valid():
            form.save()
            return redirect("/")
        return render(request, 'todoapp/index.html')
    return render(request, 'todoapp/index.html', {"data": content})

def Edittodo(request, id):
    try:
        tdata = Todo.objects.get(id=id)
        tdata.delete()

        return HttpResponse("<h1> ToDo is Deleted! </h1>")
    except:
        return redirect("/")
    return HttpResponse(f"<h1> {id}</h1>")

def Updatetodo(request, id):
    try:
        tdata = Todo.objects.get(id = id)
        return HttpResponse(f"{id}")
    except:
        return redirect("/")
