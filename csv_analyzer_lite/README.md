## csv_analyzer_lite

Jednoduchý Python program pro analýzu CSV souborů – načítá data a počítá základní statistiky.

### Spuštění a testy

#### Klonování repozitáře a přechod do složky projektu

git clone https://github.com/marketakor/csv_analyzer_lite.git

cd csv_analyzer_lite

#### Spuštění hlavního skriptu
python run.py

#### Spuštění testů
Linux / Mac
PYTHONPATH=. pytest tests/

Windows (PowerShell)
$env:PYTHONPATH="."
pytest tests/
