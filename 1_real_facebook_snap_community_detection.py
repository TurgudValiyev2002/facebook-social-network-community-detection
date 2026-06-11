from __future__ import annotations

import gzip
import urllib.request
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import networkx as nx
import pandas as pd
from networkx.algorithms.community import greedy_modularity_communities, modularity


ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data"
RESULTS = ROOT / "results"
ASSETS = ROOT / "assets"
URL = "https://snap.stanford.edu/data/facebook_combined.txt.gz"
ARCHIVE = DATA / "facebook_combined.txt.gz"


def download_facebook() -> None:
    DATA.mkdir(exist_ok=True)
    if not ARCHIVE.exists():
        print(f"Downloading SNAP Facebook network from {URL}")
        urllib.request.urlretrieve(URL, ARCHIVE)


def load_graph() -> nx.Graph:
    download_facebook()
    g = nx.Graph()
    with gzip.open(ARCHIVE, "rt", encoding="utf-8") as handle:
        for line in handle:
            u, v = line.strip().split()
            g.add_edge(int(u), int(v))
    return g


def main() -> None:
    RESULTS.mkdir(exist_ok=True)
    ASSETS.mkdir(exist_ok=True)
    g = load_graph()
    communities = list(greedy_modularity_communities(g))
    community_id = {}
    for cid, nodes in enumerate(communities):
        for node in nodes:
            community_id[node] = cid

    degree_cent = nx.degree_centrality(g)
    betweenness = nx.betweenness_centrality(g, k=350, seed=42)
    pagerank = nx.pagerank(g)

    graph_summary = pd.DataFrame(
        [
            {
                "nodes": g.number_of_nodes(),
                "edges": g.number_of_edges(),
                "density": nx.density(g),
                "connected_components": nx.number_connected_components(g),
                "average_clustering": nx.average_clustering(g),
                "communities": len(communities),
                "modularity": modularity(g, communities),
            }
        ]
    )
    graph_summary.to_csv(RESULTS / "graph_summary.csv", index=False)

    node_table = pd.DataFrame(
        {
            "node": list(g.nodes()),
            "degree": [g.degree[n] for n in g.nodes()],
            "degree_centrality": [degree_cent[n] for n in g.nodes()],
            "betweenness_centrality_sampled": [betweenness[n] for n in g.nodes()],
            "pagerank": [pagerank[n] for n in g.nodes()],
            "community": [community_id[n] for n in g.nodes()],
        }
    ).sort_values("degree", ascending=False)
    node_table.to_csv(RESULTS / "node_centrality.csv", index=False)

    community_table = pd.DataFrame(
        [
            {
                "community": cid,
                "size": len(nodes),
                "share_of_nodes": len(nodes) / g.number_of_nodes(),
                "internal_edges": g.subgraph(nodes).number_of_edges(),
            }
            for cid, nodes in enumerate(communities)
        ]
    ).sort_values("size", ascending=False)
    community_table.to_csv(RESULTS / "community_summary.csv", index=False)

    plt.figure(figsize=(7, 4))
    top = community_table.head(12).sort_values("size")
    plt.barh(top["community"].astype(str), top["size"], color="#3d6fb6")
    plt.xlabel("Nodes")
    plt.ylabel("Community")
    plt.title("Largest SNAP Facebook Communities")
    plt.tight_layout()
    plt.savefig(RESULTS / "community_sizes.png", dpi=180)
    plt.close()

    sample_nodes = node_table.head(700)["node"].tolist()
    sub = g.subgraph(sample_nodes)
    pos = nx.spring_layout(sub, seed=42)
    plt.figure(figsize=(8, 7))
    nx.draw_networkx_edges(sub, pos, alpha=0.06, width=0.4)
    nx.draw_networkx_nodes(
        sub,
        pos,
        node_size=18,
        node_color=[community_id[n] for n in sub.nodes()],
        cmap="tab20",
    )
    plt.title("High-Degree Sample of Real Facebook Network")
    plt.axis("off")
    plt.tight_layout()
    plt.savefig(RESULTS / "facebook_graph_sample.png", dpi=180)
    plt.close()

    fig, ax = plt.subplots(figsize=(10, 4))
    ax.axis("off")
    boxes = [
        ("SNAP Facebook\n4039 nodes", 0.16),
        ("Real friendship\nedges", 0.40),
        ("Greedy modularity\ncommunities", 0.64),
        ("Centrality +\ncommunity tables", 0.86),
    ]
    for text, xpos in boxes:
        ax.text(xpos, 0.55, text, ha="center", va="center", fontsize=12, bbox=dict(boxstyle="round,pad=0.45", facecolor="#eef6ff", edgecolor="#336699"))
    for start, end in zip(boxes[:-1], boxes[1:]):
        ax.annotate("", xy=(end[1] - 0.11, 0.55), xytext=(start[1] + 0.11, 0.55), arrowprops=dict(arrowstyle="->", lw=2))
    ax.set_title("Real Facebook network community-detection workflow", fontsize=15)
    fig.tight_layout()
    fig.savefig(ASSETS / "readme_project_overview.png", dpi=180)
    plt.close(fig)

    print(graph_summary.to_string(index=False))
    print(community_table.head(10).to_string(index=False))


if __name__ == "__main__":
    main()
