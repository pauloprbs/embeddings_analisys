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

    | syndrome_id | subject_id | image_id | dim_0 | ... | dim_319 !

    - Os 320 valores do vetor de embeddings agora estão divididos em colunas (dim_0 a dim_319).