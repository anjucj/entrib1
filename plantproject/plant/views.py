from django.shortcuts import render

from django.views.decorators.cache import cache_page
# Create your views here.

def index(request):
    return render(request, 'plant.html')




@cache_page(60 * 1)  # Cache the view for 1 minutes
def indexs(request):
    return render(request, 'index.html')