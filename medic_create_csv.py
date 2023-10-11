import pandas as pd
from br_nome_gen import pessoa_random
from random import randrange

crm = []
names = []
nCol = 10
for x in range(nCol):
    names.append(pessoa_random().nome)

for x in range(nCol):
    randCrm = randrange(start=100000000000000, stop=1000000000000000000000000)
    if randCrm not in crm:
        crm.append(randCrm)
    else:
        randCrm = randrange(start=110003000400000000, stop=100000000000000000000)
        crm.append(randCrm)
        
df = pd.DataFrame(
    {
    'crm': crm,
    'name': names
    }
)
pd.set_option('float_format', '{:.0f}'.format)
df.to_csv('ex.csv', index=False, header=False)