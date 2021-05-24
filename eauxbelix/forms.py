from django import forms
from .models import *
from core.forms import ArrayFieldSelectMultiple


class BoilerForm(forms.ModelForm):
    class Meta:
        model = Boiler
        widgets = {
            'boiler_data_shown': ArrayFieldSelectMultiple(choices=Boiler.BoilerDataShown.choices),
        }
        fields = '__all__'


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
        }
        fields = '__all__'


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
        }
        fields = '__all__'


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


class InventoryDataForm(forms.ModelForm):
    class Meta:
        model = InventoryData
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['product'].widget.attrs.update(
            {'class': 'w3-input w3-border w3-round w3-border-black'})
        self.fields['quantity'].widget.attrs.update(
            {'class': 'w3-input w3-border w3-round w3-border-black'})

        self.fields['product'].label = "Produit"
        self.fields['quantity'].label = "Quantité"


class PretreatmentForm(forms.ModelForm):
    class Meta:
        model = Boiler
        widgets = {
            'softener_data_shown': ArrayFieldSelectMultiple(choices=Pretreatment.SoftenerDataShown.choices),
            'dealkalizer_data_shown': ArrayFieldSelectMultiple(choices=Pretreatment.DealkalizerDataShown.choices),
            'reverse_osmosis_data_shown': ArrayFieldSelectMultiple(choices=Pretreatment.ReverseOsmosisDataShown.choices),
            'degasser_data_shown': ArrayFieldSelectMultiple(choices=Pretreatment.DegasserDataShown.choices),
            'mix_data_shown': ArrayFieldSelectMultiple(choices=Pretreatment.MixDataShown.choices),
            'condensate_data_shown': ArrayFieldSelectMultiple(choices=Pretreatment.CondensateDataShown.choices),
        }
        fields = '__all__'


class SoftenerDataForm(forms.ModelForm):
    class Meta:
        model = SoftenerData
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['dt_1'].widget.attrs.update({'class': 'w3-input w3-border w3-round w3-border-black'})
        self.fields['dt_2'].widget.attrs.update({'class': 'w3-input w3-border w3-round w3-border-black'})
        self.fields['dt_3'].widget.attrs.update({'class': 'w3-input w3-border w3-round w3-border-black'})
        self.fields['cond_1'].widget.attrs.update({'class': 'w3-input w3-border w3-round w3-border-black'})
        self.fields['cond_2'].widget.attrs.update({'class': 'w3-input w3-border w3-round w3-border-black'})
        self.fields['cond_3'].widget.attrs.update({'class': 'w3-input w3-border w3-round w3-border-black'})

        self.fields['dt_1'].label = 'D.T. #1'
        self.fields['dt_2'].label = 'D.T. #2'
        self.fields['dt_3'].label = 'D.T. #3'
        self.fields['cond_1'].label = 'Cond #1'
        self.fields['cond_2'].label = 'Cond #2'
        self.fields['cond_3'].label = 'Cond #3'


class DealkalizerDataForm(forms.ModelForm):
    class Meta:
        model = DealkalizerData
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['p_1'].widget.attrs.update({'class': 'w3-input w3-border w3-round w3-border-black'})
        self.fields['p_2'].widget.attrs.update({'class': 'w3-input w3-border w3-round w3-border-black'})
        self.fields['m_1'].widget.attrs.update({'class': 'w3-input w3-border w3-round w3-border-black'})
        self.fields['m_2'].widget.attrs.update({'class': 'w3-input w3-border w3-round w3-border-black'})
        self.fields['cl'].widget.attrs.update({'class': 'w3-input w3-border w3-round w3-border-black'})
        self.fields['ph'].widget.attrs.update({'class': 'w3-input w3-border w3-round w3-border-black'})

        self.fields['p_1'].label = 'P #1'
        self.fields['p_2'].label = 'P #2'
        self.fields['m_1'].label = 'M #1'
        self.fields['m_2'].label = 'M #2'
        self.fields['cl'].label = 'Cl-'
        self.fields['ph'].label = 'pH'


class ReverseOsmosisDataForm(forms.ModelForm):
    class Meta:
        model = ReverseOsmosisData
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cl2'].widget.attrs.update({'class': 'w3-input w3-border w3-round w3-border-black'})
        self.fields['permeat'].widget.attrs.update({'class': 'w3-input w3-border w3-round w3-border-black'})
        self.fields['reject'].widget.attrs.update({'class': 'w3-input w3-border w3-round w3-border-black'})
        self.fields['recirc'].widget.attrs.update({'class': 'w3-input w3-border w3-round w3-border-black'})
        self.fields['temp'].widget.attrs.update({'class': 'w3-input w3-border w3-round w3-border-black'})
        self.fields['p_in'].widget.attrs.update({'class': 'w3-input w3-border w3-round w3-border-black'})
        self.fields['p_out'].widget.attrs.update({'class': 'w3-input w3-border w3-round w3-border-black'})
        self.fields['delta_p'].widget.attrs.update({'class': 'w3-input w3-border w3-round w3-border-black'})
        self.fields['m'].widget.attrs.update({'class': 'w3-input w3-border w3-round w3-border-black'})
        self.fields['ph'].widget.attrs.update({'class': 'w3-input w3-border w3-round w3-border-black'})

        self.fields['cl2'].label = 'Cl2'
        self.fields['permeat'].label = 'Permeat'
        self.fields['reject'].label = 'Rejet'
        self.fields['recirc'].label = 'Recirc'
        self.fields['temp'].label = 'Temp.'
        self.fields['p_in'].label = 'P in'
        self.fields['p_out'].label = 'P out'
        self.fields['delta_p'].label = 'Delta P'
        self.fields['m'].label = 'M'
        self.fields['ph'].label = 'pH'


