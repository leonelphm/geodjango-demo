# -*- coding: utf-8 -*-
"""
geodjango-demo

Copyleft (@) 2017 CENDITEL nodo Mérida - Copyleft (@) 2017 CENDITEL nodo Mérida
"""
## @package geolocation.models
#
# Modelos correspondientes a la geolocation
# @author Ing. Leonel Paolo Hernandez Macchiarulo (lhernandez at cenditel.gob.ve)
# @author <a href='http://www.cenditel.gob.ve'>Centro Nacional de Desarrollo e Investigación en Tecnologías Libres
# (CENDITEL) nodo Mérida - Venezuela</a>
# @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
# @version 1.0
from django.contrib.gis.db import models


class Zipcode(models.Model):
    """!
    Clase que gestiona los datos del Zipcode

    @author Ing. Leonel Paolo Hernandez Macchiarulo (lhernandez at cenditel.gob.ve)
    @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
    @date 04-10-2017
    @version 1.0.0
    """
    # Campo del ZioCode
    code = models.CharField(max_length=5)
    # Campo de la poligonal
    poly = models.PolygonField()

    class Meta:
        """!
            Clase que construye los meta datos del modelo

            @author Ing. Leonel P. Hernandez M. (lhernandez at cenditel.gob.ve)
            @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
            @date 04-10-2017
            @version 1.0.0
        """
        ordering = ('code',)
        verbose_name = 'Zipcode'
        verbose_name_plural = 'Zipcodes'

    def __str__(self):
        """!
            Funcion que muestra la informacion de los Zipcodes
            @author Ing. Leonel P. Hernandez M. (lhernandez at cenditel.gob.ve)
            @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
            @date 04-10-2017
            @param self <b>{object}</b> Objeto que instancia la clase
            @return Devuelve los datos de la asignacion del Zipcode
        """
        return self.code


class Elevation(models.Model):
    """!
    Clase que gestiona los datos de la Elevation

    @author Ing. Leonel Paolo Hernandez Macchiarulo (lhernandez at cenditel.gob.ve)
    @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
    @date 04-10-2017
    @version 1.0.0
    """
    name = models.CharField(max_length=100)
    rast = models.RasterField()

    class Meta:
        """!
            Clase que construye los meta datos del modelo

            @author Ing. Leonel P. Hernandez M. (lhernandez at cenditel.gob.ve)
            @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
            @date 04-10-2017
            @version 1.0.0
        """
        ordering = ('name',)
        verbose_name = 'Elevation'
        verbose_name_plural = 'Elevations'

    def __str__(self):
        """!
            Funcion que muestra la informacion de las Elevations
            @author Ing. Leonel P. Hernandez M. (lhernandez at cenditel.gob.ve)
            @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
            @date 04-10-2017
            @param self <b>{object}</b> Objeto que instancia la clase
            @return Devuelve los datos de la asignacion del Elevation
        """
        return self.name
