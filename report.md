# One-Page Report: Facebook Community Detection

## Motivation

We use the real SNAP Facebook combined network to study community structure in a real social graph.

## Dataset

The SNAP Facebook graph has 4,039 nodes and 88,234 undirected edges. It is one connected component with density 0.0108 and average clustering 0.6055.

## Method

We used NetworkX to load the graph, detect communities with greedy modularity optimization, and calculate centrality metrics including degree centrality, sampled betweenness, and PageRank.

## Results

The algorithm detected 13 communities with modularity 0.7774. The largest community has 983 nodes, followed by communities of 815, 548, 543, and 372 nodes.

## Interpretation

The high modularity shows strong group structure. The high clustering coefficient also fits social-network behavior, where friends of a user are often connected to each other.

## Conclusion

Project 10 uses real Facebook/SNAP data. The result supports the main idea that social networks contain strong communities, not only random connections.
