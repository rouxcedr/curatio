from django.contrib import admin
from .models import *
from .forms import *


class BoilerFormAdmin(admin.ModelAdmin):
    form = BoilerForm

class WaterTowerFormAdmin(admin.ModelAdmin):
    form = WaterTowerForm

class ClosedNetworkFormAdmin(admin.ModelAdmin):
    form = ClosedNetworkForm

# Register your models here.
admin.site.register(BoilerMinMax)
admin.site.register(Boiler, BoilerFormAdmin)
admin.site.register(BoilerData)

admin.site.register(WaterTowerMinMax)
admin.site.register(WaterTower, WaterTowerFormAdmin)
admin.site.register(WaterTowerData)

admin.site.register(ClosedNetworkMinMax)
admin.site.register(ClosedNetwork, ClosedNetworkFormAdmin)
admin.site.register(ClosedNetworkData)


# admin.site.register(InventoryMinMax)
admin.site.register(Inventory)
admin.site.register(InventoryData)
admin.site.register(Product)

admin.site.register(Pretreatment)