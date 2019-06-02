from django.shortcuts import render,redirect
from salesactivity.forms import BranchesForm
from salesactivity.models import Branches

def sales(request):
    if request.method=="POST":
        form=BranchesForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show')
            except:
                pass
    else:
        form=BranchesForm()
    return render(request, 'salesactivity/index.html', {'form':form})
def show(request):
    salesactivities=Branches.objects.all()
    return render(request, "salesactivity/show.html", {'salesactivities':salesactivities})
def edit(request,id):
    salesactivity=Branches.objects.get(id=id)
    return render(request, 'salesactivity/edit.html', {'salesactivity':salesactivity})
def update(request,id):
    salesactivity=Branches.objects.get(id=id)

    form=BranchesForm(request.POST,instance=salesactivity)
    if form.is_valid():
        form.save()
        return redirect("/show")
    return render(request, 'salesactivity/edit.html', {'salesactivity': salesactivity})
def destroy(request, id):
    salesactivity = Branches.objects.get(id=id)
    salesactivity.delete()
    return redirect("/show")



# Create your views here.
