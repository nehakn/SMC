# -*- coding: utf-8 -*-
"""
/***************************************************************************
 SoilMoisture
                                 A QGIS plugin
 It computes soil moisture at high resolution using the SMAP/SMOS 36km coarse resolution global soil moisture data
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2022-09-16
        copyright            : (C) 2022 by Neha K. Nawandar
        email                : nehanawandar@gmail.com
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load SoilMoisture class from file SoilMoisture.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .soil_moisture import SoilMoisture
    return SoilMoisture(iface)
