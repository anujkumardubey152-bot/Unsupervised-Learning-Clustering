# Clustering Algorithm Comparison

## Dataset
Mall Customer Segmentation Dataset

## K-Means
Advantages:
- Fast
- Easy to understand
- Works well on this dataset

Disadvantages:
- Number of clusters must be chosen manually.

## Hierarchical Clustering
Advantages:
- Produces a dendrogram.
- No need for random initialization.

Disadvantages:
- Slower for large datasets.

## DBSCAN
Advantages:
- Finds clusters of different shapes.
- Detects noise points automatically.

Disadvantages:
- Sensitive to eps and min_samples.

## Conclusion
K-Means produced the clearest customer segmentation for the Mall Customer dataset. Hierarchical Clustering also gave meaningful groups, while DBSCAN identified dense regions and outliers.


