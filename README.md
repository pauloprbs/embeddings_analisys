# Análise de Embeddings e Classificação de Síndromes Genéticas

O arquivo mini_gm_public_v0.1.p contém outputs(embeddings derivados de imagens) de um modelo pré-treinado de classificação de síndromes genéticas.

O objetivo deste estudo é realizar o pré-processamento dos dados, visualização e classificação, incluindo também métricas e insights.

## Estrutura do Dataset

Os embeddings do arquivo picle mini_gm_public_v0.1.p são vetores de 320 posições e seguem a seguinte estrutura:

{
    'syndrome_id': {
        'subject_id': {
            'image_id': [vetor de embeddings]
        }
    }
}

Estes vetores de embeddings serão usados para classificar as syndrome_id's.

## Para Análise e classificação, seguiremos algumas etapas:

1. Processamento dos dados:

- A estrutura do arquivo mini_gm_public_v0.1.p não é ideal para trabalharmos a visualização dos dados e a implementação de modelos de classificação. Por isso, no arquivo src/data_prep.py, implementamos uma função que converte a estrutura em um DataFrame do Pandas, dividindo os dados por colunas no seguinte formato:

| syndrome_id | subject_id | image_id | dim_0 | ... | dim_319 |

- Os 320 valores do vetor de embeddings agora estão divididos em colunas (dim_0 a dim_319).

- Algumas estatísticas iniciais dos dados:
- Um total de 10 síndromes são representadas nos dados. Cada síndrome é representada por uma numeração. Abaixo temos a numeração de cada sindrome e a quantidade de amostras correspondentes no dataset.
            
    - syndrome_id  
    - 300000034    210
    - 300000080    198
    - 100192430    136
    - 300000007    115
    - 300000082     98
    - 100610443     89
    - 300000018     74
    - 100180860     67
    - 100610883     65
    - 700018215     64

- A distribuição das amostras varia bastante, entre 64 a 210 amostras. Uma baixa quantidade de amostras para o treinamento pode resultar em um modelo não tão bom para generalizar as amostras de teste e não classificar tão bem para as síndromes de baixa amostragem.

2. Visualizaçao dos Dados:

- Nossa visão se limita a 3 dimensões, ou seja, não temos capacidade de interpretar de forma gráfica um vetor de 320 posições. Mas para estes casos, podemos tentar simplificar os dados através de técnicas de redução de dimensionalidade, como PCA ou t-SNE (como usaremos aqui), e assim conseguir interpretar de forma visual a distribuição dos dados.

- O t-SNE (t-distributed Stochastic Neighbor Embedding) [1] é um algoritmo que permite a visualização de dados multidimensionais. Os gráficos t-SNE modelam cada objeto de alta dimensionalidade em um ponto de duas ou três dimensões de mod que objetos semelhantes são modelados por pontos próximos [2].
    
- O gráfico de dispersão a seguir mostra a modelagem t-SNE dos embeddings em duas dimensões.

![Visualização t-SNE](plots/tsne_plot.png)

- Em duas dimensões, algumas síndromes, principalmente as representadas em verde mais claro, se agrupam em regiões mais específicas do gráfico, indicando que mesmo em com os embeddings representados de forma simplificada, é possível diferenciar bem estas síndromes das demais. No entanto, nas fronteiras dos grupos destas síndromes também há incidência de amostras de outras síndromes.

- As demais síndromes estão mais dispersas. É possível encontrar agrupamentos menores de suas amostras em regiões específicas dos gráficos, mas as amostras não se limitam às proximidades, indicando que um algoritmo de classificação utilizando os dados com dimensionalidade reduzida não será tão eficiente para classificar estas síndromes.

3. Classificação com KNN

- O KNN (K-Nearest Neighbors) calcula a distância entre as amostras que deseja classificar e amostras próximas de um conjunto de treinamento fornecido ao algoritmo. Entre as amostras mais próximas, quando um número k (pode ser definido pelo usuário ou encontrado através de testes) de amostras de uma determinada classe está entre os vizinhos mais próximos deste novo ponto, a amostra é classificada como pertencente a esta classe.

- Nos teste realizados, foram utilizadas as métricas de distância euclidiana e coseno.

- Para a distância euclidiana, o melhor valor K para a classificação foi 11, alcançando a acurácia de 75.89%, F1-Score = 0.754365 e AUC de 0.949369.

- Para a distância coseno, K = 15 se mostrou superior, com acurácia de 79.02%, F1-Score de 0.783229 e AUC = 0.953145.

- Mais informações sobre as métricas estão disponíveis em [3] e [4].

4. Métricas e Validação

- Abaixo, as curvas ROC AUC são apresentadas.

![ROC Curve - Euclidean](plots/euclidean.png)

- Para o KNN utilizando distância euclidiana, os valores mais baixos de AUC são de 0.92, em 4 classes que podem ser conferidas na imagem.

- A melhor AUC obtida é a da classe 6, de 0.99. 

![ROC Curve - Cosine](plots/cosine.png)

- Para o KNN com a distância de cosenos, o menor desempenho é da classe 9, em que o AUC é igual a 0.92.

- Tivemos 4 classes com AUC = 0.99, conforme o gráfico.

5. Conclusões

- Este estudo visou classificar sindromes genéticas através de embeddings obtidos de imagens por meio de um modelo de aprendizado de máquina. Os dados obtidos foram formatados e analisados e classificados.

- Para analisar a dispersão das amostras, utilizamos o algoritmo t-SNE para redução de dimensionalidade de 320 para 2. O gráfico de dispersão gerado mostrou o agrupamento de cada classe, sendo alguns dos clusters mais bem delimitados, e outros um pouco mais dispersos.

- Para a classificação, modelamos o problema utilizando KNN e testando com as distâncias euclidianas e coseno. Nos testes realizados, a utilização de coseno foi mais efetiva, obtendo acurácia de 79.02%.

- Para melhorar os resultados, podemos tentar obter mais dados para treinamento, já que certas classes possuem muito mais amostras que outras. Também é possível testar outros classificadores, como redes neurais perceptron multicamadas.

# Referências Bibliográficas

[1] van der Maaten, L.J.P. t-Distributed Stochastic Neighbor Embedding
https://lvdmaaten.github.io/tsne/

[2] gráficos t-SNE
https://www.ibm.com/docs/pt-br/spss-modeler/18.5.0?topic=types-t-sne-charts

[3] Precisão, Recall e F1 Score Em Machine Learning
https://mariofilho.com/precisao-recall-e-f1-score-em-machine-learning/

[4] Entenda o que é AUC e ROC nos modelos de Machine Learning
https://medium.com/bio-data-blog/entenda-o-que-%C3%A9-auc-e-roc-nos-modelos-de-machine-learning-8191fb4df772