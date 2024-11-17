import requests


API_KEY = "05da7237cd24ca5771098056be17b8c4"
cidade = input('Digite aqui a cidade:')
link = (f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={API_KEY}&lang=pt_br&units=metric")

requisicao = requests.get(link)
requisicao_dic = requisicao.json()
descricao = requisicao_dic['weather'][0]['description']
temperatura = requisicao_dic['main']['temp']
sensacao = requisicao_dic['main']['feels_like']

print(f'Atualmente o tempo se encontra {descricao} e a temperatura em {temperatura}ºC com sensação térmica de {sensacao}ºC')