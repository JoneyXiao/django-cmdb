# Introduction #

Django-CMDB supports filtering of Configuration Items to support both security and also to make the information presented to users (i.e. You can hide CI's belonging to COMPANY\_A from a user belonging to COMPANY\_B)

You can filter CI's under the /Devices/ namespace using the first method of Access Control (Security Groups) and you can also filter the presence of Companies, Backup Systems, Patching Systems and so on using the second method (Explicit ACLs)

You must define a Security Group in order to make django-cmdb functional.

# Device Security Groups (Mandatory) #

Users must be a member of a security group (created in the admin interface). A user can be a member of multiple groups.

Each group has fields called **Read ACL** and **Write ACL** that can contain multiple Django query statements that define the objects user can view.

The most permissive ACL would be _Device.objects.all()_ where you can also be very restrictive

`# Only show devices that are in the London location`

`Device.objects.filter(location__path__icontains='London')`

`# Only show devices that are routers in Manchester`

`Device.objects.filter(location__path__icontains='Manchester',path__startswith='/Devices/Router')`

# Explicit ACL (Optional) #

Device Security Groups provide a way of hiding certain Device Configuration Items from view. It might also be desirable to hide other CI's such as /Company /AuthenticationSource /BackupSystem

There is no point showing these options to users if it isn't relevant to do so. For this purpose you can provide an explicit ACL. The filter() is appended to the SecurityGroup queryset