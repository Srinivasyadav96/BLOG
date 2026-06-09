from django.contrib import admin

from about.models import About, SocialLink

'''class AboutAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        count=About.objects.count()
        if count == 0:
            return True
        return False'''
# Register your models here.
#admin.site.register(About, AboutAdmin)
admin.site.register(SocialLink)