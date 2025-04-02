import pandas as pd
from utils.Regex import Regex
from utils.Extraction import Extraction
from utils.Charts import Charts
from utils.Transform import Transform
from utils.RandomForest import RandomForest
from sklearn.preprocessing import LabelEncoder


regexObject = Regex()
extractionObject = Extraction()
chartsObject = Charts()
transformDataframeObject = Transform()
randomForestAlgorithm = RandomForest()

def periodo_do_dia(timestamp):
    hora = timestamp.hour
    if 6 <= hora < 12:
        return 'MANHA'
    elif 12 <= hora < 18:
        return 'TARDE'
    elif 18 <= hora < 24:
        return 'NOITE'
    else:
        return 'MADRUGADA'

def menu(dataset_files):
    print("\nEscolha um dataset para análise:")
    for idx, file in enumerate(dataset_files, start = 1):
        print(f"{idx} - {file}")
    print("0 - Sair")


def main():

    df = pd.read_csv('mocks/dataset.csv')
    news = {i: f"news/{i}.txt" for i in range(1, 21)} # declara um array indexado para armazenar o caminho das noticias na pasta news


    timestamp = pd.to_datetime(df['timestamp'], unit='ms')
    df['periodo'] = timestamp.apply(periodo_do_dia)
    user_name = df['name'] 
    user_age = df['age']
    user_state = df['state'] 
    df['gender'] = df['gender'].apply(lambda x: 'M' if x == 'Male' else 'F') # caso o valor do gender for igual a "Male" ele aplica o valor M, caso não ele aplica F
    gender = df['gender']
    news_id = df['news_id']
    time_spent = df['time_spent']
    device = df['device']

    df['best_category'] = news_id.apply(lambda x: regexObject.identifyNewsCategory(news[int(x)]))
    # para cada iteração do news_id ele pega o valor e aplica o identify para verificar qual é a categoria que mais se identifica baseado em REGEX


    bins = [0, 600, 1800, float('inf')]
    labels = ['baixo', 'medio', 'alto']
    df['time_spent_category'] = pd.cut(df['time_spent'], bins=bins, labels=labels, right=False)
    
    y = df['time_spent']
    df = df.drop(columns=['time_spent', 'name', 'timestamp'])

    x, label_encoders = randomForestAlgorithm.datasetPreprocessor(df=df)

    print(x)

    model, X_train_processed, X_test_processed, y_train, y_test, preprocessor, X_test = randomForestAlgorithm.trainModel(x, y)
    y_pred = randomForestAlgorithm.predict(model, X_test, preprocessor)

    randomForestAlgorithm.avaliateModel(y_pred, y_test)


if __name__ == "__main__":
    main()
