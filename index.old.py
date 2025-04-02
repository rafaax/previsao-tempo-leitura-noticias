import pandas as pd
from utils.Regex import Regex
from utils.Extraction import Extraction
from utils.Charts import Charts
from utils.Transform import Transform
from utils.RandomForest import RandomForest


regexObject = Regex()
extractionObject = Extraction()
chartsObject = Charts()
transformDataframeObject = Transform()
randomForestAlgorithm = RandomForest()

def menu(dataset_files):
    print("\nEscolha um dataset para análise:")
    for idx, file in enumerate(dataset_files, start = 1):
        print(f"{idx} - {file}")
    print("0 - Sair")


def main():

    df = pd.read_csv('mocks/dataset.csv')
    news = {i: f"news/{i}.txt" for i in range(1, 21)} # declara um array indexado para armazenar o caminho das noticias na pasta news


    timestamp = df['timestamp']
    user_name = df['name'] 
    user_age = df['age']
    user_state = df['state'] 
    df['gender'] = df['gender'].apply(lambda x: 'M' if x == 'Male' else 'F') # caso o valor do gender for igual a "Male" ele aplica o valor M, caso não ele aplica F
    gender = df['gender']
    news_id = df['news_id']
    time_spent = df['time_spent']
    device = df['device']

    df['best_category'] = news_id.apply(lambda x: regexObject.identifyNewsCategory(news[int(x)])) # para cada iteração do news_id ele pega o 
                                                                                            #   valor e aplica o identify para verificar qual é a categoria 
                                                                                            #   que mais se identifica baseado em REGEX

    extractionObject.extract_dataset_by_state(df) # criando os csv extraidos da df original 
    dataset_files = [f"datasets/logs_{estado}.csv" for estado in df['state'].unique()] # criando um array de estados que geraram logs baseado na df 

    # MENU DE ESCOLHA DE DATASET PARA ANALISE
    while True:
        menu(dataset_files)
        option = input("Escolha uma opcao: ")
        if option == '0':
            print("Saindo...")
            break
        try:
            dataset_for_analysis = option
            selected_file = dataset_files[int(dataset_for_analysis) - 1]
            selected_df =  pd.read_csv(selected_file)
        except (IndexError, ValueError):
            print("Opção invalida. Tente novamente.")
            continue

        x = selected_df.drop(columns=['time_spent', 'name'])
        
        bins = [0, 600, 1800, float('inf')]
        labels = ['baixo', 'medio', 'alto']
        selected_df['time_spent_category'] = pd.cut(selected_df['time_spent'], bins=bins, labels=labels, right=False)
        y = selected_df['time_spent_category']

        print(f"Tamanho de x: {len(x)}")
        print(f"Tamanho de y: {len(y)}")

        # categorical_cols = ['gender', 'state', 'device', 'best_category']
        # x = pd.get_dummies(x, columns=categorical_cols, drop_first=True)

        # df_importance = randomForestAlgorithm.calculateImportance(x, y)
        model, X_train_processed, X_test_processed, y_train, y_test, preprocessor, X_test = randomForestAlgorithm.trainModel(x, y)
        pred = randomForestAlgorithm.predict(model, X_test, preprocessor)
        randomForestAlgorithm.avaliateModel(pred, y_test)

        # chartsObject.featureImportance(df_importance)
        # chartsObject.generatePieChart(selected_df['best_category'].value_counts(), selected_file) ## faz a contagem das categorias, para gerar o gráfico


if __name__ == "__main__":
    main()
