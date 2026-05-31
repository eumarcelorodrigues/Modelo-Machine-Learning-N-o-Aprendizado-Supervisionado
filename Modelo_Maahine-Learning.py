import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
from sklearn.preprocessing import StandardScaler

# Gerar dados aleatórios para clusterização
np.random.seed(42)
X, y_true = make_blobs(n_samples=300, centers=4, n_features=2, 
                       cluster_std=0.60, random_state=42)

# Normalizar os dados
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Criar e treinar o modelo K-means
kmeans = KMeans(n_clusters=4, random_state=42, n_init=10)
y_pred = kmeans.fit_predict(X_scaled)

# Obter centroides
centroides = kmeans.cluster_centers_

# Visualizar os clusters
plt.figure(figsize=(10, 6))
plt.scatter(X_scaled[:, 0], X_scaled[:, 1], c=y_pred, s=50, 
            cmap='viridis', alpha=0.6, edgecolors='k')
plt.scatter(centroides[:, 0], centroides[:, 1], c='red', s=300, 
            marker='*', edgecolors='black', linewidth=2, label='Centroides')
plt.xlabel('Recurso 1')
plt.ylabel('Recurso 2')
plt.title('Clusterização com K-means')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()

# Exibir informações do modelo
print(f"Número de clusters: {kmeans.n_clusters}")
print(f"Inércia: {kmeans.inertia_:.2f}")
print(f"Número de iterações: {kmeans.n_iter_}")
print(f"\nCentroides:\n{centroides}")
