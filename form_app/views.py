from django.shortcuts import render, redirect

# Create your views here.


def index(request):
    return render(request, "index.html")


def create_user(request):
    print("Got info")
    print(request.POST)
    # name = request.POST['name']
    # comments = request.POST['comments']
    # favorite_language = request.POST['favorite_language']
    # sede = sede.POST['sede']
    request.session['name'] = request.POST['name']
    request.session['comments'] = request.POST['comments']
    request.session['favorite_language'] = request.POST['favorite_language']
    request.session['sede'] = request.POST['sede']
    return redirect("/results")


def success(request):
    return render(request, 'show.html')
