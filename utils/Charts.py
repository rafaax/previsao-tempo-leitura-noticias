import matplotlib.pyplot as matplot
import seaborn as sns

class Charts:
    def __init__(self):
        self.colors = sns.color_palette("pastel")


    def generatePieChart(self, values, df_file):  
        matplot.figure(figsize=(8, 8))
        matplot.pie(values, labels=values.index, autopct='%1.1f%%', colors=self.colors, startangle=140)
        matplot.title(f'Porcentagem de Categorias de Notícias Mais Lidas - {df_file}')
        state_name = df_file.split('/')[-1].replace('.csv', '')  # extrai o nome do estado do caminho do arquivo

        matplot.savefig(f'results/categorias_mais_lidas_{state_name}.jpg', dpi=300)
        matplot.show()