from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound, JsonResponse
from django.urls import reverse
from django.core import serializers
from main.forms import ManhwaForm
from main.models import Manhwa
import datetime, json

# Create your views here.
@login_required(login_url='/login')
def show_main(request):
    manhwas = Manhwa.objects.filter(user=request.user)

    context = {
        'name': request.user.username,
        'class': 'PBP A Genap',
        'manhwas': manhwas,
        'last_login': request.COOKIES['last_login'],
    }

    return render(request, "main.html", context)

def create_manhwa(request):
    form = ManhwaForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        manhwa = form.save(commit=False)
        manhwa.user = request.user
        manhwa.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_manhwa.html", context)

def edit_manhwa(request, id):
    # Get manhwa berdasarkan ID
    book = Manhwa.objects.get(pk = id)

    # Set manhwa sebagai instance dari form
    form = ManhwaForm(request.POST or None, instance=book)

    if form.is_valid() and request.method == "POST":
        # Simpan form dan kembali ke halaman awal
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "edit_manhwa.html", context)

def delete_manhwa(request, id):
    # Get data berdasarkan ID
    manhwa = Manhwa.objects.get(pk = id)
    # Hapus data
    manhwa.delete()
    # Kembali ke halaman awal
    return HttpResponseRedirect(reverse('main:show_main'))

def show_xml(request):
    data = Manhwa.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Manhwa.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Manhwa.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Manhwa.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

@csrf_exempt
def add_manhwa_ajax(request):
    if request.method == 'POST':
        title = request.POST.get("title")
        chapter = request.POST.get("chapter")
        genre = request.POST.get("genre")
        sinopsis = request.POST.get("sinopsis")
        rating = request.POST.get("rating")
        user = request.user

        new_manhwa = Manhwa(title=title, chapter=chapter, genre=genre, sinopsis=sinopsis, rating=rating, user=user)
        new_manhwa.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()

@csrf_exempt
def create_manhwa_flutter(request):
    if request.method == 'POST':

        data = json.loads(request.body)

        new_manhwa = Manhwa.objects.create(
            user = request.user,
            title = data["title"],
            chapter = int(data["chapter"]),
            genre = data["genre"],
            sinopsis = data["sinopsis"],
            rating = float(data["rating"])
        )

        new_manhwa.save()

        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)