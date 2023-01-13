OpenData
========

Welche Daten sind verfügbar?
----------------------------

Die verfügbaren Daten sind auf der `OpenData-Seite der Bayerischen Vermessungsverwaltung <https://geodaten.bayern.de/opengeodata/>`_ aufgelistet und beschrieben.

Daten mittels ``aria2`` herunterladen und aktualisieren (Linux)
---------------------------------------------------------------

``aria2`` installieren (Debian-basierte Distributionen)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code-block:: console

 $ sudo apt install aria2

Gewünschte Daten heraussuchen und den URL zur meta4-Datei bekommen
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Die benötigten MetaLink-Dateien haben einen URL, der wie ``https://geodaten.bayern.de/[...].meta4`` aussieht.

* In die Karte klicken
* Rechtsklick auf **Download (Metalink)**
* Den URL in die Zwischenablage kopieren

Die Daten herunterladen
^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: console

 Zielverzeichnis erstellen
 $ mkdir /path/to/local_geodata/
 aria2 zum Herunterladen der Daten verwenden
 $ aria2c -V --follow-metalink=mem --dir=/path/to/local_geodata/ <kopierten URL hier einfügen>

Beispiel:

.. code-block:: console

 $ aria2c -V --follow-metalink=mem --dir=/tmp https://geodaten.bayern.de/odd/a/lod2/citygml/meta/metalink/09276115.meta4

Erläuterung:

* ``follow-metalink=mem`` meta4-Datei nicht schreiben
* ``-V`` zum Prüfen der heruntergeladenen Daten gegen die im der meta4-Datei enthaltenen Checksumme.
* ``-dir=/path/to/data/`` Zielverzeichnis zum Speichern der Daten.

.. note::

 Wenn die Metalink-Datei > 5 MB ist, dann funktioniert ``follow-metalink=mem`` nicht. In diesem Falle wirft aria2 einen
 Fehler. In diesem Falle diese Angabe einfach weglassen. aria2 speichert die MetaLink-Datei dann im Zielverzeichnis ab.
 Dort kann sie nach dem Download der Dateien - wenn gewünscht - nachträglich gelöscht werden.

Updates automatisieren
^^^^^^^^^^^^^^^^^^^^^^

Die Daten der Bayerischen Vermessungsverwaltung werden regelmässig aktualisiert. Um den eigenen heruntergeladenen Datenbestand
zu aktualisieren und dafür nur die aktualisierten Dateien herunterzuladen verwendet man den Schalter ``-V``.

Einfach den passenden Aufruf in die ``crontab``, sinnvolles Intervall einstellen (z.B. einmal wöchentlich) der Datenbestand
wird automatisch aktualisiert.

TL;DR
-----

Beispiele zum Download kompletter Datenbestände
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

3D-Gebäude LOD-2
""""""""""""""""

* Format: CITYGML
* EPSG: 25832 (UTM32)
* Tile-Size 2 km * 2 km

.. note::

 Download-Größe ~ 150 GB


.. code-block:: console

 $ aria2c -V --dir=/data/on_big_hdd/lod2/ https://geodaten.bayern.de/odd/a/lod2/citygml/meta/metalink/09.meta4

Digitales Geländemodell (DEM) - Auflösung 1 m
"""""""""""""""""""""""""""""""""""""""""""""

* Format: GeoTiff
* EPSG: 25832 (UTM32)
* Tile-Size: 1 km * 1 km

.. note::
 Download-Größe ~ 240 GB

.. code-block:: console

 $ aria2c -V --dir=/data/on_big_hdd/dem/ https://geodaten.bayern.de/odd/a/dgm/dgm1/meta/metalink/09.meta4

Digitales Orthophoto (DOP) - Auflösung 40 cm
""""""""""""""""""""""""""""""""""""""""""""

* Format: GeoTiff (RGB)
* EPSG: 25832 (UTM32)
* Tile-Size: 1 km * 1 km

.. warning::
 Download-Größe ~ 1,2 **TB** ~ 1200 GB

.. code-block:: bash

 for i in 1 2 3 4 5 6 7
 do
   aria2c -V --dir=/data/on_big_hdd/dop/ https://geodaten.bayern.de/odd/a/dop40/meta/metalink/09${i}.meta4
 done







