from django.contrib import admin
from django import forms
from .models import Laboratorio, DirectorGeneral, Producto

admin.site.site_header = 'Laboratorio'

class LaboratorioAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')  

class DirectorGeneralAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'get_laboratorio_nombre')
    list_display_links = ('id', 'nombre')
    list_filter = ('laboratorio',) 

    def get_laboratorio_nombre(self, obj):
        return obj.laboratorio.nombre if obj.laboratorio else None

    get_laboratorio_nombre.short_description = 'Laboratorio' 

class ProductoForm(forms.ModelForm):
    f_fabricacion_year = forms.IntegerField(label='Año de Fabricación', min_value=2015, max_value=9999, widget=forms.NumberInput(attrs={'type': 'number'}))

    class Meta:
        model = Producto
        fields = ['nombre', 'laboratorio', 'f_fabricacion_year', 'p_costo', 'p_venta']

class ProductoAdmin(admin.ModelAdmin):
    form = ProductoForm 
    list_display = ('id', 'nombre', 'get_laboratorio_nombre', 'get_year_fabricacion', 'p_costo', 'p_venta')
    
    def get_laboratorio_nombre(self, obj):
        return obj.laboratorio.nombre if obj.laboratorio else None
    
    get_laboratorio_nombre.short_description = 'Laboratorio'  
    
    def get_year_fabricacion(self, obj):
        return obj.f_fabricacion.year

    get_year_fabricacion.short_description = 'Año de Fabricación'  

    def save_model(self, request, obj, form, change):
        obj.f_fabricacion = f"{form.cleaned_data['f_fabricacion_year']}-01-01"
        super().save_model(request, obj, form, change)

admin.site.register(Laboratorio, LaboratorioAdmin)
admin.site.register(DirectorGeneral, DirectorGeneralAdmin)
admin.site.register(Producto, ProductoAdmin)