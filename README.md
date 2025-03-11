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
from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import pandas as pd
from urllib.parse import urljoin
import time
```

## Pas 3: Funcionalitat d'exploració del domini

### Funció per extreure enllaços d'una pàgina
```python
def get_links(url, driver):
    driver.get(url)
    time.sleep(2)
    soup = BeautifulSoup(driver.page_source, "html.parser")
    links = set()
    for a_tag in soup.find_all("a", href=True):
        link = urljoin(url, a_tag['href'])
        if link.startswith("http://quotes.toscrape.com/"):
            links.add(link)
    return links
```

### Funció per explorar el domini de manera recursiva
```python
def crawl_domain(start_url, driver, visited=set()):
    to_visit = [start_url]
    while to_visit:
        url = to_visit.pop()
        if url not in visited:
            visited.add(url)
            new_links = get_links(url, driver)
            to_visit.extend(new_links - visited)
    return visited
```

### Funció per verificar l'estat HTTP d'una URL
```python
def check_url_status(url):
    try:
        response = requests.head(url, timeout=5)
        return response.status_code
    except requests.RequestException:
        return None
```

### Funció per trobar errors 4XX en una llista de URLs
```python
def find_4xx_errors(urls):
    errors = []
    for url in urls:
        status_code = check_url_status(url)
        if status_code and 400 <= status_code < 500:
            errors.append((url, status_code))
    return errors
```

### Funció per guardar els errors en un fitxer CSV
```python
def save_to_csv(errors, filename="errors_4xx.csv"):
    df = pd.DataFrame(errors, columns=["URL", "HTTP Status"])
    df.to_csv(filename, index=False)
    print(f"Informe guardat a {filename}")
```

### Bloc principal
```python
if __name__ == "__main__":
    start_url = "http://quotes.toscrape.com/"
    driver = webdriver.Chrome()
    print(f"Explorant el domini {start_url}...")
    visited_urls = crawl_domain(start_url, driver)
    print(f"Total URLs visitades: {len(visited_urls)}")
    print("Verificant errors 4XX...")
    errors_4xx = find_4xx_errors(visited_urls)
    print(f"Total errors 4XX trobats: {len(errors_4xx)}")
    save_to_csv(errors_4xx)
    driver.quit()
    print("Exploració finalitzada!")
```

## Pas 4: Executar el fitxer i comprovar els resultats

Desa els canvis al fitxer `crawler_4xx.py` i executa el programa des del terminal:

```sh
python crawler_4xx.py
```

El crawler explorarà `http://quotes.toscrape.com/` i cercarà errors 4XX. Quan acabi, generarà un fitxer `errors_4xx.csv` amb els errors trobats.

---

Aquest projecte pot ser ampliat per rastrejar altres dominis i detectar altres tipus d'errors!

