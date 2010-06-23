import sys
import logging
logging.basicConfig(level=logging.DEBUG)

from django.core.management import setup_environ
sys.path.append('.')
import settings
setup_environ(settings)

from cmdb.models import *


logging.debug('**** Loading Initial Schema')

Schema(path='/', module_name='cmdb', class_name='ConfigurationItem',
    edit_template='cmdb/ci-edit.html', view_template='cmdb/ci-view.html',
    add_template='cmdb/ci-add.html', form_name='CIForm',
    edit_form_name='CIEditForm').save()
logging.debug('Loaded schema for /')

Schema(path='/Devices', module_name='cmdb', class_name='Device',
    edit_template='cmdb/device-edit.html', view_template='cmdb/device-view.html',
    add_template='cmdb/device-add.html', form_name='DeviceForm',
    edit_form_name='DeviceEditForm').save()
logging.debug('Loaded schema for /Devices')

Schema(path='/Devices/Servers', module_name='cmdb', class_name='Server',
    edit_template='cmdb/server-edit.html', view_template='cmdb/server-view.html',
    add_template='cmdb/server-add.html', form_name='ServerForm',
    edit_form_name='ServerEditForm').save()
logging.debug('Loaded schema for /Devices/Servers')

Schema(path='/Company', module_name='cmdb', class_name='Company',
    edit_template='cmdb/company-edit.html', view_template='cmdb/company-view.html',
    add_template='cmdb/company-add.html', form_name='CompanyForm',
    edit_form_name='CompanyEditForm').save()
logging.debug('Loaded schema for /Company')

Schema(path='/HardwareVendor', module_name='cmdb', class_name='Model',
    edit_template='cmdb/model-edit.html', view_template='cmdb/model-view.html',
    add_template='cmdb/model-add.html', form_name='HWModelForm',
    edit_form_name='HWModelEditForm').save()
logging.debug('Loaded schema for /HardwareVendor')

Schema(path='/Locations', module_name='cmdb', class_name='Location',
    edit_template='cmdb/location-edit.html', view_template='cmdb/location-view.html',
    add_template='cmdb/location-add.html', form_name='LocationForm',
    edit_form_name='LocationEditForm').save()
logging.debug('Loaded schema for /Locations')

Schema(path='/OperatingSystem', module_name='cmdb', class_name='OperatingSystem',
    edit_template='cmdb/os-edit.html', view_template='cmdb/os-view.html',
    add_template='cmdb/os-add.html', form_name='OSForm',
    edit_form_name='OSEditForm').save()
logging.debug('Loaded schema for /OperatingSystem')


logging.debug('**** Loaded Initial Schema')

logging.debug('**** Creating tree objects')
ConfigurationItem(path='/', is_leaf=False).save()
logging.debug('Created /')

company = Company(path='/Company', is_leaf=False)
company.save()
logging.debug('Created /Company')

acme = Company(path='/Company/ACME Corp')
acme.save()
logging.debug('Created /Company/ACME Corp')

model = Model(path='/HardwareVendor', is_leaf=False)
model.save()
logging.debug('Created /HardwareVendor')

hp = Model(path='/HardwareVendor/HP')
hp.save()
logging.debug('Created /HardwareVendor/HP')

location = Location(path='/Locations', is_leaf=False)
location.save()
logging.debug('Created /Locations')

london = Location(path='/Locations/London')
london.save()
logging.debug('Created /Locations/London')

Device(path='/Devices', location=location, model=model, company=company,
        is_leaf=False).save()
logging.debug('Created /Devices')

Device(path='/Devices/ROUTER01', company=acme, model=hp, location=london).save()
logging.debug('Created /Devices/ROUTER01')

OperatingSystem(path='/OperatingSystem', is_leaf=False).save()
logging.debug('Created /OperatingSystem')

linux = OperatingSystem(path='/OperatingSystem/Linux')
linux.save()
logging.debug('Created /OperatingSystem/Linux')

ConfigurationItem(path='/PatchingSystem', is_leaf=False).save()
logging.debug('Created /PatchingSystem')

patching_system = ConfigurationItem(path='/PatchingSystem/Default Patching System')
patching_system.save()
logging.debug('Created /PatchingSystem/Default Patching System')

ConfigurationItem(path='/AuthenticationSource', is_leaf=False).save()
logging.debug('Created /AuthenticationSource')

auth = ConfigurationItem(path='/AuthenticationSource/Default Authentication System')
auth.save()
logging.debug('Created /AuthenticationSource/Default Authentication Source')


ConfigurationItem(path='/BackupSystem', is_leaf=False).save()
logging.debug('Created /BackupSystem')

backup = ConfigurationItem(path='/BackupSystem/Default Backup System')
backup.save()
logging.debug('Created /BackupSystem/Default Backup System')

Server(path='/Devices/Servers', company=company, location=location, is_leaf=False).save()
logging.debug('Created /Devices/Servers')

Server(path='/Devices/Servers/SERVER01', company=acme, location=london, model=hp,
        operating_system=linux).save()
logging.debug('Created /Devices/Servers/SERVER01')
