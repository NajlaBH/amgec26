from django.contrib import admin
from .filters import ContactFilter
from .models import Contact

from import_export.admin import ImportExportModelAdmin
from import_export import resources

class ContactDemandFilter(admin.SimpleListFilter):
    title = "DEMANDE TYPE"

    # Parameter for the filter that will be used in the URL query.
    parameter_name = "demane"

    def lookups(self, request, model_admin):
        """
        Returns a list of tuples. The first element in each
        tuple is the coded value for the option that will
        appear in the URL query. The second element is the
        human-readable name for the option that will appear
        in the right sidebar.
        """
        return [
            ("INFO-ABSTRACT", 'ABSTRACT SUBMISSION'),
            ("INFO-PAPER", 'PAPER SUBMISSION'),
        ]

    def queryset(self, request, queryset):
            """
            Returns the filtered queryset based on the selected lookup.
            """
            if self.value() == '"INFO-ABSTRACT"':
                return queryset.filter(demande='ABSTRACT SUBMISSION')
            if self.value() == 'INFO-PAPER':
                return queryset.filter(demande='INFO-PAPER')
            return queryset  # Return the original queryset if no filter is applied

# ADD ORGANISM TO ADMIN INTERFACE
class ContactResource(resources.ModelResource):
    fieldsets = [
        ("Section title", {
            "classes": ("collapse", "expanded"),
            "fields": ('demande_date','demande', 'message', 'email','phone', 'first_name','last_name'),
        }),
    ]
    class Meta:
        model = Contact 

class ContactAdmin(ImportExportModelAdmin):
    resource_classes = [ContactResource]
    list_filter = [ContactDemandFilter]
    list_display = ('demande_date','demande', 'message', 'email','phone', 'first_name','last_name')

admin.site.register(Contact,ContactAdmin)

#@admin.register(Contact)
