from django.shortcuts import render
from .models import ceos
# Create your views here.
def index(request):

    Ceos = ceos.objects.all()

    return render(
        request,
        "index.html",
        context={"Ceos": Ceos},
    )