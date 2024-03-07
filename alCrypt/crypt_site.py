import requests
from bs4 import BeautifulSoup

url = 'https://www.turkhackteam.org/konular/bettercap-kullanimi.2010928/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Tüm <p> (paragraf) etiketlerini bul
paragraflar = soup.find_all('p')
spans = soup.find_all('span')

# Paragrafların metin içeriğini al
metinler = [p.get_text() for p in paragraflar], [span.get_text() for span in spans]

# Alınan metinleri ekrana yazdır
for metin in metinler:
    print(metin)
