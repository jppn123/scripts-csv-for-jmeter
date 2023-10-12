import pandas as pd 
from br_nome_gen import pessoa_random
from random import randrange, choice


nCol = 5
names = []
gender = []
allNat = ["acreano", "alagoano", "amapaense", "amazonense", "baiano", "cearense", "brasiliense", 
               "espírito-santense", "goiano", "maranhense", "mato-grossense", "sul-mato-grossense", "mineiro", 
               "paraense", "paraibano", "paranaense", "pernambucano", "piauiense", "fluminense", "norte-rio-grandense", 
               "gaúcho", "rondoniano", "roraimense", "catarinense", "paulista", "sergipano", "tocantinense"]
naturalness = []
bDate = []
record = []
usId = []

for x in range(nCol):
    name = pessoa_random()
    names.append(name.nome)
    gender.append(name.masc)
    naturalness.append(choice(allNat))
    usId.append(1)

for x in range(nCol):
    randBDate = randrange(start=10000000, stop=99999999999999999)
    randNum = randrange(start=10, stop=99999999999999999)
    if randBDate not in bDate or randNum not in record:
        bDate.append(randBDate)
        record.append(randNum)
    else:
        randBDate = randrange(start=50000000, stop=999999999999)
        randNum = randrange(start=10, stop=99999999999999999)
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