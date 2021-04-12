from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

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

    inventory_data_template = ()
    inventories = client.inventory_set.all()
    for inventory in inventories:
        inventory_data = inventory.inventorydata_set.all().order_by("product__name")
        

    context = {"client" : client, "inventory_data" : inventory_data_template}
    return render(request, 'eaubelix/inventory.html', context)


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
    # boiler_data = ()
    # for boiler in client.boiler_set.all():
    #     boiler_data += (boiler.name, [boiler.boiler_data.values(fieldname) for fieldname in boiler.boiler_data_shown])
    context = {'boilers' : client.boiler_set.all().order_by('name'), 'form': BoilerDataForm(), "client" : client}
    return render(request, 'eaubelix/boiler.html', context)

@login_required
@allowed_users(allowed_roles=['EAUBELIX'])
def add_boiler_data(request):
    if request.method == 'POST':
        form = BoilerDataForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
        return redirect('boilers')


@login_required
@allowed_users(allowed_roles=['EAUBELIX'])
def water_tower(request):
    if request.user.type == User.Types.OPERATOR:
        client = request.user.operatormore.client
    else:
        client = request.user

    context = {'water_towers': client.watertower_set.all().order_by('name'), 'form': WaterTowerDataForm(), "client" : client}
    return render(request, 'eaubelix/water_tower.html', context)

@login_required
@allowed_users(allowed_roles=['EAUBELIX'])
def add_water_tower_data(request):
    if request.method == 'POST':
        form = WaterTowerDataForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
        return redirect('water_towers')


@login_required
@allowed_users(allowed_roles=['EAUBELIX'])
def closed_networks(request):
    if request.user.type == User.Types.OPERATOR:
        client = request.user.operatormore.client
    else:
        client = request.user

    context = {'closed_networks': client.closednetwork_set.all().order_by('name'), 'form': ClosedNetworkDataForm(), "client" : client}
    return render(request, 'eaubelix/closed_networks.html', context)

def add_closed_network_data(request):
    if request.method == 'POST':
        form = ClosedNetworkDataForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
        return redirect('closed_networks')