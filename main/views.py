from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core import serializers
from main.forms import ManhwaForm
from main.models import Manhwa

# Create your views here.
def show_main(request):
    manhwas = Manhwa.objects.all()

    context = {
        'name': 'A. Nurcahaya Tampubolon',
        'class': 'PBP A Genap',
        'manhwas': manhwas
    }

    return render(request, "main.html", context)

def create_manhwa(request):
    form = ManhwaForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_manhwa.html", context)

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