from django.contrib import admin
from landing.models import Information
from django.http import HttpResponse
import csv, datetime

# Register your models here.
class ExportCsvMixin:
        def export_as_csv(self, request, queryset):
            meta = self.model._meta
            field_names = [field.name for field in meta.fields]

            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
            writer = csv.writer(response)

            writer.writerow(field_names)
            for obj in queryset:
                row = writer.writerow([getattr(obj, field) for field in field_names])

            return response

        export_as_csv.short_description = "Export Selected"

@admin.register(Information)
class InformationAdmin(admin.ModelAdmin, ExportCsvMixin):
    list_display = ('firstName', 'lastName', 'email')
    actions = ["export_as_csv"]
