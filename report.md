# Report: Social Network Community Detection

## Motivation

We studied community detection because it helps summarize social networks into meaningful groups.

## Dataset / Problem

The graph is a controlled social-network-style graph with planted communities. It has 72 nodes and 224 edges.

## Method

We used NetworkX to create the graph, detect communities with greedy modularity, calculate summary statistics, and save a visualization.

## Hyperparameters

The graph used 4 groups with 18 nodes each, within-community probability 0.28, cross-community probability 0.025, and random seed 42.

## Results

The algorithm detected 4 communities. The graph density was 0.0876, and modularity was 0.5564.

## Interpretation

The high modularity means the community structure is clear. Most connections stay inside groups, with fewer links between groups.

## Conclusion

This is a clear first community-detection workflow. The next step is to use a real social network dataset and compare algorithms.
