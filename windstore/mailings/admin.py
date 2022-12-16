from django.contrib import admin

from .models import MailingList


# @admin.register(Contact)
class MailingListAdmin(admin.ModelAdmin):
    list_display = ('email',)


admin.site.register(MailingList, MailingListAdmin)