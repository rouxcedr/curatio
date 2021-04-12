from django.urls import include, path
from . import views

urlpatterns = [
    path('eaubelix/home', views.eaubelix, name='eaubelix'),
    path('eaubelix/boilers', views.boiler, name='boilers'),
    path('eaubelix/add_boiler_data', views.add_boiler_data, name='add_boiler_data'),
    path('eaubelix/water_towers', views.water_tower, name='water_towers'),
    path('eaubelix/add_water_tower_data', views.add_water_tower_data, name='add_water_tower_data'),
    path('eaubelix/closed_networks', views.closed_networks, name='closed_networks'),
    path('eaubelix/add_closed_network_data', views.add_closed_network_data, name='add_closed_network_data'),
    path('eaubelix/inventory', views.inventory, name='inventory'),
    path('eaubelix/add_inventory_data', views.add_inventory_data, name='add_inventory_data'),
    path('eaubelix/pretreatment', views.pretreatment, name='pretreatment'),

]
