from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from core.decorators import allowed_users
from core.models import *

from .forms import *


# Create your views here.
@login_required
@allowed_users(allowed_roles=['EAUBELIX'])
def eaubelix(request):
    context = {}
    return render(request, 'eaubelix/eaubelix_dashboard.html', context)

@login_required
@allowed_users(allowed_roles=['EAUBELIX'])
def inventory(request):
    context = {}
    return render(request, 'eaubelix/inventory.html', context)


@login_required
@allowed_users(allowed_roles=['EAUBELIX'])
def pretreatment(request):
    context = {}
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
    context = {'boilers' : client.boiler_set.all(), 'form': BoilerDataForm()}
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
    # water_tower_data = ()
    # for water_tower in client.watertower_set.all():
    #     water_tower_data += (water_tower.name, [water_tower.water_tower_data.values(fieldname) for fieldname in water_tower.water_tower_data_shown])
    context = {'water_towers': client.watertower_set.all(), 'form': WaterTowerDataForm()}
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
    context = {}
    return render(request, 'eaubelix/closed_networks.html', context)
