# Social Network Community Detection

## Motivation

Large social networks are difficult to understand node by node. Community detection helps summarize the network by finding groups with dense internal connections and fewer external connections.

## Project Goal

We built and analyzed a Facebook-style social network graph to detect communities and measure modularity.

## Dataset / Problem

The graph is a controlled social-network-style graph with planted communities. It is not the real SNAP Facebook dataset. This choice keeps the project runnable locally while still showing the community-detection workflow.

## Tools

Python, NetworkX, pandas, and matplotlib.

## Method

We created a planted partition graph, detected communities with greedy modularity optimization, computed network summary statistics, and visualized the graph.

## Hyperparameters

- Groups: 4
- Nodes per group: 18
- Within-community edge probability: 0.28
- Cross-community edge probability: 0.025
- Random seed: 42

## Results

| Metric | Value |
|---|---:|
| Nodes | 72 |
| Edges | 224 |
| Density | 0.0876 |
| Detected communities | 4 |
| Modularity | 0.5564 |

Results are saved in `results/network_summary.csv`, `results/detected_communities.csv`, `results/degree_table.csv`, and `results/community_graph.png`.

## Interpretation

The algorithm detected four communities, matching the planted structure. The modularity score of 0.5564 indicates strong community separation: nodes connect much more inside groups than across groups.

## Conclusion

The project demonstrates community detection on a social-network-style graph. A stronger future version should use a real public Facebook network dataset and compare multiple community algorithms.

## How To Run

```bash
pip install -r requirements.txt
python 1_social_community_detection.py
```
