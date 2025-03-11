from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import pandas as pd
from urllib.parse import urljoin
import time


# Funció per extreure enllaços d'una pàgina
def get_links(url, driver):
    driver.get(url)
    time.sleep(2)  # Espera perquè la pàgina es carregui
    soup = BeautifulSoup(driver.page_source, "html.parser")
    links = set()
    for a_tag in soup.find_all("a", href=True):
        link = urljoin(url, a_tag['href'])  # Converteix enllaços relatius a absoluts
        if link.startswith("http://quotes.toscrape.com/"):  # Filtrem només enllaços vàlids
            links.add(link)
    return links


# Funció per explorar el domini de manera recursiva
def crawl_domain(start_url, driver, visited=set()):
    to_visit = [start_url]  # Llista d'enllaços pendents de visitar
    while to_visit:
        url = to_visit.pop()  # Agafa una URL de la llista
        if url not in visited:
            visited.add(url)  # Marca com a visitada
            new_links = get_links(url, driver)  # Extreu els enllaços de la pàgina
            to_visit.extend(new_links - visited)  # Afegeix només enllaços nous
    return visited


# Funció per verificar l'estat HTTP d'una URL
def check_url_status(url):
    try:
        response = requests.head(url, timeout=5)  # Només la capçalera per estalviar temps
        return response.status_code
    except requests.RequestException:
        return None


# Funció per trobar errors 4XX en una llista de URLs
def find_4xx_errors(urls):
    errors = []
    for url in urls:
        status_code = check_url_status(url)
        if status_code and 400 <= status_code < 500:  # Verifica codis 4XX
            errors.append((url, status_code))
    return errors


# Funció per guardar els errors en un fitxer CSV
def save_to_csv(errors, filename="errors_4xx.csv"):
    df = pd.DataFrame(errors, columns=["URL", "HTTP Status"])
    df.to_csv(filename, index=False)
    print(f"Informe guardat a {filename}")


# Bloc principal
if __name__ == "__main__":
    # URL inicial
    start_url = "http://quotes.toscrape.com/"

    # Inicialitza el WebDriver
    driver = webdriver.Chrome()

    # Pas 1: Exploració del domini
    print(f"Explorant el domini {start_url}...")
    visited_urls = crawl_domain(start_url, driver)
    print(f"Total URLs visitades: {len(visited_urls)}")

    # Pas 2: Detecció d'errors 4XX
    print("Verificant errors 4XX...")
    errors_4xx = find_4xx_errors(visited_urls)
    print(f"Total errors 4XX trobats: {len(errors_4xx)}")

    # Pas 3: Generació d'informe
    save_to_csv(errors_4xx)

    # Tanca el WebDriver
    driver.quit()
    print("Exploració finalitzada!")
