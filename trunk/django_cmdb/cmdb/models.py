from django.db import models
from django.contrib.auth.models import Group, User
from django.utils.http import urlquote
import settings

class Schema(models.Model):

    path = models.CharField('Path', max_length=255, blank=True, unique=True)
    module_name = models.CharField('Module Name', max_length=1024, blank=True)
    class_name = models.CharField('Class', max_length=1024, blank=True)
    edit_form = models.CharField('Edit Form', max_length=1024, blank=True)
    view_form = models.CharField('View Form', max_length=1024, blank=True)
    add_form = models.CharField('Add Form', max_length=1024,  blank=True)
    form_name = models.CharField('Form Name', max_length=1024, blank=True)
    edit_form_name = models.CharField('Edit Form Name', max_length=1024, blank=True)

    def __unicode__(self):
                return u'''%s''' % self.path
                                
class ConfigurationItem(models.Model):

    path = models.CharField('Path', max_length=1024)
    name = models.CharField('Name', max_length=1024)
    description = models.CharField('Description', max_length=1024, blank=True)
    active = models.BooleanField('Active', default=True)
    is_leaf = models.BooleanField('Is a Leaf item', default=False)
    date_created = models.DateTimeField('Date Created', auto_now_add=True)
    date_modified = models.DateTimeField('Date Modified', auto_now=True)
    extension_attribute_1 = models.CharField('Extension Attribute 1', max_length=255, blank=True)
    extension_attribute_2 = models.CharField('Extension Attribute 2',max_length=255, blank=True)
    extension_attribute_3 = models.CharField('Extension Attribute 3',max_length=255, blank=True)
    extension_attribute_4 = models.CharField('Extension Attribute 4',max_length=255, blank=True)
    extension_attribute_5 = models.CharField('Extension Attribute 5',max_length=255, blank=True)
    extension_attribute_6 = models.CharField('Extension Attribute 6',max_length=255, blank=True)
    extension_attribute_7 = models.CharField('Extension Attribute 7',max_length=255, blank=True)
    extension_attribute_8 = models.CharField('Extension Attribute 8',max_length=255, blank=True)
    extension_attribute_9 = models.CharField('Extension Attribute 9',max_length=255, blank=True)
    extension_attribute_10 = models.CharField('Extension Attribute 10',max_length=255, blank=True)
    extension_attribute_11 = models.BooleanField()
      
    def __unicode__(self):
        return u'''%s''' % self.path

    def get_absolute_url(self):
        return self.path
        
    class Meta:
            ordering = ["path"]

class Device(ConfigurationItem):

    DEPLOYMENT_STATUS = (
        ('Awaiting Decommission', 'Awaiting Decommission'),
        ('Awaiting Deployment', 'Awaiting Deployment'),
        ('Client Development', 'Client Development'),
        ('Critical', 'Critical'),
        ('Internal Development', 'Internal Development'),
        ('Production', 'Production'),
    )

    asset_tag = models.CharField('Asset Tag', max_length=255, blank=True)
    serial_number = models.CharField('Serial Number', max_length=255, blank=True)
    location = models.ForeignKey(ConfigurationItem, verbose_name='Location',
            related_name="devices_in_location")
    model = models.ForeignKey(ConfigurationItem, verbose_name='Model',
            related_name="devices_of_type")
    machine_type = models.CharField('Machine Type', max_length=255, blank=True)
    company = models.ForeignKey(ConfigurationItem, verbose_name='Company',
            related_name="devices_in_company")
    ip_addresses = models.CharField('IP Address', max_length=1024, blank=True)
    purchase_date = models.DateField('Purchase Date', blank=True, null=True)
    warranty_expire = models.DateField('Warranty Expire', blank=True, null=True)
    url = models.URLField('URL', blank=True)
    soc_number = models.CharField('PO/SOC Number', max_length=1024, blank=True)
    in_scope = models.BooleanField('Compliance In Scope', default=False)
    alert_group = models.TextField('Alert Group', blank=True)
    notify_group = models.TextField('Notify Group', blank=True)
    deployment_status = models.CharField('Deployment Status', max_length=255, blank=True, choices=DEPLOYMENT_STATUS)
    sku_number = models.TextField('SKU Number', max_length=255, blank=True)
    purchase_price = models.FloatField(blank=True)
    depreciation_period = models.IntegerField(blank=True)
    depreciation_start_date = models.DateField(blank=True)
    invoice_number = models.TextField(max_length=255, blank=True)



class OperatingSystem(ConfigurationItem):

    icon = models.ImageField(upload_to="os_icons", blank=True)
    telnet_connections = models.BooleanField()
    ssh_connections = models.BooleanField()
    http_connections = models.BooleanField()
    telnet_connections = models.BooleanField()
    rdp_connections = models.BooleanField()
    vnc_connections = models.BooleanField()

