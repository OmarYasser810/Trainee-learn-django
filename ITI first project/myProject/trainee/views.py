from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Trainee
# Create your views here.
def trainee_list(request):
    trainee = Trainee.objects.all()
    return render(request, 'trainee.html', context={'trainees': trainee})

def insert_trainee(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        img = request.FILES.get('image')
        if img is None:
            img = 'trainee/images/default.jpg'
        statue = request.POST.get('statue')
        if statue == 'true':
            statue = True
        else:
            statue = False
        Trainee.objects.create(name=name, email=email, photo=img, statue=statue)  # create a new record
        Trainee.objects.all().order_by('id', 'name', 'email')
        return redirect('insert_trainee')
    return render(request, 'insert.html')

def update_trainee(request, id):
    try:
        trainee = Trainee.objects.get(id=id)  # fetch trainee by primary key
        if request.method == 'POST':
            name = request.POST.get('name')
            email = request.POST.get('email')
            img = request.FILES.get('image')
            if img is None:
                pass  # retain existing image if no new image is uploaded
            else:
                trainee.photo = img
                
            statue = request.POST.get('statue')
            if statue == 'true':
                statue = True
            else:
                statue = False
                
            trainee.name = name
            trainee.email = email
            trainee.statue = statue
            trainee.save()  # save the updated record
            Trainee.objects.all().order_by('id', 'name', 'email')
            return redirect('trainee_list')
    except Trainee.DoesNotExist:
        return HttpResponse("Trainee not found", status=404)
    return render(request, 'update.html')
        

def delete_trainee(request, id):
    try:
        trainee = Trainee.objects.get(id=id)
        trainee.statue = False
        trainee.save()
        return redirect('trainee_list')
    except Trainee.DoesNotExist:
        return HttpResponse("Trainee not found", status=404)