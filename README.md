# previsao-tempo-leitura-noticias

Pipeline em Python que lê logs de acesso de um site de notícias (CSV),
classifica cada notícia por tema com regex e prevê o tempo de leitura
com Random Forest.

## O que faz
- Separa o dataset por estado e gera um CSV por estado
- Classifica as 20 notícias em esporte, tecnologia, saúde, política ou entretenimento
- Gera um gráfico de pizza das categorias mais lidas por estado (`results/`)
- Treina um `RandomForestRegressor` para prever `time_spent` e exibe MAE, MSE e R²

## Como rodar
```bash
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
python index.py        # escolha um estado no menu
```

## Estrutura
`index.py` · `utils/` (Regex, Extraction, Charts, RandomForest, Transform, Utility) ·
`mocks/dataset.csv` (2.000 acessos sintéticos) · `news/` (20 textos)

## Autores
Henry Lampoglio e Raphael Meireles
