from django.forms import *
from django.core.validators import validate_ipv4_address, validate_email
from django.utils.text import normalize_newlines

from cmdb.models import *

class MultiIPAddressField(fields.Field):
    def to_python(self, value):
        return normalize_newlines(value)

    def validate(self, value):
        super(MultiIPAddressField, self).validate(value)
        for address in normalize_newlines(value).split('\n'):
            if address:
                validate_ipv4_address(address)

    def clean(self, value):
        super(MultiIPAddressField, self).clean(value)
        addresses = normalize_newlines(value).split('\n')
        addresses.sort()
        ret = ''
        for a in addresses:
            if a:
                ret += '''%s\n''' % a 
        return ret


class DeviceForm(ModelForm):

    ip_addresses = MultiIPAddressField(required=False)

    class Meta:
        model = Device
        exclude = ('active', 'is_leaf')
    def __init__(self, *args, **kwargs):
        super(DeviceForm, self).__init__(*args, **kwargs)
        #self.fields['path'].widget.attrs['readonly'] = True
        self.fields['ip_addresses'].widget = Textarea()

        