class Server(Device):

    operating_system = models.ForeignKey(OperatingSystem, verbose_name='Operating System')
    authentication_source = models.ForeignKey(ConfigurationItem,
            verbose_name='Authentication Source',
            related_name='servers_in_authentication_source')
    patching_system = models.ForeignKey(ConfigurationItem,
            verbose_name='Patching System',
            related_name='servers_in_patching_system')
    backup_system = models.ForeignKey(ConfigurationItem, 
            verbose_name='Backup System', related_name='servers_in_backup_system')

class Location(ConfigurationItem):

    address = models.CharField(max_length=1024, blank=True)
    phoneNumber = models.CharField(max_length=255, blank=True)
    url = models.URLField(blank=True)
    read_acl = models.ManyToManyField(Group, related_name='location_readACL', blank=True, default=None)
    write_acl = models.ManyToManyField(Group, related_name='location_writeACL', blank=True, default=None)
    alert_group= models.EmailField(blank=True)

class People(ConfigurationItem):

    first_name = models.CharField(max_length=1024)
    last_name = models.CharField(max_length=1024)
    user_principal_name = models.CharField(max_length=1024)
    email = models.CharField(max_length=1024)
    job_title = models.CharField(max_length=1024, blank=True)
    telephone_number = models.CharField(max_length=1024, blank=True)
    extension_number = models.CharField(max_length=1024, blank=True)
    company = models.ForeignKey(ConfigurationItem, related_name='personCompany', blank=True, null=True)
    last_updated = models.DateTimeField(auto_now=True)
    created_date = models.DateTimeField(auto_now_add=True)
    object_sid = models.CharField(max_length=1024)

class Computer(Device):

    user = models.ForeignKey(People, verbose_name='User', related_name='computerUser', blank=True, null=True)
    assigned_devices = models.ManyToManyField(Device, related_name='computerDevices', blank=True)
    mac_address = models.CharField('MAC Address', max_length=32, blank=True)

class Company(ConfigurationItem):

    address = models.CharField(max_length=1024, blank=True)
    phoneNumber = models.CharField(max_length=255, blank=True)
    url = models.URLField(blank=True)
    read_acl = models.ManyToManyField(Group, related_name='company_readACL', blank=True, default=None)
    write_acl = models.ManyToManyField(Group, related_name='company_writeACL', blank=True, default=None)
    alert_group = models.EmailField(blank=True)

class System(ConfigurationItem):

    device_list = models.ManyToManyField(ConfigurationItem, related_name='systemDevices', blank=True)
    alert_group = models.TextField('Alert Group', blank=True)
    notify_group = models.TextField('Notify Group', blank=True)
    company = models.ForeignKey(ConfigurationItem, related_name='systemCompany')
    url = models.URLField(blank=True)
    dynamic_query = models.CharField('Dynamic Query String', max_length=1024, blank=True)
                
class ServiceAccount(ConfigurationItem):

    realm = models.CharField(max_length=1024)
    bind_dn = models.CharField(max_length=1024)
    bind_pw = models.CharField(max_length=1024)
    base_dn = models.CharField(max_length=1024)
    ldap_servers = models.CharField(max_length=1024)

class ADImportLocation(ConfigurationItem):

    ou = models.CharField(max_length=1024)
    credentials = models.ForeignKey(ServiceAccount, related_name='importLocationCredentials')
    company = models.ForeignKey(Company, related_name='importLocationCompany')
    exclude_group = models.CharField(max_length=255, blank=True)

class IPNetwork(ConfigurationItem):

    NETWORK_TYPES = (
        ('Internal', 'Internal'),
        ('DMZ', 'DMZ'),
        ('Storage', 'Storage'),
    )

    ip_address = models.IPAddressField()
    subnet_length = models.IntegerField()
    network_type = models.CharField(max_length=255, choices=NETWORK_TYPES)

class HistoryLog(models.Model):       

    LOG_UPDATE_TYPES = (
        ('CI Creation', 'CI Creation'),
        ('CI Modification', 'CI Modification'),
        ('CI Decommission', 'CI Decommission'),
    )

    date = models.DateTimeField(auto_now_add=True)
    device = models.ForeignKey(ConfigurationItem, related_name='deviceLog')
    user = models.CharField(max_length=1024)
    change_type = models.CharField(max_length=1024, choices=LOG_UPDATE_TYPES)
    info = models.CharField(max_length=1024)

class AlertProfile(models.Model):

    user = models.ForeignKey(User, unique=True)
    alert_device_classes = models.ManyToManyField(ConfigurationItem, related_name='userAlertDeviceClass')
    alert_locations = models.ManyToManyField(Location, related_name='userAlertLocation')
    alert_email = models.BooleanField()
    alert_system = models.BooleanField()
    alert_incident = models.BooleanField()
    alert_rfc = models.BooleanField()
        
    def __str__(self):
        return '''%s Alert Profile''' % self.user.username
