# Manhwa Tracker

[ ] Membuat sebuah proyek Django baru.
Pertama kita buat sebuah direktori utama dengan nama manhwa-tracker yang menampung semua file project kita, kemudian buka terminal pada path direktori untuk membuat virtual environment dengan perintah:

> python3 -m venv env 

Setelah itu, aktifkan virtual environment dengan perintah berikut:

> source env/bin/activate

Didalam direktori utama, buat file requirements.txt yang berisi dependencies yang kita perlukan nanti

```
django
gunicorn
whitenoise
psycopg2-binary
requests
urllib3
```

lakukan instalasi pada dependencies dengan mengetikkan perintah pada terminal direktori

> pip install -r requirements.txt 

Setelah itu, buat proyek django dengan perintah berikut:

> django-admin startproject manhwa_tracker . 

Proyek django dengan nama subdirektori manhwa_tracker telah ada di didalam direktori utama kita.

[ ] Membuat aplikasi dengan nama main pada proyek tersebut.

Untuk membuat aplikasi baru bernama main jalankan perintah ini pada terminal di direktori utama

> python3 manage.py startapp main

Kemudian daftarkan aplikasi main tersebut kedalam proyek. Dengan cara buka settings.py di dalam direktori manhwa_tracker, kemudian tambahkan main ke variabel INSTALLED_APPS.

```
    INSTALLED_APPS = [
    'main',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

[ ] Melakukan routing pada proyek agar dapat menjalankan aplikasi main.

buka berkas dengan nama urls.py di dalam direktori proyek manhwa_tracker untuk menambahkan routing ke proyek main.
sebelumnya impor fungsi include dari django.urls

```
    ...
    from django.urls import path, include
    ...
```

kemudian, tambahkan rute URL seperti berikut untuk mengarahkan ke tampilan main di dalam variabel urlpatterns.

```
    urlpatterns = [
    ...
    path('', include('main.urls')),
    ...
]
```

path('') tidak diisi agar halaman aplikasi main dapat diakses secara langsung

[ ] Membuat model pada aplikasi main dengan nama Item dan memiliki atribut wajib sebagai berikut.
name sebagai nama item dengan tipe CharField.
amount sebagai jumlah item dengan tipe IntegerField.
description sebagai deskripsi item dengan tipe TextField.

Pada manhwa tracker terdapat lima item, yakni title, chapter, genre, sinopsis, dan rating. 
* title sebagai judul dan genre sebagai jenis manhwa dengan tipe CharField.
* chapter sebagai jumlah episode dengan tipe IntegerField
* sinopsis sebagai deksripsi manhwa dengan tipe TextField
* rating sebagai rating manhwa dengan tipe FloatField

```
from django.db import models

# Create your models here.
class Manhwa(models.Model):
    title = models.CharField(max_length=255)
    chapter = models.IntegerField()
    genre = models.CharField(max_length=255)
    sinopsis = models.TextField()
    rating = models.FloatField()
```

[ ] Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu.

Buka berkas views.py pada direktori main, kemudian tambahkan fungsi show main dibawah baris impor

```
    def show_main(request):
    context = {
        'name': 'A. Nurcahaya Tampubolon',
        'class': 'PBP A'
    }

    return render(request, "main.html", context)
```

kemudian buka berkas main.html yang telah dibuat sebelumnya di direktori manhwa-tracker/main/templates. Kemudian ubah nama dan kelas  menjadi kode django untuk menampilkan nilai dari variabel yang telah didefenisikan dalam context.

```
    <h5>Name:</h5>
    <p>{{ name }}</p>
    <p></p>
    <h5>Class:</h5>
    <p>{{ class }}</p>
```

[ ] Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py.

untuk membuat routing pada aplikasi main yaitu dengan membuat urls.py pada direktori aplikasi main kemudian menghubungkan juga dengan fungsi show_main

```
from django.urls import path

