import requests

def getData():

    # URL da API
    url = "https://api.wheretheiss.at/v1/satellites/25544"

    try:
        # Faz a solicitação GET para a API
        response = requests.get(url)

        # Verifica se a resposta foi bem-sucedida (código de status 200)
        if response.status_code == 200:
            # Retorna os dados JSON da resposta
            return response.json()
        else:
            print("Erro na solicitação da API:", response.status_code)

    except requests.exceptions.RequestException as e:
        print("Ocorreu um erro ao obter dados:", e)
