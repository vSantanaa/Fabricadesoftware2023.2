from django.shortcuts import render, redirect
from app.forms import FuncionariosForm
from app.models import Funcionarios

def home(request):
    data = {}
    data ["db"] = Funcionarios.objects.all()
    return render(request, "index.html", data)

def form(request):
    data = {}
    data ["form"] = FuncionariosForm()
    return render(request, "form.html", data)

def create(request):
    form = FuncionariosForm(request.POST or None)
    if form_is_valid():
        form.save()
        return redirect("home")

def view(request, pk):
    data = {}
    data ["db"]= Funcionarios.objects, get(pk=pk)
    return render(request, "view.html", data)

def edit(request, pk):
    data = {}
    data ["db"]= Funcionarios.objects, get(pk=pk)
    data ["form"] = FuncionariosForm(instance=data ["db"])
    return render(request, "form.html", data)

def update(request, pk):
    data = {}
    data ["db"]= Funcionarios.objects, get(pk=pk)
    form = FuncionariosForm(request.POST or None, instance=data ["db"])
    if form.is_valid():
        form.save
        return redirect("home")     

def update(request, pk):
    data ["db"]= Funcionarios.objects,get(pk=pk) 
    db.delete()
    return redirect("home")        

#adiocinando paginas home, form, create e read