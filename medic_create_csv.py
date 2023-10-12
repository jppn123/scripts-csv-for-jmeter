import pandas as pd
from br_nome_gen import pessoa_random
from random import randrange, choice

crm = []
names = []
estados= ["AC", "AL", "AP", "AM", "BA", "CE", "DF", "ES", "GO", "MA", "MS", "MT", "MG", "PA", "PB", "PR", "PE", "PI", "RJ", "RN", "RS", "RO", "RR", "SC", "SP", "SE", "TO"]
nCol = 10
for x in range(nCol):
    names.append(pessoa_random().nome)

for x in range(nCol):
    randCrm = randrange(start=100, stop=100000000000000)
    if randCrm not in crm:
        crm.append(str(randCrm) + "/" + choice(estados))
    else:
        randCrm = randrange(start=30000, stop=5000000)
        crm.append(str(randCrm) + "/" + choice(estados))



df = pd.DataFrame(
    {
    'crm': crm,
    'name': names
    }
)
pd.set_option('float_format', '{:.0f}'.format)
df.to_csv('ex.csv', index=False, header=False)