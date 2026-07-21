from sklearn.cluster import KMeans, AgglomerativeClustering, DBSCAN

def kmeans_model(X):
    model = KMeans(n_clusters=5, random_state=42, n_init=10)
    return model.fit_predict(X)

def hierarchical_model(X):
    model = AgglomerativeClustering(n_clusters=5)
    return model.fit_predict(X)

def dbscan_model(X):
    model = DBSCAN(eps=0.8, min_samples=5)
    return model.fit_predict(X)
