from sklearn.cluster import KMeans, DBSCAN, AgglomerativeClustering
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
from sklearn.metrics import silhouette_score
from umap import UMAP

def calculate_silhouette_score(df, labels):
    return silhouette_score(df, labels)

def apply_kmeans(df, n_clusters=3):
    model = KMeans(n_clusters=n_clusters, random_state=42)
    return model.fit_predict(df)

def apply_dbscan(df, eps=0.5, min_samples=5):
    model = DBSCAN(eps=eps, min_samples=min_samples)
    return model.fit_predict(df)

def apply_agglomerative_clustering(df, n_clusters=3):
    model = AgglomerativeClustering(n_clusters=n_clusters)
    return model.fit_predict(df)

def apply_pca(df, n_components=2):
    pca = PCA(n_components=n_components)
    return pca.fit_transform(df)

def apply_tsne(df, n_components=2, perplexity=30):
    tsne = TSNE(n_components=n_components, perplexity=perplexity)
    return tsne.fit_transform(df)

def apply_umap(df, n_components=2):
    umap_model = UMAP(n_components=n_components)
    return umap_model.fit_transform(df)
