from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render, get_object_or_404
from .forms import BraceletForm
from .models import Bracelet
from .image_mapping import load_bracelet_image_map

bracelet_image_map = load_bracelet_image_map()


def landing_page(request):
    bracelets = Bracelet.objects.order_by('-created_at')[:9]
    for bracelet in bracelets:
        bracelet.local_image = bracelet_image_map.get(bracelet.name)
    return render(request, 'bracelets/landing.html', {'bracelets': bracelets})


def bracelets_list(request):
    qs = Bracelet.objects.all()

    # Filters from GET
    q = request.GET.get('q')
    material = request.GET.get('material')
    color = request.GET.get('color')
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    in_stock = request.GET.get('in_stock')
    sort = request.GET.get('sort')

    if q:
        qs = qs.filter(name__icontains=q) | qs.filter(description__icontains=q)
    if material:
        qs = qs.filter(material__iexact=material)
    if color:
        qs = qs.filter(color__iexact=color)
    if min_price:
        try:
            qs = qs.filter(price__gte=float(min_price))
        except ValueError:
            pass
    if max_price:
        try:
            qs = qs.filter(price__lte=float(max_price))
        except ValueError:
            pass
    if in_stock:
        if in_stock.lower() in ['1', 'true', 'yes', 'on']:
            qs = qs.filter(stock__gt=0)

    # Sorting
    sort_map = {
        'new': '-created_at',
        'price_asc': 'price',
        'price_desc': '-price',
        'name_asc': 'name',
        'name_desc': '-name'
    }
    order = sort_map.get(sort or 'new', '-created_at')
    qs = qs.order_by(order)

    bracelets = list(qs)
    for bracelet in bracelets:
        bracelet.local_image = bracelet_image_map.get(bracelet.name)

    # values for filter controls
    materials = Bracelet.objects.values_list('material', flat=True).distinct()
    colors = Bracelet.objects.values_list('color', flat=True).distinct()

    return render(request, 'bracelets/bracelets_list.html', {
        'bracelets': bracelets,
        'materials': materials,
        'colors': colors,
        'current_filters': request.GET.dict(),
        'selected_sort': sort or 'new',
    })


def bracelet_detail(request, pk):
    bracelet = get_object_or_404(Bracelet, pk=pk)
    bracelet.local_image = bracelet_image_map.get(bracelet.name)
    return render(request, 'bracelets/bracelet_detail.html', {'bracelet': bracelet})


@login_required(login_url='login_admin')
def admin_dashboard(request):
    bracelets = Bracelet.objects.order_by('-created_at')
    for bracelet in bracelets:
        bracelet.local_image = bracelet_image_map.get(bracelet.name)
    return render(request, 'bracelets/admin_dashboard.html', {'bracelets': bracelets})


@login_required(login_url='login_admin')
def create_bracelet(request):
    if request.method == 'POST':
        form = BraceletForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('admin_dashboard')
    else:
        form = BraceletForm()
    return render(request, 'bracelets/bracelet_form.html', {'form': form, 'title': 'Add Bracelet'})


@login_required(login_url='login_admin')
def update_bracelet(request, pk):
    bracelet = get_object_or_404(Bracelet, pk=pk)
    if request.method == 'POST':
        form = BraceletForm(request.POST, request.FILES, instance=bracelet)
        if form.is_valid():
            form.save()
            return redirect('admin_dashboard')
    else:
        form = BraceletForm(instance=bracelet)
    return render(request, 'bracelets/bracelet_form.html', {'form': form, 'title': 'Edit Bracelet'})


@login_required(login_url='login_admin')
def delete_bracelet(request, pk):
    bracelet = get_object_or_404(Bracelet, pk=pk)
    if request.method == 'POST':
        bracelet.delete()
        return redirect('admin_dashboard')
    return render(request, 'bracelets/bracelet_confirm_delete.html', {'bracelet': bracelet})
