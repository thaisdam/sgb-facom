from django.db import models

class Benefit(models.Model):
    type_benefit = models.CharField(max_length=100, verbose_name='Tipo de Benefício')
    description_benefit = models.TextField(null=True, blank=True, verbose_name='Detalhes sobre o benefício')

    class Meta:
        verbose_name = 'Tipos de Benefício'
        verbose_name_plural = 'Tipos de Benefícios'
        ordering = ['type_benefit']

    def __str__(self):
        return self.type_benefit


class Beneficiary(models.Model):
    STUDENT = 'Estudante'
    STAFF = 'Técnico'
    TEACHER = 'Docente'

    TYPE_CHOICES = [
        (STUDENT, 'Estudante'),
        (STAFF, 'Técnico'),
        (TEACHER, 'Docente'),
    ]
    name = models.CharField(max_length=100, verbose_name='Nome do Beneficiário')
    type_beneficiary = models.CharField(
        max_length=50,
        choices=TYPE_CHOICES,
        verbose_name='Tipo de Beneficiário'
    )

    class Meta:
        verbose_name = 'Beneficiário'
        ordering = ['name']

    def __str__(self):
        return self.name


class Cost_center(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nome do Centro de Custo')
    description = models.TextField(null=True, blank=True, verbose_name='Descrição do Centro de Custo')

    class Meta:
        verbose_name = 'Centro de Custo'
        verbose_name_plural = 'Centros de Custos'
        ordering = ['name']

    def __str__(self):
        return self.name

class Source(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nome da Fonte de Recursos')
    description = models.TextField(null=True, blank=True, verbose_name='Descrição da Fonte de Recursos')
    
    class Meta:
        verbose_name = 'Fonte de Recursos'
        verbose_name_plural = 'Fontes de Recursos'
        ordering = ['name']

    def __str__(self):
        return self.name
    

class Concession(models.Model):
    beneficiary = models.ForeignKey(Beneficiary, on_delete=models.CASCADE, verbose_name='Beneficiário')
    benefit = models.ForeignKey(Benefit, on_delete=models.CASCADE, verbose_name='Benefício')
    cost_center = models.ForeignKey(Cost_center, on_delete=models.CASCADE, verbose_name='Centro de Custo')
    source = models.ForeignKey(Source, on_delete=models.CASCADE, verbose_name='Fonte de Recursos')
    date_concession = models.DateField(verbose_name='Data da Concessão')
    value = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Valor da Concessão')
    class Meta:
        verbose_name = 'Concessão'
        verbose_name_plural = 'Concessões'
        ordering = ['-date_concession']

    def __str__(self):
        return f'{self.beneficiary} - {self.benefit} ({self.date_concession})'



