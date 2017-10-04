# -*- coding: utf-8 -*-
"""
geodjango-demo

Copyleft (@) 2017 CENDITEL nodo Mérida - Copyleft (@) 2017 CENDITEL nodo Mérida
"""
## @package geolocation.views
#
# Views correspondientes a la geolocation
# @author Ing. Leonel Paolo Hernandez Macchiarulo (lhernandez at cenditel.gob.ve)
# @author <a href='http://www.cenditel.gob.ve'>Centro Nacional de Desarrollo e Investigación en Tecnologías Libres
# (CENDITEL) nodo Mérida - Venezuela</a>
# @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
# @version 1.0

from django.contrib import messages
from django.shortcuts import render
from django.views.generic.edit import (
    FormView
    )

from .forms import *


class RegisterPolyView(FormView):
    """!
    Clase que controla el formulario del zipcode para el template

    @author Ing. Leonel P. Hernandez M. (lhernandez at cenditel.gob.ve)
    @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
    @date 04-10-2017
    @version 1.0.0
    """
    form_class = ZipcodeForms
    template_name = 'geodjango-template.html'
    success_url = '/geolocation/register-poly/'

    def form_valid(self, form, **kwargs):
        """
        Funcion que valida el formulario de registro de la explicacion situacional
        @return: Dirige con un mensaje de exito a el geolocation
        """
        new_zipcode = form.save()
        messages.success(self.request, "ZipCode %s, registrado con exito" % (str(new_zipcode)))
        return super(RegisterPolyView, self).form_valid(form)
