from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse

def root(request):
    return redirect('/blogs')

def index(request):
    return HttpResponse("placeholder para luego mostrar una lista de todos los blogs")

def new(request):
    return HttpResponse("placeholder para mostrar un nuevo formulario para crear un nuevo blog")

def create(request):
    return redirect('/')

def show(request, number):
    return HttpResponse(f"placeholder para mostrar el blog nro {number}")

def edit(request, number):
    return HttpResponse(f"placeholder para editar el blog nro {number}")

def destroy(request, number):
    return redirect('/blogs')

def jsons(request):
    data = {
        "name": "Bruniro",
        "age": 7,
        "hobbies": ["Eating", "Walking", "Barking", "Smelling", "Giving some autographs"]
    }

    return JsonResponse(data)