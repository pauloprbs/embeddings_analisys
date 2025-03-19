import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.metrics import roc_curve, auc
from sklearn.preprocessing import label_binarize


def plot_roc_auc(knn, X_test, y_test, title="ROC Curve"):

    # Converter rótulos para formato binário
    y_test_bin = label_binarize(y_test, classes=np.unique(y_test))  # One-hot encoding

    # Probabilidades para cada classe
    y_score = knn.predict_proba(X_test)

    plt.figure(figsize=(8, 6))
    
    for i in range(y_test_bin.shape[1]):
        fpr, tpr, _ = roc_curve(y_test_bin[:, i], y_score[:, i])
        roc_auc = auc(fpr, tpr)
        plt.plot(fpr, tpr, label=f'Class {i} (AUC = {roc_auc:.2f})')
    
    plt.plot([0, 1], [0, 1], 'k--')
    plt.xlabel("Taxa de False Positives")
    plt.ylabel("Taxa de True Positives")
    plt.title(title)
    plt.legend()
    plt.savefig(f"plots/{title}", dpi=300, bbox_inches="tight")
    plt.show()

def gerar_tabelas(X_test, y_test, best_results):
    metrics_results = []

    for metric, ( knn, k, acc, f1) in best_results.items():

        # AUC
        y_test_bin = label_binarize(y_test, classes=np.unique(y_test))
        y_score = knn.predict_proba(X_test)
        auc_score = np.mean([auc(*roc_curve(y_test_bin[:, i], y_score[:, i])[:2]) for i in range(y_test_bin.shape[1])])

        metrics_results.append([metric, k, acc, f1, auc_score])

    # DF com os resultados
    df_results = pd.DataFrame(metrics_results, columns=["Métrica", "Melhor K", "Acurácia", "F1-Score", "AUC"])
    print()
    print(df_results)

    # Arquivo CSV
    df_results.to_csv("resultados_knn.csv", index=False)