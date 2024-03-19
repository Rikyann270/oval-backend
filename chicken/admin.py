from django.contrib import admin

from chicken.models import (
    
    ChickInfor,
    EquipmentsInfor,
    FeedsInfor,
    VaccineInfor,
    
    
    
    )

admin.site.register(ChickInfor)
admin.site.register(EquipmentsInfor)
admin.site.register(FeedsInfor)
admin.site.register(VaccineInfor)