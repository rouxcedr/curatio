from django.shortcuts import render, redirect
from .models import Formation
from .forms import FormationsForm
from core.decorators import allowed_users
import time


# Create your views here.
@allowed_users(allowed_roles=['FORMATION'])
def formations(request):
    form = FormationsForm()
    sections = ({'id': 'ANALYSIS', 'name': "Analyses", 'formations': Formation.objects.filter(section='ANALYSIS')},
                {'id': 'PRETREATMENT', 'name': "Prétraitement", 'formations': Formation.objects.filter(section='PRETREATMENT')},
                {'id': 'CHEMICAL_TREATMENT', 'name': "Traitement Chimique", 'formations': Formation.objects.filter(section='CHEMICAL_TREATMENT')},
                {'id': 'CONTROL', 'name': "Controle", 'formations': Formation.objects.filter(section='CONTROL')},
                {'id': 'WATER_TOWER', 'name': 'Tours d\'eau', 'formations': Formation.objects.filter(section='WATER_TOWER')},
                {'id': 'BOILER', 'name': 'Chaudière', 'formations': Formation.objects.filter(section='BOILER')},
                {'id': 'CLOSED_NETWORK', 'name': 'Réseaux fermés', 'formations': Formation.objects.filter(section='CLOSED_NETWORK')})

    context = {'sections':sections,
               'user': request.user,
               'formations_form': form}
    return render(request, 'formations/formations.html', context)

# def upload_formation(request):
#     if request.method == 'POST':
#         time.sleep(0.01)
#         form = FormationsForm(request.POST or None, request.FILES or None)
#         if form.is_valid():
#             form.save()
#         time.sleep(0.01)
#         return redirect('formations')
