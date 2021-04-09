from django import forms
from .models import *
from core.forms import ArrayFieldSelectMultiple

class BoilerForm(forms.ModelForm):
    class Meta:
        model = Boiler
        widgets = {
            'boiler_data_shown': ArrayFieldSelectMultiple(choices=Boiler.BoilerDataShown.choices),
            # 'boiler_data_shown': ArrayFieldSelectMultiple(choices=ClientMore.BOILER_DATA_CHOICES)
        }
        fields = '__all__'  # required for Django 3.x

class BoilerDataForm(forms.ModelForm):
    class Meta:
        model = BoilerData
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['inhibitor'].widget.attrs.update(
            {'class': 'w3-input w3-border w3-round w3-border-black'})
        self.fields['p'].widget.attrs.update(
            {'class': 'w3-input w3-border w3-round w3-border-black'})
        self.fields['m'].widget.attrs.update(
            {'class': 'w3-input w3-border w3-round w3-border-black'})
        self.fields['oh'].widget.attrs.update(
            {'class': 'w3-input w3-border w3-round w3-border-black'})
        self.fields['cl'].widget.attrs.update(
            {'class': 'w3-input w3-border w3-round w3-border-black'})
        self.fields['so3'].widget.attrs.update(
            {'class': 'w3-input w3-border w3-round w3-border-black'})
        self.fields['cond'].widget.attrs.update(
            {'class': 'w3-input w3-border w3-round w3-border-black'})
        self.fields['pointeaux'].widget.attrs.update(
            {'class': 'w3-input w3-border w3-round w3-border-black'})
        self.fields['mbd'].widget.attrs.update(
            {'class': 'w3-input w3-border w3-round w3-border-black'})
        self.fields['on_off'].widget.attrs.update(
            {'class': 'w3-input w3-border w3-round w3-border-black'})
        self.fields['vapor_pound_kg'].widget.attrs.update(
            {'class': 'w3-input w3-border w3-round w3-border-black'})
        self.fields['vaper_cond'].widget.attrs.update(
            {'class': 'w3-input w3-border w3-round w3-border-black'})
        #
        #
        self.fields['inhibitor'].label = "Inhibiteur"
        self.fields['p'].label = "P"
        self.fields['m'].label = "M"
        self.fields['oh'].label = "OH"
        self.fields['cl'].label = "Cl-"
        self.fields['so3'].label = "SO3"
        self.fields['cond'].label = "Cond"
        self.fields['pointeaux'].label = "Pointeaux"
        self.fields['mbd'].label = "MBD(s)"
        self.fields['on_off'].label = "On / Off"
        self.fields['vapor_pound_kg'].label = "Vapeur(lbs / kg)"
        self.fields['vaper_cond'].label = "Vapeur(Cond)"


class WaterTowerForm(forms.ModelForm):
    class Meta:
        model = WaterTower
        widgets = {
            'water_tower_data_shown': ArrayFieldSelectMultiple(choices=WaterTower.WaterTowerDataShown.choices),
            # 'boiler_data_shown': ArrayFieldSelectMultiple(choices=ClientMore.BOILER_DATA_CHOICES)
        }
        fields = '__all__'  # required for Django 3.x

