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
        # self.fields['inhibitor'].widget.attrs.update(
        #     {'class': 'w3-input w3-border w3-round w3-border-black'})
        # self.fields['p'].widget.attrs.update(
        #     {'class': 'w3-input w3-border w3-round w3-border-black'})
        # self.fields['m'].widget.attrs.update(
        #     {'class': 'w3-input w3-border w3-round w3-border-black'})
        # self.fields['oh'].widget.attrs.update(
        #     {'class': 'w3-input w3-border w3-round w3-border-black'})
        # self.fields['cl'].widget.attrs.update(
        #     {'class': 'w3-input w3-border w3-round w3-border-black'})
        # self.fields['so3'].widget.attrs.update(
        #     {'class': 'w3-input w3-border w3-round w3-border-black'})
        # self.fields['cond'].widget.attrs.update(
        #     {'class': 'w3-input w3-border w3-round w3-border-black'})
        # self.fields['pointeaux'].widget.attrs.update(
        #     {'class': 'w3-input w3-border w3-round w3-border-black'})
        # self.fields['mbd'].widget.attrs.update(
        #     {'class': 'w3-input w3-border w3-round w3-border-black'})
        # self.fields['on_off'].widget.attrs.update(
        #     {'class': 'w3-input w3-border w3-round w3-border-black'})
        # self.fields['vapor_pound_kg'].widget.attrs.update(
        #     {'class': 'w3-input w3-border w3-round w3-border-black'})
        # self.fields['vaper_cond'].widget.attrs.update(
        #     {'class': 'w3-input w3-border w3-round w3-border-black'})
        #
        # self.fields['inhibitor'].label = "Inhibiteur"
        # self.fields['p'].label = "P"
        # self.fields['m'].label = "M"
        # self.fields['oh'].label = "OH"
        # self.fields['cl'].label = "Cl-"
        # self.fields['so3'].label = "SO3"
        # self.fields['cond'].label = "Cond"
        # self.fields['pointeaux'].label = "Pointeaux"
        # self.fields['mbd'].label = "MBD(s)"
        # self.fields['on_off'].label = "On / Off"
        # self.fields['vapor_pound_kg'].label = "Vapeur(lbs / kg)"
        # self.fields['vaper_cond'].label = "Vapeur(Cond)"
