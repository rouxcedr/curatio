from django.db import models
from core.models import *


# Create your models here.
class Inventory(models.Model):
    name = models.CharField(max_length=100)
    client = models.OneToOneField(Client, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Inventory"
        verbose_name = "Inventories"

class Product(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=100)
    fonction = models.CharField(max_length=100)
    format = models.CharField(max_length=100)
    min = models.IntegerField(null=True, blank=True)
    max = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Product"
        verbose_name = "Products"

class InventoryData(models.Model):
    inventory = models.ForeignKey(Inventory, on_delete=models.CASCADE)
    operator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField(auto_now_add=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.product.name + "_" + str(self.date)
        # return self.inventory.name + "_" + str(self.date)

    class Meta:
        verbose_name_plural = "Inventory Data"
        verbose_name = "Inventory Data"

#------------------------------------- PRETREATMENT -------------------------------------#

class SoftenerMinMax(models.Model):
    dt_1_min = models.FloatField()
    dt_1_max = models.FloatField()
    dt_2_min = models.FloatField()
    dt_2_max = models.FloatField()
    dt_3_min = models.FloatField()
    dt_3_max = models.FloatField()
    cond_1_min = models.FloatField()
    cond_1_max = models.FloatField()
    cond_2_min = models.FloatField()
    cond_2_max = models.FloatField()
    cond_3_min = models.FloatField()
    cond_3_max = models.FloatField()

class DealkalizerMinMax(models.Model):
    p_1_min = models.IntegerField()
    p_1_max = models.IntegerField()
    p_2_min = models.IntegerField()
    p_2_max = models.IntegerField()
    m_1_min = models.IntegerField()
    m_1_max = models.IntegerField()
    m_2_min = models.IntegerField()
    m_2_max = models.IntegerField()
    cl_min = models.IntegerField()
    cl_max = models.IntegerField()
    ph_min = models.FloatField()
    ph_max = models.FloatField()

class ReverseOsmosisMinMax(models.Model):
    cl2_min = models.FloatField()
    cl2_max = models.FloatField()
    permeat_min = models.FloatField()
    permeat_max = models.FloatField()
    reject_min = models.FloatField()
    reject_max = models.FloatField()
    recirc_min = models.FloatField()
    recirc_max = models.FloatField()
    temp_min = models.FloatField()
    temp_max = models.FloatField()
    p_in_min = models.FloatField()
    p_in_max = models.FloatField()
    p_out_min = models.FloatField()
    p_out_max = models.FloatField()
    delta_p_min = models.FloatField()
    delta_p_max = models.FloatField()
    m_min_max = models.FloatField()
    m_max = models.FloatField()
    ph_min = models.FloatField()
    ph_max = models.FloatField()

class DegasserMinMax(models.Model):
    dt_min = models.FloatField()
    dt_max = models.FloatField()
    cond_min = models.IntegerField()
    cond_max = models.IntegerField()
    ph_min = models.FloatField()
    ph_max = models.FloatField()
    p_min = models.IntegerField()
    p_max = models.IntegerField()
    m_min = models.IntegerField()
    m_max = models.IntegerField()
    cl_min = models.IntegerField()
    cl_max = models.IntegerField()
    fe_min = models.FloatField()
    fe_max = models.FloatField()
    cu_min = models.FloatField()
    cu_max = models.FloatField()
    temp_min = models.IntegerField()
    temp_max = models.IntegerField()
    inh_min = models.IntegerField()
    inh_max = models.IntegerField()
    counter_min = models.FloatField()
    counter_max = models.FloatField()

class MixMinMax(models.Model):
    dt_min = models.FloatField()
    dt_max = models.FloatField()
    cond_min = models.IntegerField()
    cond_max = models.IntegerField()
    ph_min = models.FloatField()
    ph_max = models.FloatField()
    p_min = models.IntegerField()
    p_max = models.IntegerField()
    m_min = models.IntegerField()
    m_max = models.IntegerField()
    cl_min = models.IntegerField()
    cl_max = models.IntegerField()
    fe_min = models.FloatField()
    fe_max = models.FloatField()
    cu_min = models.FloatField()
    cu_max = models.FloatField()
    temp_min = models.IntegerField()
    temp_max = models.IntegerField()
    inh_min = models.IntegerField()
    inh_max = models.IntegerField()
    counter_min = models.FloatField()
    counter_max = models.FloatField()

class CondensateMinMax(models.Model):
    dt_min = models.FloatField()
    dt_max = models.FloatField()
    cond_min = models.IntegerField()
    cond_max = models.IntegerField()
    ph_min = models.FloatField()
    ph_max = models.FloatField()
    p_min = models.IntegerField()
    p_max = models.IntegerField()
    m_min = models.IntegerField()
    m_max = models.IntegerField()
    cl_min = models.IntegerField()
    cl_max = models.IntegerField()
    fe_min = models.FloatField()
    fe_max = models.FloatField()
    cu_min = models.FloatField()
    cu_max = models.FloatField()
    temp_min = models.IntegerField()
    temp_max = models.IntegerField()
    counter_min = models.FloatField()
    counter_max = models.FloatField()



class Pretreatment(models.Model):
    name = models.CharField(max_length=100)
    client = models.OneToOneField(Client, on_delete=models.SET_NULL, null=True)

    softener_minmax = models.ForeignKey(SoftenerMinMax, on_delete=models.CASCADE)
    dealkalizer_minmax = models.ForeignKey(DealkalizerMinMax, on_delete=models.CASCADE)
    reverse_osmosis_minmax = models.ForeignKey(ReverseOsmosisMinMax, on_delete=models.CASCADE)
    degasser_minmax = models.ForeignKey(DegasserMinMax, on_delete=models.CASCADE)
    mix_minmax = models.ForeignKey(MixMinMax, on_delete=models.CASCADE)
    condensate_minmax = models.ForeignKey(CondensateMinMax, on_delete=models.CASCADE)

    class SoftenerDataShown(models.TextChoices):
        dt_1 = 'dt_1', 'D.T. #1'
        dt_2 = 'dt_2', 'D.T. #2'
        dt_3 = 'dt_3', 'D.T. #3'
        cond_1 = 'cond_1', 'Cond #1'
        cond_2 = 'cond_2', 'Cond #2'
        cond_3 = 'cond_3', 'Cond #3'

    softener_data_shown = ArrayField(
        models.CharField('Softener Data Shown', max_length=255, choices=SoftenerDataShown.choices, default=None, null=True),
    )

    class DealkalizerDataShown(models.TextChoices):
        p_1 = 'p_1', 'P #1'
        p_2 = 'p_2', 'P #2'
        m_1 = 'm_1', 'M #1'
        m_2 = 'm_2', 'M #2'
        cl = 'cl', 'Cl-'
        ph =  'ph', 'pH'

    dealkalizer_data_shown = ArrayField(
        models.CharField('Dealkalizer Data Shown', max_length=255, choices=DealkalizerDataShown.choices, default=None, null=True),
    )

    class ReverseOsmosisDataShown(models.TextChoices):
        cl2 = 'cl2', 'Cl2'
        permeat = 'permeat', 'Permeat'
        reject = 'reject', 'Rejet'
        recirc = 'recirc', 'Recirc'
        temp = 'temp', 'Temp.'
        p_in = 'p_in', 'P in'
        p_out = 'p_out', 'P out'
        delta_p = 'delta_p', 'Delta P'
        m = 'm', 'M'
        ph = 'ph', 'pH'

    reverse_osmosis_data_shown = ArrayField(
        models.CharField('Reverse Osmosis Data Shown', max_length=255, choices=ReverseOsmosisDataShown.choices, default=None, null=True),
    )

    class DegasserDataShown(models.TextChoices):
        dt = 'dt', 'D.T.'
        cond = 'cond', 'Cond'
        ph = 'ph', 'pH'
        p = 'p', 'P'
        m = 'm', 'M'
        cl = 'cl', 'Cl-'
        fe = 'fe', 'Fe'
        cu = 'cu', 'Cu'
        temp = 'temp', 'Temp'
        inh = 'inh', 'Inh.'
        counter = 'counter', 'Compteur'

    degasser_data_shown = ArrayField(
        models.CharField('Degasser Data Shown', max_length=255, choices=DegasserDataShown.choices, default=None, null=True),
    )

    class MixDataShown(models.TextChoices):
        dt = 'dt', 'D.T.'
        cond = 'cond', 'Cond'
        ph = 'ph', 'pH'
        p = 'p', 'P'
        m = 'm', 'M'
        cl = 'cl', 'Cl-'
        fe = 'fe', 'Fe'
        cu = 'cu', 'Cu'
        temp = 'temp', 'Temp'
        inh = 'inh', 'Inh.'
        counter = 'counter', 'Compteur'

    mix_data_shown = ArrayField(
        models.CharField('Mix Data Shown', max_length=255, choices=MixDataShown.choices, default=None, null=True),
    )

    class CondensateDataShown(models.TextChoices):
        dt = 'dt', 'D.T.'
        cond = 'cond', 'Cond'
        ph = 'ph', 'pH'
        p = 'p', 'P'
        m = 'm', 'M'
        cl = 'cl', 'Cl-'
        fe = 'fe', 'Fe'
        cu = 'cu', 'Cu'
        temp = 'temp', 'Temp'
        counter = 'counter', 'Compteur'

    condensate_data_shown = ArrayField(
        models.CharField('Condensate Data Shown', max_length=255, choices=CondensateDataShown.choices, default=None, null=True),
    )




    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Pretreatment"
        verbose_name = "Pretreatments"

class SoftenerData(models.Model):
    pretreatment = models.ForeignKey(Pretreatment, on_delete=models.SET_NULL, null=True, related_name="softener_data")
    date = models.DateTimeField(auto_now_add=True, blank=True)
    operator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    dt_1 = models.FloatField(null=True, blank=True)
    dt_2 = models.FloatField(null=True, blank=True)
    dt_3 = models.FloatField(null=True, blank=True)
    cond_1 = models.FloatField(null=True, blank=True)
    cond_2 = models.FloatField(null=True, blank=True)
    cond_3 = models.FloatField(null=True, blank=True)

class DealkalizerData(models.Model):
    pretreatment = models.ForeignKey(Pretreatment, on_delete=models.SET_NULL, null=True, related_name="dealkalizer_data")
    date = models.DateTimeField(auto_now_add=True, blank=True)
    operator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    p_1 = models.IntegerField(null=True, blank=True)
    p_2 = models.IntegerField(null=True, blank=True)
    m_1 = models.IntegerField(null=True, blank=True)
    m_2 = models.IntegerField(null=True, blank=True)
    cl = models.IntegerField(null=True, blank=True)
    ph = models.FloatField(null=True, blank=True)

class ReverseOsmosisData(models.Model):
    pretreatment = models.ForeignKey(Pretreatment, on_delete=models.SET_NULL, null=True, related_name="reverse_osmosis_data")
    date = models.DateTimeField(auto_now_add=True, blank=True)
    operator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    cl2 = models.FloatField(null=True, blank=True)
    permeat = models.FloatField(null=True, blank=True)
    reject = models.FloatField(null=True, blank=True)
    recirc = models.FloatField(null=True, blank=True)
    temp = models.FloatField(null=True, blank=True)
    p_in = models.FloatField(null=True, blank=True)
    p_out = models.FloatField(null=True, blank=True)
    delta_p = models.FloatField(null=True, blank=True)
    m = models.FloatField(null=True, blank=True)
    ph = models.FloatField(null=True, blank=True)

class DegasserData(models.Model):
    pretreatment = models.ForeignKey(Pretreatment, on_delete=models.SET_NULL, null=True, related_name="degasser_data")
    date = models.DateTimeField(auto_now_add=True, blank=True)
    operator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    dt = models.FloatField(null=True, blank=True)
    cond = models.IntegerField(null=True, blank=True)
    ph = models.FloatField(null=True, blank=True)
    p = models.IntegerField(null=True, blank=True)
    m = models.IntegerField(null=True, blank=True)
    cl = models.IntegerField(null=True, blank=True)
    fe = models.FloatField(null=True, blank=True)
    cu = models.FloatField(null=True, blank=True)
    temp = models.IntegerField(null=True, blank=True)
    inh = models.IntegerField(null=True, blank=True)
    counter = models.FloatField(null=True, blank=True)

class MixData(models.Model):
    pretreatment = models.ForeignKey(Pretreatment, on_delete=models.SET_NULL, null=True, related_name="mix_data")
    date = models.DateTimeField(auto_now_add=True, blank=True)
    operator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    dt = models.FloatField(null=True, blank=True)
    cond = models.IntegerField(null=True, blank=True)
    ph = models.FloatField(null=True, blank=True)
    p = models.IntegerField(null=True, blank=True)
    m = models.IntegerField(null=True, blank=True)
    cl = models.IntegerField(null=True, blank=True)
    fe = models.FloatField(null=True, blank=True)
    cu = models.FloatField(null=True, blank=True)
    temp = models.IntegerField(null=True, blank=True)
    inh = models.IntegerField(null=True, blank=True)
    counter = models.FloatField(null=True, blank=True)

class CondensateData(models.Model):
    pretreatment = models.ForeignKey(Pretreatment, on_delete=models.SET_NULL, null=True, related_name="condensate_data")
    date = models.DateTimeField(auto_now_add=True, blank=True)
    operator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    dt = models.FloatField(null=True, blank=True)
    cond = models.IntegerField(null=True, blank=True)
    ph = models.FloatField(null=True, blank=True)
    p = models.IntegerField(null=True, blank=True)
    m = models.IntegerField(null=True, blank=True)
    cl = models.IntegerField(null=True, blank=True)
    fe = models.FloatField(null=True, blank=True)
    cu = models.FloatField(null=True, blank=True)
    temp = models.IntegerField(null=True, blank=True)
    counter = models.FloatField(null=True, blank=True)


#-----------------------------------------------------------------------------------#

#------------------------------------- BOILERS -------------------------------------#


class BoilerMinMax(models.Model):
    name = models.CharField(max_length=100)
    inhibitor_min = models.IntegerField()
    inhibitor_max = models.IntegerField()
    p_min = models.IntegerField()
    p_max = models.IntegerField()
    m_min = models.IntegerField()
    m_max = models.IntegerField()
    oh_min = models.IntegerField()
    oh_max = models.IntegerField()
    cl_min = models.IntegerField()
    cl_max = models.IntegerField()
    so3_min = models.IntegerField()
    so3_max = models.IntegerField()
    cond_min = models.IntegerField()
    cond_max = models.IntegerField()
    pointeaux_min = models.FloatField()
    pointeaux_max = models.FloatField()
    mbd_min = models.IntegerField()
    mbd_max = models.IntegerField()
    on_off_min = models.BooleanField(default=True)
    on_off_max = models.BooleanField(default=False)
    vapor_pound_kg_min = models.IntegerField()
    vapor_pound_kg_max = models.IntegerField()
    vaper_cond_min = models.IntegerField()
    vaper_cond_max = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Boilers MinMax"
        verbose_name = "Boiler MinMax"

class BoilerControlChart(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Boilers Control Chart"
        verbose_name = "Boiler Control Chart"

class Boiler(models.Model):
    name = models.CharField(max_length=100)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    control_chart = models.ImageField(blank=True)
    flow_chart = models.ImageField(blank=True)
    min_max = models.ForeignKey(BoilerMinMax, on_delete=models.SET_NULL, null=True)

    class BoilerDataShown(models.TextChoices):
        inhibitor = "inhibitor", "Inhibiteur"
        p = "p", "P"
        m = "m", "M"
        oh = "oh", "OH"
        cl = "cl", "Cl-"
        so3 = "so3", "SO3"
        cond = "cond", "Cond"
        pointeaux = "pointeaux", "Pointeaux"
        mbd = "mbd", "MBD(s)"
        on_off = "on_off", "On / Off"
        vapor_pound_kg = "vapor_pound_kg", "Vapeur(lbs / kg)"
        vaper_cond = "vaper_cond", "Vapeur(Cond)"

    boiler_data_shown = ArrayField(
        models.CharField('Boiler Data Shown', max_length=255, choices=BoilerDataShown.choices, default=None, null=True),
    )
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Boilers"
        verbose_name = "Boiler"


class BoilerData(models.Model):
    boiler = models.ForeignKey(Boiler, on_delete=models.SET_NULL, null=True, related_name="boiler_data")
    date = models.DateTimeField(auto_now_add=True, blank=True)
    operator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    inhibitor = models.IntegerField(null=True, blank=True)
    p = models.IntegerField(null=True, blank=True)
    m = models.IntegerField(null=True, blank=True)
    oh = models.IntegerField(null=True, blank=True)
    cl = models.IntegerField(null=True, blank=True)
    so3 = models.IntegerField(null=True, blank=True)
    cond = models.IntegerField(null=True, blank=True)
    pointeaux = models.FloatField(null=True, blank=True)
    mbd = models.IntegerField(null=True, blank=True)
    on_off = models.BooleanField(null=True, blank=True)
    vapor_pound_kg = models.IntegerField(null=True, blank=True)
    vaper_cond = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.boiler.name + "_" + str(self.date)

    class Meta:
        verbose_name_plural = "Boilers Data"
        verbose_name = "Boiler Data"

#----------------------------------------------------------------------------------------#




#------------------------------------- WATER TOWERS -------------------------------------#

class WaterTowerMinMax(models.Model):
    name = models.CharField(max_length=100)
    Dipslide_min = models.IntegerField()
    Dipslide_max = models.IntegerField()
    inhibitor_min = models.IntegerField()
    inhibitor_max = models.IntegerField()
    cond_min = models.IntegerField()
    cond_max = models.IntegerField()
    orp_min = models.IntegerField()
    orp_max = models.IntegerField()
    cl2_libre_min = models.FloatField()
    cl2_libre_max = models.FloatField()
    atp_l_min = models.IntegerField()
    atp_l_max = models.IntegerField()
    atp_t_min = models.IntegerField()
    atp_t_max = models.IntegerField()
    atp_min_max = models.IntegerField()
    atp_max = models.IntegerField()
    iron_min = models.FloatField()
    iron_max = models.FloatField()
    copper_min = models.FloatField()
    copper_max = models.FloatField()
    p_min = models.IntegerField()
    p_max = models.IntegerField()
    m_min = models.IntegerField()
    m_max = models.IntegerField()
    cl_min = models.IntegerField()
    cl_max = models.IntegerField()
    appoint_min = models.FloatField()
    appoint_max = models.FloatField()
    purge_min = models.FloatField()
    purge_max = models.FloatField()
    cycle_min = models.FloatField()
    cycle_max = models.FloatField()
    dt_min = models.IntegerField()
    dt_max = models.IntegerField()
    ca_min = models.IntegerField()
    ca_max = models.IntegerField()
    ph_min = models.FloatField()
    ph_max = models.FloatField()
    bw_min = models.IntegerField()
    bw_max = models.IntegerField()
    p1_min = models.IntegerField()
    p1_max = models.IntegerField()
    p2_min = models.IntegerField()
    p2_max = models.IntegerField()
    p3_min = models.IntegerField()
    p3_max = models.IntegerField()
    p4_min = models.IntegerField()
    p4_max = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Water Tower MinMax"
        verbose_name = "Water Towers MinMax"

class WaterTower(models.Model):
    name = models.CharField(max_length=100)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    control_chart = models.ImageField(blank=True)
    flow_chart = models.ImageField(blank=True)
    min_max = models.ForeignKey(WaterTowerMinMax, on_delete=models.SET_NULL, null=True)

    class WaterTowerDataShown(models.TextChoices):
        Dipslide = "Dipslide", "Dipslide"
        inhibitor = "inhibitor", "Inhibiteur"
        cond = "cond", "Cond"
        orp = "orp", "ORP"
        cl2_libre = "cl2_libre", "CL2 Libre"
        atp_l = "atp_l", "ATP L"
        atp_t = "atp_t", "ATP T"
        atp = "atp", "ATP"
        iron = "iron", "Fer"
        copper = "copper", "Cuivre"
        p = "p", "P"
        m = "m", "M"
        cl = "cl", "Cl-"
        appoint = "appoint", "Appoint"
        purge = "purge", "Purge"
        cycle = "cycle", "Cycle"
        dt = "dt", "DT"
        ca = "ca", "Ca"
        ph = "ph", "pH"
        bw = "bw", "BW"
        p1 = "p1", "P1"
        p2 = "p2", "P2"
        p3 = "p3", "P3"
        p4 = "p4", "P4"

    water_tower_data_shown = ArrayField(
        models.CharField('Water Tower Data Shown', max_length=255, choices=WaterTowerDataShown.choices, default=None, null=True),
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Water Tower"
        verbose_name = "Water Towers"


class WaterTowerData(models.Model):
    water_tower = models.ForeignKey(WaterTower, on_delete=models.SET_NULL, null=True, related_name="water_tower_data")
    date = models.DateTimeField(auto_now_add=True, blank=True)
    operator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    Dipslide = models.IntegerField(null=True, blank=True)
    inhibitor = models.IntegerField(null=True, blank=True)
    cond = models.IntegerField(null=True, blank=True)
    orp = models.IntegerField(null=True, blank=True)
    cl2_libre = models.FloatField(null=True, blank=True)
    atp_l = models.IntegerField(null=True, blank=True)
    atp_t = models.IntegerField(null=True, blank=True)
    atp = models.IntegerField(null=True, blank=True)
    iron = models.FloatField(null=True, blank=True)
    copper = models.FloatField(null=True, blank=True)
    p = models.IntegerField(null=True, blank=True)
    m = models.IntegerField(null=True, blank=True)
    cl = models.IntegerField(null=True, blank=True)
    appoint = models.FloatField(null=True, blank=True)
    purge = models.FloatField(null=True, blank=True)
    cycle = models.FloatField(null=True, blank=True)
    dt = models.IntegerField(null=True, blank=True)
    ca = models.IntegerField(null=True, blank=True)
    ph = models.FloatField(null=True, blank=True)
    bw = models.IntegerField(null=True, blank=True)
    p1 = models.IntegerField(null=True, blank=True)
    p2 = models.IntegerField(null=True, blank=True)
    p3 = models.IntegerField(null=True, blank=True)
    p4 = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.water_tower.name + "_" + str(self.date)

    class Meta:
        verbose_name_plural = "Water Tower Data"
        verbose_name = "Water Towers Data"


#----------------------------------------------------------------------------------------#



#------------------------------------- CLOSED NETWORKS -------------------------------------#

class ClosedNetworkMinMax(models.Model):
    name = models.CharField(max_length=100)
    inhibitor_min = models.FloatField()
    inhibitor_max = models.FloatField()
    cond_min = models.IntegerField()
    cond_max = models.IntegerField()
    ph_min = models.FloatField()
    ph_max = models.FloatField()
    p_min = models.IntegerField()
    p_max = models.IntegerField()
    m_min = models.IntegerField()
    m_max = models.IntegerField()
    dt_min = models.IntegerField()
    dt_max = models.IntegerField()
    iron_min = models.FloatField()
    iron_max = models.FloatField()
    copper_min = models.FloatField()
    copper_max = models.FloatField()
    turb_min = models.IntegerField()
    turb_max = models.IntegerField()
    coul_min = models.IntegerField()
    coul_max = models.IntegerField()
    filter_min = models.BooleanField()
    filter_max = models.BooleanField()
    quantity_min = models.FloatField()
    quantity_max = models.FloatField()
    appoint_min = models.FloatField()
    appoint_max = models.FloatField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Closed Network MinMax"
        verbose_name = "Closed Networks MinMax"


class ClosedNetwork(models.Model):
    name = models.CharField(max_length=100)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    control_chart = models.ImageField(blank=True)
    flow_chart = models.ImageField(blank=True)
    min_max = models.ForeignKey(ClosedNetworkMinMax, on_delete=models.SET_NULL, null=True)

    class ClosedNetworkDataShown(models.TextChoices):
        inhibitor = "inhibitor", "Inhibiteur"
        cond = "cond", "Cond"
        ph = "ph", "pH"
        p = "p", "P"
        m = "m", "M"
        dt = "dt", "DT"
        iron = "iron", "Fer"
        copper = "copper", "Cuivre"
        turb = "turb", "Turb"
        coul = "coul", "Coul"
        filter = "filter", "Filtre"
        quantity = "quantity", "Quantité"
        appoint = "appoint", "Appoint"

    closed_network_data_shown = ArrayField(
        models.CharField('Closed Network Data Shown', max_length=255, choices=ClosedNetworkDataShown.choices, default=None, null=True),
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Closed Network"
        verbose_name = "Closed Networks"


class ClosedNetworkData(models.Model):
    closed_network = models.ForeignKey(ClosedNetwork, on_delete=models.SET_NULL, null=True, related_name="closed_network_data")
    date = models.DateTimeField(auto_now_add=True, blank=True)
    operator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    inhibitor = models.FloatField(null=True, blank=True)
    cond = models.IntegerField(null=True, blank=True)
    ph = models.FloatField(null=True, blank=True)
    p = models.IntegerField(null=True, blank=True)
    m = models.IntegerField(null=True, blank=True)
    dt = models.IntegerField(null=True, blank=True)
    iron = models.FloatField(null=True, blank=True)
    copper = models.FloatField(null=True, blank=True)
    turb = models.IntegerField(null=True, blank=True)
    coul = models.IntegerField(null=True, blank=True)
    filter = models.BooleanField(null=True, blank=True)
    quantity = models.FloatField(null=True, blank=True)
    appoint = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.closed_network.name + "_" + str(self.date)

    class Meta:
        verbose_name_plural = "Closed Network Data"
        verbose_name = "Closed Networks Data"