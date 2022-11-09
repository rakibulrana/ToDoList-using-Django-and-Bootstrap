from django.shortcuts import render, redirect

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