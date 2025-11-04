import csv
from django.http import HttpResponse
from django.shortcuts import render
from .models import Concession, Benefit, Cost_center, Source
from django.db.models import Q # Keep Q just in case you decide to add a general search later

def concession_list_public(request):
    # Capture parameters
    data_inicio = request.GET.get('data_inicio')
    data_fim = request.GET.get('data_fim')
    beneficio_id = request.GET.get('beneficio')
    centro_custo_id = request.GET.get('centro_custo')
    fonte_recurso_id = request.GET.get('fonte_recurso')
    nome_beneficiario = request.GET.get('nome_beneficiario')

    # Base QuerySet
    concessions = Concession.objects.select_related('beneficiary', 'benefit', 'cost_center', 'source').order_by('-date_concession') # Added ordering for better display

    # Apply filters
    if data_inicio and data_fim:
        concessions = concessions.filter(date_concession__range=[data_inicio, data_fim])
    
    if beneficio_id:
        concessions = concessions.filter(benefit_id=beneficio_id)
    
    if centro_custo_id:
        concessions = concessions.filter(cost_center_id=centro_custo_id)
    
    if fonte_recurso_id:
        concessions = concessions.filter(source_id=fonte_recurso_id) 
    
    if nome_beneficiario:
        concessions = concessions.filter(beneficiary__name__icontains=nome_beneficiario)

    # Handle CSV export
    if request.GET.get('export') == 'csv':
        return export_concessions_to_csv(concessions)

    return render(request, 'concessions/public_list.html', {
        'concessions': concessions,
        # 'query': query, # Removed as per discussion
        'beneficios': Benefit.objects.all(),
        'centros_custo': Cost_center.objects.all(),
        'fontes_recurso': Source.objects.all(), # Corrected context variable name
        'request': request, # Good practice for retaining filter states in template
    })

def export_concessions_to_csv(concessions):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="concessoes.csv"'

    writer = csv.writer(response)
    writer.writerow(['Beneficiário', 'Benefício', 'Centro de Custo', 'Fonte de Recurso', 'Data', 'Valor'])

    for c in concessions:
        writer.writerow([
            c.beneficiary.name,
            c.benefit.type_benefit,
            c.cost_center.name,
            c.source.name,
            c.date_concession.strftime('%d/%m/%Y'),
            f'{c.value:.2f}'.replace('.', ','), # Format for Brazilian currency with comma
        ])

    return response