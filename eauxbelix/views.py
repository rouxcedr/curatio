from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from collections import defaultdict

from core.decorators import allowed_users
from core.models import *

from .forms import *


# Create your views here.
@login_required
@allowed_users(allowed_roles=['EAUBELIX'])
def eaubelix(request):
    if request.user.type == User.Types.OPERATOR:
        client = request.user.operatormore.client
    else :
        client = request.user
    context = {"client" : client}
    print(client.boiler_set.all().order_by('name'))
    return render(request, 'eaubelix/eaubelix_dashboard.html', context)

@login_required
@allowed_users(allowed_roles=['EAUBELIX'])
def inventory(request):
    if request.user.type == User.Types.OPERATOR:
        client = request.user.operatormore.client
    else :
        client = request.user
    inventory_data_template = defaultdict(list)
    inventory_data = client.inventory.inventorydata_set.all().order_by("product__name", "-date")
    for data in inventory_data:
        inventory_data_template[data.product.name].append(data)
    print(inventory_data_template)
    context = {"client" : client, "inventory_data" : dict(inventory_data_template), "form" : InventoryDataForm()}
    return render(request, 'eaubelix/inventory.html', context)

@login_required
@allowed_users(allowed_roles=['EAUBELIX'])
def add_inventory_data(request):
    if request.method == 'POST':
        form = InventoryDataForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
        return redirect('inventory')


@login_required
@allowed_users(allowed_roles=['EAUBELIX'])
def pretreatment(request):
    if request.user.type == User.Types.OPERATOR:
        client = request.user.operatormore.client
    else :
        client = request.user
    context = {"client" : client}
    return render(request, 'eaubelix/pretreatment.html', context)


@login_required
@allowed_users(allowed_roles=['EAUBELIX'])
def boiler(request):
    if request.user.type == User.Types.OPERATOR:
        client = request.user.operatormore.client
    else :
        client = request.user
    display_boiler_id = request.GET.get('boiler_id')
    context = {'boilers' : client.boiler_set.all().order_by('name'), 'form': BoilerDataForm(), "client" : client, "display_element_by_id" : display_boiler_id}
    return render(request, 'eaubelix/boiler.html', context)

@login_required
@allowed_users(allowed_roles=['EAUBELIX'])
def add_boiler_data(request):
    if request.method == 'POST':
        form = BoilerDataForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
        base_url = reverse("boilers")
        param = "boiler_id=" + str(form.cleaned_data['boiler'].id)
        url = '{}?{}'.format(base_url, param)
        return redirect(url)


@login_required
@allowed_users(allowed_roles=['EAUBELIX'])
def water_tower(request):
    if request.user.type == User.Types.OPERATOR:
        client = request.user.operatormore.client
    else:
        client = request.user
    display_water_tower_id = request.GET.get('water_tower_id')
    context = {'water_towers': client.watertower_set.all().order_by('name'), 'form': WaterTowerDataForm(), "client" : client, "display_element_by_id" : display_water_tower_id}
    return render(request, 'eaubelix/water_tower.html', context)

@login_required
@allowed_users(allowed_roles=['EAUBELIX'])
def add_water_tower_data(request):
    if request.method == 'POST':
        form = WaterTowerDataForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
        base_url = reverse("water_towers")
        param = "water_tower_id=" + str(form.cleaned_data['water_tower'].id)
        url = '{}?{}'.format(base_url, param)
        return redirect(url)


@login_required
@allowed_users(allowed_roles=['EAUBELIX'])
def closed_networks(request):
    if request.user.type == User.Types.OPERATOR:
        client = request.user.operatormore.client
    else:
        client = request.user
    display_closed_network_id = request.GET.get('closed_network_id')
    context = {'closed_networks': client.closednetwork_set.all().order_by('name'), 'form': ClosedNetworkDataForm(), "client" : client, "display_element_by_id" : display_closed_network_id}
    return render(request, 'eaubelix/closed_networks.html', context)

@login_required
@allowed_users(allowed_roles=['EAUBELIX'])
def add_closed_network_data(request):
    if request.method == 'POST':
        form = ClosedNetworkDataForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
        base_url = reverse("closed_networks")
        param = "closed_network_id=" + str(form.cleaned_data['closed_network'].id)
        url = '{}?{}'.format(base_url, param)
        return redirect(url)