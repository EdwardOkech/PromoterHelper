from django.contrib import admin
from sms.models import (Coordinator, Group, Member)

admin.site.register(Coordinator)
admin.site.register(Group)
admin.site.register(Member)
