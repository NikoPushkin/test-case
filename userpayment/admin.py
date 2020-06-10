from django.contrib import admin
from .models import Profile, Payment, Payout
from django.conf.urls import url
from django.http import HttpResponseRedirect

from datetime import datetime
from .services import withdraw


class ProfileAdmin(admin.ModelAdmin):
    readonly_fields = ('commission',)
    list_display = ('firstname', 'lastname', 'commission')

class PayoutAdmin(admin.ModelAdmin):
    list_display = ('author', 'sum', 'request_date', 'status')
    readonly_fields = ('status', 'processing_date')
    actions = ('confirmPayout',)
    empty_value_display = 'is not confirmed'

    def get_readonly_fields(self, request, obj):
        if obj.status is True:
            return self.readonly_fields + (
                'author', 'sum', 'status',
                'request_date', 'processing_date'
            )
        else:
            return self.readonly_fields

    def confirmPayout(self, request, queryset):
        row_update = queryset.update(status=True, processing_date=datetime.now())
        withdraw(queryset)

        if row_update == '1':
            message_bit = "Payout was confirmed"
        else:
            message_bit = "Payouts were confirmed"
        self.message_user(request, '{}'.format(message_bit))

    confirmPayout.short_description = "Confirm payout"
    confirmPayout.allowed_permissions = ('change', )


admin.site.register(Profile, ProfileAdmin)
admin.site.register(Payment)
admin.site.register(Payout, PayoutAdmin)