class WaterTowerDataForm(forms.ModelForm):
    class Meta:
        model = WaterTowerData
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['Dipslide'].widget.attrs.update(
            {'class': 'w3-input w3-border w3-round w3-border-black'})
        self.fields['inhibitor'].widget.attrs.update(
            {'class': 'w3-input w3-border w3-round w3-border-black'})
        self.fields['cond'].widget.attrs.update(
            {'class': 'w3-input w3-border w3-round w3-border-black'})
        self.fields['orp'].widget.attrs.update(
            {'class': 'w3-input w3-border w3-round w3-border-black'})
        self.fields['cl2_libre'].widget.attrs.update(
            {'class': 'w3-input w3-border w3-round w3-border-black'})
        self.fields['atp_l'].widget.attrs.update(
            {'class': 'w3-input w3-border w3-round w3-border-black'})
        self.fields['atp_t'].widget.attrs.update(
            {'class': 'w3-input w3-border w3-round w3-border-black'})
        self.fields['atp'].widget.attrs.update(
            {'class': 'w3-input w3-border w3-round w3-border-black'})
        self.fields['iron'].widget.attrs.update(
            {'class': 'w3-input w3-border w3-round w3-border-black'})
        self.fields['copper'].widget.attrs.update(
            {'class': 'w3-input w3-border w3-round w3-border-black'})
        self.fields['p'].widget.attrs.update(
            {'class': 'w3-input w3-border w3-round w3-border-black'})
        self.fields['m'].widget.attrs.update(
            {'class': 'w3-input w3-border w3-round w3-border-black'})
        self.fields['cl'].widget.attrs.update(
            {'class': 'w3-input w3-border w3-round w3-border-black'})
        self.fields['appoint'].widget.attrs.update(
            {'class': 'w3-input w3-border w3-round w3-border-black'})
        self.fields['purge'].widget.attrs.update(
            {'class': 'w3-input w3-border w3-round w3-border-black'})
        self.fields['cycle'].widget.attrs.update(
            {'class': 'w3-input w3-border w3-round w3-border-black'})
        self.fields['dt'].widget.attrs.update(
            {'class': 'w3-input w3-border w3-round w3-border-black'})
        self.fields['ca'].widget.attrs.update(
            {'class': 'w3-input w3-border w3-round w3-border-black'})
        self.fields['ph'].widget.attrs.update(
            {'class': 'w3-input w3-border w3-round w3-border-black'})
        self.fields['bw'].widget.attrs.update(
            {'class': 'w3-input w3-border w3-round w3-border-black'})
        self.fields['p1'].widget.attrs.update(
            {'class': 'w3-input w3-border w3-round w3-border-black'})
        self.fields['p2'].widget.attrs.update(
            {'class': 'w3-input w3-border w3-round w3-border-black'})
        self.fields['p3'].widget.attrs.update(
            {'class': 'w3-input w3-border w3-round w3-border-black'})
        self.fields['p4'].widget.attrs.update(
            {'class': 'w3-input w3-border w3-round w3-border-black'})

        self.fields['Dipslide'].label = "Dipslide"
        self.fields['inhibitor'].label = "Inhibiteur"
        self.fields['cond'].label = "Cond"
        self.fields['orp'].label = "ORP"
        self.fields['cl2_libre'].label = "CL2 Libre"
        self.fields['atp_l'].label = "ATP L"
        self.fields['atp_t'].label = "ATP T"
        self.fields['atp'].label = "ATP"
        self.fields['iron'].label = "Fer"
        self.fields['copper'].label = "Cuivre"
        self.fields['p'].label = "P"
        self.fields['m'].label = "M"
        self.fields['cl'].label = "Cl-"
        self.fields['appoint'].label = "Appoint"
        self.fields['purge'].label = "Purge"
        self.fields['cycle'].label = "Cycle"
        self.fields['dt'].label = "DT"
        self.fields['ca'].label = "Ca"
        self.fields['ph'].label = "pH"
        self.fields['bw'].label = "BW"
        self.fields['p1'].label = "P1"
        self.fields['p2'].label = "P2"
        self.fields['p3'].label = "P3"
        self.fields['p4'].label = "P4"

class ClosedNetworkForm(forms.ModelForm):
    class Meta:
        model = ClosedNetwork
        widgets = {
            'closed_network_data_shown': ArrayFieldSelectMultiple(choices=ClosedNetwork.ClosedNetworkDataShown.choices),
            # 'boiler_data_shown': ArrayFieldSelectMultiple(choices=ClientMore.BOILER_DATA_CHOICES)
        }
        fields = '__all__'  # required for Django 3.x

class ClosedNetworkDataForm(forms.ModelForm):
    class Meta:
        model = ClosedNetworkData
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['inhibitor'].widget.attrs.update(
            {'class': 'w3-input w3-border w3-round w3-border-black'})
        self.fields['cond'].widget.attrs.update(
            {'class': 'w3-input w3-border w3-round w3-border-black'})
        self.fields['ph'].widget.attrs.update(
            {'class': 'w3-input w3-border w3-round w3-border-black'})
        self.fields['p'].widget.attrs.update(
            {'class': 'w3-input w3-border w3-round w3-border-black'})
        self.fields['m'].widget.attrs.update(
            {'class': 'w3-input w3-border w3-round w3-border-black'})
        self.fields['dt'].widget.attrs.update(
            {'class': 'w3-input w3-border w3-round w3-border-black'})
        self.fields['iron'].widget.attrs.update(
            {'class': 'w3-input w3-border w3-round w3-border-black'})
        self.fields['copper'].widget.attrs.update(
            {'class': 'w3-input w3-border w3-round w3-border-black'})
        self.fields['turb'].widget.attrs.update(
            {'class': 'w3-input w3-border w3-round w3-border-black'})
        self.fields['coul'].widget.attrs.update(
            {'class': 'w3-input w3-border w3-round w3-border-black'})
        self.fields['filter'].widget.attrs.update(
            {'class': 'w3-input w3-border w3-round w3-border-black'})
        self.fields['quantity'].widget.attrs.update(
            {'class': 'w3-input w3-border w3-round w3-border-black'})
        self.fields['appoint'].widget.attrs.update(
            {'class': 'w3-input w3-border w3-round w3-border-black'})

        self.fields['inhibitor'].label = "Inhibiteur"
        self.fields['cond'].label = "Cond"
        self.fields['ph'].label = "pH"
        self.fields['p'].label = "P"
        self.fields['m'].label = "M"
        self.fields['dt'].label = "DT"
        self.fields['iron'].label = "Fer"
        self.fields['copper'].label = "Cuivre"
        self.fields['turb'].label = "Turb"
        self.fields['coul'].label = "Coul"
        self.fields['filter'].label = "Filtre"
        self.fields['quantity'].label = "Quantité"
        self.fields['appoint'].label = "Appoint"
