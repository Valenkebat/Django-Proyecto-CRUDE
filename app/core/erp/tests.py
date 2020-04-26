from config.wsgi import *
from core.erp.models import Type
from django.test import TestCase

# Listar
query = Type.objects.all()
print(query)
# insercion en la tabla
# t = Type()
# t.name = 'terry'
# t.save()


# Edicion

# t = Type.objects.get(pk=1)
# print(t.name)
# t.name = 'nnn'
# t.save()

obj = Type.objects.filter(name__icontains='pre')# Para buscar palabras con o sin mayusculas
obj2 = Type.objects.filter(name__startswith='p')
print(obj)
print('Empiezan con la letra p', obj2)