from main.views import show_main

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
]
```

[ ] Melakukan deployment ke PWS terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.

Pertama, kita melakukan register di http://pbp.cs.ui.ac.id/register. Kemudian login, buat New Project sesuai dengan nama direktori kita seperti manhwatracker.
Setelah itu, pada terminal direktori utama kita ketikkan perintah berikut:

```
git remote add pws http://pbp.cs.ui.ac.id/a.nurcahaya/manhwatracker
git branch -M master
git push pws master
```

Pertanyaan:
Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
- Ada beberapa alasan mengapa kita menggunakan virtual environment dalam pengembangan aplikasi web Django:
  * Mengisolasi Dependencies: Virtual environment membantu mengisolasi dependencies (ketergantungan) project Django kita dari project Python lainnya di sistem kita. 
  * Meningkatkan Keamanan: Virtual environment membantu meningkatkan keamanan project kita dengan membatasi akses ke dependencies yang diinstal. Hal ini dapat membantu mencegah kerentanan keamanan dieksploitasi.
  * Mempermudah Debugging: Virtual environment dapat membantu mempermudah debugging project kita dengan memungkinkan kita untuk mengidentifikasi dan menyelesaikan masalah yang terkait dengan dependencies.
  * Mempermudah Deployment: Virtual environment dapat membantu mempermudah deployment project kita dengan memungkinkan kita untuk mengemas semua dependencies yang diperlukan bersama dengan project Anda.

- Ya, kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment. Namun, tidak disarankan untuk melakukan hal ini karena beberapa alasan yang disebutkan di atas.

Tanpa virtual environment, kita bisa:

* Mengalami konflik dan masalah kompatibilitas dengan dependencies.
* Menurunkan keamanan project Anda.
* Menghadapi kesulitan saat debugging project Anda.
* Mengalami kesulitan saat deploying project Anda.

Oleh karena itu, sangat disarankan untuk menggunakan virtual environment saat mengembangkan aplikasi web Django.Virtual environment dapat membantu kita menghindari berbagai masalah dan meningkatkan alur kerja pengembangan Anda.


Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.
- MVC (Model-View-Controller), MVT (Model-View-Template), dan MVVM (Model-View-ViewModel) adalah pola desain arsitektur perangkat lunak yang populer untuk memisahkan berbagai aspek aplikasi.
**MVC:**

* **Model:** Menyimpan data dan logika aplikasi.
* **View:** Menampilkan data kepada pengguna dan menerima input pengguna.
* **Controller:** Mengontrol interaksi antara Model dan View, dan memproses input pengguna.

**MVT:**

* **Model:** Menyimpan data dan logika aplikasi.
* **View:** Menampilkan data kepada pengguna.
* **Template:** Menentukan struktur dan format View.

**MVVM:**

* **Model:** Menyimpan data dan logika aplikasi.
* **View:** Menampilkan data kepada pengguna.
* **ViewModel:** Bertindak sebagai perantara antara Model dan View, dan mengonversi data Model menjadi format yang dapat dipahami oleh View.

**Berikut adalah tabel yang menunjukkan perbedaan utama antara MVC, MVT, dan MVVM:**

| Fitur | MVC | MVT | MVVM |
|---|---|---|---|
| **Controller** | Ada | Tidak ada | Tidak ada |
| **Template** | Tidak ada | Ada | Tidak ada |
| **ViewModel** | Tidak ada | Tidak ada | Ada |
| **Pemisahan logika UI** | Sedang | Tinggi | Tinggi |
| **Pengujian unit** | Mudah | Mudah | Sedikit lebih sulit |
| **Kompleksitas** | Sedang | Rendah | Tinggi |

**Berikut adalah beberapa contoh penggunaan MVC, MVT, dan MVVM:**

* **MVC:** Cocok untuk aplikasi web dan desktop yang kompleks dengan banyak interaksi pengguna.
* **MVT:** Cocok untuk aplikasi web dan desktop yang sederhana dengan sedikit interaksi pengguna.
* **MVVM:** Cocok untuk aplikasi mobile dan desktop dengan UI yang kompleks dan data yang sering berubah.

**Kesimpulan:**

MVC, MVT, dan MVVM adalah pola desain arsitektur perangkat lunak yang populer dengan kelebihan dan kekurangannya masing-masing. Pilihan pola desain yang tepat tergantung pada kebutuhan dan kompleksitas aplikasi kita.

## Tugas 3
[ ] Apa perbedaan antara form POST dan form GET dalam Django?
>* Form Post mengirimkan data melalui method POST. Data disembunyikan di dalam body request. Sedangkan form Get mengirimkan data melalui method GET. Data ditampilkan di URL sebagai query parameters.
>* Form Post tidak ada batas ukuran data yang dikirim. Sedangkan form Get ada batasan ukuran data karena dibatasi oleh URL length limit.

[ ] Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data?
>* XML memiliki tag/format terstruktur mirip HTML, ukuran filenya cenderung lebih besar, dan formatnya berbasis teks untuk menyimpan dan mentransfer data. XML juga lebih fleksibel dan self-descriptive, digunakan untuk integrasi sistem dan web services.
>* JSON memiliki format yang lebih sederhana mirip object literal di bahasa pemrograman, ukurannya kecil sehingga transfer data lebih cepat, formatnya ringan berbasis teks untuk pertukaran data, dan banyak digunakan untuk AJAX web dan mobile apps.
>* HTML adalah markup language untuk menampilkan konten web, berfokus pada tampilan dan presentation, dan tidak didesain secara spesifik untuk transfer data. Lebih banyak digunakan untuk menampilkan data daripada mentransfernya.

[ ] Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?
>JSON tidak tergantung pada bahasa pemrograman apapun walaupun namanya JavaScript Object Notation, formatnya juga berbasis teks sehingga ukurannya kecil. JSON juga memiliki struktur yang sederhana dan ringan, memudahkan parsing dan pengiriman melalui jaringan.

[ ] Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
>[ ] Membuat input form untuk menambahkan objek model pada app sebelumnya.

Pertama buat folder templates pada direktori utama, yaitu manhwa-tracker. Kemudian isi templates tersebut dengan berkas HTML bernama base.html. Kemudian kita mengisi berkas tersebut dengan kode dibawah ini.
```
{% load static %}
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    {% block meta %} {% endblock meta %}
  </head>

  <body>
    {% block content %} {% endblock content %}
  </body>
