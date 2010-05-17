from cmdb.models import *
from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

class ConfigurationItemAdmin(admin.ModelAdmin):
    list_display = ['path', 'name', 'active', 'description']
    search_fields = ['path']

class DeviceAdmin(admin.ModelAdmin):
    list_display = ['path', 'company', 'active', 'description']
    search_fields = ['path', 'serialNumber', 'assetTag']
	
class ServerAdmin(admin.ModelAdmin):
    exclude = ('ipAddresses')

admin.site.register(Schema)
admin.site.register(ConfigurationItem, ConfigurationItemAdmin)
admin.site.register(Device, DeviceAdmin)
admin.site.register(Server, DeviceAdmin)
admin.site.register(Computer, DeviceAdmin)
admin.site.register(ServiceAccount)
admin.site.register(Location)
admin.site.register(System)
admin.site.register(Company)
admin.site.register(IPNetwork)
admin.site.register(OperatingSystem)
admin.site.register(HistoryLog)
admin.site.register(People, DeviceAdmin)
admin.site.register(ADImportLocation)



admin.site.unregister(User)

# Set it up so we can edit a user's sprockets inline in the admin
class UserProfileInline(admin.StackedInline):
    model = AlertProfile

class MyUserAdmin(UserAdmin):
    inlines = [UserProfileInline]

# re-register the User with the extended admin options
admin.site.register(User, MyUserAdmin)

