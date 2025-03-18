# CONVERSÃO E FORMATAÇÃO DE DATAS E HORAS
"""
==> Para isso, usamos os métodos 'strftime' (string format time) e 'strptime' (string parse time).
"""

# Exemplo
from datetime import datetime

data = datetime.now()

# Formatando data e hora
print(data.strftime("%d/%m/%Y %H:%M")) # 17/03/2025 22:02

# Convertendo string para datetime
date_string = "20/12/2002 15:30"
data = datetime.strptime(date_string, "%d/%m/%Y %H:%M")
print(data) # 2002-12-20 15:30:00