from django.shortcuts import render, redirect

# Create your views here.
from .models import Task

def index(request):
    # 1 Logic HTTP Method
    if request.method == 'POST':
        # Collect data from form (HTTP Body)
        title = request.POST.get('title')
        if title:
            Task.objects.create(title=title) #Save into Database
        return redirect('/')
    
    # 2. Show Data
    tasks= Task.objects.all().order_by('-created_at')
    
    #3. Dong goi du lieu --> UI
    context = {'tasks': tasks}
    return render(request, 'todo/index.html', context)