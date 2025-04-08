Titulo: Pipeline de logs de noticias utilizando Random Forest e Regex

Descrição breve:
Algoritmo em python para analisar um csv com informações referente à um sistema hipotético de um site de noticias. 
O log armazena informações como o ID da noticia, qual dispositivo foi utilizado para acessar, e mais informações do usuário e do seu acesso.
Modelo chegou num coeficiente médio de R² = 0.80. 

Principais funcionalidades:
  Menu para interação do usuario;
  Análise de csv e separação por localidade;
  Geração de gráficos para melhor visibilidade da porcentagem das categorias mais lidas por estado;
  Aplicação de regex para avaliação do tema da noticia baseado no conteudo;
  Aplicação de modelo Random Forest Regressor para previsão de tempo de leitura de usuarios à noticias baseados em todos os parametros do dataset.

Instruções de instalação/configuração:
  python (3.13+)
  pip install em todas bibliotecas do requirements.txt e rodar o projeto em qualquer terminal de sua preferência: python3/python/py index.py

Autores:
  Henry Murilo Lampoglio de Andrade
  Raphael Gustavo Meireles

