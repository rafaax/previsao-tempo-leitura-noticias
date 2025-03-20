import pandas as pd
from utils.Regex import Regex
from utils.Extraction import Extraction
from utils.Charts import Charts
from utils.Transform import Transform


regexObject = Regex()
extractionObject = Extraction()
chartsObject = Charts()
transformDataframeObject = Transform()

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

        print(selected_df)
        category_counts = selected_df['best_category'].value_counts() ## faz a contagem das categorias, para gerar o gráfico
        chartsObject.generatePieChart(category_counts, selected_file)


if __name__ == "__main__":
    main()
