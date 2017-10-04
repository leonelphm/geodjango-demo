# -*- coding: utf-8 -*-
"""
geodjango-demo

Copyleft (@) 2017 CENDITEL nodo Mérida - Copyleft (@) 2017 CENDITEL nodo Mérida
"""
## @package geodjango.forms
#
# Formularios correspondientes a la geolocation
# @author Ing. Leonel Paolo Hernandez Macchiarulo (lhernandez at cenditel.gob.ve)
# @author <a href='http://www.cenditel.gob.ve'>Centro Nacional de Desarrollo e Investigación en Tecnologías Libres
# (CENDITEL) nodo Mérida - Venezuela</a>
# @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
# @version 1.0

from django.contrib.gis import forms

from .models import *


class ZipcodeForms(forms.ModelForm):
    """!
    Clase que permite crear el formulario para el Zipcode

    @author Ing. Leonel P. Hernandez M. (lhernandez at cenditel.gob.ve)
    @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
    @date 04-10-2017
    @version 1.0.0
    """

    class Meta:
        """!
        Clase que construye los meta datos del formulario

        @author Ing. Leonel P. Hernandez M. (lhernandez at cenditel.gob.ve)
        @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
        @date 04-10-2017
        @version 1.0.0
        """
        model = Zipcode
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        """!
        Funcion que construye el init del formulario

        @author Ing. Leonel P. Hernandez M. (lhernandez at cenditel.gob.ve)
        @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
        @date 04-10-2017
        """
        super(ZipcodeForms, self).__init__(*args, **kwargs)
        self.fields['code'].widget.attrs.update({'class': 'form-control',
                                                 'placeholder': 'Zip Code'})
        self.fields['code'].label = 'Zip Code'
        self.fields['code'].required = True

        # Se le agrega la ruta donde se construye el mapa con el default_zoom
        self.fields['poly'].widget = forms.OSMWidget.template_name = 'openlayers-cust.html'

        # Se le agrega al campo los atributos que por defecto tiene la ubicacion (lat lon) de Venezuela
        # Con un zoom por defecto de 5.2 y
        # Un alto y ancho de 600X400
        self.fields['poly'].widget = forms.OSMWidget(attrs={
                                    'default_zoom': 5.2, 'map_width': 600,
                                    'map_height': 400, 'default_lat': 8,
                                    'default_lon': -66})
        self.fields['poly'].label = 'Cordenadas Poligonales'
        self.fields['poly'].required = True
