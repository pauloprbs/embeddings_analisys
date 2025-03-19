import pandas as pd
from sklearn.model_selection import train_test_split

from src.data_prep import data_prep
from src.visualization import visualization
from src.knn_classifier import knn_classifier
from src.evaluation import plot_roc_auc, gerar_tabelas

# Leitura do arquivo
data = pd.read_pickle("data/mini_gm_public_v0.1.p")

df = data_prep(data)

print(df.head())

# Estatísticas básicas dos dados
print("Quantidade total de amostras: ", df["image_id"].nunique())
print()

print("Número de síndromes: ", df["syndrome_id"].nunique())
print()

print("Quantidade de imagens por síndrome:")
print(df["syndrome_id"].value_counts())
print()

# Visualização t-SNE dos embeddings
visualization(df)

# Separação dos embeddings e rótulos
X = df.iloc[:, 3:].values  # Embeddings
y = df["syndrome_id"].values  # Rótulos

# Divisão dos dados em train e test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# Teste para as métricas Euclidean e Cosine
best_results = {}

for metric in ["euclidean", "cosine"]:
    best_k = 1
    best_score = 0
    best_f1 = 0
    print(f"\nTestando métrica: {metric}")

    for k in range(1, 16):
        knn, acc, f1 = knn_classifier(X_train, X_test, y_train, y_test, k=k, metric=metric)

        if acc > best_score:
            best_score = acc
            best_f1
            best_k = k

    best_results[metric] = (knn, best_k, best_score, best_f1)
    print(f"Melhor K para {metric}: {best_k} com Acurácia de {best_score:.4f}")

# Exibir comparação final
print("\nComparação Final entre Métricas:")
for metric, (knn, k, acc, f1) in best_results.items():
    print(f"- {metric} - Melhor K: {k}, Acurácia: {acc:.4f}")

# AUC
for metric, (knn, k, acc, f1) in best_results.items():
    plot_roc_auc(knn, X_test, y_test, title=f"metric")

gerar_tabelas(X_train, y_train, X_test, y_test, best_results)