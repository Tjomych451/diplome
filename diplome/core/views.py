from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Master, Service
from .forms import VisitForm

def main_page(request):
    masters = Master.objects.all()
    form = VisitForm()
    return render(request, 'core/main.html', {'masters': masters, 'form': form})

def thank_you(request):
    return render(request, 'core/thank_you.html')

def get_services(request, master_id):
    services = Service.objects.filter(masters__id=master_id)
    data = [{'id': service.id, 'name': service.name} for service in services]
    return JsonResponse(data, safe=False)
