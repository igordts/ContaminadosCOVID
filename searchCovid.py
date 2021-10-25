#Igor Duarte Torres Sena
#RA 31712411

import requests

resposta = requests.get('http://dados.mg.gov.br/api/3/action/datastore_search?resource_id=8a1743d9-e689-4112-afb3-8247369b63d7&limit=5')

if resposta.status_code == 200:

  dados = resposta.json()  
  count = 0
  for key in dados['result']['records']:
    if key['EVOLUCAO'] == 'RECUPERADO':
      count += 1

  #print('Endereço completo em JSON : ', dados)
  print("Total de casos recuperados: ", count)

else:
    print('Nao localizado!')