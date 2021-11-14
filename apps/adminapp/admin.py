from django.contrib import admin
from .models import MajourCriteria, SubCriteria, FinalCriteria, \
    EventUploader,CriteriaManager

# Register your models here.
admin.site.register(MajourCriteria)
admin.site.register(SubCriteria)
admin.site.register(FinalCriteria)
admin.site.register(EventUploader)
admin.site.register(CriteriaManager)