</html>
```
Kemudian pada manhwa_tracker/settings.py kita menambahkan potongan kode dibawah supaya base.html terdeteksi sebagai berkas template.
```
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        ...
    },
]
```
Pada main/templates/main.html kita mengubah berkas menjadi seperti kode dibawah ini.
```
{% extends 'base.html' %} {% block content %}
<h1>Manhwa Tracker Page</h1>

<h5>Name:</h5>
<p>{{name}}</p>

<h5>Class:</h5>
<p>{{class}}</p>
{% endblock content %}
```
Setelah itu, pada direktori main, kita tambahkan berkas dengan nama forms.py untuk membuat struktur form yang dapat menerima data manhwa baru. Tambahkan fields sesuai dengan field yang sudah kita isi pada model Manhwa sebelumnya.
```
from django.forms import ModelForm
from main.models import Manhwa

class ManhwaForm(ModelForm):
    class Meta:
        model = Manhwa
        fields = ["title", "chapter", "genre", "sinopsis", "rating"]
```
Selanjutnya, buka main/views.py tambahkan impor redirect untuk melakukan redirect ke fungsi show_main pada views aplikasi main setealh data form berhasil disimpan.
```
from django.shortcuts import render, redirect
```
Setelah itu, buat fungsi baru dengan nama create_manhwa yang menerima parameter request. Ubah juga fungsi show_main menjadi seperti dibawah.
```
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
```
Selanjutnya buka main/urls.py dan impor fungsi create_manhwa yang sudah kita buat sebelumnya. Tambahkan juga path URL untuk mengakses fungsi yang sudah diimpor.
```
from django.urls import path
from main.views import show_main, create_manhwa

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-manhwa', create_manhwa, name='create_manhwa'),
]
```
Setelahnya, buat berkas HTML pada main/templates dengan nama create_manhwa.html. Kita isi dengan kode berikut.
```
{% extends 'base.html' %} {% block content %}
<h1>Add New Manhwa</h1>

