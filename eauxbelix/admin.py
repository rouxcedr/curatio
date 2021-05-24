from django.contrib import admin
from .models import *
from .forms import *


class BoilerFormAdmin(admin.ModelAdmin):
    form = BoilerForm

class WaterTowerFormAdmin(admin.ModelAdmin):
    form = WaterTowerForm

class ClosedNetworkFormAdmin(admin.ModelAdmin):
    form = ClosedNetworkForm

class PretreatmentFormAdmin(admin.ModelAdmin):
    form = PretreatmentForm

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


admin.site.register(SoftenerMinMax)
admin.site.register(DealkalizerMinMax)
admin.site.register(ReverseOsmosisMinMax)
admin.site.register(DegasserMinMax)
admin.site.register(MixMinMax)
admin.site.register(CondensateMinMax)
admin.site.register(Pretreatment, PretreatmentFormAdmin)
admin.site.register(SoftenerData)
admin.site.register(DealkalizerData)
admin.site.register(ReverseOsmosisData)
admin.site.register(DegasserData)
admin.site.register(MixData)
admin.site.register(CondensateData)