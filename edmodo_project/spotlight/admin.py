from django.contrib import admin

# Register your models here.
from spotlight.models import Prod,Source,Owner,Flag
admin.site.register(Prod)
admin.site.register(Source)
admin.site.register(Owner)
admin.site.register(Flag)
