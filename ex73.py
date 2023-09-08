times = ('Botafogo', 'Palmeiras', 'Grêmio', 'Flamengo', 'Fluminense', 'Red Bull Bragantino',
         'Athletico-PR', 'Fortaleza', 'Atlético-MG', 'Cuiabá' ,'São Paulo', 'Cruzeiro', 'Corinthians',
         'Internacional' ,'Goiás' ,'Bahia', 'Santos', 'Vasco', 'América-MG', 'Coritiba')
print(f'Lista de times do Brasileirãao 2023: {times}')
print(f'Os 5 primeiros são {times[0:5]}')
print(f'Os 4 últimos colocados são: {times[-4:]}')
print(f'Times em ordem alfabética : {sorted(times)}')
print(f'O São Paulo está na {times.index("São Paulo")+1}ª posição')