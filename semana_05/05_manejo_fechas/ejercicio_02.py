from datetime import datetime

str_date = "2/10/2025 07:30 PM"

"""
%H: Hora en formato de 24h (00 a 23)
%M: minutos (00 a 500)

%p: AM o PM
"""

conversion_fecha = datetime.strptime(str_date, "%d/%m/%Y %H:%M %p")

print(conversion_fecha)

"""
%I: Formato de 12h (01 a 12)
"""
conversion_fecha_2 = datetime.strptime(str_date, "%d/%m/%Y %I:%M %p")

print(conversion_fecha_2)