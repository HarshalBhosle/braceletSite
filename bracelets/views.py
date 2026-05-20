from django.shortcuts import render, get_object_or_404
from .models import Bracelet
from .image_mapping import load_bracelet_image_map

bracelet_image_map = load_bracelet_image_map()

def landing_page(request):
    return render(request, 'bracelets/landing.html')

def bracelets_list(request):
    bracelets = Bracelet.objects.all()
    for bracelet in bracelets:
        bracelet.local_image = bracelet_image_map.get(bracelet.name)
    return render(request, 'bracelets/bracelets_list.html', {'bracelets': bracelets})

def bracelet_detail(request, pk):
    bracelet = get_object_or_404(Bracelet, pk=pk)
    bracelet.local_image = bracelet_image_map.get(bracelet.name)
    return render(request, 'bracelets/bracelet_detail.html', {'bracelet': bracelet})
