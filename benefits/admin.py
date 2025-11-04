import csv
from django.http import HttpResponse
from django.contrib import admin
from .models import Benefit, Beneficiary, Cost_center, Concession, Source


@admin.register(Benefit)
class BenefitAdmin(admin.ModelAdmin):
    list_display = ('type_benefit', 'description_benefit')
    search_fields = ('type_benefit',)
    list_filter = ('type_benefit',)


@admin.register(Beneficiary)
class BeneficiaryAdmin(admin.ModelAdmin):
    list_display = ('name', 'type_beneficiary')
    search_fields = ('name',)
    list_filter = ('type_beneficiary',)


@admin.register(Cost_center)
class CostCenterAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)
    list_filter = ('name',)

@admin.register(Source)
class SourceAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)
    list_filter = ('name',)

@admin.register(Concession)
class ConcessionAdmin(admin.ModelAdmin):
    list_display = ('beneficiary', 'benefit', 'cost_center', 'date_concession', 'value', 'source')
    search_fields = ('beneficiary__name', 'benefit__type_benefit', 'cost_center__name', 'source__name')
    list_filter = ('date_concession', 'beneficiary__type_beneficiary', 'benefit')
    date_hierarchy = 'date_concession'


    def export_to_csv(self, request, queryset):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="concessions.csv"'

        writer = csv.writer(response)
        writer.writerow(['Beneficiário', 'Benefício', 'Centro de Custo', 'Data da Concessão', 'Valor', 'Fonte'])

        for concession in queryset:
            writer.writerow([
                concession.beneficiary.name,
                concession.benefit.type_benefit,
                concession.cost_center.name,
                concession.date_concession.strftime('%d/%m/%Y'),
                f'{concession.value:.2f}',
                concession.source.name
            ])

        return response

    export_to_csv.short_description = 'Exportar concessões para CSV'
    actions = [export_to_csv]
