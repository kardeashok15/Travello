from django.contrib import admin
from abk.models import Contact
from abk.models import Destination
from abk.models import memories
# Register your models here.
admin.site.register(Contact)
admin.site.register(Destination)
admin.site.register(memories)