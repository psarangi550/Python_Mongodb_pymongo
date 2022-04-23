from django.shortcuts import render
from .forms import RevForm
from.models import RevModel
from django.shortcuts import HttpResponseRedirect

# Create your views here.
def index(request):
    form=RevForm()#creating the object of the  revForm
    return render(request,template_name="revapp/home.html",context={"form":form})

def fetch_index(request):
    if request.method=="POST":
        form=RevForm(request.POST)
        if form.is_valid:
            print(form.cleaned_data)
            # name=form.cleaned_data["name"]
            # age=form.cleaned_data["age"]
        # print(name)
        # print(age)
            # print(request.POST)
            # name=request.POST["name"]
            # age=request.POST["age"]
            # my_mod=RevModel(name=name,age=age)
            # my_mod.save()
        # {"name":name,"age":age}
        return render(request,"revapp/fetch.html")
    else:
        # print(request.GET)
        return render(request,"revapp/fetch.html")
    from django.shortcuts import render
from .forms import RevForm
from.models import RevModel
from django.shortcuts import HttpResponseRedirect

# Create your views here.
def index(request):
    form=RevForm()#creating the object of the  revForm
    return render(request,template_name="revapp/home.html",context={"form":form})

def fetch_index(request):
    if request.method=="POST":
        form=RevForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            name=form.cleaned_data["name"]
            age=form.cleaned_data["age"]
             # print(name)
            # print(age)
            # print(request.POST)
            # name=request.POST["name"]
            # age=request.POST["age"]
            my_mod=RevModel(name=name,age=age)
            my_mod.save()
            my_obj=RevModel.objects.all()
            # print(my_obj)
            # {"name":name,"age":age}
        return render(request,"revapp/fetch.html",{"my_obj":my_obj})
    else:
        # print(request.GET)
        return render(request,"revapp/fetch.html")
    