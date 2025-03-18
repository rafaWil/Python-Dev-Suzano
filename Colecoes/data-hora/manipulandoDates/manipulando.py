# TIME DELTA

# Exemplo
from datetime import datetime, date, time

# criando data e hora
data_hora = datetime.datetime(2025, 3, 17, 21, 5)
print(data_hora) # 2025-03-17 21:05:00

# adicionando uma semana
data_hora += datetime.timedelta(weeks=1)
print(data_hora) # 2025-03-24 21:05:00