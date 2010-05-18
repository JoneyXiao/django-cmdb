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

logging.debug('**** Loaded Initial Schema')

logging.debug('**** Creating tree objects')
ConfigurationItem(path='/').save()
logging.debug('Created /')

ConfigurationItem(path='/Company/').save()
logging.debug('Created /Company')

acme = Company(path='/Company/ACME Corp')
acme.save()
logging.debug('Created /Company/ACME Corp')

ConfigurationItem(path='/HardwareVendor').save()
logging.debug('Created /HardwareVendor')

hp = Model(path='/HardwareVendor/HP')
hp.save()
logging.debug('Created /HardwareVendor/HP')

ConfigurationItem(path='/Locations').save()
logging.debug('Created /Locations')

london = Location(path='/Locations/London')
london.save()
logging.debug('Created /Locations/London')

ConfigurationItem(path='/Devices').save()
logging.debug('Created /Devices')

Device(path='/Devices/ROUTER01', company=acme, model=hp, location=london).save()
logging.debug('Created /Devices/ROUTER01')
