"""Reusable PCA and K-Means helpers for the customer segmentation project."""

from sklearn.decomposition import PCA
from sklearn.cluster import KMeans


def fit_pca(data, n_components=None, random_state=42):
    """Fit PCA and return the fitted transformer and transformed data."""
    pca = PCA(n_components=n_components, random_state=random_state)
    transformed = pca.fit_transform(data)
    return pca, transformed


def fit_kmeans(data, n_clusters, random_state=42):
    """Fit K-Means clustering and return the fitted model and labels."""
    model = KMeans(
        n_clusters=n_clusters,
        random_state=random_state,
        n_init=10
    )
    labels = model.fit_predict(data)
    return model, labels
