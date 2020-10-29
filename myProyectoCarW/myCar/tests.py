from django.test import TestCase
import unittest
from .models import Insumos,MisionyVision

# Create your tests here.
class TestInsumo(unittest.TestCase):

    def grabar_insumo(self):

        insum = Insumos(
                nombre="mm", 
                precio=199, 
                descripcion="cualquiera", 
                stock=200)
        valor = 0
        try:            
            insum.save()
            valor = 1
        except:
            valor = 0
        self.assertIn(valor,1)

    def grabar_misionyvision(self):

        vym = MisionyVision(
                ident="unico", 
                mision="Garantizar la satisfacción y servicio de excelencia, ofreciendo una alternativa para maximizar el tiempo del cliente, creando la combinación perfecta entre servicio y calidad que provoque la lealtad de nuestros clientes.", 
                vision="Ser una de las empresas más eficientes para el lavado de automóviles en Chile, ofreciendo a cada uno de nuestros clientes soluciones prácticas para el aseo de sus vehículos con la calidad, servicio y compromiso que nos caracteriza, y así poder garantizar la lealtad del consumidor.")
        valor = 0
        try:            
            vym.save()
            valor = 1
        except:
            valor = 0
        self.assertIn(valor,1)

if __name__ == "__main__":
    unittest.main()