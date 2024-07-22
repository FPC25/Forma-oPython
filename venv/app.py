import requests
import json

url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'

response = requests.get(url)
print(response)

if response.status_code == 200:
    dados_json = response.json()
    dados_restaurante = {}
    for item in dados_json:
        nome_do_restaurante = item['Company']
        if nome_do_restaurante not in dados_restaurante: #se não achar um dado restaurante na lista 
            dados_restaurante[nome_do_restaurante] = [] #cria uma nova lista vazia para todas as informações desse restaurante 

        dados_restaurante[nome_do_restaurante].append({
            "item": item['Item'],
            "preco": item['price'],
            "descricao": item['description']
        })  

else:
    print(f'ERROR {response.status_code}')

for nome_do_restaurante, dados in dados_restaurante.items():
    nome_do_arquivo = f'{nome_do_restaurante}.json'
    with open(nome_do_restaurante, 'w') as arq_restaurante:
        json.dump(dados, arq_restaurante, indent = 4)