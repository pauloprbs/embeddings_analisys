import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.manifold import TSNE

def visualization(df):
    X = df.iloc[:, 3:].values  # X recebe os Embeddings
    y = df["syndrome_id"].values  # Rótulos

    tsne = TSNE(n_components=2, perplexity=30, random_state=42)
    X_2d = tsne.fit_transform(X)

    df_tsne = pd.DataFrame(X_2d, columns=["tsne_1", "tsne_2"])
    df_tsne["syndrome_id"] = y

    plt.figure(figsize=(10, 6))
    sns.scatterplot(x="tsne_1", y="tsne_2", hue="syndrome_id", palette="viridis", data=df_tsne, alpha=0.7)
    plt.title("Visualização t-SNE dos Embeddings")
    plt.legend(title="Síndrome ID", bbox_to_anchor=(1, 1))
    plt.savefig("plots/Visualização t-SNE dos Embeddings.png", dpi=300, bbox_inches="tight")
    plt.show()