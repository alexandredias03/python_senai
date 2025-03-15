import requests # Reponsável por enviar a requisição
from bs4 import BeautifulSoup #Responsável por tratar a requisição

#_class -> feed-post-link

#URL do site

url = "https://g1.globo.com/"

headers = {
    "User-Agent": "Mozilla/5.0(Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/.36"
}

# Fazendo a requisição HTTP 
resposta = requests.get(url)

# Verificar se deu tudo certo
if resposta.status_code == 200:
    # Código 200 -> sucesso
    print("Requisição feita com sucesso.")
    # print(resposta.text) # Retorno
    # preechendo nossa sopa
    soup = BeautifulSoup(resposta.text, "html.parser")      
    # Encontrando as noticias
    noticias = soup.find_all("a", class_="feed-post-link")

    print("Ultimas noticias do G1:")
    for index, noticia in enumerate(noticias):
        print(f"{index + 1}.{noticia.text.strip()} - {noticia['href']}")


"""
 # OPção 2

url = "https://www.kayak.com.br/aluguel-de-carros-Cotia.307071.cars.ksp?r9ck=iq&gad_source=1&gclid=Cj0KCQjwytS-BhCKARIsAMGJyzqKcNx4aftn81Vx0R4Uv6cRn4CoGS0t2rOLbmmp2g7ZSjFszqOSs78aAvDTEALw_wcB"

headers = {
    "User-Agent": "Mozilla/5.0(Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/.36"
}

# Fazendo a requisição HTTP 
resposta = requests.get(url)

# Verificar se deu tudo certo
if resposta.status_code == 200:
    # Código 200 -> sucesso
    print("Requisição feita com sucesso.")
    
    #print(resposta.text) # Retorno
    
    # preechendo nossa sopa
    soup = BeautifulSoup(resposta.text, "html.parser")      
    # Encontrando as noticias
    alugueis = soup.find_all("div", class_="uH1B-category")

    print("Aluguel carros: ")
    for index, aluguel in enumerate(alugueis):
        print(f"{index + 1}.{aluguel.text.strip()}")

 
"""