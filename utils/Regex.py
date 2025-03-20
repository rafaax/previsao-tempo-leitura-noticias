import re
import os

class Regex():
    def __init__(self):
        self._regex = { ## cria os patterns do regex
            "esporte": r'\b('
                r'esporte|futebol|basquete|vôlei|volei|atleta|jogos|campeonato|liga|'
                r'seleção|selecao|olimpíadas|olimpiadas|treinador|treino|competição|'
                r'competicao|gol|cesta|ponto|medalha|torcida|estádio|estadio'
            r')\b',

            "tecnologia": r'\b('
                r'tecnologia|inovacao|inovação|ciência|ciencia|inteligência artificial|'
                r'inteligencia artificial|IA|robótica|robotica|computação|computacao|software|'
                r'hardware|aplicativo|app|startup|empresa tech|redes sociais|internet|big data|'
                r'nuvem|cloud|blockchain|criptomoeda|bitcoin|realidade virtual|realidade aumentada|'
                r'IoT|internet das coisas|5G|6G|satélite|satelite|espacial|ciber segurança|cybersecurity|'
                r'hacker|vazamento de dados|drones|carro autônomo|carro autonomo|carro elétrico|carro eletrico|'
                r'bateria|energia renovável|energia renovavel|smartphone|tablet|notebook|laptop|processador|'
                r'chip|eletrônico|eletronico|gadget|dispositivo|inovador|desenvolvimento|laboratório|laboratorio|'
                r'cientista|engenheiro|programador|desenvolvedor|startup|fintech|edtech|healthtech|agritech|NFT|'
                r'automação|automaçao|algoritmo|machine learning|aprendizado de máquina|aprendizado de maquina|'
                r'deep learning|dados|analytics|transformação digital|transformacao digital|digitalização|digitalizacao'
            r')\b',

            "saude": r'\b('
                r'saúde|saude|medicina|hospital|médico|medico|enfermeiro|paciente|tratamento|doença|doenca|'
                r'câncer|cancer|diabetes|alzheimer|parkinson|cardiovascular|coronavírus|coronavirus|COVID|vacina|'
                r'imunização|imunizacao|epidemia|pandemia|surto|vírus|virus|bactéria|bacteria|infecção|infeccao|'
                r'cirurgia|transplante|órgão|orgao|sangue|hemograma|diagnóstico|diagnostico|sintoma|prevenção|'
                r'prevencao|reabilitação|reabilitacao|fisioterapia|psiquiatria|psicologia|terapia|remédio|remedio|'
                r'farmacêutico|farmaceutico|pesquisa clínica|pesquisa clinica|estudo clínico|estudo clinico|saúde pública|'
                r'saude publica|epidemiologia|OMS|organização mundial da saúde|organizacao mundial da saude|SUS|'
                r'sistema único de saúde|sistema unico de saude|bem-estar|bem estar|nutrição|nutricao|obesidade|'
                r'exercício|exercicio|saúde mental|saude mental|ansiedade|depressão|depressao|estresse|stress|'
                r'longevidade|envelhecimento|genética|genetica|biotecnologia|telemedicina|pronto-socorro|emergência|'
                r'emergencia|UTI|unidade de terapia intensiva|farmacologia|antibiótico|antibiotico|imunidade|alergia|'
                r'asma|hipertensão|hipertensao|colesterol|diarreia|febre|dor|inflamação|inflamacao|reumatismo|'
                r'osteoporose|autismo|esquizofrenia|bipolaridade|transtorno|saúde infantil|saude infantil|gravidez|'
                r'parto|neonatal|pediatria|geriatria|oncologia|hematologia|endocrinologia|dermatologia|oftalmologia|'
                r'odontologia|ortopedia|urologia|ginecologia|obstetrícia|obstetricia|cardiologia|neurologia|'
                r'pneumologia|gastroenterologia|infectologia|nefrologia|reumatologia|alimentação|alimentacao|'
                r'suplemento|vitamina|mineral|proteína|proteina|carboidrato|gordura|caloria|metabolismo|imunoterapia|'
                r'quimioterapia|radioterapia|fisiatria|acupuntura|homeopatia|fitoterapia|medicina alternativa|'
                r'medicina tradicional|medicina integrativa'
            r')\b',

            "politica": r'\b('
                r'política|politica|governo|presidente|senado|câmara|camara|deputado|senador|prefeito|'
                r'vereador|eleição|eleicao|voto|urnas|partido|legislativo|executivo|judiciário|judiciario|'
                r'congresso|planalto|palácio|palacio|ministro|ministério|ministerio|reforma|impeachment|'
                r'corrupção|corrupcao|escândalo|escandalo|democracia|ditadura|autoritarismo|esquerda|direita|'
                r'centro|ideologia|coalizão|coalizao|oposição|oposicao|aliança|alianca|orçamento|orcamento|'
                r'imposto|tributo|deficit|superavit|dívida|divida|pública|publica|privatização|privatizacao|'
                r'estatização|estatizacao|político|politico|mandato|gestão|gestao|projeto de lei|proposta|'
                r'votação|votacao|plebiscito|referendo|constituição|constituicao|fiscalização|fiscalizacao|'
                r'CPI|comissão parlamentar de inquérito|comissao parlamentar de inquérito|lobby|transparência|'
                r'transparencia|accountability'
            r')\b',

            "entretenimento": r'\b('
                r'entretenimento|cinema|filme|série|serie|Netflix|streaming|ator|atriz|diretor|'
                r'bilheteria|estreia|crítica|música|musica|artista|show|festival|teatro|TV|novela|'
                r'reality|celebridade|hollywood|prêmio|premio|trailer|jogo|videogame|podcast|YouTube|'
                r'influencer|redes sociais|moda|fashion|evento|lançamento|lancamento'
            r')\b'
        }

        self.news_best_category = {}

    def identifyNewsCategory(self, news_path):
        
        if news_path in self.news_best_category: ## valida se a noticia ja foi analisada, e retorna a melhor categoria salva no array
            return self.news_best_category[news_path] # busca o caminho da noticia que esta no csv no array de news_best_category que armazena a melhor categoria baseada num id de noticia ja avalido

        try:
            with open(news_path, 'r', encoding='utf-8') as arquivo: ## abre o arquivo da noticia
                news_text = arquivo.read() ## lê a noticia e atribui à variavel
            
            category_count = {
                category: len(re.findall(pattern, news_text, re.IGNORECASE))
                for category, pattern in self._regex.items()
            } 
            ############################ Comentarios


            # len() conta quantas vezes aquela categoria passou pela iteração e cabe no regex passado acima na classe
            # re.IGNORECASE faz a busca independente de letras maiusculas e minusculas 
            # o metodo .items retorna o conteudo do array _regex que contem as regras para cada categoria de noticia
            # o metodo findAll do regex busca todas ocorrencias do padrão que foi estipulado na _regex, e retorna uma lista, com essa lista ele faz a contagem com o len()

            
            ############################

            # print(category_count)

            best_category = max(category_count, key=category_count.get) # pega a categoria com maior numero de correspondências avaliados anteriormente

            if category_count[best_category] == 0:
                return "Indefinido" # caso a melhor categoria aparece 0x no array, ou seja, nao tem melhor categoria, ele atribui um indefinido
            
            print(f"A melhor categoria para a noticia {news_path} eh:  {best_category}")

            self.news_best_category[news_path] = best_category
            
            return best_category
            
        except Exception as e:
            print(f"Erro encontrado ao identificar a categoria da notícia: {e}")
            return False
            