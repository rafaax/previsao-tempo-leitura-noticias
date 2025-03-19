import re
import os

class Regex():
    def __init__(self):
        self._regex = {
            "esporte": r'\b(esporte|futebol|basquete|vôlei|volei|atleta|jogos|campeonato|liga|seleção|selecao|olimpíadas|olimpiadas|treinador|treino|competição|competicao|gol|cesta|ponto|medalha|torcida|estádio|estadio)\b',
            "tecnologia": r'\b(tecnologia|inovacao|inovação|ciência|ciencia|inteligência artificial|inteligencia artificial|IA|robótica|robotica|computação|computacao|software|hardware|aplicativo|app|startup|empresa tech|redes sociais|internet|big data|nuvem|cloud|blockchain|criptomoeda|bitcoin|realidade virtual|realidade aumentada|IoT|internet das coisas|5G|6G|satélite|satelite|espacial|ciber segurança|cybersecurity|hacker|vazamento de dados|drones|carro autônomo|carro autonomo|carro elétrico|carro eletrico|bateria|energia renovável|energia renovavel|smartphone|tablet|notebook|laptop|processador|chip|eletrônico|eletronico|gadget|dispositivo|inovador|desenvolvimento|laboratório|laboratorio|cientista|engenheiro|programador|desenvolvedor|startup|fintech|edtech|healthtech|agritech|NFT|automação|automaçao|algoritmo|machine learning|aprendizado de máquina|aprendizado de maquina|deep learning|dados|analytics|transformação digital|transformacao digital|digitalização|digitalizacao)\b',
            "saude": r'\b(saúde|saude|medicina|hospital|médico|medico|enfermeiro|paciente|tratamento|doença|doenca|câncer|cancer|diabetes|alzheimer|parkinson|cardiovascular|coronavírus|coronavirus|COVID|vacina|imunização|imunizacao|epidemia|pandemia|surto|vírus|virus|bactéria|bacteria|infecção|infeccao|cirurgia|transplante|órgão|orgao|sangue|hemograma|diagnóstico|diagnostico|sintoma|prevenção|prevencao|reabilitação|reabilitacao|fisioterapia|psiquiatria|psicologia|terapia|remédio|remedio|farmacêutico|farmaceutico|pesquisa clínica|pesquisa clinica|estudo clínico|estudo clinico|saúde pública|saude publica|epidemiologia|OMS|organização mundial da saúde|organizacao mundial da saude|SUS|sistema único de saúde|sistema unico de saude|bem-estar|bem estar|nutrição|nutricao|obesidade|exercício|exercicio|saúde mental|saude mental|ansiedade|depressão|depressao|estresse|stress|longevidade|envelhecimento|genética|genetica|biotecnologia|telemedicina|pronto-socorro|emergência|emergencia|UTI|unidade de terapia intensiva|farmacologia|antibiótico|antibiotico|imunidade|alergia|asma|hipertensão|hipertensao|colesterol|diarreia|febre|dor|inflamação|inflamacao|reumatismo|osteoporose|autismo|esquizofrenia|bipolaridade|transtorno|saúde infantil|saude infantil|gravidez|parto|neonatal|pediatria|geriatria|oncologia|hematologia|endocrinologia|dermatologia|oftalmologia|odontologia|ortopedia|urologia|ginecologia|obstetrícia|obstetricia|cardiologia|neurologia|pneumologia|gastroenterologia|infectologia|nefrologia|reumatologia|alimentação|alimentacao|suplemento|vitamina|mineral|proteína|proteina|carboidrato|gordura|caloria|metabolismo|imunoterapia|quimioterapia|radioterapia|fisiatria|acupuntura|homeopatia|fitoterapia|medicina alternativa|medicina tradicional|medicina integrativa)\b',
            "politica": r'\b(política|politica|governo|presidente|senado|câmara|camara|deputado|senador|prefeito|vereador|eleição|eleicao|voto|urnas|partido|legislativo|executivo|judiciário|judiciario|congresso|planalto|palácio|palacio|ministro|ministério|ministerio|reforma|impeachment|corrupção|corrupcao|escândalo|escandalo|democracia|ditadura|autoritarismo|esquerda|direita|centro|ideologia|coalizão|coalizao|oposição|oposicao|aliança|alianca|orçamento|orcamento|imposto|tributo|deficit|superavit|dívida|divida|pública|publica|privatização|privatizacao|estatização|estatizacao|político|politico|mandato|gestão|gestao|projeto de lei|proposta|votação|votacao|plebiscito|referendo|constituição|constituicao|fiscalização|fiscalizacao|CPI|comissão parlamentar de inquérito|comissao parlamentar de inquérito|lobby|transparência|transparencia|accountability)\b',
            "entretenimento": r'\b(entretenimento|cinema|filme|série|serie|Netflix|streaming|ator|atriz|diretor|bilheteria|estreia|crítica|música|musica|artista|show|festival|teatro|TV|novela|reality|celebridade|hollywood|prêmio|premio|trailer|jogo|videogame|podcast|YouTube|influencer|redes sociais|moda|fashion|evento|lançamento|lancamento)\b'
        }

    def identifyNewsCategory(self, news_path):
        try:
            with open(news_path, 'r', encoding='utf-8') as arquivo:
                news_text = arquivo.read()
            
            category_count = {category: len(re.findall(pattern, news_text, re.IGNORECASE)) 
                              for category, pattern in self._regex.items()} 
            
            # print(category_count)

            best_category = max(category_count, key=category_count.get) # Determina a categoria com maior número de correspondências

            if category_count[best_category] == 0:
                return "Indefinido"
            
            print(f"A melhor categoria para a noticia {news_path} eh:  {best_category}")
            
            return best_category
            
            # correspondencias = re.search(regex_esporte, noticia_texto, re.IGNORECASE)
            
        except Exception as e:
            print(f"Erro encontrado ao identificar a categoria da notícia: {e}")
            return False