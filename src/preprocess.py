import pandas as pd
import numpy as np

def data_prep(data):

    # Criação e ordenação do df
    flattened_data = []

    for syndrome_id, subjects in data.items():
        for subject_id, images in subjects.items():
            for image_id, embedding in images.items():
                flattened_data.append([syndrome_id, subject_id, image_id, embedding])

    df = pd.DataFrame(flattened_data, columns=["syndrome_id", "subject_id", "image_id", "embedding"])

    # Separação dos Embeddings
    embedding_matrix = np.array(df["embedding"].tolist())

    embedding_columns = [f"dim_{i}" for i in range(embedding_matrix.shape[1])]

    df_embeddings = pd.DataFrame(embedding_matrix, columns=embedding_columns)

    df = pd.concat([df.drop(columns=["embedding"]), df_embeddings], axis=1)

    return df