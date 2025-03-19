from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, f1_score

def knn_classifier(X_train, X_test, y_train, y_test, k=5, metric="euclidean"):
    
    knn = KNeighborsClassifier(n_neighbors=k, metric=metric)
    knn.fit(X_train, y_train)  # Treinamento do modelo

    y_pred = knn.predict(X_test)  # Previsão no conjunto de teste
    
    accuracy = accuracy_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred, average="weighted")

    return knn, accuracy, f1