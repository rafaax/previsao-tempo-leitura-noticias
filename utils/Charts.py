import matplotlib.pyplot as matplot
import seaborn as sns

class Charts:
    def __init__(self):
        self.colors = sns.color_palette("pastel")


    def generatePieChart(self, values):  
        matplot.figure(figsize=(8, 8))
        matplot.pie(values, labels=values.index, autopct='%1.1f%%', colors=self.colors, startangle=140)
        matplot.title('Porcentagem de Categorias de Notícias Mais Lidas')
        matplot.show()