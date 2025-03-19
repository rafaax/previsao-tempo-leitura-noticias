import pandas as pd
from Regex import Regex
from Extraction import Extraction

regexObject = Regex()
extractionObject = Extraction()
df = pd.read_csv('datasets/MOCK_DATA.csv')
# print(df.to_json())

timestamp = df['timestamp']
user_name = df['name'] 
user_age = df['age']
user_state = df['state'] 
df['gender'] = df['gender'].apply(lambda x: 'M' if x == 'Male' else 'F')
news_id = df['news_id']
time_spent = df['time_spent']
device = df['device']

news = {i: f"news/{i}.txt" for i in range(1, 21)}

for index, row in df.iterrows():
    regexObject.noticia_relacionada_a_esporte(news[int(row['news_id'])])
    # print(response)

# Regex.noticia_relacionada_a_esporte(news, )

# extract_dataset_by_state(df)

