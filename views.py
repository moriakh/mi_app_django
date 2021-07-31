from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
from time import gmtime, strftime, localtime

USUARIOS = [
        {'name':'Shishi', 'pass':'gang'},
        {'name':'Pablito', 'pass':'bendicion'},
        {'name':'Rando', 'pass':'Ramd0'}
    ]


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

def page(request):
    context = {
    	'name': "Bruno",
    	'favorite_food': "Meat",
    	'hobbies': ["Eating", "Walking", "Barking", "Smelling", "Giving some autographs"]
    }
    return render(request, "index.html", context)


def tarea1(request):
    context = {
    	'images': [
            "https://lastfm.freetls.fastly.net/i/u/ar0/1e9472c5e698bb00fa81172ea361f681.jpg", 
            "https://i.ytimg.com/vi/TRFWpESdr20/maxresdefault.jpg", 
            "https://edmidentity.com/wp-content/uploads/2020/12/daft-punk-41711-42689-hd-wallpapers.jpg", 
            "https://playtusu.com/wp-content/uploads/2019/12/jon-hopkins-in-the-studio.jpg"
        ]
    }
    return render(request, "tarea1.html", context)

def time_display(request):
    context = {
        "time": strftime("%Y-%m-%d %H:%M:%S", localtime())
    }
    return render(request,'time_display.html', context)

def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
        
    user = next((u for u in USUARIOS if u['name'] == request.POST['name']), None)
    
    if user is None:
        return redirect("/login")
    
    if user['pass'] != request.POST['pass']:
        return redirect("/login")
    
    request.session['name'] = request.POST['name']
    request.session['pass'] = request.POST['pass']
    # redirigimos a una página interna
    return redirect('/time_display')
    # return HttpResponse('Logueando al usuario')

def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html')

    user = next((u for u in USUARIOS if u['name'] == request.POST['name']), None)

    if user is None:
        if request.POST['pass'] == request.POST['pass2']:
            USUARIOS.append({'name' : request.POST['name'], 'pass' : request.POST['pass']})
            return redirect('/login')
    else:
        return redirect('/signin')
    
    
