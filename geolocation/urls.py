# -*- coding: utf-8 -*-
"""
geodjango-demo

Copyleft (@) 2017 CENDITEL nodo Mérida - Copyleft (@) 2017 CENDITEL nodo Mérida
"""
## @package geolocation.urls
#
# Urls correspondientes a la geolocation
# @author Ing. Leonel Paolo Hernandez Macchiarulo (lhernandez at cenditel.gob.ve)
# @author <a href='http://www.cenditel.gob.ve'>Centro Nacional de Desarrollo e Investigación en Tecnologías Libres
# (CENDITEL) nodo Mérida - Venezuela</a>
# @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
# @version 1.0
from django.conf.urls import url

from .views import *

urlpatterns = [
                url(r'^register-poly/',
                    RegisterPolyView.as_view(),
                    name="register_poly"),
                url(r'^list-zipcode/',
                    ListZipcodeView.as_view(),
                    name="list_zipcode"),
                url(r'^delete-zipcode/(?P<pk>\d+)/',
                    ZipcodeDeleteView.as_view(),
                    name="delete_zipcode"),
                url(r'update-zipcode/(?P<pk>\d+)/$',
                    ZipCodeUpdate.as_view(),
                    name='update_zipcode')
              ]
