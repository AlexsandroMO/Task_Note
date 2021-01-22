from django.contrib import admin
from . models import Activity, AppUser, Status, Task

class ActivityAdmin(admin.ModelAdmin):
    fields = ('activity_name',)
    list_display = ('id','activity_name',)
    

class AppUserAdmin(admin.ModelAdmin):
    fields = ('name','activity','photo', 'user')
    list_display = ('id','name','activity','photo')


class StatusAdmin(admin.ModelAdmin):
    fields = ('status_name',)
    list_display = ('id','status_name')


class TaskAdmin(admin.ModelAdmin):
    fields = ('status', 'doc','rev','comment', 'elab', 'verif')
    list_display = ('id','status', 'doc','rev','comment', 'elab', 'verif')


admin.site.register(Activity, ActivityAdmin)
admin.site.register(AppUser, AppUserAdmin)
admin.site.register(Status, StatusAdmin)
admin.site.register(Task, TaskAdmin)

