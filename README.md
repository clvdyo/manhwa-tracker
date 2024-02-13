# Manhwa Tracker

[ ] Membuat sebuah proyek Django baru.
Pertama kita buat sebuah direktori utama dengan nama manhwa-tracker yang menampung semua file project kita, kemudian buka terminal pada path direktori untuk membuat virtual environment dengan perintah:

{{ python3 -m venv env }}

Setelah itu, aktifkan virtual environment dengan perintah berikut:

{{ source env/bin/activate }}

Didalam direktori utama, buat file requirements.txt yang berisi dependencies yang kita perlukan nanti

{{ 
django
gunicorn
whitenoise
psycopg2-binary
requests
urllib3
}}

lakukan instalasi pada dependencies dengan mengetikkan perintah pada terminal direktori

{{ pip install -r requirements.txt }}

Setelah itu, buat proyek django dengan perintah berikut:

{{ django-admin startproject manhwa_tracker . }}

Proyek django dengan nama subdirektori manhwa_tracker telah ada di didalam direktori utama kita.

[ ] Membuat aplikasi dengan nama main pada proyek tersebut.

Untuk membuat aplikasi baru bernama main jalankan perintah ini pada terminal di direktori utama

{{
    python3 manage.py startapp main
}}

Kemudian daftarkan aplikasi main tersebut kedalam proyek, dengan cara buka settings.py di dalam direktori manhwa_tracker. Kemudian tambahkan main ke variabel INSTALLED_APPS.

{{
    INSTALLED_APPS = [
    'main',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
}}

[ ] Melakukan routing pada proyek agar dapat menjalankan aplikasi main.

buka berkas dengan nama urls.py di dalam direktori proyek manhwa_tracker untuk menambahkan routing ke proyek main.
sebelumnya impor fungsi include dari django.urls

{{
    ...
    from django.urls import path, include
    ...
}}

kemudian, tambahkan rute URL seperti berikut untuk mengarahkan ke tampilan main di dalam variabel urlpatterns.

{{
    urlpatterns = [
    ...
    path('', include('main.urls')),
    ...
]
}}

path('') tidak diisi agar halaman aplikasi main dapat diakses secara langsung

[ ] Membuat model pada aplikasi main dengan nama Item dan memiliki atribut wajib sebagai berikut.
name sebagai nama item dengan tipe CharField.
amount sebagai jumlah item dengan tipe IntegerField.
description sebagai deskripsi item dengan tipe TextField.

Pada manhwa tracker terdapat lima item, yakni title, chapter, genre, sinopsis, dan rating. 
title sebagai judul dan genre sebagai jenis manhwa dengan tipe CharField.
chapter sebagai jumlah episode dengan tipe IntegerField
sinopsis sebagai deksripsi manhwa dengan tipe TextField
rating sebagai rating manhwa dengan tipe FloatField

{{
    from django.db import models

#Create your models here.
class Manhwa(models.Model):
    title = models.CharField(max_length=255)
    chapter = models.IntegerField()
    genre = models.CharField(max_length=255)
    sinopsis = models.TextField()
    rating = models.FloatField()
}}

[ ] Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu.

Buka berkas views.py pada direktori main, kemudian tambahkan fungsi show main dibawah baris impor

{{
    def show_main(request):
    context = {
        'name': 'A. Nurcahaya Tampubolon',
        'class': 'PBP A'
    }

    return render(request, "main.html", context)
}}

kemudian buka berkas main.html yang telah dibuat sebelumnya di direktori manhwa-tracker/main/templates. Kemudian ubah nama dan kelas  menjadi kode django untuk menampilkan nilai dari variabel yang telah didefenisikan dalam context.

{{
    <h5>Name:</h5>
    <p>{{ name }}</p>
    <p></p>
    <h5>Class:</h5>
    <p>{{ class }}</p>
}}

[ ] Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py.

untuk membuat routing pada aplikasi main yaitu dengan membuat urls.py pada direktori aplikasi main kemudian menghubungkan juga dengan fungsi show_main

{{
    from django.urls import path
from main.views import show_main

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
]
}}

[ ] Melakukan deployment ke PWS terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.

Pertama, kita melakukan register di http://pbp.cs.ui.ac.id/register. Kemudian login, buat New Project sesuai dengan nama direktori kita seperti manhwatracker.
Setelah itu, pada terminal direktori utama kita ketikkan perintah berikut:

{{
    git remote add pws http://pbp.cs.ui.ac.id/a.nurcahaya/manhwatracker
    git branch -M master
    git push pws master
}}

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
