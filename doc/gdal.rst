gdal
====

`gdal <https://gdal.org/>`_ ist eine Bibliothek zur Bearbeitung und Umwandlung von räumlichen Raster- und Vektordaten. Daneben
bietet es auch zahlreiche Kommandozeilenprogramme.

gdal ist Open Source und für Linux und Windows verfügbar. Zur Installation sei auf die oben verlinkte Website verwiesen.

Beispiele
---------

Datenumwandlung
^^^^^^^^^^^^^^^
Das Digitale Geländemodell wird im Format GeoTIFF zur Verfügung gestellt. Sie wollen die Daten jedoch
im Format ASCII Grid:

.. code-block:: console

 $ gdal_translate -of AAIGrid 691_5327.tif 691_5327.asc

Der Schalter ``-of`` gibt hierbei das Ausgabeformat an. ``gdal_translate --formats`` listet die verfügbaren Quell- und Zielformate auf,
``gdal_translate -h`` liefert eine Kurzbeschreibung der Parameter und die Seite `gdal_translate <https://gdal.org/programs/gdal_translate.html>`_ zeigt eine
ausführliche Anleitung zu diesem Kommandozeilentool.


Datenaggregation
^^^^^^^^^^^^^^^^
Sie haben Sich mittels aria2c und dem entsprechenden MetaLink-File die DOP-Kacheln ihrer Gemeinde heruntergeladen. Jetzt haben Sie ein Verzeichnis voll mit 1km²-Kacheln,
Sie hätten aber gerne nur **ein** Bild.

.. figure:: _static/qgis-tiles.png

 QGIS mit allen heruntergeladenen Kacheln der Gemeinde Taufkirchen

Abhilfe schafft hier ``gdalwarp``.

.. code-block:: console

 $ gdalwarp -dstalpha -co "TILED=YES" -co "COMPRESS=LZW" 32*.tif taufkirchen.tif

.. figure:: _static/qgis-single.png

 QGIS mit dem aggregierten Bild und einer freien Webkarte (Top Plus Open des BKG) als Hintergrund

``-dstalpha``
    fügt einen Alpha-Kanal für die Transparenz hinzu. Dadurch wird an den Stellen ohne Informationen der Hintergrund sichtbar.

``-co "TILED=YES"``
    sorgt für eine interne Kachelung des Bildes. Dadurch werden beim Hineinzoomen in das Bild nur die Teile gelesen, die für die Darstellung benötigt werden.

``-co "COMPRESS=LZW"``
    sorgt dafür, dass die Rasterdaten im GeoTIFF komprimiert werden.

``32*.tif``
  Die Dateinamen der Kacheln beginnen in diesem Falle alle mit 32. ``gdalwarp`` liest alle Dateien ein, die auf dieses Pattern passen.

``taufkirchen.tif``
    Der Name der Zieldatei, die durch ``gdalwarp`` erzeugt wird.

Wenn die durch ``gdalwarp`` erzeugte Datei jetzt beispielsweise in QGIS geladen wird, dauert die Darstellung etwas, weil zunächst das ganze Bild geladen und dann
für die Darstellung verkleinert werden muss. Abhilfe schafft hier ``gdaladdo``, mit dem *Overviews* (Übersichten) in das Bild gerechnet werden können. Die Datei
wird dadurch zwar größer, aber die deutlich kürzeren Ladezeiten entschädigen dafür ausreichend.

.. code-block:: console

 Erzeugen der Übersichten
 Die Zahlen sind Bruchteile der Ursprungsauflösung, hier also 1/2, 1/4, ...
 $ gdaladdo taufkirchen.tif 2 4 8 16
 Das Resultat mit gdalinfo betrachten:
 $ gdalinfo taufkirchen.tif
    Driver: GTiff/GeoTIFF
    Files: taufkirchen.tif
    Size is 20000, 17500
    Coordinate System is:
    PROJCRS["ETRS89 / UTM zone 32N",
        BASEGEOGCRS["ETRS89",
            DATUM["European Terrestrial Reference System 1989",
                ELLIPSOID["GRS 1980",6378137,298.257222101,
                    LENGTHUNIT["metre",1]]],
            PRIMEM["Greenwich",0,
                ANGLEUNIT["degree",0.0174532925199433]],
            ID["EPSG",4258]],
        CONVERSION["UTM zone 32N",
            METHOD["Transverse Mercator",
                ID["EPSG",9807]],
            PARAMETER["Latitude of natural origin",0,
                ANGLEUNIT["degree",0.0174532925199433],
                ID["EPSG",8801]],
            PARAMETER["Longitude of natural origin",9,
                ANGLEUNIT["degree",0.0174532925199433],
                ID["EPSG",8802]],
            PARAMETER["Scale factor at natural origin",0.9996,
                SCALEUNIT["unity",1],
                ID["EPSG",8805]],
            PARAMETER["False easting",500000,
                LENGTHUNIT["metre",1],
                ID["EPSG",8806]],
            PARAMETER["False northing",0,
                LENGTHUNIT["metre",1],
                ID["EPSG",8807]]],
        CS[Cartesian,2],
            AXIS["(E)",east,
                ORDER[1],
                LENGTHUNIT["metre",1]],
            AXIS["(N)",north,
                ORDER[2],
                LENGTHUNIT["metre",1]],
        USAGE[
            SCOPE["unknown"],
            AREA["Europe - 6°E to 12°E and ETRS89 by country"],
            BBOX[38.76,6,83.92,12]],
        ID["EPSG",25832]]
    Data axis to CRS axis mapping: 1,2
    Origin = (692000.000000000000000,5326000.000000000000000)
    Pixel Size = (0.400000000000000,-0.400000000000000)
    Metadata:
      AREA_OR_POINT=Area
      BILDFLUG_DATUM=*
      BILDFLUG_NUMMER=*
      BILDFLUG_UNTERNUMMER=0
    Image Structure Metadata:
      COMPRESSION=LZW
      INTERLEAVE=PIXEL
    Corner Coordinates:
    Upper Left  (  692000.000, 5326000.000) ( 11d34'36.77"E, 48d 3'30.12"N)
    Lower Left  (  692000.000, 5319000.000) ( 11d34'25.48"E, 47d59'43.62"N)
    Upper Right (  700000.000, 5326000.000) ( 11d41' 2.87"E, 48d 3'21.27"N)
    Lower Right (  700000.000, 5319000.000) ( 11d40'51.11"E, 47d59'34.79"N)
    Center      (  696000.000, 5322500.000) ( 11d37'44.06"E, 48d 1'32.50"N)
    Band 1 Block=256x256 Type=Byte, ColorInterp=Red
      Overviews: 10000x8750, 5000x4375, 2500x2188, 1250x1094
      Mask Flags: PER_DATASET ALPHA
      Overviews of mask band: 10000x8750, 5000x4375, 2500x2188, 1250x1094
    Band 2 Block=256x256 Type=Byte, ColorInterp=Green
      Overviews: 10000x8750, 5000x4375, 2500x2188, 1250x1094
      Mask Flags: PER_DATASET ALPHA
      Overviews of mask band: 10000x8750, 5000x4375, 2500x2188, 1250x1094
    Band 3 Block=256x256 Type=Byte, ColorInterp=Blue
      Overviews: 10000x8750, 5000x4375, 2500x2188, 1250x1094
      Mask Flags: PER_DATASET ALPHA
      Overviews of mask band: 10000x8750, 5000x4375, 2500x2188, 1250x1094
    Band 4 Block=256x256 Type=Byte, ColorInterp=Alpha
      Overviews: 10000x8750, 5000x4375, 2500x2188, 1250x1094








