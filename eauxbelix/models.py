from django.db import models
from core.models import *


# Create your models here.
class Inventory(models.Model):
    name = models.CharField(max_length=100)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)

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
        return self.product.name
        # return self.inventory.name + "_" + str(self.date)

    class Meta:
        verbose_name_plural = "Inventory Data"
        verbose_name = "Inventory Data"

#------------------------------------- PRETREATMENT -------------------------------------#

class Pretreatment(models.Model):
    name = models.CharField(max_length=100)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    # min_max = models.ForeignKey(ClosedNetworkMinMax, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Pretreatment"
        verbose_name = "Pretreatments"


class PretreatmentData(models.Model):
    pass

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