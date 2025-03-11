# Web Crawler per a Errors 4XX

Aquest projecte permet explorar un domini web i detectar errors 4XX utilitzant Python i Selenium.

## Pas 1: Configurar l'entorn

### Instal·la Python i Pip
Primer, assegura't de tenir Python instal·lat a la teva màquina. També necessitaràs `pip` per gestionar les biblioteques (ve amb les versions modernes de Python). Pots descarregar Python des d'aquí: [https://www.python.org/downloads/](https://www.python.org/downloads/).

### Instal·la les dependències
Executa les següents ordres al terminal per instal·lar les biblioteques necessàries:
```sh
pip install selenium requests beautifulsoup4 pandas
```

### Configura el WebDriver de Selenium

Ens descarregarem un WebDriver compatible amb el nostre navegador. En aquest exemple, utilitzarem `ChromeDriver`, que es pot descarregar des de:

[https://googlechromelabs.github.io/chrome-for-testing/](https://googlechromelabs.github.io/chrome-for-testing/)

1. Busca la versió corresponent al teu navegador.
2. Copia l'enllaç, obre'l en una nova pestanya i descarrega el ZIP.
3. Extreu els fitxers del ZIP i col·loca'ls en una carpeta accessible (per exemple, `C:\Tools\chromedriver`).
4. Copia la ruta de la carpeta i afegeix-la al `PATH` del sistema:
   - Cerca "variables d'entorn" al sistema.
   - A "Variables del sistema", selecciona la variable `Path` i fes clic a "Editar...".
   - Afegeix una nova entrada amb el camí complet de `chromedriver.exe`.
   - Guarda els canvis.

Per verificar la instal·lació, obre un terminal i executa:
```sh
chromedriver --version
```

## Pas 2: Crear el fitxer del projecte

Crearem un nou fitxer Python, anomenat `crawler_4xx.py`, i l'editarem amb Visual Studio Code. Pots descarregar VS Code aquí: [https://code.visualstudio.com/](https://code.visualstudio.com/).

A dins del fitxer, importarem les biblioteques necessàries:
```python
import selenium
import requests
import beautifulsoup4
import pandas as pd
```

## Pas 3: Funcionalitat d'exploració del domini

1. Afegir les funcions per extreure enllaços i explorar el domini de manera recursiva.
2. Implementar la detecció d'errors 4XX.
3. Generar un informe en format CSV (`errors_4xx.csv`).
4. Afegir el bloc principal del programa per integrar-ho tot.

L'exploració es realitzarà sobre la pàgina [http://quotes.toscrape.com/](http://quotes.toscrape.com/).

## Pas 4: Executar el fitxer i comprovar els resultats

Desa els canvis al fitxer `crawler_4xx.py` i executa el programa des del terminal:
```sh
python crawler_4xx.py
```

El crawler explorarà `http://quotes.toscrape.com/` i cercarà errors 4XX. Quan acabi, generarà un fitxer `errors_4xx.csv` amb els errors trobats.

---

Aquest projecte pot ser ampliat per rastrejar altres dominis i detectar altres tipus d'errors!

