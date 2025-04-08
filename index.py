# importando as bibliotecas necessárias para o funcionamento do código
import pandas as pd
from utils.Regex import Regex
from utils.Extraction import Extraction
from utils.Charts import Charts
from utils.Transform import Transform
from utils.RandomForest import RandomForest
from utils.Utility import menu, periodo_do_dia

# Instanciando as classes necessárias para o funcionamento do código
regexObject = Regex() 
extractionObject = Extraction()
chartsObject = Charts()
transformDataframeObject = Transform()
randomForestAlgorithm = RandomForest()

def main():

    df = pd.read_csv('mocks/dataset.csv') # lendo o arquivo csv que contém os dados de entrada
    news = {i: f"news/{i}.txt" for i in range(1, 21)} # declara um array indexado para armazenar o caminho das noticias na pasta news


    timestamp = pd.to_datetime(df['timestamp'], unit='ms') # converte a coluna timestamp para o formato datetime
    df['periodo'] = timestamp.apply(periodo_do_dia) # aplica a função periodo_do_dia para cada elemento da coluna timestamp e armazena o resultado na coluna periodo
    user_name = df['name'] 
    user_age = df['age']
    user_state = df['state'] 
    df['gender'] = df['gender'].apply(lambda x: 'M' if x == 'Male' else 'F') # caso o valor do gender for igual a "Male" ele aplica o valor M, caso não ele aplica F
    gender = df['gender']
    news_id = df['news_id']
    time_spent = df['time_spent']
    device = df['device']

    df['best_category'] = news_id.apply(lambda x: regexObject.identifyNewsCategory(news[int(x)])) # para cada iteração do news_id ele pega o valor e aplica o identify para verificar qual é a categoria que mais se identifica baseado em REGEX

    extractionObject.extract_dataset_by_state(df) # criando os csv dos estados extraidos da df original 
    dataset_files = [f"datasets/logs_{estado}.csv" for estado in df['state'].unique()] # criando um array de estados que geraram logs baseado na df 

    while True:
        menu(dataset_files) # chama a função menu que imprime na tela os estados que foram extraidos e os arquivos csv gerados
        option = input("Escolha uma opcao: ") # solicita ao usuário que escolha um estado para análise
        if option == '0': 
            print("Saindo...")
            break
        try:
            dataset_for_analysis = option 
            selected_file = dataset_files[int(dataset_for_analysis) - 1]
            selected_df =  pd.read_csv(selected_file) # lê o arquivo csv do estado escolhido pelo usuário
        except (IndexError, ValueError):
            print("Opção invalida. Tente novamente.")
            continue

        x = selected_df.drop(columns=['time_spent', 'name']) # remove a coluna time_spent e name da df para aplicar o pre-processamento
        
        bins = [0, 600, 1800, float('inf')] # define os limites dos bins para categorizar o tempo gasto
        labels = ['baixo', 'medio', 'alto'] # define os rótulos para cada bin
        selected_df['time_spent_category'] = pd.cut(selected_df['time_spent'], bins=bins, labels=labels, right=False) # aplica a categorização do tempo gasto na coluna time_spent_category
        y = selected_df['time_spent'] # define a variável y como a coluna time_spent da df
        selected_df = selected_df.drop(columns=['time_spent', 'name', 'timestamp']) # remove as colunas time_spent, name e timestamp da df para aplicar o pre-processamento

        x, label_encoders = randomForestAlgorithm.datasetPreprocessor(df=selected_df) # aplica o pre-processamento na df, transformando as colunas categóricas em numéricas e aplicando o one-hot encoding nas colunas que precisam

        model, X_train_processed, X_test_processed, y_train, y_test, preprocessor, X_test = randomForestAlgorithm.trainModel(x, y) # aplica o modelo de Random Forest na df, separando os dados em treino e teste, aplicando o pre-processamento e treinando o modelo
        y_pred = randomForestAlgorithm.predict(model, X_test, preprocessor) # aplica o modelo treinado na df de teste para prever os valores de y

        randomForestAlgorithm.avaliateModel(y_pred, y_test) # avalia o modelo treinado comparando os valores previstos com os valores reais de y
        
        chartsObject.generatePieChart(selected_df['best_category'].value_counts(), selected_file) ## faz a contagem das categorias, para gerar o gráfico

if __name__ == "__main__":
    main()
