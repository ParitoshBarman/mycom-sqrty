from django.contrib import admin
from pantharooapp.models import History, AllowDevice, NotAllow, AvailableFiles, FileHistory, FileHistoryNotAllowSPAM

# Register your models here.
admin.site.register(History)
admin.site.register(AllowDevice)
admin.site.register(NotAllow)
admin.site.register(FileHistory)
admin.site.register(AvailableFiles)
admin.site.register(FileHistoryNotAllowSPAM)