<form method="POST">
  {% csrf_token %}
  <table>
    {{ form.as_table }}
    <tr>
      <td></td>
      <td>
        <input type="submit" value="Add Manhwa" />
      </td>
    </tr>
  </table>
</form>

{% endblock %}
```
Kemudian, kita buka main.html dan menambahkan kode dibawah ini untuk menampilkan data manhwa dalam bentuk tabel serta tombol "Add New Manhwa" yang akan redirect ke halaman form.
```
{% extends 'base.html' %} {% block content %}
<h1>Manhwa Tracker Page</h1>

<h5>Name:</h5>
<p>{{name}}</p>

<h5>Class:</h5>
<p>{{class}}</p>
  <table>
    <tr>
      <th>Title</th>
      <th>Chapter</th>
      <th>Genre</th>
      <th>Sinopsis</th>
      <th>Rating</th>
    </tr>
  
    {% comment %} Berikut cara memperlihatkan data produk di bawah baris ini
    {%endcomment %} {% for manhwa in manhwas %}
    <tr>
      <td>{{manhwa.title}}</td>
      <td>{{manhwa.chapter}}</td>
      <td>{{manhwa.genre}}</td>
      <td>{{manhwa.sinopsis}}</td>
      <td>{{manhwa.rating}}</td>
    </tr>
    {% endfor %}
  </table>
  
  <br />
  
  <a href="{% url 'main:create_manhwa' %}">
    <button>Add New Manhwa</button>
  </a>
{% endblock content %}
```
>[ ] Tambahkan 4 fungsi views baru untuk melihat objek yang sudah ditambahkan dalam format XML, JSON, XML by ID, dan JSON by ID.

Buka main/views.py dan tambahkan kode dibawah ini.
```
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
```
HttpResponse berisi parameter data hasil query yang sudah diserialisasi menjadi XML/JSON dan parameter content_type="application/xml" atau content_type="application/json". Serializers digunakan untuk translate objek model menjadi format lain seperti XML atau JSON.

Kita menambahkan juga variabel  didalam fungsi yang menyimpan hasil query dari data dengan id tertentu yang ada pada Manhwa.
```
data = Manhwa.objects.filter(pk=id)
```
>[ ] Membuat routing URL untuk masing-masing views yang telah ditambahkan pada poin 2.

Pada main/urls.py kita mengimpor fungsi yang telah kita buat sebelumnya di views.py dan menambahkan path URL ke dalam urlpatterns dengan menambahkan kode dibawah ini supaya bisa mengakses fungsi yang sudah diimpor tadi.
```
from django.urls import path
from main.views import show_main, create_manhwa, show_xml, show_json, show_xml_by_id, show_json_by_id

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-manhwa', create_manhwa, name='create_manhwa'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),
]
```

[ ] Mengakses keempat URL di poin 2 menggunakan Postman, membuat screenshot dari hasil akses URL pada Postman, dan menambahkannya ke dalam README.md.
<img src="photosofpostman/xml.png" alt="localhost:8000/xml/">
<img src="photosofpostman/xml:1.png" alt="localhost:8000/xml/1">
<img src="photosofpostman/xml:2.png" alt="localhost:8000/xml/2">
<img src="photosofpostman/xml:3.png" alt="localhost:8000/xml/3">
<img src="photosofpostman/xml:4.png" alt="localhost:8000/xml/4">
<img src="photosofpostman/json.png" alt="localhost:8000/json/">
<img src="photosofpostman/json:1.png" alt="localhost:8000/json/1">
<img src="photosofpostman/json:2.png" alt="localhost:8000/json/2">
<img src="photosofpostman/json:3.png" alt="localhost:8000/json/3">
<img src="photosofpostman/json:4.png" alt="localhost:8000/json/4">