import querido_diario as qd
from datetime import date
from dateutil.rrule import DAILY, rrule
import pandas as pd

dados = {
#    IBGE_CODE: { DATA 1: "",
#                 DATA 2: "",
#                 DATA 3: "",  
#               },  
#    IBGE_CODE: { DATA 1: "",
#                 DATA 2: "",
#                 DATA 3: "", 
#               }
}

start=date(2023,11,1)
end=date.today()

for city_id in qd.available_cities_codes():
    dados[city_id] = {}

countdays = 0
for dt in rrule(freq=DAILY, dtstart=start, until=end):
    countdays+=1
    count = 0
    for city_id in qd.available_cities_codes():
        count+=1
        strdate = dt.strftime("%Y-%m-%d")        
        dados[city_id][strdate] = qd.gazette_date_validation(city_id, strdate)

        print(f"PROGRESSO: {countdays}/30 | {count}/263")
        
df = pd.DataFrame(dados).transpose()
df.to_csv("./tabela.csv")