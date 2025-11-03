from django.contrib import admin

from .models import AbstractSubmission

from import_export.admin import ImportExportModelAdmin
from import_export import resources

# ADD AbstractSubmission TO ADMIN INTERFACE
class AbstractSubmissionResource(resources.ModelResource):
    fieldsets = [
        ("Section title", {
            "classes": ("collapse", "expanded"),
            "fields": ('demande_date','title', 'institution', 'email','phone', 'first_name','last_name',
            'laboratory','presentation','subject','document'),
        }),
    ]
    class Meta:
        model = AbstractSubmission 

class AbstractSubmissionAdmin(ImportExportModelAdmin):
    resource_classes = [AbstractSubmissionResource]
    list_display = ('demande_date','title', 'institution', 'email','phone', 'first_name','last_name',
            'laboratory','presentation','subject','document')

admin.site.register(AbstractSubmission,AbstractSubmissionAdmin)

#@admin.register(AbstractSubmission)
