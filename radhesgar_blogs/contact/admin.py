from django.contrib import admin
from .models import ContactMessage

from django.contrib import admin
from django.http import HttpResponse
import csv
from .models import ContactMessage


from django.contrib import admin
from .models import ContactMessage
import csv
from django.http import HttpResponse

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'company', 'submitted_at')
    search_fields = ('first_name', 'last_name', 'email', 'company')
    list_filter = ('submitted_at', 'company')
    actions = ['export_as_csv']

    def export_as_csv(self, request, queryset):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="contacts.csv"'

        writer = csv.writer(response)
        writer.writerow(['First Name', 'Last Name', 'Email', 'Company', 'Message', 'Submitted At'])

        for contact in queryset:
            writer.writerow([
                contact.first_name,
                contact.last_name,
                contact.email,
                contact.company,
                contact.message,
                contact.submitted_at
            ])

        return response

    export_as_csv.short_description = "Export Selected Contacts to CSV"
