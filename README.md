## LDBV-BY Dokumentation

Sphinx-Sources zum Generieren der Seite https://ldbv-by.github.io.

Die Quelldateien (reText) befinden sich im Verzeichnis `doc`.

Wenn nach `master` gepusht wird, wird die Regel in `.github/workflows/documentation.yaml` ausgeführt und in den orphaned branch `gh-pages` geschrieben, aus die obengenannte Seite automatisch generiert wird.

Abbildungen *keinesfalls* mit LFS speichern, weil `gh-pages` damit nicht klar kommt.