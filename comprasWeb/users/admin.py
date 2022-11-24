from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export import resources


from .models import Usuario

# class UsuarioRerourse(resources.ModelResource):
#     class Meta:
#         model = Usuario



# class UsuarioAmin(ImportExportModelAdmin,admin.ModelAdmin): #Formato para listar en columnas los datos segun nombres que deben ser iguales que en el modelo
#     list_display = ('usuario_id','nombres','apellidos','correo_electronico','telefono')
#     search_fields = ['nombres','apellidos','correo_electronico','telefono']
    # resource_class = UsuarioRerourse

admin.site.register(Usuario)


# Register your models here.
