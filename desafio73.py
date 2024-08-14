times = ('Botafogo','Fortaleza', 'Flamengo', 'Palmeiras', 'São Paulo', 'Cruzeiro', 'Bahia',
         'Athletico-PR', 'Atlético-MG', 'Vasco', 'Bragantino', 'Juventude', 'Grêmio', 'Criciúma', 'Internacional',
         'Vitória', 'Corinthians', 'Fluminense', 'Cuiabá', 'Atlético-GO')
print('=+'*20)
print(f'Lista dos times do Brasileiro : {times}')
print('=+'*20)
print(f'Os 5 primeiros times são : {times[0:5]}')
print('=+'*20)
print(f'Os ultimos são : {times[-4:]}')
print('=+'*20)
print(f'Times em ordem alfabética: {sorted(times)}')
print(f'o vaco esta na {times.index("Vasco")} posição')