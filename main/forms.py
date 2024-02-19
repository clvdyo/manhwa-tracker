from django.forms import ModelForm
from main.models import Manhwa

class ManhwaForm(ModelForm):
    class Meta:
        model = Manhwa
        fields = ["title", "chapter", "genre", "sinopsis", "rating"]