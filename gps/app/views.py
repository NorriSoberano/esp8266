# from django.shortcuts import render

# Create your views here.
# En app/views.py

from django.shortcuts import render
from django.http import JsonResponse
from .models import GPSData

def map_view(request):
    gps_data = GPSData.objects.all()
    return render(request, 'map.html', {'gps_data': gps_data})

def receive_gps(request):
    if request.method == 'POST':
        latitude = request.POST.get('latitude')
        longitude = request.POST.get('longitude')
        GPSData.objects.create(latitude=latitude, longitude=longitude)
        return JsonResponse({'status': 'success'})
    else:
        return JsonResponse({'status': 'error'})
