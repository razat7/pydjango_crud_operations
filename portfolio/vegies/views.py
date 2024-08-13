from django.shortcuts import render, redirect
from .models import *

# Create your views here.
def receipes(request):
    if request.method == "POST":
        data = request.POST
        receipe_name = data.get('receipe_name')
        receipe_description = data.get('receipe_description')
        receipe_image = request.FILES.get('receipe_image')

        Receipe.objects.create(
                receipe_name= receipe_name,
                receipe_description = receipe_description,
                receipe_image = receipe_image,)
        
        return redirect('receipes')
    
    records = Receipe.objects.all()


    if request.GET.get('search'): #Search bar functions
       records = records.filter(receipe_name__icontains = request.GET.get('search'))

    context = {'records' : records}
    return render(request, "receipes.html", context)

def delete_rec(request, id):
    alldata = Receipe.objects.get(id = id)
    alldata.delete()
    return redirect('receipes')

def update_rec(request, id):
   udata = Receipe.objects.get(id=id)

   if request.method == "POST":
       data = request.POST

       receipe_name = data.get('receipe_name')
       receipe_description = data.get('receipe_description')
       receipe_image = request.FILES.get('receipe_image')
       
       udata.receipe_name = receipe_name
       udata.receipe_description = receipe_description
       udata.receipe_image = receipe_image
       udata.save()
       return redirect('receipes')
   return render (request, "update.html" , context={'udata': udata})