class DegasserDataForm(forms.ModelForm):
    class Meta:
        model = DegasserData
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['dt'].widget.attrs.update({'class': 'w3-input w3-border w3-round w3-border-black'})
        self.fields['cond'].widget.attrs.update({'class': 'w3-input w3-border w3-round w3-border-black'})
        self.fields['ph'].widget.attrs.update({'class': 'w3-input w3-border w3-round w3-border-black'})
        self.fields['p'].widget.attrs.update({'class': 'w3-input w3-border w3-round w3-border-black'})
        self.fields['m'].widget.attrs.update({'class': 'w3-input w3-border w3-round w3-border-black'})
        self.fields['cl'].widget.attrs.update({'class': 'w3-input w3-border w3-round w3-border-black'})
        self.fields['fe'].widget.attrs.update({'class': 'w3-input w3-border w3-round w3-border-black'})
        self.fields['cu'].widget.attrs.update({'class': 'w3-input w3-border w3-round w3-border-black'})
        self.fields['temp'].widget.attrs.update({'class': 'w3-input w3-border w3-round w3-border-black'})
        self.fields['inh'].widget.attrs.update({'class': 'w3-input w3-border w3-round w3-border-black'})
        self.fields['counter'].widget.attrs.update({'class': 'w3-input w3-border w3-round w3-border-black'})

        self.fields['dt'].label = 'D.T.'
        self.fields['cond'].label = 'Cond'
        self.fields['ph'].label = 'pH'
        self.fields['p'].label = 'P'
        self.fields['m'].label = 'M'
        self.fields['cl'].label = 'Cl-'
        self.fields['fe'].label = 'Fe'
        self.fields['cu'].label = 'Cu'
        self.fields['temp'].label = 'Temp'
        self.fields['inh'].label = 'Inh.'
        self.fields['counter'].label = 'Compteur'


class MixDataForm(forms.ModelForm):
    class Meta:
        model = MixData
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['dt'].widget.attrs.update({'class': 'w3-input w3-border w3-round w3-border-black'})
        self.fields['cond'].widget.attrs.update({'class': 'w3-input w3-border w3-round w3-border-black'})
        self.fields['ph'].widget.attrs.update({'class': 'w3-input w3-border w3-round w3-border-black'})
        self.fields['p'].widget.attrs.update({'class': 'w3-input w3-border w3-round w3-border-black'})
        self.fields['m'].widget.attrs.update({'class': 'w3-input w3-border w3-round w3-border-black'})
        self.fields['cl'].widget.attrs.update({'class': 'w3-input w3-border w3-round w3-border-black'})
        self.fields['fe'].widget.attrs.update({'class': 'w3-input w3-border w3-round w3-border-black'})
        self.fields['cu'].widget.attrs.update({'class': 'w3-input w3-border w3-round w3-border-black'})
        self.fields['temp'].widget.attrs.update({'class': 'w3-input w3-border w3-round w3-border-black'})
        self.fields['inh'].widget.attrs.update({'class': 'w3-input w3-border w3-round w3-border-black'})
        self.fields['counter'].widget.attrs.update({'class': 'w3-input w3-border w3-round w3-border-black'})

        self.fields['dt'].label = 'D.T.'
        self.fields['cond'].label = 'Cond'
        self.fields['ph'].label = 'pH'
        self.fields['p'].label = 'P'
        self.fields['m'].label = 'M'
        self.fields['cl'].label = 'Cl-'
        self.fields['fe'].label = 'Fe'
        self.fields['cu'].label = 'Cu'
        self.fields['temp'].label = 'Temp'
        self.fields['inh'].label = 'Inh.'
        self.fields['counter'].label = 'Compteur'


class CondensateDataForm(forms.ModelForm):
    class Meta:
        model = CondensateData
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['dt'].widget.attrs.update({'class': 'w3-input w3-border w3-round w3-border-black'})
        self.fields['cond'].widget.attrs.update({'class': 'w3-input w3-border w3-round w3-border-black'})
        self.fields['ph'].widget.attrs.update({'class': 'w3-input w3-border w3-round w3-border-black'})
        self.fields['p'].widget.attrs.update({'class': 'w3-input w3-border w3-round w3-border-black'})
        self.fields['m'].widget.attrs.update({'class': 'w3-input w3-border w3-round w3-border-black'})
        self.fields['cl'].widget.attrs.update({'class': 'w3-input w3-border w3-round w3-border-black'})
        self.fields['fe'].widget.attrs.update({'class': 'w3-input w3-border w3-round w3-border-black'})
        self.fields['cu'].widget.attrs.update({'class': 'w3-input w3-border w3-round w3-border-black'})
        self.fields['temp'].widget.attrs.update({'class': 'w3-input w3-border w3-round w3-border-black'})
        self.fields['counter'].widget.attrs.update({'class': 'w3-input w3-border w3-round w3-border-black'})

        self.fields['dt'].label = 'D.T.'
        self.fields['cond'].label = 'Cond'
        self.fields['ph'].label = 'pH'
        self.fields['p'].label = 'P'
        self.fields['m'].label = 'M'
        self.fields['cl'].label = 'Cl-'
        self.fields['fe'].label = 'Fe'
        self.fields['cu'].label = 'Cu'
        self.fields['temp'].label = 'Temp'
        self.fields['counter'].label = 'Compteur'