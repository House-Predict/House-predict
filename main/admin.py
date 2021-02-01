from django.contrib import admin
from .models import Property,Feedback
from django.contrib.auth.models import Group

class FeedbackAdmin(admin.ModelAdmin):
    list_display=('name','date')
    list_filter=('date',)
    
class PropertyAdmin(admin.ModelAdmin):
    list_display=('id','user','location','price')

admin.site.register(Property,PropertyAdmin)
admin.site.register(Feedback,FeedbackAdmin)
admin.site.unregister(Group)

admin.site.site_header='House Predict Admin Dashboard'