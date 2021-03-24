![](https://camo.githubusercontent.com/c0757aa456cbea5f494bc0b6a62a98820ecacc659719aaf6f0d4f7ff2ab1b008/68747470733a2f2f692e6962622e636f2f447448513346472f383032783236352d4c6f676f2d47542e706e67)

# NLP: Fake Citation
**Análise exploratória de dados e modelos de classificação utilizando as reportagens crawleadas do site [Aos fatos](https://www.aosfatos.org).**

## Sobre o projeto
O [Aos fatos](https://www.aosfatos.org) é um website dedicado a acompanhar declarações de políticos e autoridades de expressão nacional, de modo a verificar se a declaração deles é verdadeira ou não. 

Cada uma das declarações pode ser classificada dentro de uma das categorias: VERDADEIRO, IMPRECISO, EXAGERADO, CONTRADITÓRIO, INSUSTENTÁVEL, DISTORCIDO ou FALSO.

## Extração dos dados
Os dados foram extraídos do site [Aos fatos](https://www.aosfatos.org) utilizando
[scrapy](https://scrapy.org/) e estão disponíveis no arquivo _[fakequote.csv](Data/citations/fakequote.csv)_.
As colunas do dataset estão exemplificadas abaixo:

|   id | title                   | citation                           | category | url   |
|-----:|:------------------------|:-----------------------------------|:---------|:--------------------------------------------------------------|
|    1 | Ao atacar vacina chinesa, Bolsonaro distorce fatos e cita informação falsa   | Não se justifica um bilionário aporte financeiro num medicamento que sequer ultrapassou sua fase de testagem| CONTRADITÓRIO | 'https://www.aosfatos.org/noticias/ao-atacar-vacina-chinesa-bolsonaro-distorce-fatos-e-cita-informacao-falsa/'

O código utilizado para crawlear o site pode ser encontrado no arquivo _[aosfatos.py](Data/citations/spiders/aosfatos.py)_. 

## Análise de Dados
A análise de dados está disponível no arquivo _[EDA.ipynb](EDA.ipynb)_ . No notebook, você pode encontrar análises de contagens de palavras, suas frequências relativas nas notícias, ... **add o restante** 

## Classificação das notícias 
add modelos e notebook 



