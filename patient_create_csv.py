import pandas as pd 
from br_nome_gen import pessoa_random
from random import randrange, choice


nCol = 100000
names = []
gender = []
allNat = ["AC", "AL", "AP", "AM", "BA", "CE", "DF", "ES", "GO", "MA", "MS", "MT", "MG", "PA", "PB", "PR", "PE", "PI", "RJ", "RN", "RS", "RO", "RR", "SC", "SP", "SE", "TO"]
naturalness = []
bDate = []
record = []
usId = []

for x in range(nCol):
    name = pessoa_random()
    names.append(name.nome)
    gender.append(str(name.masc).lower())
    naturalness.append(choice(allNat))
    usId.append(1)

for x in range(nCol):
    randBDate = randrange(start=10000000, stop=999999999999)
    randNum = randrange(start=10, stop=99999999999999)
    if randBDate not in bDate or randNum not in record:
        bDate.append(randBDate)
        record.append(randNum)
    else:
        randBDate = randrange(start=10000, stop=99999999)
        randNum = randrange(start=10, stop=999999999999)
        bDate.append(randBDate)
        record.append(randNum)

df = pd.DataFrame(
    {
    "name": names,
    "medical_record": record,
    "birth_date": bDate,
    "male": gender,
    "naturalness": naturalness,
    "user_id": usId
    }
)
pd.set_option('float_format', '{:.0f}'.format)
df.to_csv('ex.csv', index=False, header=False)